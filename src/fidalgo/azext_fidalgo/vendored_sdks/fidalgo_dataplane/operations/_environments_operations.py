# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_list_by_project_request(
    project_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    top = kwargs.pop('top', None)  # type: Optional[int]

    api_version = "2021-09-01-privatepreview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/projects/{projectName}/environments')
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if top is not None:
        query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    project_name,  # type: str
    environment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2021-09-01-privatepreview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/projects/{projectName}/environments/{environmentName}')
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, 'str'),
        "environmentName": _SERIALIZER.url("environment_name", environment_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    project_name,  # type: str
    environment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-09-01-privatepreview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/projects/{projectName}/environments/{environmentName}')
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, 'str'),
        "environmentName": _SERIALIZER.url("environment_name", environment_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_update_request(
    project_name,  # type: str
    environment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-09-01-privatepreview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/projects/{projectName}/environments/{environmentName}')
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, 'str'),
        "environmentName": _SERIALIZER.url("environment_name", environment_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_delete_request(
    project_name,  # type: str
    environment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = "2021-09-01-privatepreview"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/projects/{projectName}/environments/{environmentName}')
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, 'str'),
        "environmentName": _SERIALIZER.url("environment_name", environment_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_deploy_request(
    project_name,  # type: str
    environment_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/projects/{projectName}/environments/{environmentName}/deploy')
    path_format_arguments = {
        "projectName": _SERIALIZER.url("project_name", project_name, 'str'),
        "environmentName": _SERIALIZER.url("environment_name", environment_name, 'str'),
    }

    url = _format_url_section(url, **path_format_arguments)

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class EnvironmentsOperations(object):
    """EnvironmentsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.fidalgo.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list_by_project(
        self,
        dev_center,  # type: str
        project_name,  # type: str
        fidalgo_dns_suffix="devcenters.fidalgo.azure.com",  # type: str
        top=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.EnvironmentListResult"]
        """Lists the environments for a project.

        :param dev_center: The DevCenter to operate on.
        :type dev_center: str
        :param project_name: The Fidalgo Project upon which to execute operations.
        :type project_name: str
        :param fidalgo_dns_suffix: The DNS suffix used as the base for all fidalgo requests.
        :type fidalgo_dns_suffix: str
        :param top: The maximum number of resources to return from the operation. Example: '$top=10'.
        :type top: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either EnvironmentListResult or the result of
         cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.fidalgo.models.EnvironmentListResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EnvironmentListResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_project_request(
                    project_name=project_name,
                    top=top,
                    template_url=self.list_by_project.metadata['url'],
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
                    "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

            else:
                
                request = build_list_by_project_request(
                    project_name=project_name,
                    top=top,
                    template_url=next_link,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
                    "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)

                path_format_arguments = {
                    "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
                    "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
                }
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("EnvironmentListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list_by_project.metadata = {'url': '/projects/{projectName}/environments'}  # type: ignore

    @distributed_trace
    def get(
        self,
        dev_center,  # type: str
        project_name,  # type: str
        environment_name,  # type: str
        fidalgo_dns_suffix="devcenters.fidalgo.azure.com",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Environment"
        """Gets an environment.

        :param dev_center: The DevCenter to operate on.
        :type dev_center: str
        :param project_name: The Fidalgo Project upon which to execute operations.
        :type project_name: str
        :param environment_name: The name of the environment.
        :type environment_name: str
        :param fidalgo_dns_suffix: The DNS suffix used as the base for all fidalgo requests.
        :type fidalgo_dns_suffix: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Environment, or the result of cls(response)
        :rtype: ~azure.fidalgo.models.Environment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Environment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_get_request(
            project_name=project_name,
            environment_name=environment_name,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
            "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize('Environment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': '/projects/{projectName}/environments/{environmentName}'}  # type: ignore


    @distributed_trace
    def create_or_update(
        self,
        dev_center,  # type: str
        project_name,  # type: str
        environment_name,  # type: str
        body,  # type: "_models.Environment"
        fidalgo_dns_suffix="devcenters.fidalgo.azure.com",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Environment"
        """Creates or updates an environment.

        :param dev_center: The DevCenter to operate on.
        :type dev_center: str
        :param project_name: The Fidalgo Project upon which to execute operations.
        :type project_name: str
        :param environment_name: The name of the environment.
        :type environment_name: str
        :param body: Represents a environment.
        :type body: ~azure.fidalgo.models.Environment
        :param fidalgo_dns_suffix: The DNS suffix used as the base for all fidalgo requests.
        :type fidalgo_dns_suffix: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Environment, or the result of cls(response)
        :rtype: ~azure.fidalgo.models.Environment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Environment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        json = self._serialize.body(body, 'Environment')

        request = build_create_or_update_request(
            project_name=project_name,
            environment_name=environment_name,
            content_type=content_type,
            json=json,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
            "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('Environment', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Environment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': '/projects/{projectName}/environments/{environmentName}'}  # type: ignore


    @distributed_trace
    def update(
        self,
        dev_center,  # type: str
        project_name,  # type: str
        environment_name,  # type: str
        body,  # type: "_models.EnvironmentUpdate"
        fidalgo_dns_suffix="devcenters.fidalgo.azure.com",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.Environment"
        """Partially updates an environment.

        :param dev_center: The DevCenter to operate on.
        :type dev_center: str
        :param project_name: The Fidalgo Project upon which to execute operations.
        :type project_name: str
        :param environment_name: The name of the environment.
        :type environment_name: str
        :param body: Updatable environment properties.
        :type body: ~azure.fidalgo.models.EnvironmentUpdate
        :param fidalgo_dns_suffix: The DNS suffix used as the base for all fidalgo requests.
        :type fidalgo_dns_suffix: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Environment, or the result of cls(response)
        :rtype: ~azure.fidalgo.models.Environment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Environment"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        json = self._serialize.body(body, 'EnvironmentUpdate')

        request = build_update_request(
            project_name=project_name,
            environment_name=environment_name,
            content_type=content_type,
            json=json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
            "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if response.status_code == 200:
            deserialized = self._deserialize('Environment', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('Environment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': '/projects/{projectName}/environments/{environmentName}'}  # type: ignore


    @distributed_trace
    def delete(
        self,
        dev_center,  # type: str
        project_name,  # type: str
        environment_name,  # type: str
        fidalgo_dns_suffix="devcenters.fidalgo.azure.com",  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes an environment and all it's associated resources.

        :param dev_center: The DevCenter to operate on.
        :type dev_center: str
        :param project_name: The Fidalgo Project upon which to execute operations.
        :type project_name: str
        :param environment_name: The name of the environment.
        :type environment_name: str
        :param fidalgo_dns_suffix: The DNS suffix used as the base for all fidalgo requests.
        :type fidalgo_dns_suffix: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        
        request = build_delete_request(
            project_name=project_name,
            environment_name=environment_name,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
            "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': '/projects/{projectName}/environments/{environmentName}'}  # type: ignore


    @distributed_trace
    def deploy(
        self,
        dev_center,  # type: str
        project_name,  # type: str
        environment_name,  # type: str
        fidalgo_dns_suffix="devcenters.fidalgo.azure.com",  # type: str
        deployment=None,  # type: Optional["_models.EnvironmentDeploy"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deploys an environment's resources.

        :param dev_center: The DevCenter to operate on.
        :type dev_center: str
        :param project_name: The Fidalgo Project upon which to execute operations.
        :type project_name: str
        :param environment_name: The name of the environment.
        :type environment_name: str
        :param fidalgo_dns_suffix: The DNS suffix used as the base for all fidalgo requests.
        :type fidalgo_dns_suffix: str
        :param deployment: Deployment properties overriding the environment's default values.
        :type deployment: ~azure.fidalgo.models.EnvironmentDeploy
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        if deployment is not None:
            json = self._serialize.body(deployment, 'EnvironmentDeploy')
        else:
            json = None

        request = build_deploy_request(
            project_name=project_name,
            environment_name=environment_name,
            content_type=content_type,
            json=json,
            template_url=self.deploy.metadata['url'],
        )
        request = _convert_request(request)
        path_format_arguments = {
            "devCenter": self._serialize.url("dev_center", dev_center, 'str', skip_quote=True),
            "fidalgoDnsSuffix": self._serialize.url("fidalgo_dns_suffix", fidalgo_dns_suffix, 'str', skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client.send_request(request, stream=False, _return_pipeline_response=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.CloudError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        if cls:
            return cls(pipeline_response, None, {})

    deploy.metadata = {'url': '/projects/{projectName}/environments/{environmentName}/deploy'}  # type: ignore
