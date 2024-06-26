# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional
from knack.log import get_logger

from azext_aosm.build_processors.arm_processor import AzureCoreArmBuildProcessor
from azext_aosm.build_processors.vhd_processor import VHDProcessor
from azext_aosm.common.constants import (
    BASE_FOLDER_NAME,
    VNF_CORE_BASE_TEMPLATE_FILENAME,
    VNF_TEMPLATE_FOLDER_NAME,
    VNF_OUTPUT_FOLDER_FILENAME,
    DEPLOY_PARAMETERS_FILENAME,
    VHD_PARAMETERS_FILENAME,
    TEMPLATE_PARAMETERS_FILENAME
)
from azext_aosm.configuration_models.onboarding_vnf_input_config import (
    OnboardingCoreVNFInputConfig,
)
from azext_aosm.configuration_models.common_parameters_config import (
    CoreVNFCommonParametersConfig,
)
from azext_aosm.definition_folder.builder.bicep_builder import (
    BicepDefinitionElementBuilder,
)
from azext_aosm.definition_folder.builder.json_builder import (
    JSONDefinitionElementBuilder,
)
from azext_aosm.inputs.arm_template_input import ArmTemplateInput
from azext_aosm.inputs.vhd_file_input import VHDFileInput
from azext_aosm.common.utils import render_bicep_contents_from_j2, get_template_path

from .onboarding_vnf_handler import OnboardingVNFCLIHandler
logger = get_logger(__name__)


class OnboardingCoreVNFCLIHandler(OnboardingVNFCLIHandler):
    """CLI handler for publishing NFDs."""

    config: OnboardingCoreVNFInputConfig

    def _get_input_config(
        self, input_config: Optional[dict] = None
    ) -> OnboardingCoreVNFInputConfig:
        """Get the configuration for the command."""
        if input_config is None:
            input_config = {}
        return OnboardingCoreVNFInputConfig(**input_config)

    def _get_params_config(
        self, config_file: Path
    ) -> CoreVNFCommonParametersConfig:
        """Get the configuration for the command."""
        with open(config_file, "r", encoding="utf-8") as _file:
            params_dict = json.load(_file)
        if params_dict is None:
            params_dict = {}
        return CoreVNFCommonParametersConfig(**params_dict)

    def _get_processor_list(self) -> List[AzureCoreArmBuildProcessor | VHDProcessor]:
        """Get the list of processors."""
        processor_list: List[AzureCoreArmBuildProcessor | VHDProcessor] = []
        # for each arm template, instantiate arm processor
        for arm_template in self.config.arm_templates:
            arm_input = ArmTemplateInput(
                artifact_name=arm_template.artifact_name,
                artifact_version=arm_template.version,
                default_config={"imageName": self.config.nf_name + "Image"},
                template_path=Path(arm_template.file_path).absolute(),
            )
            processor_list.append(
                AzureCoreArmBuildProcessor(
                    arm_input.artifact_name, arm_input,
                    expose_all_params=self.config.expose_all_parameters)
            )

        # Instantiate vhd processor
        if not self.config.vhd.artifact_name:
            self.config.vhd.artifact_name = self.config.nf_name + "-vhd"

        if self.config.vhd.file_path:
            file_path = Path(self.config.vhd.file_path).absolute()
        else:
            file_path = None

        vhd_processor = VHDProcessor(
            name=self.config.vhd.artifact_name,
            input_artifact=VHDFileInput(
                artifact_name=self.config.vhd.artifact_name,
                artifact_version=self.config.vhd.version,
                default_config=self._get_default_config(self.config.vhd),
                file_path=file_path,
                blob_sas_uri=self.config.vhd.blob_sas_url,
            ),
            expose_all_params=self.config.expose_all_parameters
        )
        processor_list.append(vhd_processor)
        return processor_list

    def build_base_bicep(self) -> BicepDefinitionElementBuilder:
        """Build the base bicep file."""
        # Build manifest bicep contents, with j2 template
        template_path = get_template_path(
            VNF_TEMPLATE_FOLDER_NAME, VNF_CORE_BASE_TEMPLATE_FILENAME
        )
        bicep_contents = render_bicep_contents_from_j2(template_path, {})
        # Create Bicep element with manifest contents
        bicep_file = BicepDefinitionElementBuilder(
            Path(VNF_OUTPUT_FOLDER_FILENAME, BASE_FOLDER_NAME), bicep_contents
        )
        return bicep_file

    def build_all_parameters_json(self) -> JSONDefinitionElementBuilder:
        """Create object for all_parameters.json."""
        params_content = {
            "location": self.config.location,
            "publisherName": self.config.publisher_name,
            "publisherResourceGroupName": self.config.publisher_resource_group_name,
            "acrArtifactStoreName": self.config.acr_artifact_store_name,
            "saArtifactStoreName": self.config.blob_artifact_store_name,
            "acrManifestName": self.config.acr_manifest_name,
            "saManifestName": self.config.sa_manifest_name,
            "nfDefinitionGroup": self.config.nf_name,
            "nfDefinitionVersion": self.config.version
        }
        base_file = JSONDefinitionElementBuilder(
            Path(VNF_OUTPUT_FOLDER_FILENAME), json.dumps(params_content, indent=4)
        )
        return base_file

    def _get_default_config(self, vhd) -> Dict[str, Any]:
        """Get default VHD config for Azure Core VNF."""
        default_config = {}
        if vhd.image_disk_size_GB:
            default_config.update({"image_disk_size_GB": vhd.image_disk_size_GB})
        if vhd.image_hyper_v_generation:
            default_config.update(
                {"image_hyper_v_generation": vhd.image_hyper_v_generation}
            )
        else:
            # Default to V1 if not specified
            default_config.update({"image_hyper_v_generation": "V1"})
        if vhd.image_api_version:
            default_config.update({"image_api_version": vhd.image_api_version})

        # Add imageName
        default_config["imageName"] = self.config.nf_name + 'Image'
        return default_config

    def _generate_type_specific_nf_application(self, processor) -> Tuple[List, List]:
        """Generate the type specific nf application."""
        arm_nf = []
        image_nf = []
        nf_application = processor.generate_nf_application()

        if isinstance(processor, AzureCoreArmBuildProcessor):
            arm_nf.append(nf_application)
        elif isinstance(processor, VHDProcessor):
            image_nf.append(nf_application)
        else:
            raise TypeError(f"Type: {type(processor)} is not valid")
        logger.debug("Created nf application %s", nf_application.name)
        return (arm_nf, image_nf)

    def _generate_type_specific_artifact_manifest(self, processor):
        """Generate the type specific artifact manifest list."""
        arm_artifacts = []
        sa_artifacts = []

        if isinstance(processor, AzureCoreArmBuildProcessor):
            arm_artifacts = processor.get_artifact_manifest_list()
            logger.debug(
                "Created list of artifacts from %s arm template(s) provided: %s",
                len(self.config.arm_templates),
                arm_artifacts,
            )
        elif isinstance(processor, VHDProcessor):
            sa_artifacts = processor.get_artifact_manifest_list()
            logger.debug(
                "Created list of artifacts from vhd image provided: %s",
                sa_artifacts,
            )

        return (arm_artifacts, sa_artifacts)

    def _get_nfd_template_params(
            self, arm_nf_application_list, image_nf_application_list) -> Dict[str, Any]:
        """Get the nfd template params."""
        return {
            "nfvi_type": 'AzureCore',
            "acr_nf_applications": arm_nf_application_list,
            "sa_nf_applications": image_nf_application_list,
            "nexus_image_nf_applications": [],
            "deploy_parameters_file": DEPLOY_PARAMETERS_FILENAME,
            "vhd_parameters_file": VHD_PARAMETERS_FILENAME,
            "template_parameters_file": TEMPLATE_PARAMETERS_FILENAME
        }
