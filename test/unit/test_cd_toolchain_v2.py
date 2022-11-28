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
Unit Tests for CdToolchainV2
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_continuous_delivery.cd_toolchain_v2 import *


_service = CdToolchainV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2'
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


def test_get_service_url_for_region():
    """
    get_service_url_for_region()
    """
    assert CdToolchainV2.get_service_url_for_region('INVALID_REGION') is None
    assert CdToolchainV2.get_service_url_for_region('us-south') == 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('us-east') == 'https://api.us-east.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('eu-de') == 'https://api.eu-de.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('eu-gb') == 'https://api.eu-gb.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('jp-osa') == 'https://api.jp-osa.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('jp-tok') == 'https://api.jp-tok.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('au-syd') == 'https://api.au-syd.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('ca-tor') == 'https://api.ca-tor.devops.cloud.ibm.com/toolchain/v2'
    assert CdToolchainV2.get_service_url_for_region('br-sao') == 'https://api.br-sao.devops.cloud.ibm.com/toolchain/v2'


##############################################################################
# Start of Service: Toolchains
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

        service = CdToolchainV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdToolchainV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdToolchainV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListToolchains():
    """
    Test Class for list_toolchains
    """

    @responses.activate
    def test_list_toolchains_all_params(self):
        """
        list_toolchains()
        """
        # Set up mock
        url = preprocess_url('/toolchains')
        mock_response = '{"total_count": 11, "limit": 5, "first": {"href": "href"}, "previous": {"start": "start", "href": "href"}, "next": {"start": "start", "href": "href"}, "last": {"start": "start", "href": "href"}, "toolchains": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_group_id = 'testString'
        limit = 1
        start = 'testString'

        # Invoke method
        response = _service.list_toolchains(
            resource_group_id,
            limit=limit,
            start=start,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'resource_group_id={}'.format(resource_group_id) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_toolchains_all_params_with_retries(self):
        # Enable retries and run test_list_toolchains_all_params.
        _service.enable_retries()
        self.test_list_toolchains_all_params()

        # Disable retries and run test_list_toolchains_all_params.
        _service.disable_retries()
        self.test_list_toolchains_all_params()

    @responses.activate
    def test_list_toolchains_required_params(self):
        """
        test_list_toolchains_required_params()
        """
        # Set up mock
        url = preprocess_url('/toolchains')
        mock_response = '{"total_count": 11, "limit": 5, "first": {"href": "href"}, "previous": {"start": "start", "href": "href"}, "next": {"start": "start", "href": "href"}, "last": {"start": "start", "href": "href"}, "toolchains": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_group_id = 'testString'

        # Invoke method
        response = _service.list_toolchains(
            resource_group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'resource_group_id={}'.format(resource_group_id) in query_string

    def test_list_toolchains_required_params_with_retries(self):
        # Enable retries and run test_list_toolchains_required_params.
        _service.enable_retries()
        self.test_list_toolchains_required_params()

        # Disable retries and run test_list_toolchains_required_params.
        _service.disable_retries()
        self.test_list_toolchains_required_params()

    @responses.activate
    def test_list_toolchains_value_error(self):
        """
        test_list_toolchains_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains')
        mock_response = '{"total_count": 11, "limit": 5, "first": {"href": "href"}, "previous": {"start": "start", "href": "href"}, "next": {"start": "start", "href": "href"}, "last": {"start": "start", "href": "href"}, "toolchains": [{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        resource_group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "resource_group_id": resource_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_toolchains(**req_copy)

    def test_list_toolchains_value_error_with_retries(self):
        # Enable retries and run test_list_toolchains_value_error.
        _service.enable_retries()
        self.test_list_toolchains_value_error()

        # Disable retries and run test_list_toolchains_value_error.
        _service.disable_retries()
        self.test_list_toolchains_value_error()

    @responses.activate
    def test_list_toolchains_with_pager_get_next(self):
        """
        test_list_toolchains_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/toolchains')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"toolchains":[{"id":"id","name":"name","description":"description","account_id":"account_id","location":"location","resource_group_id":"resource_group_id","crn":"crn","href":"href","ui_href":"ui_href","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","created_by":"created_by"}],"limit":1}'
        mock_response2 = '{"total_count":2,"toolchains":[{"id":"id","name":"name","description":"description","account_id":"account_id","location":"location","resource_group_id":"resource_group_id","crn":"crn","href":"href","ui_href":"ui_href","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","created_by":"created_by"}],"limit":1}'
        responses.add(responses.GET,
                      url,
                      body=mock_response1,
                      content_type='application/json',
                      status=200)
        responses.add(responses.GET,
                      url,
                      body=mock_response2,
                      content_type='application/json',
                      status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ToolchainsPager(
            client=_service,
            resource_group_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_toolchains_with_pager_get_all(self):
        """
        test_list_toolchains_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/toolchains')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"toolchains":[{"id":"id","name":"name","description":"description","account_id":"account_id","location":"location","resource_group_id":"resource_group_id","crn":"crn","href":"href","ui_href":"ui_href","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","created_by":"created_by"}],"limit":1}'
        mock_response2 = '{"total_count":2,"toolchains":[{"id":"id","name":"name","description":"description","account_id":"account_id","location":"location","resource_group_id":"resource_group_id","crn":"crn","href":"href","ui_href":"ui_href","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","created_by":"created_by"}],"limit":1}'
        responses.add(responses.GET,
                      url,
                      body=mock_response1,
                      content_type='application/json',
                      status=200)
        responses.add(responses.GET,
                      url,
                      body=mock_response2,
                      content_type='application/json',
                      status=200)

        # Exercise the pager class for this operation
        pager = ToolchainsPager(
            client=_service,
            resource_group_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2

class TestCreateToolchain():
    """
    Test Class for create_toolchain
    """

    @responses.activate
    def test_create_toolchain_all_params(self):
        """
        create_toolchain()
        """
        # Set up mock
        url = preprocess_url('/toolchains')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'TestToolchainV2'
        resource_group_id = '6a9a01f2cff54a7f966f803d92877123'
        description = 'A sample toolchain to test the API'

        # Invoke method
        response = _service.create_toolchain(
            name,
            resource_group_id,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'TestToolchainV2'
        assert req_body['resource_group_id'] == '6a9a01f2cff54a7f966f803d92877123'
        assert req_body['description'] == 'A sample toolchain to test the API'

    def test_create_toolchain_all_params_with_retries(self):
        # Enable retries and run test_create_toolchain_all_params.
        _service.enable_retries()
        self.test_create_toolchain_all_params()

        # Disable retries and run test_create_toolchain_all_params.
        _service.disable_retries()
        self.test_create_toolchain_all_params()

    @responses.activate
    def test_create_toolchain_value_error(self):
        """
        test_create_toolchain_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'TestToolchainV2'
        resource_group_id = '6a9a01f2cff54a7f966f803d92877123'
        description = 'A sample toolchain to test the API'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "resource_group_id": resource_group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_toolchain(**req_copy)

    def test_create_toolchain_value_error_with_retries(self):
        # Enable retries and run test_create_toolchain_value_error.
        _service.enable_retries()
        self.test_create_toolchain_value_error()

        # Disable retries and run test_create_toolchain_value_error.
        _service.disable_retries()
        self.test_create_toolchain_value_error()

class TestGetToolchainById():
    """
    Test Class for get_toolchain_by_id
    """

    @responses.activate
    def test_get_toolchain_by_id_all_params(self):
        """
        get_toolchain_by_id()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        toolchain_id = 'testString'

        # Invoke method
        response = _service.get_toolchain_by_id(
            toolchain_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_toolchain_by_id_all_params_with_retries(self):
        # Enable retries and run test_get_toolchain_by_id_all_params.
        _service.enable_retries()
        self.test_get_toolchain_by_id_all_params()

        # Disable retries and run test_get_toolchain_by_id_all_params.
        _service.disable_retries()
        self.test_get_toolchain_by_id_all_params()

    @responses.activate
    def test_get_toolchain_by_id_value_error(self):
        """
        test_get_toolchain_by_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        toolchain_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_toolchain_by_id(**req_copy)

    def test_get_toolchain_by_id_value_error_with_retries(self):
        # Enable retries and run test_get_toolchain_by_id_value_error.
        _service.enable_retries()
        self.test_get_toolchain_by_id_value_error()

        # Disable retries and run test_get_toolchain_by_id_value_error.
        _service.disable_retries()
        self.test_get_toolchain_by_id_value_error()

class TestDeleteToolchain():
    """
    Test Class for delete_toolchain
    """

    @responses.activate
    def test_delete_toolchain_all_params(self):
        """
        delete_toolchain()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        toolchain_id = 'testString'

        # Invoke method
        response = _service.delete_toolchain(
            toolchain_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_toolchain_all_params_with_retries(self):
        # Enable retries and run test_delete_toolchain_all_params.
        _service.enable_retries()
        self.test_delete_toolchain_all_params()

        # Disable retries and run test_delete_toolchain_all_params.
        _service.disable_retries()
        self.test_delete_toolchain_all_params()

    @responses.activate
    def test_delete_toolchain_value_error(self):
        """
        test_delete_toolchain_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        toolchain_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_toolchain(**req_copy)

    def test_delete_toolchain_value_error_with_retries(self):
        # Enable retries and run test_delete_toolchain_value_error.
        _service.enable_retries()
        self.test_delete_toolchain_value_error()

        # Disable retries and run test_delete_toolchain_value_error.
        _service.disable_retries()
        self.test_delete_toolchain_value_error()

class TestUpdateToolchain():
    """
    Test Class for update_toolchain
    """

    @responses.activate
    def test_update_toolchain_all_params(self):
        """
        update_toolchain()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ToolchainPrototypePatch model
        toolchain_prototype_patch_model = {}
        toolchain_prototype_patch_model['name'] = 'newToolchainName'
        toolchain_prototype_patch_model['description'] = 'New toolchain description'

        # Set up parameter values
        toolchain_id = 'testString'
        toolchain_prototype_patch = toolchain_prototype_patch_model

        # Invoke method
        response = _service.update_toolchain(
            toolchain_id,
            toolchain_prototype_patch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == toolchain_prototype_patch

    def test_update_toolchain_all_params_with_retries(self):
        # Enable retries and run test_update_toolchain_all_params.
        _service.enable_retries()
        self.test_update_toolchain_all_params()

        # Disable retries and run test_update_toolchain_all_params.
        _service.disable_retries()
        self.test_update_toolchain_all_params()

    @responses.activate
    def test_update_toolchain_value_error(self):
        """
        test_update_toolchain_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "account_id": "account_id", "location": "location", "resource_group_id": "resource_group_id", "crn": "crn", "href": "href", "ui_href": "ui_href", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "created_by": "created_by"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ToolchainPrototypePatch model
        toolchain_prototype_patch_model = {}
        toolchain_prototype_patch_model['name'] = 'newToolchainName'
        toolchain_prototype_patch_model['description'] = 'New toolchain description'

        # Set up parameter values
        toolchain_id = 'testString'
        toolchain_prototype_patch = toolchain_prototype_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
            "toolchain_prototype_patch": toolchain_prototype_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_toolchain(**req_copy)

    def test_update_toolchain_value_error_with_retries(self):
        # Enable retries and run test_update_toolchain_value_error.
        _service.enable_retries()
        self.test_update_toolchain_value_error()

        # Disable retries and run test_update_toolchain_value_error.
        _service.disable_retries()
        self.test_update_toolchain_value_error()

# endregion
##############################################################################
# End of Service: Toolchains
##############################################################################

##############################################################################
# Start of Service: Tools
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

        service = CdToolchainV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdToolchainV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdToolchainV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListTools():
    """
    Test Class for list_tools
    """

    @responses.activate
    def test_list_tools_all_params(self):
        """
        list_tools()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools')
        mock_response = '{"limit": 5, "total_count": 11, "first": {"href": "href"}, "previous": {"start": "start", "href": "href"}, "next": {"start": "start", "href": "href"}, "last": {"start": "start", "href": "href"}, "tools": [{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        toolchain_id = 'testString'
        limit = 1
        start = 'testString'

        # Invoke method
        response = _service.list_tools(
            toolchain_id,
            limit=limit,
            start=start,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'start={}'.format(start) in query_string

    def test_list_tools_all_params_with_retries(self):
        # Enable retries and run test_list_tools_all_params.
        _service.enable_retries()
        self.test_list_tools_all_params()

        # Disable retries and run test_list_tools_all_params.
        _service.disable_retries()
        self.test_list_tools_all_params()

    @responses.activate
    def test_list_tools_required_params(self):
        """
        test_list_tools_required_params()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools')
        mock_response = '{"limit": 5, "total_count": 11, "first": {"href": "href"}, "previous": {"start": "start", "href": "href"}, "next": {"start": "start", "href": "href"}, "last": {"start": "start", "href": "href"}, "tools": [{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        toolchain_id = 'testString'

        # Invoke method
        response = _service.list_tools(
            toolchain_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tools_required_params_with_retries(self):
        # Enable retries and run test_list_tools_required_params.
        _service.enable_retries()
        self.test_list_tools_required_params()

        # Disable retries and run test_list_tools_required_params.
        _service.disable_retries()
        self.test_list_tools_required_params()

    @responses.activate
    def test_list_tools_value_error(self):
        """
        test_list_tools_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools')
        mock_response = '{"limit": 5, "total_count": 11, "first": {"href": "href"}, "previous": {"start": "start", "href": "href"}, "next": {"start": "start", "href": "href"}, "last": {"start": "start", "href": "href"}, "tools": [{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        toolchain_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tools(**req_copy)

    def test_list_tools_value_error_with_retries(self):
        # Enable retries and run test_list_tools_value_error.
        _service.enable_retries()
        self.test_list_tools_value_error()

        # Disable retries and run test_list_tools_value_error.
        _service.disable_retries()
        self.test_list_tools_value_error()

    @responses.activate
    def test_list_tools_with_pager_get_next(self):
        """
        test_list_tools_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/toolchains/testString/tools')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"tools":[{"id":"id","resource_group_id":"resource_group_id","crn":"crn","tool_type_id":"tool_type_id","toolchain_id":"toolchain_id","toolchain_crn":"toolchain_crn","href":"href","referent":{"ui_href":"ui_href","api_href":"api_href"},"name":"name","updated_at":"2019-01-01T12:00:00.000Z","parameters":{"anyKey":"anyValue"},"state":"configured"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"tools":[{"id":"id","resource_group_id":"resource_group_id","crn":"crn","tool_type_id":"tool_type_id","toolchain_id":"toolchain_id","toolchain_crn":"toolchain_crn","href":"href","referent":{"ui_href":"ui_href","api_href":"api_href"},"name":"name","updated_at":"2019-01-01T12:00:00.000Z","parameters":{"anyKey":"anyValue"},"state":"configured"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response1,
                      content_type='application/json',
                      status=200)
        responses.add(responses.GET,
                      url,
                      body=mock_response2,
                      content_type='application/json',
                      status=200)

        # Exercise the pager class for this operation
        all_results = []
        pager = ToolsPager(
            client=_service,
            toolchain_id='testString',
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_tools_with_pager_get_all(self):
        """
        test_list_tools_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/toolchains/testString/tools')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"tools":[{"id":"id","resource_group_id":"resource_group_id","crn":"crn","tool_type_id":"tool_type_id","toolchain_id":"toolchain_id","toolchain_crn":"toolchain_crn","href":"href","referent":{"ui_href":"ui_href","api_href":"api_href"},"name":"name","updated_at":"2019-01-01T12:00:00.000Z","parameters":{"anyKey":"anyValue"},"state":"configured"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"tools":[{"id":"id","resource_group_id":"resource_group_id","crn":"crn","tool_type_id":"tool_type_id","toolchain_id":"toolchain_id","toolchain_crn":"toolchain_crn","href":"href","referent":{"ui_href":"ui_href","api_href":"api_href"},"name":"name","updated_at":"2019-01-01T12:00:00.000Z","parameters":{"anyKey":"anyValue"},"state":"configured"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response1,
                      content_type='application/json',
                      status=200)
        responses.add(responses.GET,
                      url,
                      body=mock_response2,
                      content_type='application/json',
                      status=200)

        # Exercise the pager class for this operation
        pager = ToolsPager(
            client=_service,
            toolchain_id='testString',
            limit=10,
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2

class TestCreateTool():
    """
    Test Class for create_tool
    """

    @responses.activate
    def test_create_tool_all_params(self):
        """
        create_tool()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools')
        mock_response = '{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        toolchain_id = 'testString'
        tool_type_id = 'draservicebroker'
        name = 'testString'
        parameters = {'foo': 'bar'}

        # Invoke method
        response = _service.create_tool(
            toolchain_id,
            tool_type_id,
            name=name,
            parameters=parameters,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tool_type_id'] == 'draservicebroker'
        assert req_body['name'] == 'testString'
        assert req_body['parameters'] == {'foo': 'bar'}

    def test_create_tool_all_params_with_retries(self):
        # Enable retries and run test_create_tool_all_params.
        _service.enable_retries()
        self.test_create_tool_all_params()

        # Disable retries and run test_create_tool_all_params.
        _service.disable_retries()
        self.test_create_tool_all_params()

    @responses.activate
    def test_create_tool_value_error(self):
        """
        test_create_tool_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools')
        mock_response = '{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        toolchain_id = 'testString'
        tool_type_id = 'draservicebroker'
        name = 'testString'
        parameters = {'foo': 'bar'}

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
            "tool_type_id": tool_type_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tool(**req_copy)

    def test_create_tool_value_error_with_retries(self):
        # Enable retries and run test_create_tool_value_error.
        _service.enable_retries()
        self.test_create_tool_value_error()

        # Disable retries and run test_create_tool_value_error.
        _service.disable_retries()
        self.test_create_tool_value_error()

class TestGetToolById():
    """
    Test Class for get_tool_by_id
    """

    @responses.activate
    def test_get_tool_by_id_all_params(self):
        """
        get_tool_by_id()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools/testString')
        mock_response = '{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        toolchain_id = 'testString'
        tool_id = 'testString'

        # Invoke method
        response = _service.get_tool_by_id(
            toolchain_id,
            tool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tool_by_id_all_params_with_retries(self):
        # Enable retries and run test_get_tool_by_id_all_params.
        _service.enable_retries()
        self.test_get_tool_by_id_all_params()

        # Disable retries and run test_get_tool_by_id_all_params.
        _service.disable_retries()
        self.test_get_tool_by_id_all_params()

    @responses.activate
    def test_get_tool_by_id_value_error(self):
        """
        test_get_tool_by_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools/testString')
        mock_response = '{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        toolchain_id = 'testString'
        tool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
            "tool_id": tool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tool_by_id(**req_copy)

    def test_get_tool_by_id_value_error_with_retries(self):
        # Enable retries and run test_get_tool_by_id_value_error.
        _service.enable_retries()
        self.test_get_tool_by_id_value_error()

        # Disable retries and run test_get_tool_by_id_value_error.
        _service.disable_retries()
        self.test_get_tool_by_id_value_error()

class TestDeleteTool():
    """
    Test Class for delete_tool
    """

    @responses.activate
    def test_delete_tool_all_params(self):
        """
        delete_tool()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        toolchain_id = 'testString'
        tool_id = 'testString'

        # Invoke method
        response = _service.delete_tool(
            toolchain_id,
            tool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tool_all_params_with_retries(self):
        # Enable retries and run test_delete_tool_all_params.
        _service.enable_retries()
        self.test_delete_tool_all_params()

        # Disable retries and run test_delete_tool_all_params.
        _service.disable_retries()
        self.test_delete_tool_all_params()

    @responses.activate
    def test_delete_tool_value_error(self):
        """
        test_delete_tool_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        toolchain_id = 'testString'
        tool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
            "tool_id": tool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tool(**req_copy)

    def test_delete_tool_value_error_with_retries(self):
        # Enable retries and run test_delete_tool_value_error.
        _service.enable_retries()
        self.test_delete_tool_value_error()

        # Disable retries and run test_delete_tool_value_error.
        _service.disable_retries()
        self.test_delete_tool_value_error()

class TestUpdateTool():
    """
    Test Class for update_tool
    """

    @responses.activate
    def test_update_tool_all_params(self):
        """
        update_tool()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools/testString')
        mock_response = '{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ToolchainToolPrototypePatch model
        toolchain_tool_prototype_patch_model = {}
        toolchain_tool_prototype_patch_model['name'] = 'MyTool'
        toolchain_tool_prototype_patch_model['tool_type_id'] = 'draservicebroker'
        toolchain_tool_prototype_patch_model['parameters'] = {'foo': 'bar'}

        # Set up parameter values
        toolchain_id = 'testString'
        tool_id = 'testString'
        toolchain_tool_prototype_patch = toolchain_tool_prototype_patch_model

        # Invoke method
        response = _service.update_tool(
            toolchain_id,
            tool_id,
            toolchain_tool_prototype_patch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == toolchain_tool_prototype_patch

    def test_update_tool_all_params_with_retries(self):
        # Enable retries and run test_update_tool_all_params.
        _service.enable_retries()
        self.test_update_tool_all_params()

        # Disable retries and run test_update_tool_all_params.
        _service.disable_retries()
        self.test_update_tool_all_params()

    @responses.activate
    def test_update_tool_value_error(self):
        """
        test_update_tool_value_error()
        """
        # Set up mock
        url = preprocess_url('/toolchains/testString/tools/testString')
        mock_response = '{"id": "id", "resource_group_id": "resource_group_id", "crn": "crn", "tool_type_id": "tool_type_id", "toolchain_id": "toolchain_id", "toolchain_crn": "toolchain_crn", "href": "href", "referent": {"ui_href": "ui_href", "api_href": "api_href"}, "name": "name", "updated_at": "2019-01-01T12:00:00.000Z", "parameters": {"anyKey": "anyValue"}, "state": "configured"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ToolchainToolPrototypePatch model
        toolchain_tool_prototype_patch_model = {}
        toolchain_tool_prototype_patch_model['name'] = 'MyTool'
        toolchain_tool_prototype_patch_model['tool_type_id'] = 'draservicebroker'
        toolchain_tool_prototype_patch_model['parameters'] = {'foo': 'bar'}

        # Set up parameter values
        toolchain_id = 'testString'
        tool_id = 'testString'
        toolchain_tool_prototype_patch = toolchain_tool_prototype_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "toolchain_id": toolchain_id,
            "tool_id": tool_id,
            "toolchain_tool_prototype_patch": toolchain_tool_prototype_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_tool(**req_copy)

    def test_update_tool_value_error_with_retries(self):
        # Enable retries and run test_update_tool_value_error.
        _service.enable_retries()
        self.test_update_tool_value_error()

        # Disable retries and run test_update_tool_value_error.
        _service.disable_retries()
        self.test_update_tool_value_error()

# endregion
##############################################################################
# End of Service: Tools
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_ToolModel():
    """
    Test Class for ToolModel
    """

    def test_tool_model_serialization(self):
        """
        Test serialization/deserialization for ToolModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tool_model_referent_model = {} # ToolModelReferent
        tool_model_referent_model['ui_href'] = 'https://my-team.slack.com/messages/my-channel'
        tool_model_referent_model['api_href'] = 'testString'

        # Construct a json representation of a ToolModel model
        tool_model_model_json = {}
        tool_model_model_json['id'] = 'testString'
        tool_model_model_json['resource_group_id'] = 'testString'
        tool_model_model_json['crn'] = 'testString'
        tool_model_model_json['tool_type_id'] = 'testString'
        tool_model_model_json['toolchain_id'] = 'testString'
        tool_model_model_json['toolchain_crn'] = 'testString'
        tool_model_model_json['href'] = 'testString'
        tool_model_model_json['referent'] = tool_model_referent_model
        tool_model_model_json['name'] = 'testString'
        tool_model_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        tool_model_model_json['parameters'] = {'foo': 'bar'}
        tool_model_model_json['state'] = 'configured'

        # Construct a model instance of ToolModel by calling from_dict on the json representation
        tool_model_model = ToolModel.from_dict(tool_model_model_json)
        assert tool_model_model != False

        # Construct a model instance of ToolModel by calling from_dict on the json representation
        tool_model_model_dict = ToolModel.from_dict(tool_model_model_json).__dict__
        tool_model_model2 = ToolModel(**tool_model_model_dict)

        # Verify the model instances are equivalent
        assert tool_model_model == tool_model_model2

        # Convert model instance back to dict and verify no loss of data
        tool_model_model_json2 = tool_model_model.to_dict()
        assert tool_model_model_json2 == tool_model_model_json

class TestModel_ToolModelReferent():
    """
    Test Class for ToolModelReferent
    """

    def test_tool_model_referent_serialization(self):
        """
        Test serialization/deserialization for ToolModelReferent
        """

        # Construct a json representation of a ToolModelReferent model
        tool_model_referent_model_json = {}
        tool_model_referent_model_json['ui_href'] = 'testString'
        tool_model_referent_model_json['api_href'] = 'testString'

        # Construct a model instance of ToolModelReferent by calling from_dict on the json representation
        tool_model_referent_model = ToolModelReferent.from_dict(tool_model_referent_model_json)
        assert tool_model_referent_model != False

        # Construct a model instance of ToolModelReferent by calling from_dict on the json representation
        tool_model_referent_model_dict = ToolModelReferent.from_dict(tool_model_referent_model_json).__dict__
        tool_model_referent_model2 = ToolModelReferent(**tool_model_referent_model_dict)

        # Verify the model instances are equivalent
        assert tool_model_referent_model == tool_model_referent_model2

        # Convert model instance back to dict and verify no loss of data
        tool_model_referent_model_json2 = tool_model_referent_model.to_dict()
        assert tool_model_referent_model_json2 == tool_model_referent_model_json

class TestModel_Toolchain():
    """
    Test Class for Toolchain
    """

    def test_toolchain_serialization(self):
        """
        Test serialization/deserialization for Toolchain
        """

        # Construct a json representation of a Toolchain model
        toolchain_model_json = {}
        toolchain_model_json['id'] = 'testString'
        toolchain_model_json['name'] = 'testString'
        toolchain_model_json['description'] = 'testString'
        toolchain_model_json['account_id'] = 'testString'
        toolchain_model_json['location'] = 'testString'
        toolchain_model_json['resource_group_id'] = 'testString'
        toolchain_model_json['crn'] = 'testString'
        toolchain_model_json['href'] = 'testString'
        toolchain_model_json['ui_href'] = 'testString'
        toolchain_model_json['created_at'] = '2019-01-01T12:00:00Z'
        toolchain_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        toolchain_model_json['created_by'] = 'testString'

        # Construct a model instance of Toolchain by calling from_dict on the json representation
        toolchain_model = Toolchain.from_dict(toolchain_model_json)
        assert toolchain_model != False

        # Construct a model instance of Toolchain by calling from_dict on the json representation
        toolchain_model_dict = Toolchain.from_dict(toolchain_model_json).__dict__
        toolchain_model2 = Toolchain(**toolchain_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_model == toolchain_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_model_json2 = toolchain_model.to_dict()
        assert toolchain_model_json2 == toolchain_model_json

class TestModel_ToolchainCollection():
    """
    Test Class for ToolchainCollection
    """

    def test_toolchain_collection_serialization(self):
        """
        Test serialization/deserialization for ToolchainCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        toolchain_collection_first_model = {} # ToolchainCollectionFirst
        toolchain_collection_first_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains?resource_group_id=6a9a01f2cff54a7f966f803d92877123&limit=3'

        toolchain_collection_previous_model = {} # ToolchainCollectionPrevious
        toolchain_collection_previous_model['start'] = 'eyJ0b29sY2hhaW5fZ3VpZCI6IjA4NDFlYTMxLTEzMDMtNDJiZC1hYmMyLTQzMjYzZDg0YmU0OSJ9'
        toolchain_collection_previous_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains?resource_group_id=6a9a01f2cff54a7f966f803d92877123&limit=3&start=eyJ0b29sY2hhaW5fZ3VpZCI6IjA4NDFlYTMxLTEzMDMtNDJiZC1hYmMyLTQzMjYzZDg0YmU0OSJ9'

        toolchain_collection_next_model = {} # ToolchainCollectionNext
        toolchain_collection_next_model['start'] = 'eyJ0b29sY2hhaW5fZ3VpZCI6ImVhZGVmNGYzLThlMzktNDY2OS04NmY0LWU1NTA1MWExMjMzOCJ9'
        toolchain_collection_next_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains?resource_group_id=6a9a01f2cff54a7f966f803d92877123&limit=3&start=eyJ0b29sY2hhaW5fZ3VpZCI6ImVhZGVmNGYzLThlMzktNDY2OS04NmY0LWU1NTA1MWExMjMzOCJ9'

        toolchain_collection_last_model = {} # ToolchainCollectionLast
        toolchain_collection_last_model['start'] = 'eyJ0b29sY2hhaW5fZ3VpZCI6ImYxNTI3ZjkyLTQyOTAtNGUzZi1iMmIzLTc3ODg5YTE0NDkzOCJ9'
        toolchain_collection_last_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains?resource_group_id=6a9a01f2cff54a7f966f803d92877123&limit=3&start=eyJ0b29sY2hhaW5fZ3VpZCI6ImYxNTI3ZjkyLTQyOTAtNGUzZi1iMmIzLTc3ODg5YTE0NDkzOCJ9'

        toolchain_model_model = {} # ToolchainModel
        toolchain_model_model['id'] = '62935028-0202-48fe-b877-7e99c817b856'
        toolchain_model_model['name'] = 'TestToolchainV2-2'
        toolchain_model_model['description'] = 'A second sample toolchain'
        toolchain_model_model['account_id'] = 'f2337426699b4041bc50f1d45042f777'
        toolchain_model_model['location'] = 'us-south'
        toolchain_model_model['resource_group_id'] = '6a9a01f2cff54a7f966f803d92877123'
        toolchain_model_model['crn'] = 'crn:v1:staging:public:toolchain:us-south:a/f2337426699b4041bc50f1d45042f777:62935028-0202-48fe-b877-7e99c817b856::'
        toolchain_model_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains/62935028-0202-48fe-b877-7e99c817b856'
        toolchain_model_model['ui_href'] = 'testString'
        toolchain_model_model['created_at'] = '2021-05-05T17:07:09.354000Z'
        toolchain_model_model['updated_at'] = '2022-01-01T13:13:07.968000Z'
        toolchain_model_model['created_by'] = 'IBMid-123456AB7C'

        # Construct a json representation of a ToolchainCollection model
        toolchain_collection_model_json = {}
        toolchain_collection_model_json['total_count'] = 38
        toolchain_collection_model_json['limit'] = 38
        toolchain_collection_model_json['first'] = toolchain_collection_first_model
        toolchain_collection_model_json['previous'] = toolchain_collection_previous_model
        toolchain_collection_model_json['next'] = toolchain_collection_next_model
        toolchain_collection_model_json['last'] = toolchain_collection_last_model
        toolchain_collection_model_json['toolchains'] = [toolchain_model_model]

        # Construct a model instance of ToolchainCollection by calling from_dict on the json representation
        toolchain_collection_model = ToolchainCollection.from_dict(toolchain_collection_model_json)
        assert toolchain_collection_model != False

        # Construct a model instance of ToolchainCollection by calling from_dict on the json representation
        toolchain_collection_model_dict = ToolchainCollection.from_dict(toolchain_collection_model_json).__dict__
        toolchain_collection_model2 = ToolchainCollection(**toolchain_collection_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_collection_model == toolchain_collection_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_collection_model_json2 = toolchain_collection_model.to_dict()
        assert toolchain_collection_model_json2 == toolchain_collection_model_json

class TestModel_ToolchainCollectionFirst():
    """
    Test Class for ToolchainCollectionFirst
    """

    def test_toolchain_collection_first_serialization(self):
        """
        Test serialization/deserialization for ToolchainCollectionFirst
        """

        # Construct a json representation of a ToolchainCollectionFirst model
        toolchain_collection_first_model_json = {}
        toolchain_collection_first_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainCollectionFirst by calling from_dict on the json representation
        toolchain_collection_first_model = ToolchainCollectionFirst.from_dict(toolchain_collection_first_model_json)
        assert toolchain_collection_first_model != False

        # Construct a model instance of ToolchainCollectionFirst by calling from_dict on the json representation
        toolchain_collection_first_model_dict = ToolchainCollectionFirst.from_dict(toolchain_collection_first_model_json).__dict__
        toolchain_collection_first_model2 = ToolchainCollectionFirst(**toolchain_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_collection_first_model == toolchain_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_collection_first_model_json2 = toolchain_collection_first_model.to_dict()
        assert toolchain_collection_first_model_json2 == toolchain_collection_first_model_json

class TestModel_ToolchainCollectionLast():
    """
    Test Class for ToolchainCollectionLast
    """

    def test_toolchain_collection_last_serialization(self):
        """
        Test serialization/deserialization for ToolchainCollectionLast
        """

        # Construct a json representation of a ToolchainCollectionLast model
        toolchain_collection_last_model_json = {}
        toolchain_collection_last_model_json['start'] = 'testString'
        toolchain_collection_last_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainCollectionLast by calling from_dict on the json representation
        toolchain_collection_last_model = ToolchainCollectionLast.from_dict(toolchain_collection_last_model_json)
        assert toolchain_collection_last_model != False

        # Construct a model instance of ToolchainCollectionLast by calling from_dict on the json representation
        toolchain_collection_last_model_dict = ToolchainCollectionLast.from_dict(toolchain_collection_last_model_json).__dict__
        toolchain_collection_last_model2 = ToolchainCollectionLast(**toolchain_collection_last_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_collection_last_model == toolchain_collection_last_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_collection_last_model_json2 = toolchain_collection_last_model.to_dict()
        assert toolchain_collection_last_model_json2 == toolchain_collection_last_model_json

class TestModel_ToolchainCollectionNext():
    """
    Test Class for ToolchainCollectionNext
    """

    def test_toolchain_collection_next_serialization(self):
        """
        Test serialization/deserialization for ToolchainCollectionNext
        """

        # Construct a json representation of a ToolchainCollectionNext model
        toolchain_collection_next_model_json = {}
        toolchain_collection_next_model_json['start'] = 'testString'
        toolchain_collection_next_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainCollectionNext by calling from_dict on the json representation
        toolchain_collection_next_model = ToolchainCollectionNext.from_dict(toolchain_collection_next_model_json)
        assert toolchain_collection_next_model != False

        # Construct a model instance of ToolchainCollectionNext by calling from_dict on the json representation
        toolchain_collection_next_model_dict = ToolchainCollectionNext.from_dict(toolchain_collection_next_model_json).__dict__
        toolchain_collection_next_model2 = ToolchainCollectionNext(**toolchain_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_collection_next_model == toolchain_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_collection_next_model_json2 = toolchain_collection_next_model.to_dict()
        assert toolchain_collection_next_model_json2 == toolchain_collection_next_model_json

class TestModel_ToolchainCollectionPrevious():
    """
    Test Class for ToolchainCollectionPrevious
    """

    def test_toolchain_collection_previous_serialization(self):
        """
        Test serialization/deserialization for ToolchainCollectionPrevious
        """

        # Construct a json representation of a ToolchainCollectionPrevious model
        toolchain_collection_previous_model_json = {}
        toolchain_collection_previous_model_json['start'] = 'testString'
        toolchain_collection_previous_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainCollectionPrevious by calling from_dict on the json representation
        toolchain_collection_previous_model = ToolchainCollectionPrevious.from_dict(toolchain_collection_previous_model_json)
        assert toolchain_collection_previous_model != False

        # Construct a model instance of ToolchainCollectionPrevious by calling from_dict on the json representation
        toolchain_collection_previous_model_dict = ToolchainCollectionPrevious.from_dict(toolchain_collection_previous_model_json).__dict__
        toolchain_collection_previous_model2 = ToolchainCollectionPrevious(**toolchain_collection_previous_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_collection_previous_model == toolchain_collection_previous_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_collection_previous_model_json2 = toolchain_collection_previous_model.to_dict()
        assert toolchain_collection_previous_model_json2 == toolchain_collection_previous_model_json

class TestModel_ToolchainModel():
    """
    Test Class for ToolchainModel
    """

    def test_toolchain_model_serialization(self):
        """
        Test serialization/deserialization for ToolchainModel
        """

        # Construct a json representation of a ToolchainModel model
        toolchain_model_model_json = {}
        toolchain_model_model_json['id'] = 'testString'
        toolchain_model_model_json['name'] = 'testString'
        toolchain_model_model_json['description'] = 'testString'
        toolchain_model_model_json['account_id'] = 'testString'
        toolchain_model_model_json['location'] = 'testString'
        toolchain_model_model_json['resource_group_id'] = 'testString'
        toolchain_model_model_json['crn'] = 'testString'
        toolchain_model_model_json['href'] = 'testString'
        toolchain_model_model_json['ui_href'] = 'testString'
        toolchain_model_model_json['created_at'] = '2019-01-01T12:00:00Z'
        toolchain_model_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        toolchain_model_model_json['created_by'] = 'testString'

        # Construct a model instance of ToolchainModel by calling from_dict on the json representation
        toolchain_model_model = ToolchainModel.from_dict(toolchain_model_model_json)
        assert toolchain_model_model != False

        # Construct a model instance of ToolchainModel by calling from_dict on the json representation
        toolchain_model_model_dict = ToolchainModel.from_dict(toolchain_model_model_json).__dict__
        toolchain_model_model2 = ToolchainModel(**toolchain_model_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_model_model == toolchain_model_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_model_model_json2 = toolchain_model_model.to_dict()
        assert toolchain_model_model_json2 == toolchain_model_model_json

class TestModel_ToolchainPatch():
    """
    Test Class for ToolchainPatch
    """

    def test_toolchain_patch_serialization(self):
        """
        Test serialization/deserialization for ToolchainPatch
        """

        # Construct a json representation of a ToolchainPatch model
        toolchain_patch_model_json = {}
        toolchain_patch_model_json['id'] = 'testString'
        toolchain_patch_model_json['name'] = 'testString'
        toolchain_patch_model_json['description'] = 'testString'
        toolchain_patch_model_json['account_id'] = 'testString'
        toolchain_patch_model_json['location'] = 'testString'
        toolchain_patch_model_json['resource_group_id'] = 'testString'
        toolchain_patch_model_json['crn'] = 'testString'
        toolchain_patch_model_json['href'] = 'testString'
        toolchain_patch_model_json['ui_href'] = 'testString'
        toolchain_patch_model_json['created_at'] = '2019-01-01T12:00:00Z'
        toolchain_patch_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        toolchain_patch_model_json['created_by'] = 'testString'

        # Construct a model instance of ToolchainPatch by calling from_dict on the json representation
        toolchain_patch_model = ToolchainPatch.from_dict(toolchain_patch_model_json)
        assert toolchain_patch_model != False

        # Construct a model instance of ToolchainPatch by calling from_dict on the json representation
        toolchain_patch_model_dict = ToolchainPatch.from_dict(toolchain_patch_model_json).__dict__
        toolchain_patch_model2 = ToolchainPatch(**toolchain_patch_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_patch_model == toolchain_patch_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_patch_model_json2 = toolchain_patch_model.to_dict()
        assert toolchain_patch_model_json2 == toolchain_patch_model_json

class TestModel_ToolchainPost():
    """
    Test Class for ToolchainPost
    """

    def test_toolchain_post_serialization(self):
        """
        Test serialization/deserialization for ToolchainPost
        """

        # Construct a json representation of a ToolchainPost model
        toolchain_post_model_json = {}
        toolchain_post_model_json['id'] = 'testString'
        toolchain_post_model_json['name'] = 'testString'
        toolchain_post_model_json['description'] = 'testString'
        toolchain_post_model_json['account_id'] = 'testString'
        toolchain_post_model_json['location'] = 'testString'
        toolchain_post_model_json['resource_group_id'] = 'testString'
        toolchain_post_model_json['crn'] = 'testString'
        toolchain_post_model_json['href'] = 'testString'
        toolchain_post_model_json['ui_href'] = 'testString'
        toolchain_post_model_json['created_at'] = '2019-01-01T12:00:00Z'
        toolchain_post_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        toolchain_post_model_json['created_by'] = 'testString'

        # Construct a model instance of ToolchainPost by calling from_dict on the json representation
        toolchain_post_model = ToolchainPost.from_dict(toolchain_post_model_json)
        assert toolchain_post_model != False

        # Construct a model instance of ToolchainPost by calling from_dict on the json representation
        toolchain_post_model_dict = ToolchainPost.from_dict(toolchain_post_model_json).__dict__
        toolchain_post_model2 = ToolchainPost(**toolchain_post_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_post_model == toolchain_post_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_post_model_json2 = toolchain_post_model.to_dict()
        assert toolchain_post_model_json2 == toolchain_post_model_json

class TestModel_ToolchainPrototypePatch():
    """
    Test Class for ToolchainPrototypePatch
    """

    def test_toolchain_prototype_patch_serialization(self):
        """
        Test serialization/deserialization for ToolchainPrototypePatch
        """

        # Construct a json representation of a ToolchainPrototypePatch model
        toolchain_prototype_patch_model_json = {}
        toolchain_prototype_patch_model_json['name'] = 'newToolchainName'
        toolchain_prototype_patch_model_json['description'] = 'New toolchain description'

        # Construct a model instance of ToolchainPrototypePatch by calling from_dict on the json representation
        toolchain_prototype_patch_model = ToolchainPrototypePatch.from_dict(toolchain_prototype_patch_model_json)
        assert toolchain_prototype_patch_model != False

        # Construct a model instance of ToolchainPrototypePatch by calling from_dict on the json representation
        toolchain_prototype_patch_model_dict = ToolchainPrototypePatch.from_dict(toolchain_prototype_patch_model_json).__dict__
        toolchain_prototype_patch_model2 = ToolchainPrototypePatch(**toolchain_prototype_patch_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_prototype_patch_model == toolchain_prototype_patch_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_prototype_patch_model_json2 = toolchain_prototype_patch_model.to_dict()
        assert toolchain_prototype_patch_model_json2 == toolchain_prototype_patch_model_json

class TestModel_ToolchainTool():
    """
    Test Class for ToolchainTool
    """

    def test_toolchain_tool_serialization(self):
        """
        Test serialization/deserialization for ToolchainTool
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tool_model_referent_model = {} # ToolModelReferent
        tool_model_referent_model['ui_href'] = 'https://my-team.slack.com/messages/my-channel'
        tool_model_referent_model['api_href'] = 'testString'

        # Construct a json representation of a ToolchainTool model
        toolchain_tool_model_json = {}
        toolchain_tool_model_json['id'] = 'testString'
        toolchain_tool_model_json['resource_group_id'] = 'testString'
        toolchain_tool_model_json['crn'] = 'testString'
        toolchain_tool_model_json['tool_type_id'] = 'testString'
        toolchain_tool_model_json['toolchain_id'] = 'testString'
        toolchain_tool_model_json['toolchain_crn'] = 'testString'
        toolchain_tool_model_json['href'] = 'testString'
        toolchain_tool_model_json['referent'] = tool_model_referent_model
        toolchain_tool_model_json['name'] = 'testString'
        toolchain_tool_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        toolchain_tool_model_json['parameters'] = {'foo': 'bar'}
        toolchain_tool_model_json['state'] = 'configured'

        # Construct a model instance of ToolchainTool by calling from_dict on the json representation
        toolchain_tool_model = ToolchainTool.from_dict(toolchain_tool_model_json)
        assert toolchain_tool_model != False

        # Construct a model instance of ToolchainTool by calling from_dict on the json representation
        toolchain_tool_model_dict = ToolchainTool.from_dict(toolchain_tool_model_json).__dict__
        toolchain_tool_model2 = ToolchainTool(**toolchain_tool_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_model == toolchain_tool_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_model_json2 = toolchain_tool_model.to_dict()
        assert toolchain_tool_model_json2 == toolchain_tool_model_json

class TestModel_ToolchainToolCollection():
    """
    Test Class for ToolchainToolCollection
    """

    def test_toolchain_tool_collection_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        toolchain_tool_collection_first_model = {} # ToolchainToolCollectionFirst
        toolchain_tool_collection_first_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains/d02d29f1-e7bb-4977-8a6f-26d7b7bb893e/tools?limit=3'

        toolchain_tool_collection_previous_model = {} # ToolchainToolCollectionPrevious
        toolchain_tool_collection_previous_model['start'] = 'eyJpbnN0YW5jZV9pZCI6IjEzODgxYTZkLWI1ZDktNDQwNi05MzFmLWM4NTc1NDc0MmQ1NSJ9'
        toolchain_tool_collection_previous_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains/d02d29f1-e7bb-4977-8a6f-26d7b7bb893e/tools?limit=3&start=eyJpbnN0YW5jZV9pZCI6IjEzODgxYTZkLWI1ZDktNDQwNi05MzFmLWM4NTc1NDc0MmQ1NSJ9'

        toolchain_tool_collection_next_model = {} # ToolchainToolCollectionNext
        toolchain_tool_collection_next_model['start'] = 'eyJpbnN0YW5jZV9pZCI6IjlkZDBjNDc3LWYxNzMtNGMzZi1hN2NmLWQyNzAyNmFjZTM3OSJ9'
        toolchain_tool_collection_next_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains/d02d29f1-e7bb-4977-8a6f-26d7b7bb893e/tools?limit=3&start=eyJpbnN0YW5jZV9pZCI6IjlkZDBjNDc3LWYxNzMtNGMzZi1hN2NmLWQyNzAyNmFjZTM3OSJ9'

        toolchain_tool_collection_last_model = {} # ToolchainToolCollectionLast
        toolchain_tool_collection_last_model['start'] = 'eyJpbnN0YW5jZV9pZCI6ImQzYzkxMDYwLTcwOWMtNGZmZi1hODUwLTllZDFkZWMwMGYxYiJ9'
        toolchain_tool_collection_last_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains/d02d29f1-e7bb-4977-8a6f-26d7b7bb893e/tools?limit=3&start=eyJpbnN0YW5jZV9pZCI6ImQzYzkxMDYwLTcwOWMtNGZmZi1hODUwLTllZDFkZWMwMGYxYiJ9'

        tool_model_referent_model = {} # ToolModelReferent
        tool_model_referent_model['ui_href'] = 'https://team-one.slack.com/messages/channel-one'
        tool_model_referent_model['api_href'] = 'testString'

        tool_model_model = {} # ToolModel
        tool_model_model['id'] = '2983b160-fc37-4c45-8a8f-e616ad7e470b'
        tool_model_model['resource_group_id'] = '6a9a01f2cff54a7f966f803d92877123'
        tool_model_model['crn'] = 'crn:v1:staging:public:toolchain:us-south:a/f2337426699b4041bc50f1d45042f777:d02d29f1-e7bb-4977-8a6f-26d7b7bb893e:tool:2983b160-fc37-4c45-8a8f-e616ad7e470b'
        tool_model_model['tool_type_id'] = 'slack'
        tool_model_model['toolchain_id'] = 'd02d29f1-e7bb-4977-8a6f-26d7b7bb893e'
        tool_model_model['toolchain_crn'] = 'crn:v1:staging:public:toolchain:us-south:a/f2337426699b4041bc50f1d45042f777:d02d29f1-e7bb-4977-8a6f-26d7b7bb893e::'
        tool_model_model['href'] = 'https://api.us-south.devops.cloud.ibm.com/toolchain/v2/toolchains/d02d29f1-e7bb-4977-8a6f-26d7b7bb893e/tools/2983b160-fc37-4c45-8a8f-e616ad7e470b'
        tool_model_model['referent'] = tool_model_referent_model
        tool_model_model['name'] = 'MyTool-1'
        tool_model_model['updated_at'] = '2022-01-01T13:13:07.968000Z'
        tool_model_model['parameters'] = {'foo': 'bar'}
        tool_model_model['state'] = 'configured'

        # Construct a json representation of a ToolchainToolCollection model
        toolchain_tool_collection_model_json = {}
        toolchain_tool_collection_model_json['limit'] = 38
        toolchain_tool_collection_model_json['total_count'] = 38
        toolchain_tool_collection_model_json['first'] = toolchain_tool_collection_first_model
        toolchain_tool_collection_model_json['previous'] = toolchain_tool_collection_previous_model
        toolchain_tool_collection_model_json['next'] = toolchain_tool_collection_next_model
        toolchain_tool_collection_model_json['last'] = toolchain_tool_collection_last_model
        toolchain_tool_collection_model_json['tools'] = [tool_model_model]

        # Construct a model instance of ToolchainToolCollection by calling from_dict on the json representation
        toolchain_tool_collection_model = ToolchainToolCollection.from_dict(toolchain_tool_collection_model_json)
        assert toolchain_tool_collection_model != False

        # Construct a model instance of ToolchainToolCollection by calling from_dict on the json representation
        toolchain_tool_collection_model_dict = ToolchainToolCollection.from_dict(toolchain_tool_collection_model_json).__dict__
        toolchain_tool_collection_model2 = ToolchainToolCollection(**toolchain_tool_collection_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_collection_model == toolchain_tool_collection_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_collection_model_json2 = toolchain_tool_collection_model.to_dict()
        assert toolchain_tool_collection_model_json2 == toolchain_tool_collection_model_json

class TestModel_ToolchainToolCollectionFirst():
    """
    Test Class for ToolchainToolCollectionFirst
    """

    def test_toolchain_tool_collection_first_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolCollectionFirst
        """

        # Construct a json representation of a ToolchainToolCollectionFirst model
        toolchain_tool_collection_first_model_json = {}
        toolchain_tool_collection_first_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainToolCollectionFirst by calling from_dict on the json representation
        toolchain_tool_collection_first_model = ToolchainToolCollectionFirst.from_dict(toolchain_tool_collection_first_model_json)
        assert toolchain_tool_collection_first_model != False

        # Construct a model instance of ToolchainToolCollectionFirst by calling from_dict on the json representation
        toolchain_tool_collection_first_model_dict = ToolchainToolCollectionFirst.from_dict(toolchain_tool_collection_first_model_json).__dict__
        toolchain_tool_collection_first_model2 = ToolchainToolCollectionFirst(**toolchain_tool_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_collection_first_model == toolchain_tool_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_collection_first_model_json2 = toolchain_tool_collection_first_model.to_dict()
        assert toolchain_tool_collection_first_model_json2 == toolchain_tool_collection_first_model_json

class TestModel_ToolchainToolCollectionLast():
    """
    Test Class for ToolchainToolCollectionLast
    """

    def test_toolchain_tool_collection_last_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolCollectionLast
        """

        # Construct a json representation of a ToolchainToolCollectionLast model
        toolchain_tool_collection_last_model_json = {}
        toolchain_tool_collection_last_model_json['start'] = 'testString'
        toolchain_tool_collection_last_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainToolCollectionLast by calling from_dict on the json representation
        toolchain_tool_collection_last_model = ToolchainToolCollectionLast.from_dict(toolchain_tool_collection_last_model_json)
        assert toolchain_tool_collection_last_model != False

        # Construct a model instance of ToolchainToolCollectionLast by calling from_dict on the json representation
        toolchain_tool_collection_last_model_dict = ToolchainToolCollectionLast.from_dict(toolchain_tool_collection_last_model_json).__dict__
        toolchain_tool_collection_last_model2 = ToolchainToolCollectionLast(**toolchain_tool_collection_last_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_collection_last_model == toolchain_tool_collection_last_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_collection_last_model_json2 = toolchain_tool_collection_last_model.to_dict()
        assert toolchain_tool_collection_last_model_json2 == toolchain_tool_collection_last_model_json

class TestModel_ToolchainToolCollectionNext():
    """
    Test Class for ToolchainToolCollectionNext
    """

    def test_toolchain_tool_collection_next_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolCollectionNext
        """

        # Construct a json representation of a ToolchainToolCollectionNext model
        toolchain_tool_collection_next_model_json = {}
        toolchain_tool_collection_next_model_json['start'] = 'testString'
        toolchain_tool_collection_next_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainToolCollectionNext by calling from_dict on the json representation
        toolchain_tool_collection_next_model = ToolchainToolCollectionNext.from_dict(toolchain_tool_collection_next_model_json)
        assert toolchain_tool_collection_next_model != False

        # Construct a model instance of ToolchainToolCollectionNext by calling from_dict on the json representation
        toolchain_tool_collection_next_model_dict = ToolchainToolCollectionNext.from_dict(toolchain_tool_collection_next_model_json).__dict__
        toolchain_tool_collection_next_model2 = ToolchainToolCollectionNext(**toolchain_tool_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_collection_next_model == toolchain_tool_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_collection_next_model_json2 = toolchain_tool_collection_next_model.to_dict()
        assert toolchain_tool_collection_next_model_json2 == toolchain_tool_collection_next_model_json

class TestModel_ToolchainToolCollectionPrevious():
    """
    Test Class for ToolchainToolCollectionPrevious
    """

    def test_toolchain_tool_collection_previous_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolCollectionPrevious
        """

        # Construct a json representation of a ToolchainToolCollectionPrevious model
        toolchain_tool_collection_previous_model_json = {}
        toolchain_tool_collection_previous_model_json['start'] = 'testString'
        toolchain_tool_collection_previous_model_json['href'] = 'testString'

        # Construct a model instance of ToolchainToolCollectionPrevious by calling from_dict on the json representation
        toolchain_tool_collection_previous_model = ToolchainToolCollectionPrevious.from_dict(toolchain_tool_collection_previous_model_json)
        assert toolchain_tool_collection_previous_model != False

        # Construct a model instance of ToolchainToolCollectionPrevious by calling from_dict on the json representation
        toolchain_tool_collection_previous_model_dict = ToolchainToolCollectionPrevious.from_dict(toolchain_tool_collection_previous_model_json).__dict__
        toolchain_tool_collection_previous_model2 = ToolchainToolCollectionPrevious(**toolchain_tool_collection_previous_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_collection_previous_model == toolchain_tool_collection_previous_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_collection_previous_model_json2 = toolchain_tool_collection_previous_model.to_dict()
        assert toolchain_tool_collection_previous_model_json2 == toolchain_tool_collection_previous_model_json

class TestModel_ToolchainToolPatch():
    """
    Test Class for ToolchainToolPatch
    """

    def test_toolchain_tool_patch_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tool_model_referent_model = {} # ToolModelReferent
        tool_model_referent_model['ui_href'] = 'https://my-team.slack.com/messages/my-channel'
        tool_model_referent_model['api_href'] = 'testString'

        # Construct a json representation of a ToolchainToolPatch model
        toolchain_tool_patch_model_json = {}
        toolchain_tool_patch_model_json['id'] = 'testString'
        toolchain_tool_patch_model_json['resource_group_id'] = 'testString'
        toolchain_tool_patch_model_json['crn'] = 'testString'
        toolchain_tool_patch_model_json['tool_type_id'] = 'testString'
        toolchain_tool_patch_model_json['toolchain_id'] = 'testString'
        toolchain_tool_patch_model_json['toolchain_crn'] = 'testString'
        toolchain_tool_patch_model_json['href'] = 'testString'
        toolchain_tool_patch_model_json['referent'] = tool_model_referent_model
        toolchain_tool_patch_model_json['name'] = 'testString'
        toolchain_tool_patch_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        toolchain_tool_patch_model_json['parameters'] = {'foo': 'bar'}
        toolchain_tool_patch_model_json['state'] = 'configured'

        # Construct a model instance of ToolchainToolPatch by calling from_dict on the json representation
        toolchain_tool_patch_model = ToolchainToolPatch.from_dict(toolchain_tool_patch_model_json)
        assert toolchain_tool_patch_model != False

        # Construct a model instance of ToolchainToolPatch by calling from_dict on the json representation
        toolchain_tool_patch_model_dict = ToolchainToolPatch.from_dict(toolchain_tool_patch_model_json).__dict__
        toolchain_tool_patch_model2 = ToolchainToolPatch(**toolchain_tool_patch_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_patch_model == toolchain_tool_patch_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_patch_model_json2 = toolchain_tool_patch_model.to_dict()
        assert toolchain_tool_patch_model_json2 == toolchain_tool_patch_model_json

class TestModel_ToolchainToolPost():
    """
    Test Class for ToolchainToolPost
    """

    def test_toolchain_tool_post_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolPost
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tool_model_referent_model = {} # ToolModelReferent
        tool_model_referent_model['ui_href'] = 'https://my-team.slack.com/messages/my-channel'
        tool_model_referent_model['api_href'] = 'testString'

        # Construct a json representation of a ToolchainToolPost model
        toolchain_tool_post_model_json = {}
        toolchain_tool_post_model_json['id'] = 'testString'
        toolchain_tool_post_model_json['resource_group_id'] = 'testString'
        toolchain_tool_post_model_json['crn'] = 'testString'
        toolchain_tool_post_model_json['tool_type_id'] = 'testString'
        toolchain_tool_post_model_json['toolchain_id'] = 'testString'
        toolchain_tool_post_model_json['toolchain_crn'] = 'testString'
        toolchain_tool_post_model_json['href'] = 'testString'
        toolchain_tool_post_model_json['referent'] = tool_model_referent_model
        toolchain_tool_post_model_json['name'] = 'testString'
        toolchain_tool_post_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        toolchain_tool_post_model_json['parameters'] = {'foo': 'bar'}
        toolchain_tool_post_model_json['state'] = 'configured'

        # Construct a model instance of ToolchainToolPost by calling from_dict on the json representation
        toolchain_tool_post_model = ToolchainToolPost.from_dict(toolchain_tool_post_model_json)
        assert toolchain_tool_post_model != False

        # Construct a model instance of ToolchainToolPost by calling from_dict on the json representation
        toolchain_tool_post_model_dict = ToolchainToolPost.from_dict(toolchain_tool_post_model_json).__dict__
        toolchain_tool_post_model2 = ToolchainToolPost(**toolchain_tool_post_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_post_model == toolchain_tool_post_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_post_model_json2 = toolchain_tool_post_model.to_dict()
        assert toolchain_tool_post_model_json2 == toolchain_tool_post_model_json

class TestModel_ToolchainToolPrototypePatch():
    """
    Test Class for ToolchainToolPrototypePatch
    """

    def test_toolchain_tool_prototype_patch_serialization(self):
        """
        Test serialization/deserialization for ToolchainToolPrototypePatch
        """

        # Construct a json representation of a ToolchainToolPrototypePatch model
        toolchain_tool_prototype_patch_model_json = {}
        toolchain_tool_prototype_patch_model_json['name'] = 'MyTool'
        toolchain_tool_prototype_patch_model_json['tool_type_id'] = 'draservicebroker'
        toolchain_tool_prototype_patch_model_json['parameters'] = {'foo': 'bar'}

        # Construct a model instance of ToolchainToolPrototypePatch by calling from_dict on the json representation
        toolchain_tool_prototype_patch_model = ToolchainToolPrototypePatch.from_dict(toolchain_tool_prototype_patch_model_json)
        assert toolchain_tool_prototype_patch_model != False

        # Construct a model instance of ToolchainToolPrototypePatch by calling from_dict on the json representation
        toolchain_tool_prototype_patch_model_dict = ToolchainToolPrototypePatch.from_dict(toolchain_tool_prototype_patch_model_json).__dict__
        toolchain_tool_prototype_patch_model2 = ToolchainToolPrototypePatch(**toolchain_tool_prototype_patch_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_tool_prototype_patch_model == toolchain_tool_prototype_patch_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_tool_prototype_patch_model_json2 = toolchain_tool_prototype_patch_model.to_dict()
        assert toolchain_tool_prototype_patch_model_json2 == toolchain_tool_prototype_patch_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
