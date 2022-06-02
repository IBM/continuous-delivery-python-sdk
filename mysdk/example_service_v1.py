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

# IBM OpenAPI SDK Code Generator Version: 99-SNAPSHOT-5848cdba-20220127-161939
 
"""
The IBM SDK Squad Example Service. The Example service serves as an example of a service.

API Version: 1.0.0
See: https://{invalid host}.cloud.ibm.com/apidocs/example-service
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ExampleServiceV1(BaseService):
    """The ExampleService V1 service."""

    DEFAULT_SERVICE_URL = 'http://cloud.ibm.com/mysdk/v1'
    DEFAULT_SERVICE_NAME = 'example_service'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ExampleServiceV1':
        """
        Return a new client for the ExampleService service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the ExampleService service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # resources
    #########################


    def list_resources(self,
        *,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List all resources.

        :param int limit: (optional) How many items to return at one time (max
               100).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Resources` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_resources')
        headers.update(sdk_headers)

        params = {
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/resources'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_resource(self,
        name: str,
        tag: str,
        *,
        resource_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a resource.

        :param str name: The name of the resource.
        :param str tag: A tag value for the resource.
        :param str resource_id: (optional) The id of the resource. If not
               specified, it will be assigned by the server.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Resource` object
        """

        if name is None:
            raise ValueError('name must be provided')
        if tag is None:
            raise ValueError('tag must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_resource')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'tag': tag,
            'resource_id': resource_id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/resources'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_resource(self,
        resource_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Info for a specific resource.

        :param str resource_id: The id of the resource to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Resource` object
        """

        if resource_id is None:
            raise ValueError('resource_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_resource')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['resource_id']
        path_param_values = self.encode_path_vars(resource_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/resources/{resource_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_resource_encoded(self,
        url_encoded_resource_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Info for a specific resource.

        :param str url_encoded_resource_id: The id of the resource to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Resource` object
        """

        if url_encoded_resource_id is None:
            raise ValueError('url_encoded_resource_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_resource_encoded')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['url_encoded_resource_id']
        path_param_values = self.encode_path_vars(url_encoded_resource_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/resources/encoded/{url_encoded_resource_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class Resource():
    """
    A resource.

    :attr str resource_id: (optional) The id of the resource. If not specified, it
          will be assigned by the server.
    :attr str name: The name of the resource.
    :attr str tag: A tag value for the resource.
    :attr str read_only: (optional) This is a read only string.
    """

    def __init__(self,
                 name: str,
                 tag: str,
                 *,
                 resource_id: str = None,
                 read_only: str = None) -> None:
        """
        Initialize a Resource object.

        :param str name: The name of the resource.
        :param str tag: A tag value for the resource.
        :param str resource_id: (optional) The id of the resource. If not
               specified, it will be assigned by the server.
        """
        self.resource_id = resource_id
        self.name = name
        self.tag = tag
        self.read_only = read_only

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resource':
        """Initialize a Resource object from a json dictionary."""
        args = {}
        if 'resource_id' in _dict:
            args['resource_id'] = _dict.get('resource_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Resource JSON')
        if 'tag' in _dict:
            args['tag'] = _dict.get('tag')
        else:
            raise ValueError('Required property \'tag\' not present in Resource JSON')
        if 'read_only' in _dict:
            args['read_only'] = _dict.get('read_only')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Resource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_id') and self.resource_id is not None:
            _dict['resource_id'] = self.resource_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'tag') and self.tag is not None:
            _dict['tag'] = self.tag
        if hasattr(self, 'read_only') and getattr(self, 'read_only') is not None:
            _dict['read_only'] = getattr(self, 'read_only')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Resource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Resource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Resources():
    """
    List of resources.

    :attr int offset: Offset value for this portion of the resource list.
    :attr int limit: Limit value specified or defaulted in the list_resources
          request.
    :attr List[Resource] resources: A list of resources.
    """

    def __init__(self,
                 offset: int,
                 limit: int,
                 resources: List['Resource']) -> None:
        """
        Initialize a Resources object.

        :param int offset: Offset value for this portion of the resource list.
        :param int limit: Limit value specified or defaulted in the list_resources
               request.
        :param List[Resource] resources: A list of resources.
        """
        self.offset = offset
        self.limit = limit
        self.resources = resources

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Resources':
        """Initialize a Resources object from a json dictionary."""
        args = {}
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in Resources JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in Resources JSON')
        if 'resources' in _dict:
            args['resources'] = [Resource.from_dict(x) for x in _dict.get('resources')]
        else:
            raise ValueError('Required property \'resources\' not present in Resources JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Resources object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'resources') and self.resources is not None:
            _dict['resources'] = [x.to_dict() for x in self.resources]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Resources object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Resources') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Resources') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
