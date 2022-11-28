# coding: utf-8

# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# IBM OpenAPI SDK Code Generator Version: 3.60.0-13f6e1ba-20221019-164457

"""
This swagger document describes the options and endpoints of the Toolchain API.<br><br>
All calls require an <strong>Authorization</strong> HTTP header to be set with a bearer
token, which can be generated using the <a
href="https://cloud.ibm.com/apidocs/iam-identity-token-api">Identity and Access Management
(IAM) API</a>.<br><br>Note that all resources must have a corresponding
<b>resource_group_id</b> to use the API, resources within a Cloud Foundry organization
cannot be accessed or modified using the API.

API Version: 2.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class CdToolchainV2(BaseService):
    """The CD Toolchain V2 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2'
    DEFAULT_SERVICE_NAME = 'cd_toolchain'

    REGIONAL_ENDPOINTS = {
        'us-south': 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the us-south region
        'us-east': 'https://api.us-east.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the us-east region
        'eu-de': 'https://api.eu-de.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the eu-de region
        'eu-gb': 'https://api.eu-gb.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the eu-gb region
        'jp-osa': 'https://api.jp-osa.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the jp-osa region
        'jp-tok': 'https://api.jp-tok.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the jp-tok region
        'au-syd': 'https://api.au-syd.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the au-syd region
        'ca-tor': 'https://api.ca-tor.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the ca-tor region
        'br-sao': 'https://api.br-sao.devops.cloud.ibm.com/toolchain/v2', # The toolchain API endpoint in the br-sao region
    }

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CdToolchainV2':
        """
        Return a new client for the CD Toolchain service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    @classmethod
    def get_service_url_for_region(
        cls,
        region: str,
    ) -> str:
        """
        Returns the service URL associated with the specified region.
        :param str region: a string representing the region
        :return: The service URL associated with the specified region or None
                 if no mapping for the region exists
        :rtype: str
        """
        return cls.REGIONAL_ENDPOINTS.get(region, None)

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the CD Toolchain service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Toolchains
    #########################


    def list_toolchains(self,
        resource_group_id: str,
        *,
        limit: int = None,
        start: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of toolchains.

        Returns a list of toolchains that the caller is authorized to access and that
        meets the provided query parameters.

        :param str resource_group_id: The resource group ID where the toolchains
               exist.
        :param int limit: (optional) Limit the number of results.
        :param str start: (optional) Pagination token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainCollection` object
        """

        if not resource_group_id:
            raise ValueError('resource_group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_toolchains')
        headers.update(sdk_headers)

        params = {
            'resource_group_id': resource_group_id,
            'limit': limit,
            'start': start
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/toolchains'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_toolchain(self,
        name: str,
        resource_group_id: str,
        *,
        description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a toolchain.

        Creates a new toolchain based off the provided parameters in the body.

        :param str name: Toolchain name.
        :param str resource_group_id: Resource group where toolchain will be
               created.
        :param str description: (optional) Describes the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainPost` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if resource_group_id is None:
            raise ValueError('resource_group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_toolchain')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'resource_group_id': resource_group_id,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/toolchains'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_toolchain_by_id(self,
        toolchain_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a toolchain.

        Returns data for a single toolchain identified by its ID.

        :param str toolchain_id: ID of the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Toolchain` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_toolchain_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_toolchain(self,
        toolchain_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a toolchain.

        Delete the toolchain with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_toolchain')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_toolchain(self,
        toolchain_id: str,
        toolchain_prototype_patch: 'ToolchainPrototypePatch',
        **kwargs
    ) -> DetailedResponse:
        """
        Update a toolchain.

        Update the toolchain with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param ToolchainPrototypePatch toolchain_prototype_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainPatch` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if toolchain_prototype_patch is None:
            raise ValueError('toolchain_prototype_patch must be provided')
        if isinstance(toolchain_prototype_patch, ToolchainPrototypePatch):
            toolchain_prototype_patch = convert_model(toolchain_prototype_patch)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_toolchain')
        headers.update(sdk_headers)

        data = json.dumps(toolchain_prototype_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Tools
    #########################


    def list_tools(self,
        toolchain_id: str,
        *,
        limit: int = None,
        start: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of tools bound to a toolchain.

        Returns a list of tools bound to a toolchain that the caller is authorized to
        access and that meet the provided query parameters.

        :param str toolchain_id: ID of the toolchain that tools are bound to.
        :param int limit: (optional) Limit the number of results.
        :param str start: (optional) Pagination token.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainToolCollection` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_tools')
        headers.update(sdk_headers)

        params = {
            'limit': limit,
            'start': start
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_tool(self,
        toolchain_id: str,
        tool_type_id: str,
        *,
        name: str = None,
        parameters: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a tool.

        Provisions a new tool based off the provided parameters in the body and binds it
        to the specified toolchain.

        :param str toolchain_id: ID of the toolchain to bind the tool to.
        :param str tool_type_id: The unique short name of the tool that should be
               provisioned. A table of `tool_type_id` values corresponding to each tool
               integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str name: (optional) Name of the tool.
        :param dict parameters: (optional) Unique key-value pairs representing
               parameters to be used to create the tool. A list of parameters for each
               tool integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainToolPost` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if tool_type_id is None:
            raise ValueError('tool_type_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tool')
        headers.update(sdk_headers)

        data = {
            'tool_type_id': tool_type_id,
            'name': name,
            'parameters': parameters
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id']
        path_param_values = self.encode_path_vars(toolchain_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_tool_by_id(self,
        toolchain_id: str,
        tool_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a tool.

        Returns a tool that is bound to the provided toolchain.

        :param str toolchain_id: ID of the toolchain.
        :param str tool_id: ID of the tool bound to the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainTool` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if not tool_id:
            raise ValueError('tool_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tool_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id', 'tool_id']
        path_param_values = self.encode_path_vars(toolchain_id, tool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools/{tool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_tool(self,
        toolchain_id: str,
        tool_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a tool.

        Delete the tool with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param str tool_id: ID of the tool bound to the toolchain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if not tool_id:
            raise ValueError('tool_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_tool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['toolchain_id', 'tool_id']
        path_param_values = self.encode_path_vars(toolchain_id, tool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools/{tool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_tool(self,
        toolchain_id: str,
        tool_id: str,
        toolchain_tool_prototype_patch: 'ToolchainToolPrototypePatch',
        **kwargs
    ) -> DetailedResponse:
        """
        Update a tool.

        Update the tool with the specified ID.

        :param str toolchain_id: ID of the toolchain.
        :param str tool_id: ID of the tool bound to the toolchain.
        :param ToolchainToolPrototypePatch toolchain_tool_prototype_patch:
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ToolchainToolPatch` object
        """

        if not toolchain_id:
            raise ValueError('toolchain_id must be provided')
        if not tool_id:
            raise ValueError('tool_id must be provided')
        if toolchain_tool_prototype_patch is None:
            raise ValueError('toolchain_tool_prototype_patch must be provided')
        if isinstance(toolchain_tool_prototype_patch, ToolchainToolPrototypePatch):
            toolchain_tool_prototype_patch = convert_model(toolchain_tool_prototype_patch)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_tool')
        headers.update(sdk_headers)

        data = json.dumps(toolchain_tool_prototype_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['toolchain_id', 'tool_id']
        path_param_values = self.encode_path_vars(toolchain_id, tool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/toolchains/{toolchain_id}/tools/{tool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class ToolModel():
    """
    Model describing tool resource.

    :attr str id: Tool ID.
    :attr str resource_group_id: Resource group where the tool is located.
    :attr str crn: Tool CRN.
    :attr str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str toolchain_id: ID of toolchain which the tool is bound to.
    :attr str toolchain_crn: CRN of toolchain which the tool is bound to.
    :attr str href: URI representing the tool.
    :attr ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :attr str name: (optional) Tool name.
    :attr datetime updated_at: Latest tool update timestamp.
    :attr dict parameters: Unique key-value pairs representing parameters to be used
          to create the tool. A list of parameters for each tool integration can be found
          in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str state: Current configuration state of the tool.
    """

    def __init__(self,
                 id: str,
                 resource_group_id: str,
                 crn: str,
                 tool_type_id: str,
                 toolchain_id: str,
                 toolchain_crn: str,
                 href: str,
                 referent: 'ToolModelReferent',
                 updated_at: datetime,
                 parameters: dict,
                 state: str,
                 *,
                 name: str = None) -> None:
        """
        Initialize a ToolModel object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Tool name.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolModel':
        """Initialize a ToolModel object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ToolModel JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolModel JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ToolModel JSON')
        if 'tool_type_id' in _dict:
            args['tool_type_id'] = _dict.get('tool_type_id')
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolModel JSON')
        if 'toolchain_id' in _dict:
            args['toolchain_id'] = _dict.get('toolchain_id')
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolModel JSON')
        if 'toolchain_crn' in _dict:
            args['toolchain_crn'] = _dict.get('toolchain_crn')
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolModel JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolModel JSON')
        if 'referent' in _dict:
            args['referent'] = ToolModelReferent.from_dict(_dict.get('referent'))
        else:
            raise ValueError('Required property \'referent\' not present in ToolModel JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolModel JSON')
        if 'parameters' in _dict:
            args['parameters'] = _dict.get('parameters')
        else:
            raise ValueError('Required property \'parameters\' not present in ToolModel JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ToolModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """
        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolModelReferent():
    """
    Information on URIs to access this resource through the UI or API.

    :attr str ui_href: (optional) URI representing this resource through the UI.
    :attr str api_href: (optional) URI representing this resource through an API.
    """

    def __init__(self,
                 *,
                 ui_href: str = None,
                 api_href: str = None) -> None:
        """
        Initialize a ToolModelReferent object.

        :param str ui_href: (optional) URI representing this resource through the
               UI.
        :param str api_href: (optional) URI representing this resource through an
               API.
        """
        self.ui_href = ui_href
        self.api_href = api_href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolModelReferent':
        """Initialize a ToolModelReferent object from a json dictionary."""
        args = {}
        if 'ui_href' in _dict:
            args['ui_href'] = _dict.get('ui_href')
        if 'api_href' in _dict:
            args['api_href'] = _dict.get('api_href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolModelReferent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'api_href') and self.api_href is not None:
            _dict['api_href'] = self.api_href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolModelReferent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolModelReferent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolModelReferent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Toolchain():
    """
    Response structure for GET toolchains.

    :attr str id: Toolchain ID.
    :attr str name: Toolchain name.
    :attr str description: Toolchain description.
    :attr str account_id: Account ID where toolchain can be found.
    :attr str location: Toolchain region.
    :attr str resource_group_id: Resource group where the toolchain is located.
    :attr str crn: Toolchain CRN.
    :attr str href: URI that can be used to retrieve toolchain.
    :attr str ui_href: URL of a user-facing user interface for this toolchain.
    :attr datetime created_at: Toolchain creation timestamp.
    :attr datetime updated_at: Latest toolchain update timestamp.
    :attr str created_by: Identity that created the toolchain.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 account_id: str,
                 location: str,
                 resource_group_id: str,
                 crn: str,
                 href: str,
                 ui_href: str,
                 created_at: datetime,
                 updated_at: datetime,
                 created_by: str) -> None:
        """
        Initialize a Toolchain object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Toolchain description.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Toolchain':
        """Initialize a Toolchain object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Toolchain JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Toolchain JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in Toolchain JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in Toolchain JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in Toolchain JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in Toolchain JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in Toolchain JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in Toolchain JSON')
        if 'ui_href' in _dict:
            args['ui_href'] = _dict.get('ui_href')
        else:
            raise ValueError('Required property \'ui_href\' not present in Toolchain JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in Toolchain JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in Toolchain JSON')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in Toolchain JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Toolchain object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Toolchain object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Toolchain') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Toolchain') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainCollection():
    """
    Response structure for GET toolchains.

    :attr int total_count: Total number of toolchains found in collection.
    :attr int limit: Maximum number of toolchains returned from collection.
    :attr ToolchainCollectionFirst first: Information about retrieving first
          toolchain results from the collection.
    :attr ToolchainCollectionPrevious previous: (optional) Information about
          retrieving previous toolchain results from the collection.
    :attr ToolchainCollectionNext next: (optional) Information about retrieving next
          toolchain results from the collection.
    :attr ToolchainCollectionLast last: Information about retrieving last toolchain
          results from the collection.
    :attr List[ToolchainModel] toolchains: (optional) Toolchain results returned
          from the collection.
    """

    def __init__(self,
                 total_count: int,
                 limit: int,
                 first: 'ToolchainCollectionFirst',
                 last: 'ToolchainCollectionLast',
                 *,
                 previous: 'ToolchainCollectionPrevious' = None,
                 next: 'ToolchainCollectionNext' = None,
                 toolchains: List['ToolchainModel'] = None) -> None:
        """
        Initialize a ToolchainCollection object.

        :param int total_count: Total number of toolchains found in collection.
        :param int limit: Maximum number of toolchains returned from collection.
        :param ToolchainCollectionFirst first: Information about retrieving first
               toolchain results from the collection.
        :param ToolchainCollectionLast last: Information about retrieving last
               toolchain results from the collection.
        :param ToolchainCollectionPrevious previous: (optional) Information about
               retrieving previous toolchain results from the collection.
        :param ToolchainCollectionNext next: (optional) Information about
               retrieving next toolchain results from the collection.
        :param List[ToolchainModel] toolchains: (optional) Toolchain results
               returned from the collection.
        """
        self.total_count = total_count
        self.limit = limit
        self.first = first
        self.previous = previous
        self.next = next
        self.last = last
        self.toolchains = toolchains

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollection':
        """Initialize a ToolchainCollection object from a json dictionary."""
        args = {}
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ToolchainCollection JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ToolchainCollection JSON')
        if 'first' in _dict:
            args['first'] = ToolchainCollectionFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ToolchainCollection JSON')
        if 'previous' in _dict:
            args['previous'] = ToolchainCollectionPrevious.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = ToolchainCollectionNext.from_dict(_dict.get('next'))
        if 'last' in _dict:
            args['last'] = ToolchainCollectionLast.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in ToolchainCollection JSON')
        if 'toolchains' in _dict:
            args['toolchains'] = [ToolchainModel.from_dict(x) for x in _dict.get('toolchains')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'toolchains') and self.toolchains is not None:
            _dict['toolchains'] = [x.to_dict() for x in self.toolchains]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainCollectionFirst():
    """
    Information about retrieving first toolchain results from the collection.

    :attr str href: URI that can be used to get first results from the collection.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a ToolchainCollectionFirst object.

        :param str href: URI that can be used to get first results from the
               collection.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionFirst':
        """Initialize a ToolchainCollectionFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionFirst JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainCollectionLast():
    """
    Information about retrieving last toolchain results from the collection.

    :attr str start: (optional) Cursor that can be set as the 'start' query
          parameter to get the last set of toolchain collections.
    :attr str href: URI that can be used to get last results from the collection.
    """

    def __init__(self,
                 href: str,
                 *,
                 start: str = None) -> None:
        """
        Initialize a ToolchainCollectionLast object.

        :param str href: URI that can be used to get last results from the
               collection.
        :param str start: (optional) Cursor that can be set as the 'start' query
               parameter to get the last set of toolchain collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionLast':
        """Initialize a ToolchainCollectionLast object from a json dictionary."""
        args = {}
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionLast JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionLast object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionLast object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionLast') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionLast') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainCollectionNext():
    """
    Information about retrieving next toolchain results from the collection.

    :attr str start: (optional) Cursor that can be set as the 'start' query
          parameter to get the next set of toolchain collections.
    :attr str href: URI that can be used to get next results from the collection.
    """

    def __init__(self,
                 href: str,
                 *,
                 start: str = None) -> None:
        """
        Initialize a ToolchainCollectionNext object.

        :param str href: URI that can be used to get next results from the
               collection.
        :param str start: (optional) Cursor that can be set as the 'start' query
               parameter to get the next set of toolchain collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionNext':
        """Initialize a ToolchainCollectionNext object from a json dictionary."""
        args = {}
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionNext JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainCollectionPrevious():
    """
    Information about retrieving previous toolchain results from the collection.

    :attr str start: (optional) Cursor that can be set as the 'start' query
          parameter to get the previous set of toolchain collections.
    :attr str href: URI that can be used to get previous results from the
          collection.
    """

    def __init__(self,
                 href: str,
                 *,
                 start: str = None) -> None:
        """
        Initialize a ToolchainCollectionPrevious object.

        :param str href: URI that can be used to get previous results from the
               collection.
        :param str start: (optional) Cursor that can be set as the 'start' query
               parameter to get the previous set of toolchain collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainCollectionPrevious':
        """Initialize a ToolchainCollectionPrevious object from a json dictionary."""
        args = {}
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainCollectionPrevious JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainCollectionPrevious object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainCollectionPrevious object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainCollectionPrevious') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainCollectionPrevious') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainModel():
    """
    Model describing toolchain resource.

    :attr str id: Toolchain ID.
    :attr str name: Toolchain name.
    :attr str description: Toolchain description.
    :attr str account_id: Account ID where toolchain can be found.
    :attr str location: Toolchain region.
    :attr str resource_group_id: Resource group where the toolchain is located.
    :attr str crn: Toolchain CRN.
    :attr str href: URI that can be used to retrieve toolchain.
    :attr str ui_href: URL of a user-facing user interface for this toolchain.
    :attr datetime created_at: Toolchain creation timestamp.
    :attr datetime updated_at: Latest toolchain update timestamp.
    :attr str created_by: Identity that created the toolchain.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 account_id: str,
                 location: str,
                 resource_group_id: str,
                 crn: str,
                 href: str,
                 ui_href: str,
                 created_at: datetime,
                 updated_at: datetime,
                 created_by: str) -> None:
        """
        Initialize a ToolchainModel object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Toolchain description.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainModel':
        """Initialize a ToolchainModel object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ToolchainModel JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ToolchainModel JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in ToolchainModel JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ToolchainModel JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in ToolchainModel JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainModel JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainModel JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainModel JSON')
        if 'ui_href' in _dict:
            args['ui_href'] = _dict.get('ui_href')
        else:
            raise ValueError('Required property \'ui_href\' not present in ToolchainModel JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ToolchainModel JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainModel JSON')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in ToolchainModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainPatch():
    """
    Response structure for PATCH toolchain.

    :attr str id: Toolchain ID.
    :attr str name: Toolchain name.
    :attr str description: Toolchain description.
    :attr str account_id: Account ID where toolchain can be found.
    :attr str location: Toolchain region.
    :attr str resource_group_id: Resource group where the toolchain is located.
    :attr str crn: Toolchain CRN.
    :attr str href: URI that can be used to retrieve toolchain.
    :attr str ui_href: URL of a user-facing user interface for this toolchain.
    :attr datetime created_at: Toolchain creation timestamp.
    :attr datetime updated_at: Latest toolchain update timestamp.
    :attr str created_by: Identity that created the toolchain.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 account_id: str,
                 location: str,
                 resource_group_id: str,
                 crn: str,
                 href: str,
                 ui_href: str,
                 created_at: datetime,
                 updated_at: datetime,
                 created_by: str) -> None:
        """
        Initialize a ToolchainPatch object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Toolchain description.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainPatch':
        """Initialize a ToolchainPatch object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ToolchainPatch JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ToolchainPatch JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in ToolchainPatch JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ToolchainPatch JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in ToolchainPatch JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainPatch JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainPatch JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainPatch JSON')
        if 'ui_href' in _dict:
            args['ui_href'] = _dict.get('ui_href')
        else:
            raise ValueError('Required property \'ui_href\' not present in ToolchainPatch JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ToolchainPatch JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainPatch JSON')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in ToolchainPatch JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainPost():
    """
    Response structure for POST toolchain.

    :attr str id: Toolchain ID.
    :attr str name: Toolchain name.
    :attr str description: Toolchain description.
    :attr str account_id: Account ID where toolchain can be found.
    :attr str location: Toolchain region.
    :attr str resource_group_id: Resource group where the toolchain is located.
    :attr str crn: Toolchain CRN.
    :attr str href: URI that can be used to retrieve toolchain.
    :attr str ui_href: URL of a user-facing user interface for this toolchain.
    :attr datetime created_at: Toolchain creation timestamp.
    :attr datetime updated_at: Latest toolchain update timestamp.
    :attr str created_by: Identity that created the toolchain.
    """

    def __init__(self,
                 id: str,
                 name: str,
                 description: str,
                 account_id: str,
                 location: str,
                 resource_group_id: str,
                 crn: str,
                 href: str,
                 ui_href: str,
                 created_at: datetime,
                 updated_at: datetime,
                 created_by: str) -> None:
        """
        Initialize a ToolchainPost object.

        :param str id: Toolchain ID.
        :param str name: Toolchain name.
        :param str description: Toolchain description.
        :param str account_id: Account ID where toolchain can be found.
        :param str location: Toolchain region.
        :param str resource_group_id: Resource group where the toolchain is
               located.
        :param str crn: Toolchain CRN.
        :param str href: URI that can be used to retrieve toolchain.
        :param str ui_href: URL of a user-facing user interface for this toolchain.
        :param datetime created_at: Toolchain creation timestamp.
        :param datetime updated_at: Latest toolchain update timestamp.
        :param str created_by: Identity that created the toolchain.
        """
        self.id = id
        self.name = name
        self.description = description
        self.account_id = account_id
        self.location = location
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.href = href
        self.ui_href = ui_href
        self.created_at = created_at
        self.updated_at = updated_at
        self.created_by = created_by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainPost':
        """Initialize a ToolchainPost object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ToolchainPost JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in ToolchainPost JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in ToolchainPost JSON')
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        else:
            raise ValueError('Required property \'account_id\' not present in ToolchainPost JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError('Required property \'location\' not present in ToolchainPost JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainPost JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainPost JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainPost JSON')
        if 'ui_href' in _dict:
            args['ui_href'] = _dict.get('ui_href')
        else:
            raise ValueError('Required property \'ui_href\' not present in ToolchainPost JSON')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        else:
            raise ValueError('Required property \'created_at\' not present in ToolchainPost JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainPost JSON')
        if 'created_by' in _dict:
            args['created_by'] = _dict.get('created_by')
        else:
            raise ValueError('Required property \'created_by\' not present in ToolchainPost JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainPost object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'ui_href') and self.ui_href is not None:
            _dict['ui_href'] = self.ui_href
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_by') and self.created_by is not None:
            _dict['created_by'] = self.created_by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainPost object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainPost') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainPost') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainPrototypePatch():
    """
    Body structure for the update toolchain PATCH request.

    :attr str name: (optional) The name of the toolchain.
    :attr str description: (optional) An optional description.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None) -> None:
        """
        Initialize a ToolchainPrototypePatch object.

        :param str name: (optional) The name of the toolchain.
        :param str description: (optional) An optional description.
        """
        self.name = name
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainPrototypePatch':
        """Initialize a ToolchainPrototypePatch object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainPrototypePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainPrototypePatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainPrototypePatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainPrototypePatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainTool():
    """
    Response structure for GET tool.

    :attr str id: Tool ID.
    :attr str resource_group_id: Resource group where the tool is located.
    :attr str crn: Tool CRN.
    :attr str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str toolchain_id: ID of toolchain which the tool is bound to.
    :attr str toolchain_crn: CRN of toolchain which the tool is bound to.
    :attr str href: URI representing the tool.
    :attr ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :attr str name: (optional) Tool name.
    :attr datetime updated_at: Latest tool update timestamp.
    :attr dict parameters: Unique key-value pairs representing parameters to be used
          to create the tool. A list of parameters for each tool integration can be found
          in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str state: Current configuration state of the tool.
    """

    def __init__(self,
                 id: str,
                 resource_group_id: str,
                 crn: str,
                 tool_type_id: str,
                 toolchain_id: str,
                 toolchain_crn: str,
                 href: str,
                 referent: 'ToolModelReferent',
                 updated_at: datetime,
                 parameters: dict,
                 state: str,
                 *,
                 name: str = None) -> None:
        """
        Initialize a ToolchainTool object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Tool name.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainTool':
        """Initialize a ToolchainTool object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ToolchainTool JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainTool JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainTool JSON')
        if 'tool_type_id' in _dict:
            args['tool_type_id'] = _dict.get('tool_type_id')
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolchainTool JSON')
        if 'toolchain_id' in _dict:
            args['toolchain_id'] = _dict.get('toolchain_id')
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolchainTool JSON')
        if 'toolchain_crn' in _dict:
            args['toolchain_crn'] = _dict.get('toolchain_crn')
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolchainTool JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainTool JSON')
        if 'referent' in _dict:
            args['referent'] = ToolModelReferent.from_dict(_dict.get('referent'))
        else:
            raise ValueError('Required property \'referent\' not present in ToolchainTool JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainTool JSON')
        if 'parameters' in _dict:
            args['parameters'] = _dict.get('parameters')
        else:
            raise ValueError('Required property \'parameters\' not present in ToolchainTool JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ToolchainTool JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainTool object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainTool object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainTool') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainTool') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """
        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolchainToolCollection():
    """
    Response structure for GET tools.

    :attr int limit: Maximum number of tools returned from collection.
    :attr int total_count: Total number of tools found in collection.
    :attr ToolchainToolCollectionFirst first: Information about retrieving first
          tool results from the collection.
    :attr ToolchainToolCollectionPrevious previous: (optional) Information about
          retrieving previous tool results from the collection.
    :attr ToolchainToolCollectionNext next: (optional) Information about retrieving
          next tool results from the collection.
    :attr ToolchainToolCollectionLast last: Information about retrieving last tool
          results from the collection.
    :attr List[ToolModel] tools: Tool results returned from the collection.
    """

    def __init__(self,
                 limit: int,
                 total_count: int,
                 first: 'ToolchainToolCollectionFirst',
                 last: 'ToolchainToolCollectionLast',
                 tools: List['ToolModel'],
                 *,
                 previous: 'ToolchainToolCollectionPrevious' = None,
                 next: 'ToolchainToolCollectionNext' = None) -> None:
        """
        Initialize a ToolchainToolCollection object.

        :param int limit: Maximum number of tools returned from collection.
        :param int total_count: Total number of tools found in collection.
        :param ToolchainToolCollectionFirst first: Information about retrieving
               first tool results from the collection.
        :param ToolchainToolCollectionLast last: Information about retrieving last
               tool results from the collection.
        :param List[ToolModel] tools: Tool results returned from the collection.
        :param ToolchainToolCollectionPrevious previous: (optional) Information
               about retrieving previous tool results from the collection.
        :param ToolchainToolCollectionNext next: (optional) Information about
               retrieving next tool results from the collection.
        """
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.previous = previous
        self.next = next
        self.last = last
        self.tools = tools

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollection':
        """Initialize a ToolchainToolCollection object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ToolchainToolCollection JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ToolchainToolCollection JSON')
        if 'first' in _dict:
            args['first'] = ToolchainToolCollectionFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ToolchainToolCollection JSON')
        if 'previous' in _dict:
            args['previous'] = ToolchainToolCollectionPrevious.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = ToolchainToolCollectionNext.from_dict(_dict.get('next'))
        if 'last' in _dict:
            args['last'] = ToolchainToolCollectionLast.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in ToolchainToolCollection JSON')
        if 'tools' in _dict:
            args['tools'] = [ToolModel.from_dict(x) for x in _dict.get('tools')]
        else:
            raise ValueError('Required property \'tools\' not present in ToolchainToolCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'tools') and self.tools is not None:
            _dict['tools'] = [x.to_dict() for x in self.tools]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainToolCollectionFirst():
    """
    Information about retrieving first tool results from the collection.

    :attr str href: URI that can be used to get first results from the collection.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a ToolchainToolCollectionFirst object.

        :param str href: URI that can be used to get first results from the
               collection.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionFirst':
        """Initialize a ToolchainToolCollectionFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionFirst JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainToolCollectionLast():
    """
    Information about retrieving last tool results from the collection.

    :attr str start: (optional) Cursor that can be used to get the last set of tool
          collections.
    :attr str href: URI that can be used to get last results from the collection.
    """

    def __init__(self,
                 href: str,
                 *,
                 start: str = None) -> None:
        """
        Initialize a ToolchainToolCollectionLast object.

        :param str href: URI that can be used to get last results from the
               collection.
        :param str start: (optional) Cursor that can be used to get the last set of
               tool collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionLast':
        """Initialize a ToolchainToolCollectionLast object from a json dictionary."""
        args = {}
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionLast JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionLast object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionLast object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionLast') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionLast') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainToolCollectionNext():
    """
    Information about retrieving next tool results from the collection.

    :attr str start: (optional) Cursor that can be used to get the next set of tool
          collections.
    :attr str href: URI that can be used to get next results from the collection.
    """

    def __init__(self,
                 href: str,
                 *,
                 start: str = None) -> None:
        """
        Initialize a ToolchainToolCollectionNext object.

        :param str href: URI that can be used to get next results from the
               collection.
        :param str start: (optional) Cursor that can be used to get the next set of
               tool collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionNext':
        """Initialize a ToolchainToolCollectionNext object from a json dictionary."""
        args = {}
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionNext JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainToolCollectionPrevious():
    """
    Information about retrieving previous tool results from the collection.

    :attr str start: (optional) Cursor that can be used to get the previous set of
          tool collections.
    :attr str href: URI that can be used to get previous results from the
          collection.
    """

    def __init__(self,
                 href: str,
                 *,
                 start: str = None) -> None:
        """
        Initialize a ToolchainToolCollectionPrevious object.

        :param str href: URI that can be used to get previous results from the
               collection.
        :param str start: (optional) Cursor that can be used to get the previous
               set of tool collections.
        """
        self.start = start
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolCollectionPrevious':
        """Initialize a ToolchainToolCollectionPrevious object from a json dictionary."""
        args = {}
        if 'start' in _dict:
            args['start'] = _dict.get('start')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolCollectionPrevious JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolCollectionPrevious object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start') and self.start is not None:
            _dict['start'] = self.start
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolCollectionPrevious object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolCollectionPrevious') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolCollectionPrevious') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ToolchainToolPatch():
    """
    Response structure for PATCH tool.

    :attr str id: Tool ID.
    :attr str resource_group_id: Resource group where the tool is located.
    :attr str crn: Tool CRN.
    :attr str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str toolchain_id: ID of toolchain which the tool is bound to.
    :attr str toolchain_crn: CRN of toolchain which the tool is bound to.
    :attr str href: URI representing the tool.
    :attr ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :attr str name: (optional) Tool name.
    :attr datetime updated_at: Latest tool update timestamp.
    :attr dict parameters: Unique key-value pairs representing parameters to be used
          to create the tool. A list of parameters for each tool integration can be found
          in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str state: Current configuration state of the tool.
    """

    def __init__(self,
                 id: str,
                 resource_group_id: str,
                 crn: str,
                 tool_type_id: str,
                 toolchain_id: str,
                 toolchain_crn: str,
                 href: str,
                 referent: 'ToolModelReferent',
                 updated_at: datetime,
                 parameters: dict,
                 state: str,
                 *,
                 name: str = None) -> None:
        """
        Initialize a ToolchainToolPatch object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Tool name.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolPatch':
        """Initialize a ToolchainToolPatch object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ToolchainToolPatch JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainToolPatch JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainToolPatch JSON')
        if 'tool_type_id' in _dict:
            args['tool_type_id'] = _dict.get('tool_type_id')
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolchainToolPatch JSON')
        if 'toolchain_id' in _dict:
            args['toolchain_id'] = _dict.get('toolchain_id')
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolchainToolPatch JSON')
        if 'toolchain_crn' in _dict:
            args['toolchain_crn'] = _dict.get('toolchain_crn')
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolchainToolPatch JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolPatch JSON')
        if 'referent' in _dict:
            args['referent'] = ToolModelReferent.from_dict(_dict.get('referent'))
        else:
            raise ValueError('Required property \'referent\' not present in ToolchainToolPatch JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainToolPatch JSON')
        if 'parameters' in _dict:
            args['parameters'] = _dict.get('parameters')
        else:
            raise ValueError('Required property \'parameters\' not present in ToolchainToolPatch JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ToolchainToolPatch JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """
        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolchainToolPost():
    """
    POST tool response body.

    :attr str id: Tool ID.
    :attr str resource_group_id: Resource group where the tool is located.
    :attr str crn: Tool CRN.
    :attr str tool_type_id: The unique name of the provisioned tool. A table of
          `tool_type_id` values corresponding to each tool integration can be found in the
          <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str toolchain_id: ID of toolchain which the tool is bound to.
    :attr str toolchain_crn: CRN of toolchain which the tool is bound to.
    :attr str href: URI representing the tool.
    :attr ToolModelReferent referent: Information on URIs to access this resource
          through the UI or API.
    :attr str name: (optional) Tool name.
    :attr datetime updated_at: Latest tool update timestamp.
    :attr dict parameters: Unique key-value pairs representing parameters to be used
          to create the tool. A list of parameters for each tool integration can be found
          in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr str state: Current configuration state of the tool.
    """

    def __init__(self,
                 id: str,
                 resource_group_id: str,
                 crn: str,
                 tool_type_id: str,
                 toolchain_id: str,
                 toolchain_crn: str,
                 href: str,
                 referent: 'ToolModelReferent',
                 updated_at: datetime,
                 parameters: dict,
                 state: str,
                 *,
                 name: str = None) -> None:
        """
        Initialize a ToolchainToolPost object.

        :param str id: Tool ID.
        :param str resource_group_id: Resource group where the tool is located.
        :param str crn: Tool CRN.
        :param str tool_type_id: The unique name of the provisioned tool. A table
               of `tool_type_id` values corresponding to each tool integration can be
               found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str toolchain_id: ID of toolchain which the tool is bound to.
        :param str toolchain_crn: CRN of toolchain which the tool is bound to.
        :param str href: URI representing the tool.
        :param ToolModelReferent referent: Information on URIs to access this
               resource through the UI or API.
        :param datetime updated_at: Latest tool update timestamp.
        :param dict parameters: Unique key-value pairs representing parameters to
               be used to create the tool. A list of parameters for each tool integration
               can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param str state: Current configuration state of the tool.
        :param str name: (optional) Tool name.
        """
        self.id = id
        self.resource_group_id = resource_group_id
        self.crn = crn
        self.tool_type_id = tool_type_id
        self.toolchain_id = toolchain_id
        self.toolchain_crn = toolchain_crn
        self.href = href
        self.referent = referent
        self.name = name
        self.updated_at = updated_at
        self.parameters = parameters
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolPost':
        """Initialize a ToolchainToolPost object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ToolchainToolPost JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in ToolchainToolPost JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainToolPost JSON')
        if 'tool_type_id' in _dict:
            args['tool_type_id'] = _dict.get('tool_type_id')
        else:
            raise ValueError('Required property \'tool_type_id\' not present in ToolchainToolPost JSON')
        if 'toolchain_id' in _dict:
            args['toolchain_id'] = _dict.get('toolchain_id')
        else:
            raise ValueError('Required property \'toolchain_id\' not present in ToolchainToolPost JSON')
        if 'toolchain_crn' in _dict:
            args['toolchain_crn'] = _dict.get('toolchain_crn')
        else:
            raise ValueError('Required property \'toolchain_crn\' not present in ToolchainToolPost JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in ToolchainToolPost JSON')
        if 'referent' in _dict:
            args['referent'] = ToolModelReferent.from_dict(_dict.get('referent'))
        else:
            raise ValueError('Required property \'referent\' not present in ToolchainToolPost JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        else:
            raise ValueError('Required property \'updated_at\' not present in ToolchainToolPost JSON')
        if 'parameters' in _dict:
            args['parameters'] = _dict.get('parameters')
        else:
            raise ValueError('Required property \'parameters\' not present in ToolchainToolPost JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in ToolchainToolPost JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolPost object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'toolchain_id') and self.toolchain_id is not None:
            _dict['toolchain_id'] = self.toolchain_id
        if hasattr(self, 'toolchain_crn') and self.toolchain_crn is not None:
            _dict['toolchain_crn'] = self.toolchain_crn
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'referent') and self.referent is not None:
            _dict['referent'] = self.referent.to_dict()
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolPost object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolPost') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolPost') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Current configuration state of the tool.
        """
        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'
        MISCONFIGURED = 'misconfigured'
        UNCONFIGURED = 'unconfigured'


class ToolchainToolPrototypePatch():
    """
    Details on the new tool.

    :attr str name: (optional) Name of the tool.
    :attr str tool_type_id: (optional) The unique short name of the tool that should
          be provisioned or updated. A table of `tool_type_id` values corresponding to
          each tool integration can be found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    :attr dict parameters: (optional) Unique key-value pairs representing parameters
          to be used to create the tool. A list of parameters for each tool integration
          can be found in the <a
          href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
          tool integrations page</a>.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 tool_type_id: str = None,
                 parameters: dict = None) -> None:
        """
        Initialize a ToolchainToolPrototypePatch object.

        :param str name: (optional) Name of the tool.
        :param str tool_type_id: (optional) The unique short name of the tool that
               should be provisioned or updated. A table of `tool_type_id` values
               corresponding to each tool integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        :param dict parameters: (optional) Unique key-value pairs representing
               parameters to be used to create the tool. A list of parameters for each
               tool integration can be found in the <a
               href="https://cloud.ibm.com/docs/ContinuousDelivery?topic=ContinuousDelivery-integrations">Configuring
               tool integrations page</a>.
        """
        self.name = name
        self.tool_type_id = tool_type_id
        self.parameters = parameters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainToolPrototypePatch':
        """Initialize a ToolchainToolPrototypePatch object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'tool_type_id' in _dict:
            args['tool_type_id'] = _dict.get('tool_type_id')
        if 'parameters' in _dict:
            args['parameters'] = _dict.get('parameters')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainToolPrototypePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'tool_type_id') and self.tool_type_id is not None:
            _dict['tool_type_id'] = self.tool_type_id
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ToolchainToolPrototypePatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainToolPrototypePatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainToolPrototypePatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

##############################################################################
# Pagers
##############################################################################

class ToolchainsPager():
    """
    ToolchainsPager can be used to simplify the use of the "list_toolchains" method.
    """

    def __init__(self,
                 *,
                 client: CdToolchainV2,
                 resource_group_id: str,
                 limit: int = None,
    ) -> None:
        """
        Initialize a ToolchainsPager object.
        :param str resource_group_id: The resource group ID where the toolchains
               exist.
        :param int limit: (optional) Limit the number of results.
        """
        self._has_next = True
        self._client = client
        self._page_context = { 'next': None }
        self._resource_group_id = resource_group_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ToolchainModel.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_toolchains(
            resource_group_id=self._resource_group_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('toolchains')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ToolchainModel.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results

class ToolsPager():
    """
    ToolsPager can be used to simplify the use of the "list_tools" method.
    """

    def __init__(self,
                 *,
                 client: CdToolchainV2,
                 toolchain_id: str,
                 limit: int = None,
    ) -> None:
        """
        Initialize a ToolsPager object.
        :param str toolchain_id: ID of the toolchain that tools are bound to.
        :param int limit: (optional) Limit the number of results.
        """
        self._has_next = True
        self._client = client
        self._page_context = { 'next': None }
        self._toolchain_id = toolchain_id
        self._limit = limit

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of ToolModel.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_tools(
            toolchain_id=self._toolchain_id,
            limit=self._limit,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = next_page_link.get('start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('tools')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of ToolModel.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
