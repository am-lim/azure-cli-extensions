# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
from azure.cli.core.commands import CliCommandType
from azext_devcenter_private_rp._client_factory import (
    cf_dev_center_dp,
    cf_dev_boxes_dp,
    cf_environments_dp,
)
from .custom import (
    AttachedNetworkCreate,
    AttachedNetworkDelete,
    AttachedNetworkList,
    AttachedNetworkShow,
    AttachedNetworkWait,
    CheckNameAvailabilityExecute,
    CheckScopedNameAvailabilityExecute,
    CatalogConnect,
    CatalogCreate,
    CatalogDelete,
    CatalogList,
    CatalogShow,
    CatalogSync,
    CatalogUpdate,
    CatalogWait,
    CatalogGetSyncErrorDetail,
    CatalogTaskGetErrorDetail,
    CatalogTaskList,
    CatalogTaskShow,
    DevBoxDefinitionCreate,
    DevBoxDefinitionDelete,
    DevBoxDefinitionList,
    DevBoxDefinitionShow,
    DevBoxDefinitionUpdate,
    DevBoxDefinitionWait,
    EnvironmentDefinitionGetErrorDetail,
    EnvironmentDefinitionList,
    EnvironmentDefinitionShow,
    EnvironmentTypeCreate,
    EnvironmentTypeDelete,
    EnvironmentTypeList,
    EnvironmentTypeShow,
    EnvironmentTypeUpdate,
    GalleryCreate,
    GalleryDelete,
    GalleryList,
    GalleryShow,
    GalleryWait,
    ImageList,
    ImageShow,
    ImageVersionList,
    ImageVersionShow,
    NetworkConnectionCreate,
    PlanMemberCreate,
    PoolCreate,
    PoolDelete,
    PoolList,
    PoolShow,
    PoolUpdate,
    PoolWait,
    ProjectCreate,
    ProjectAllowedEnvironmentTypeList,
    ProjectAllowedEnvironmentTypeShow,
    ProjectCatalogConnect,
    ProjectCatalogCreate,
    ProjectCatalogDelete,
    ProjectCatalogList,
    ProjectCatalogShow,
    ProjectCatalogSync,
    ProjectCatalogUpdate,
    ProjectCatalogWait,
    ProjectCatalogGetSyncErrorDetail,
    ProjectEnvironmentDefinitionGetErrorDetail,
    ProjectEnvironmentDefinitionList,
    ProjectEnvironmentDefinitionShow,
    ProjectEnvironmentTypeCreate,
    ProjectEnvironmentTypeDelete,
    ProjectEnvironmentTypeList,
    ProjectEnvironmentTypeShow,
    ProjectEnvironmentTypeUpdate,
    ScheduleCreate,
    ScheduleDelete,
    ScheduleShow,
    ScheduleUpdate,
    ScheduleWait,
)


def load_command_table(self, _):
    # Control plane
    self.command_table["devcenter-private-rp admin attached-network create"] = (
        AttachedNetworkCreate(loader=self)
    )
    self.command_table["devcenter-private-rp admin attached-network delete"] = (
        AttachedNetworkDelete(loader=self)
    )
    self.command_table["devcenter-private-rp admin attached-network list"] = AttachedNetworkList(
        loader=self
    )
    self.command_table["devcenter-private-rp admin attached-network show"] = AttachedNetworkShow(
        loader=self
    )
    self.command_table["devcenter-private-rp admin attached-network wait"] = AttachedNetworkWait(
        loader=self
    )

    self.command_table["devcenter-private-rp admin check-name-availability execute"] = (
        CheckNameAvailabilityExecute(loader=self)
    )

    self.command_table["devcenter-private-rp admin check-scoped-name-availability execute"] = (
        CheckScopedNameAvailabilityExecute(loader=self)
    )

    self.command_table["devcenter-private-rp admin catalog create"] = CatalogCreate(loader=self)
    self.command_table["devcenter-private-rp admin catalog delete"] = CatalogDelete(loader=self)
    self.command_table["devcenter-private-rp admin catalog list"] = CatalogList(loader=self)
    self.command_table["devcenter-private-rp admin catalog show"] = CatalogShow(loader=self)
    self.command_table["devcenter-private-rp admin catalog sync"] = CatalogSync(loader=self)
    self.command_table["devcenter-private-rp admin catalog update"] = CatalogUpdate(loader=self)
    self.command_table["devcenter-private-rp admin catalog wait"] = CatalogWait(loader=self)
    self.command_table["devcenter-private-rp admin catalog connect"] = CatalogConnect(loader=self)
    self.command_table["devcenter-private-rp admin catalog get-sync-error-detail"] = (
        CatalogGetSyncErrorDetail(loader=self)
    )

    self.command_table["devcenter-private-rp admin catalog-task get-error-detail"] = (
        CatalogTaskGetErrorDetail(loader=self)
    )
    self.command_table["devcenter-private-rp admin catalog-task list"] = CatalogTaskList(
        loader=self
    )
    self.command_table["devcenter-private-rp admin catalog-task show"] = CatalogTaskShow(
        loader=self
    )

    self.command_table["devcenter-private-rp admin environment-definition get-error-detail"] = (
        EnvironmentDefinitionGetErrorDetail(loader=self)
    )
    self.command_table["devcenter-private-rp admin environment-definition list"] = (
        EnvironmentDefinitionList(loader=self)
    )
    self.command_table["devcenter-private-rp admin environment-definition show"] = (
        EnvironmentDefinitionShow(loader=self)
    )

    self.command_table["devcenter-private-rp admin devbox-definition create"] = (
        DevBoxDefinitionCreate(loader=self)
    )
    self.command_table["devcenter-private-rp admin devbox-definition delete"] = (
        DevBoxDefinitionDelete(loader=self)
    )
    self.command_table["devcenter-private-rp admin devbox-definition list"] = DevBoxDefinitionList(
        loader=self
    )
    self.command_table["devcenter-private-rp admin devbox-definition show"] = DevBoxDefinitionShow(
        loader=self
    )
    self.command_table["devcenter-private-rp admin devbox-definition update"] = (
        DevBoxDefinitionUpdate(loader=self)
    )
    self.command_table["devcenter-private-rp admin devbox-definition wait"] = DevBoxDefinitionWait(
        loader=self
    )

    self.command_table["devcenter-private-rp admin environment-type create"] = (
        EnvironmentTypeCreate(loader=self)
    )
    self.command_table["devcenter-private-rp admin environment-type delete"] = (
        EnvironmentTypeDelete(loader=self)
    )
    self.command_table["devcenter-private-rp admin environment-type list"] = EnvironmentTypeList(
        loader=self
    )
    self.command_table["devcenter-private-rp admin environment-type show"] = EnvironmentTypeShow(
        loader=self
    )
    self.command_table["devcenter-private-rp admin environment-type update"] = (
        EnvironmentTypeUpdate(loader=self)
    )

    self.command_table["devcenter-private-rp admin gallery create"] = GalleryCreate(loader=self)
    self.command_table["devcenter-private-rp admin gallery delete"] = GalleryDelete(loader=self)
    self.command_table["devcenter-private-rp admin gallery list"] = GalleryList(loader=self)
    self.command_table["devcenter-private-rp admin gallery show"] = GalleryShow(loader=self)
    self.command_table["devcenter-private-rp admin gallery wait"] = GalleryWait(loader=self)

    self.command_table["devcenter-private-rp admin image list"] = ImageList(loader=self)
    self.command_table["devcenter-private-rp admin image show"] = ImageShow(loader=self)

    self.command_table["devcenter-private-rp admin image-version list"] = ImageVersionList(
        loader=self
    )
    self.command_table["devcenter-private-rp admin image-version show"] = ImageVersionShow(
        loader=self
    )

    self.command_table["devcenter-private-rp admin network-connection create"] = (
        NetworkConnectionCreate(loader=self)
    )

    self.command_table["devcenter-private-rp admin plan-member create"] = PlanMemberCreate(
        loader=self
    )

    self.command_table["devcenter-private-rp admin pool create"] = PoolCreate(loader=self)
    self.command_table["devcenter-private-rp admin pool delete"] = PoolDelete(loader=self)
    self.command_table["devcenter-private-rp admin pool list"] = PoolList(loader=self)
    self.command_table["devcenter-private-rp admin pool show"] = PoolShow(loader=self)
    self.command_table["devcenter-private-rp admin pool update"] = PoolUpdate(loader=self)
    self.command_table["devcenter-private-rp admin pool wait"] = PoolWait(loader=self)

    self.command_table["devcenter-private-rp admin project create"] = ProjectCreate(loader=self)

    self.command_table["devcenter-private-rp admin project-allowed-environment-type list"] = (
        ProjectAllowedEnvironmentTypeList(loader=self)
    )
    self.command_table["devcenter-private-rp admin project-allowed-environment-type show"] = (
        ProjectAllowedEnvironmentTypeShow(loader=self)
    )

    self.command_table["devcenter-private-rp admin project-catalog create"] = ProjectCatalogCreate(
        loader=self
    )
    self.command_table["devcenter-private-rp admin project-catalog delete"] = ProjectCatalogDelete(
        loader=self
    )
    self.command_table["devcenter-private-rp admin project-catalog list"] = ProjectCatalogList(
        loader=self
    )
    self.command_table["devcenter-private-rp admin project-catalog show"] = ProjectCatalogShow(
        loader=self
    )
    self.command_table["devcenter-private-rp admin project-catalog sync"] = ProjectCatalogSync(
        loader=self
    )
    self.command_table["devcenter-private-rp admin project-catalog update"] = ProjectCatalogUpdate(
        loader=self
    )
    self.command_table["devcenter-private-rp admin project-catalog wait"] = ProjectCatalogWait(
        loader=self
    )
    self.command_table["devcenter-private-rp admin project-catalog connect"] = (
        ProjectCatalogConnect(loader=self)
    )
    self.command_table["devcenter-private-rp admin project-catalog get-sync-error-detail"] = (
        ProjectCatalogGetSyncErrorDetail(loader=self)
    )

    self.command_table[
        "devcenter-private-rp admin project-environment-definition get-error-detail"
    ] = ProjectEnvironmentDefinitionGetErrorDetail(loader=self)
    self.command_table["devcenter-private-rp admin project-environment-definition list"] = (
        ProjectEnvironmentDefinitionList(loader=self)
    )
    self.command_table["devcenter-private-rp admin project-environment-definition show"] = (
        ProjectEnvironmentDefinitionShow(loader=self)
    )

    self.command_table["devcenter-private-rp admin project-environment-type create"] = (
        ProjectEnvironmentTypeCreate(loader=self)
    )
    self.command_table["devcenter-private-rp admin project-environment-type delete"] = (
        ProjectEnvironmentTypeDelete(loader=self)
    )
    self.command_table["devcenter-private-rp admin project-environment-type list"] = (
        ProjectEnvironmentTypeList(loader=self)
    )
    self.command_table["devcenter-private-rp admin project-environment-type show"] = (
        ProjectEnvironmentTypeShow(loader=self)
    )
    self.command_table["devcenter-private-rp admin project-environment-type update"] = (
        ProjectEnvironmentTypeUpdate(loader=self)
    )

    self.command_table["devcenter-private-rp admin schedule create"] = ScheduleCreate(loader=self)
    self.command_table["devcenter-private-rp admin schedule delete"] = ScheduleDelete(loader=self)
    self.command_table["devcenter-private-rp admin schedule show"] = ScheduleShow(loader=self)
    self.command_table["devcenter-private-rp admin schedule update"] = ScheduleUpdate(loader=self)
    self.command_table["devcenter-private-rp admin schedule wait"] = ScheduleWait(loader=self)

    # Data plane

    devcenter_dp = CliCommandType(
        operations_tmpl="azext_devcenter_private_rp.vendored_sdks.devcenter_dataplane.operations._operations#DevCenterOperations.{}",
        client_factory=cf_dev_center_dp,
    )

    dev_boxes_dp = CliCommandType(
        operations_tmpl="azext_devcenter_private_rp.vendored_sdks.devcenter_dataplane.operations._operations#DevBoxesOperations.{}",
        client_factory=cf_dev_boxes_dp,
    )

    environments_dp = CliCommandType(
        operations_tmpl=(
            "azext_devcenter_private_rp.vendored_sdks.devcenter_dataplane.operations._operations#EnvironmentsOperations.{}"
        ),
        client_factory=cf_environments_dp,
    )

    with self.command_group("devcenter"):
        pass

    with self.command_group("devcenter-private-rp dev"):
        pass

    with self.command_group("devcenter-private-rp dev project", devcenter_dp) as g:
        g.custom_command("list", "devcenter_project_list_dp")
        g.custom_show_command("show", "devcenter_project_show_dp")

    with self.command_group("devcenter-private-rp dev pool", dev_boxes_dp) as g:
        g.custom_command("list", "devcenter_pool_list_dp")
        g.custom_show_command("show", "devcenter_pool_show_dp")

    with self.command_group("devcenter-private-rp dev schedule", dev_boxes_dp) as g:
        g.custom_command("list", "devcenter_schedule_list_dp")
        g.custom_show_command("show", "devcenter_schedule_show_dp")

    with self.command_group("devcenter-private-rp dev dev-box") as g:
        g.custom_command("list", "devcenter_dev_box_list")
        g.custom_show_command("show", "devcenter_dev_box_show")
        g.custom_command("create", "devcenter_dev_box_create", supports_no_wait=True)
        g.custom_command(
            "delete",
            "devcenter_dev_box_delete",
            supports_no_wait=True,
            confirmation=True,
        )
        g.custom_command("start", "devcenter_dev_box_start", supports_no_wait=True)
        g.custom_command("stop", "devcenter_dev_box_stop", supports_no_wait=True)
        g.custom_command("restart", "devcenter_dev_box_restart", supports_no_wait=True)
        g.custom_command("repair", "devcenter_dev_box_repair", supports_no_wait=True)
        g.custom_command(
            "show-remote-connection", "devcenter_dev_box_get_remote_connection"
        )
        g.custom_command("list-action", "devcenter_dev_box_list_action")
        g.custom_command("show-action", "devcenter_dev_box_show_action")
        g.custom_command("skip-action", "devcenter_dev_box_skip_action")
        g.custom_command("delay-action", "devcenter_dev_box_delay_action")
        g.custom_command("delay-all-actions", "devcenter_dev_box_delay_all_actions")
        g.custom_command("list-operation", "devcenter_dev_box_list_operation")
        g.custom_command("show-operation", "devcenter_dev_box_show_operation")

    with self.command_group("devcenter-private-rp dev environment") as g:
        g.custom_command("list", "devcenter_environment_list")
        g.custom_show_command("show", "devcenter_environment_show")
        g.custom_command(
            "create", "devcenter_environment_create", supports_no_wait=True
        )
        g.custom_command(
            "update", "devcenter_environment_update", supports_no_wait=True
        )
        g.custom_command(
            "deploy", "devcenter_environment_update", supports_no_wait=True
        )
        g.custom_command(
            "delete",
            "devcenter_environment_delete",
            supports_no_wait=True,
            confirmation=True,
        )
        g.custom_command("list-operation", "devcenter_environment_operation_list")
        g.custom_command("show-operation", "devcenter_environment_operation_show")
        g.custom_command(
            "show-logs-by-operation",
            "devcenter_environment_operation_show_logs_by_operation",
        )
        g.custom_command("show-action", "devcenter_environment_operation_show_action")
        g.custom_command("list-action", "devcenter_environment_operation_list_action")
        g.custom_command("delay-action", "devcenter_environment_operation_delay_action")
        g.custom_command("skip-action", "devcenter_environment_operation_skip_action")
        g.custom_command("show-outputs", "devcenter_environment_operation_show_outputs")
        g.custom_command(
            "update-expiration-date",
            "devcenter_environment_operation_update_environment",
        )

    with self.command_group("devcenter-private-rp dev catalog", environments_dp) as g:
        g.custom_command("list", "devcenter_catalog_list_dp")
        g.custom_show_command("show", "devcenter_catalog_show_dp")

    with self.command_group(
        "devcenter-private-rp dev environment-definition", environments_dp
    ) as g:
        g.custom_command("list", "devcenter_environment_definition_list_dp")
        g.custom_show_command("show", "devcenter_environment_definition_show_dp")

    with self.command_group("devcenter-private-rp dev environment-type", environments_dp) as g:
        g.custom_command("list", "devcenter_environment_type_list_dp")

    with self.command_group("devcenter-private-rp dev customization-group") as g:
        g.custom_command("list", "devcenter_customization_group_list")
        g.custom_show_command("show", "devcenter_customization_group_show")
        g.custom_command("create", "devcenter_customization_group_create")

    with self.command_group("devcenter-private-rp dev customization-task") as g:
        g.custom_command("list", "devcenter_customization_task_definition_list")
        g.custom_show_command("show", "devcenter_customization_task_definition_show")
        g.custom_command("validate", "devcenter_customization_task_definition_validate")
        g.custom_command("show-logs", "devcenter_customization_task_log_show")
