# -*- coding: utf-8 -*-
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

"""
Unit Tests for ExampleServiceV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from mysdk.example_service_v1 import *


_service = ExampleServiceV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'http://cloud.ibm.com/mysdk/v1'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: Resources
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = ExampleServiceV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ExampleServiceV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ExampleServiceV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListResources():
    """
    Test Class for list_resources
    """

    @responses.activate
    def test_list_resources_all_params(self):
        """
        list_resources()
        """
        # Set up mock
        url = preprocess_url('/resources')
        mock_response = '{"offset": 6, "limit": 5, "resources": [{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        limit = 1

        # Invoke method
        response = _service.list_resources(
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string

    def test_list_resources_all_params_with_retries(self):
        # Enable retries and run test_list_resources_all_params.
        _service.enable_retries()
        self.test_list_resources_all_params()

        # Disable retries and run test_list_resources_all_params.
        _service.disable_retries()
        self.test_list_resources_all_params()

    @responses.activate
    def test_list_resources_required_params(self):
        """
        test_list_resources_required_params()
        """
        # Set up mock
        url = preprocess_url('/resources')
        mock_response = '{"offset": 6, "limit": 5, "resources": [{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_resources()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resources_required_params_with_retries(self):
        # Enable retries and run test_list_resources_required_params.
        _service.enable_retries()
        self.test_list_resources_required_params()

        # Disable retries and run test_list_resources_required_params.
        _service.disable_retries()
        self.test_list_resources_required_params()

class TestCreateResource():
    """
    Test Class for create_resource
    """

    @responses.activate
    def test_create_resource_all_params(self):
        """
        create_resource()
        """
        # Set up mock
        url = preprocess_url('/resources')
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'The Hunt for Red October'
        tag = 'Book'
        resource_id = 'testString'

        # Invoke method
        response = _service.create_resource(
            name,
            tag,
            resource_id=resource_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'The Hunt for Red October'
        assert req_body['tag'] == 'Book'
        assert req_body['resource_id'] == 'testString'

    def test_create_resource_all_params_with_retries(self):
        # Enable retries and run test_create_resource_all_params.
        _service.enable_retries()
        self.test_create_resource_all_params()

        # Disable retries and run test_create_resource_all_params.
        _service.disable_retries()
        self.test_create_resource_all_params()

    @responses.activate
    def test_create_resource_value_error(self):
        """
        test_create_resource_value_error()
        """
        # Set up mock
        url = preprocess_url('/resources')
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'The Hunt for Red October'
        tag = 'Book'
        resource_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "tag": tag,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_resource(**req_copy)


    def test_create_resource_value_error_with_retries(self):
        # Enable retries and run test_create_resource_value_error.
        _service.enable_retries()
        self.test_create_resource_value_error()

        # Disable retries and run test_create_resource_value_error.
        _service.disable_retries()
        self.test_create_resource_value_error()

class TestGetResource():
    """
    Test Class for get_resource
    """

    @responses.activate
    def test_get_resource_all_params(self):
        """
        get_resource()
        """
        # Set up mock
        url = preprocess_url('/resources/1')
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_id = '1'

        # Invoke method
        response = _service.get_resource(
            resource_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_all_params_with_retries(self):
        # Enable retries and run test_get_resource_all_params.
        _service.enable_retries()
        self.test_get_resource_all_params()

        # Disable retries and run test_get_resource_all_params.
        _service.disable_retries()
        self.test_get_resource_all_params()

    @responses.activate
    def test_get_resource_value_error(self):
        """
        test_get_resource_value_error()
        """
        # Set up mock
        url = preprocess_url('/resources/1')
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_id = '1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resource_id": resource_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource(**req_copy)


    def test_get_resource_value_error_with_retries(self):
        # Enable retries and run test_get_resource_value_error.
        _service.enable_retries()
        self.test_get_resource_value_error()

        # Disable retries and run test_get_resource_value_error.
        _service.disable_retries()
        self.test_get_resource_value_error()

class TestGetResourceEncoded():
    """
    Test Class for get_resource_encoded
    """

    @responses.activate
    def test_get_resource_encoded_all_params(self):
        """
        get_resource_encoded()
        """
        # Set up mock
        url = preprocess_url('/resources/encoded/url%253encoded%253resource%253id')
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        url_encoded_resource_id = 'url%3encoded%3resource%3id'

        # Invoke method
        response = _service.get_resource_encoded(
            url_encoded_resource_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_encoded_all_params_with_retries(self):
        # Enable retries and run test_get_resource_encoded_all_params.
        _service.enable_retries()
        self.test_get_resource_encoded_all_params()

        # Disable retries and run test_get_resource_encoded_all_params.
        _service.disable_retries()
        self.test_get_resource_encoded_all_params()

    @responses.activate
    def test_get_resource_encoded_value_error(self):
        """
        test_get_resource_encoded_value_error()
        """
        # Set up mock
        url = preprocess_url('/resources/encoded/url%253encoded%253resource%253id')
        mock_response = '{"resource_id": "resource_id", "name": "name", "tag": "tag", "read_only": "read_only"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        url_encoded_resource_id = 'url%3encoded%3resource%3id'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "url_encoded_resource_id": url_encoded_resource_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_encoded(**req_copy)


    def test_get_resource_encoded_value_error_with_retries(self):
        # Enable retries and run test_get_resource_encoded_value_error.
        _service.enable_retries()
        self.test_get_resource_encoded_value_error()

        # Disable retries and run test_get_resource_encoded_value_error.
        _service.disable_retries()
        self.test_get_resource_encoded_value_error()

# endregion
##############################################################################
# End of Service: Resources
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Resource():
    """
    Test Class for Resource
    """

    def test_resource_serialization(self):
        """
        Test serialization/deserialization for Resource
        """

        # Construct a json representation of a Resource model
        resource_model_json = {}
        resource_model_json['resource_id'] = 'testString'
        resource_model_json['name'] = 'testString'
        resource_model_json['tag'] = 'testString'
        resource_model_json['read_only'] = 'testString'

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model = Resource.from_dict(resource_model_json)
        assert resource_model != False

        # Construct a model instance of Resource by calling from_dict on the json representation
        resource_model_dict = Resource.from_dict(resource_model_json).__dict__
        resource_model2 = Resource(**resource_model_dict)

        # Verify the model instances are equivalent
        assert resource_model == resource_model2

        # Convert model instance back to dict and verify no loss of data
        resource_model_json2 = resource_model.to_dict()
        assert resource_model_json2 == resource_model_json

class TestModel_Resources():
    """
    Test Class for Resources
    """

    def test_resources_serialization(self):
        """
        Test serialization/deserialization for Resources
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_model = {} # Resource
        resource_model['resource_id'] = '1'
        resource_model['name'] = 'The Great Gatsby'
        resource_model['tag'] = 'Book'
        resource_model['read_only'] = 'Foo'

        # Construct a json representation of a Resources model
        resources_model_json = {}
        resources_model_json['offset'] = 38
        resources_model_json['limit'] = 38
        resources_model_json['resources'] = [resource_model]

        # Construct a model instance of Resources by calling from_dict on the json representation
        resources_model = Resources.from_dict(resources_model_json)
        assert resources_model != False

        # Construct a model instance of Resources by calling from_dict on the json representation
        resources_model_dict = Resources.from_dict(resources_model_json).__dict__
        resources_model2 = Resources(**resources_model_dict)

        # Verify the model instances are equivalent
        assert resources_model == resources_model2

        # Convert model instance back to dict and verify no loss of data
        resources_model_json2 = resources_model.to_dict()
        assert resources_model_json2 == resources_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
