# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from io import IOBase
from typing import Any, AsyncIterable, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload
import urllib.parse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._source_control_configurations_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class SourceControlConfigurationsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.aio.SourceControlConfigurationClient`'s
        :attr:`source_control_configurations` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")
        self._api_version = input_args.pop(0) if input_args else kwargs.pop("api_version")

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, _models.Enum0],
        cluster_resource_name: Union[str, _models.Enum1],
        cluster_name: str,
        source_control_configuration_name: str,
        **kwargs: Any
    ) -> _models.SourceControlConfiguration:
        """Gets details of the Source Control Configuration.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters). Known values are:
         "Microsoft.ContainerService" and "Microsoft.Kubernetes". Required.
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters). Known values are:
         "managedClusters" and "connectedClusters". Required.
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param source_control_configuration_name: Name of the Source Control Configuration. Required.
        :type source_control_configuration_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControlConfiguration or the result of cls(response)
        :rtype:
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.SourceControlConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-05-01-preview")
        )
        cls: ClsType[_models.SourceControlConfiguration] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            source_control_configuration_name=source_control_configuration_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("SourceControlConfiguration", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/sourceControlConfigurations/{sourceControlConfigurationName}"
    }

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, _models.Enum0],
        cluster_resource_name: Union[str, _models.Enum1],
        cluster_name: str,
        source_control_configuration_name: str,
        source_control_configuration: _models.SourceControlConfiguration,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SourceControlConfiguration:
        """Create a new Kubernetes Source Control Configuration.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters). Known values are:
         "Microsoft.ContainerService" and "Microsoft.Kubernetes". Required.
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters). Known values are:
         "managedClusters" and "connectedClusters". Required.
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param source_control_configuration_name: Name of the Source Control Configuration. Required.
        :type source_control_configuration_name: str
        :param source_control_configuration: Properties necessary to Create KubernetesConfiguration.
         Required.
        :type source_control_configuration:
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.SourceControlConfiguration
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControlConfiguration or the result of cls(response)
        :rtype:
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.SourceControlConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_or_update(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, _models.Enum0],
        cluster_resource_name: Union[str, _models.Enum1],
        cluster_name: str,
        source_control_configuration_name: str,
        source_control_configuration: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.SourceControlConfiguration:
        """Create a new Kubernetes Source Control Configuration.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters). Known values are:
         "Microsoft.ContainerService" and "Microsoft.Kubernetes". Required.
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters). Known values are:
         "managedClusters" and "connectedClusters". Required.
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param source_control_configuration_name: Name of the Source Control Configuration. Required.
        :type source_control_configuration_name: str
        :param source_control_configuration: Properties necessary to Create KubernetesConfiguration.
         Required.
        :type source_control_configuration: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControlConfiguration or the result of cls(response)
        :rtype:
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.SourceControlConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, _models.Enum0],
        cluster_resource_name: Union[str, _models.Enum1],
        cluster_name: str,
        source_control_configuration_name: str,
        source_control_configuration: Union[_models.SourceControlConfiguration, IO],
        **kwargs: Any
    ) -> _models.SourceControlConfiguration:
        """Create a new Kubernetes Source Control Configuration.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters). Known values are:
         "Microsoft.ContainerService" and "Microsoft.Kubernetes". Required.
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters). Known values are:
         "managedClusters" and "connectedClusters". Required.
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param source_control_configuration_name: Name of the Source Control Configuration. Required.
        :type source_control_configuration_name: str
        :param source_control_configuration: Properties necessary to Create KubernetesConfiguration. Is
         either a SourceControlConfiguration type or a IO type. Required.
        :type source_control_configuration:
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.SourceControlConfiguration or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SourceControlConfiguration or the result of cls(response)
        :rtype:
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.SourceControlConfiguration
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-05-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.SourceControlConfiguration] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(source_control_configuration, (IOBase, bytes)):
            _content = source_control_configuration
        else:
            _json = self._serialize.body(source_control_configuration, "SourceControlConfiguration")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            source_control_configuration_name=source_control_configuration_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("SourceControlConfiguration", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("SourceControlConfiguration", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})  # type: ignore

        return deserialized  # type: ignore

    create_or_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/sourceControlConfigurations/{sourceControlConfigurationName}"
    }

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        cluster_rp: Union[str, _models.Enum0],
        cluster_resource_name: Union[str, _models.Enum1],
        cluster_name: str,
        source_control_configuration_name: str,
        **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-05-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            cluster_rp=cluster_rp,
            cluster_resource_name=cluster_resource_name,
            cluster_name=cluster_name,
            source_control_configuration_name=source_control_configuration_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        _stream = False
        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=_stream, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/sourceControlConfigurations/{sourceControlConfigurationName}"
    }

    @distributed_trace_async
    async def begin_delete(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, _models.Enum0],
        cluster_resource_name: Union[str, _models.Enum1],
        cluster_name: str,
        source_control_configuration_name: str,
        **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """This will delete the YAML file used to set up the Source control configuration, thus stopping
        future sync from the source repo.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters). Known values are:
         "Microsoft.ContainerService" and "Microsoft.Kubernetes". Required.
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters). Known values are:
         "managedClusters" and "connectedClusters". Required.
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :param source_control_configuration_name: Name of the Source Control Configuration. Required.
        :type source_control_configuration_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-05-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)
        polling: Union[bool, AsyncPollingMethod] = kwargs.pop("polling", True)
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token: Optional[str] = kwargs.pop("continuation_token", None)
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                cluster_rp=cluster_rp,
                cluster_resource_name=cluster_resource_name,
                cluster_name=cluster_name,
                source_control_configuration_name=source_control_configuration_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method: AsyncPollingMethod = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)  # type: ignore

    begin_delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/sourceControlConfigurations/{sourceControlConfigurationName}"
    }

    @distributed_trace
    def list(
        self,
        resource_group_name: str,
        cluster_rp: Union[str, _models.Enum0],
        cluster_resource_name: Union[str, _models.Enum1],
        cluster_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.SourceControlConfiguration"]:
        """List all Source Control Configurations.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS
         clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters). Known values are:
         "Microsoft.ContainerService" and "Microsoft.Kubernetes". Required.
        :type cluster_rp: str or ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum0
        :param cluster_resource_name: The Kubernetes cluster resource name - either managedClusters
         (for AKS clusters) or connectedClusters (for OnPrem K8S clusters). Known values are:
         "managedClusters" and "connectedClusters". Required.
        :type cluster_resource_name: str or
         ~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.Enum1
        :param cluster_name: The name of the kubernetes cluster. Required.
        :type cluster_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SourceControlConfiguration or the result of
         cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.kubernetesconfiguration.v2021_05_01_preview.models.SourceControlConfiguration]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: str = kwargs.pop(
            "api_version", _params.pop("api-version", self._api_version or "2021-05-01-preview")
        )
        cls: ClsType[_models.SourceControlConfigurationList] = kwargs.pop("cls", None)

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    resource_group_name=resource_group_name,
                    cluster_rp=cluster_rp,
                    cluster_resource_name=cluster_resource_name,
                    cluster_name=cluster_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("SourceControlConfigurationList", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)  # type: ignore
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            _stream = False
            pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=_stream, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{clusterRp}/{clusterResourceName}/{clusterName}/providers/Microsoft.KubernetesConfiguration/sourceControlConfigurations"
    }