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
Unit Tests for CdTektonPipelineV2
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
from ibm_continuous_delivery.cd_tekton_pipeline_v2 import *


_service = CdTektonPipelineV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://api.us-south.devops.cloud.ibm.com/pipeline/v2'
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
    assert CdTektonPipelineV2.get_service_url_for_region('INVALID_REGION') is None
    assert CdTektonPipelineV2.get_service_url_for_region('us-south') == 'https://api.us-south.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('us-east') == 'https://api.us-east.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('eu-de') == 'https://api.eu-de.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('eu-gb') == 'https://api.eu-gb.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('jp-osa') == 'https://api.jp-osa.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('jp-tok') == 'https://api.jp-tok.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('au-syd') == 'https://api.au-syd.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('ca-tor') == 'https://api.ca-tor.devops.cloud.ibm.com/pipeline/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('br-sao') == 'https://api.br-sao.devops.cloud.ibm.com/pipeline/v2'


##############################################################################
# Start of Service: Pipeline
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

        service = CdTektonPipelineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdTektonPipelineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdTektonPipelineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateTektonPipeline():
    """
    Test Class for create_tekton_pipeline
    """

    @responses.activate
    def test_create_tekton_pipeline_all_params(self):
        """
        create_tekton_pipeline()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines')
        mock_response = '{"name": "name", "status": "configured", "resource_group": {"id": "id"}, "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created_at": "2019-01-01T12:00:00.000Z", "triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}], "worker": {"name": "name", "type": "type", "id": "id"}, "runs_url": "runs_url", "build_number": 1, "enable_notifications": true, "enable_partial_cloning": true, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a WorkerIdentity model
        worker_identity_model = {}
        worker_identity_model['id'] = 'public'

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'
        enable_notifications = False
        enable_partial_cloning = False
        worker = worker_identity_model

        # Invoke method
        response = _service.create_tekton_pipeline(
            id=id,
            enable_notifications=enable_notifications,
            enable_partial_cloning=enable_partial_cloning,
            worker=worker,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == '94619026-912b-4d92-8f51-6c74f0692d90'
        assert req_body['enable_notifications'] == False
        assert req_body['enable_partial_cloning'] == False
        assert req_body['worker'] == worker_identity_model

    def test_create_tekton_pipeline_all_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_all_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_all_params()

        # Disable retries and run test_create_tekton_pipeline_all_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_all_params()

    @responses.activate
    def test_create_tekton_pipeline_required_params(self):
        """
        test_create_tekton_pipeline_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines')
        mock_response = '{"name": "name", "status": "configured", "resource_group": {"id": "id"}, "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created_at": "2019-01-01T12:00:00.000Z", "triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}], "worker": {"name": "name", "type": "type", "id": "id"}, "runs_url": "runs_url", "build_number": 1, "enable_notifications": true, "enable_partial_cloning": true, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = _service.create_tekton_pipeline()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_tekton_pipeline_required_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_required_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_required_params()

        # Disable retries and run test_create_tekton_pipeline_required_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_required_params()

class TestGetTektonPipeline():
    """
    Test Class for get_tekton_pipeline
    """

    @responses.activate
    def test_get_tekton_pipeline_all_params(self):
        """
        get_tekton_pipeline()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"name": "name", "status": "configured", "resource_group": {"id": "id"}, "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created_at": "2019-01-01T12:00:00.000Z", "triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}], "worker": {"name": "name", "type": "type", "id": "id"}, "runs_url": "runs_url", "build_number": 1, "enable_notifications": true, "enable_partial_cloning": true, "enabled": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.get_tekton_pipeline(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_all_params()

        # Disable retries and run test_get_tekton_pipeline_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_all_params()

    @responses.activate
    def test_get_tekton_pipeline_value_error(self):
        """
        test_get_tekton_pipeline_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"name": "name", "status": "configured", "resource_group": {"id": "id"}, "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created_at": "2019-01-01T12:00:00.000Z", "triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}], "worker": {"name": "name", "type": "type", "id": "id"}, "runs_url": "runs_url", "build_number": 1, "enable_notifications": true, "enable_partial_cloning": true, "enabled": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline(**req_copy)

    def test_get_tekton_pipeline_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_value_error()

        # Disable retries and run test_get_tekton_pipeline_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_value_error()

class TestUpdateTektonPipeline():
    """
    Test Class for update_tekton_pipeline
    """

    @responses.activate
    def test_update_tekton_pipeline_all_params(self):
        """
        update_tekton_pipeline()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"name": "name", "status": "configured", "resource_group": {"id": "id"}, "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created_at": "2019-01-01T12:00:00.000Z", "triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}], "worker": {"name": "name", "type": "type", "id": "id"}, "runs_url": "runs_url", "build_number": 1, "enable_notifications": true, "enable_partial_cloning": true, "enabled": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a WorkerIdentity model
        worker_identity_model = {}
        worker_identity_model['id'] = 'public'

        # Construct a dict representation of a TektonPipelinePatch model
        tekton_pipeline_patch_model = {}
        tekton_pipeline_patch_model['enable_notifications'] = True
        tekton_pipeline_patch_model['enable_partial_cloning'] = True
        tekton_pipeline_patch_model['worker'] = worker_identity_model

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'
        tekton_pipeline_patch = tekton_pipeline_patch_model

        # Invoke method
        response = _service.update_tekton_pipeline(
            id,
            tekton_pipeline_patch=tekton_pipeline_patch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == tekton_pipeline_patch

    def test_update_tekton_pipeline_all_params_with_retries(self):
        # Enable retries and run test_update_tekton_pipeline_all_params.
        _service.enable_retries()
        self.test_update_tekton_pipeline_all_params()

        # Disable retries and run test_update_tekton_pipeline_all_params.
        _service.disable_retries()
        self.test_update_tekton_pipeline_all_params()

    @responses.activate
    def test_update_tekton_pipeline_required_params(self):
        """
        test_update_tekton_pipeline_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"name": "name", "status": "configured", "resource_group": {"id": "id"}, "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created_at": "2019-01-01T12:00:00.000Z", "triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}], "worker": {"name": "name", "type": "type", "id": "id"}, "runs_url": "runs_url", "build_number": 1, "enable_notifications": true, "enable_partial_cloning": true, "enabled": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.update_tekton_pipeline(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_tekton_pipeline_required_params_with_retries(self):
        # Enable retries and run test_update_tekton_pipeline_required_params.
        _service.enable_retries()
        self.test_update_tekton_pipeline_required_params()

        # Disable retries and run test_update_tekton_pipeline_required_params.
        _service.disable_retries()
        self.test_update_tekton_pipeline_required_params()

    @responses.activate
    def test_update_tekton_pipeline_value_error(self):
        """
        test_update_tekton_pipeline_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"name": "name", "status": "configured", "resource_group": {"id": "id"}, "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created_at": "2019-01-01T12:00:00.000Z", "triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}], "worker": {"name": "name", "type": "type", "id": "id"}, "runs_url": "runs_url", "build_number": 1, "enable_notifications": true, "enable_partial_cloning": true, "enabled": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_tekton_pipeline(**req_copy)

    def test_update_tekton_pipeline_value_error_with_retries(self):
        # Enable retries and run test_update_tekton_pipeline_value_error.
        _service.enable_retries()
        self.test_update_tekton_pipeline_value_error()

        # Disable retries and run test_update_tekton_pipeline_value_error.
        _service.disable_retries()
        self.test_update_tekton_pipeline_value_error()

class TestDeleteTektonPipeline():
    """
    Test Class for delete_tekton_pipeline
    """

    @responses.activate
    def test_delete_tekton_pipeline_all_params(self):
        """
        delete_tekton_pipeline()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.delete_tekton_pipeline(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tekton_pipeline_all_params_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_all_params.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_all_params()

        # Disable retries and run test_delete_tekton_pipeline_all_params.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_all_params()

    @responses.activate
    def test_delete_tekton_pipeline_value_error(self):
        """
        test_delete_tekton_pipeline_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tekton_pipeline(**req_copy)

    def test_delete_tekton_pipeline_value_error_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_value_error.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_value_error()

        # Disable retries and run test_delete_tekton_pipeline_value_error.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_value_error()

# endregion
##############################################################################
# End of Service: Pipeline
##############################################################################

##############################################################################
# Start of Service: PipelineRuns
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

        service = CdTektonPipelineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdTektonPipelineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdTektonPipelineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListTektonPipelineRuns():
    """
    Test Class for list_tekton_pipeline_runs
    """

    @responses.activate
    def test_list_tekton_pipeline_runs_all_params(self):
        """
        list_tekton_pipeline_runs()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response = '{"pipeline_runs": [{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url", "href": "href"}], "limit": 20, "first": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        start = 'testString'
        limit = 1
        status = 'succeeded'
        trigger_name = 'manual-trigger'

        # Invoke method
        response = _service.list_tekton_pipeline_runs(
            pipeline_id,
            start=start,
            limit=limit,
            status=status,
            trigger_name=trigger_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'status={}'.format(status) in query_string
        assert 'trigger.name={}'.format(trigger_name) in query_string

    def test_list_tekton_pipeline_runs_all_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_runs_all_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_runs_all_params()

        # Disable retries and run test_list_tekton_pipeline_runs_all_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_runs_all_params()

    @responses.activate
    def test_list_tekton_pipeline_runs_required_params(self):
        """
        test_list_tekton_pipeline_runs_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response = '{"pipeline_runs": [{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url", "href": "href"}], "limit": 20, "first": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.list_tekton_pipeline_runs(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tekton_pipeline_runs_required_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_runs_required_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_runs_required_params()

        # Disable retries and run test_list_tekton_pipeline_runs_required_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_runs_required_params()

    @responses.activate
    def test_list_tekton_pipeline_runs_value_error(self):
        """
        test_list_tekton_pipeline_runs_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response = '{"pipeline_runs": [{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url", "href": "href"}], "limit": 20, "first": {"href": "href"}, "next": {"href": "href"}, "last": {"href": "href"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tekton_pipeline_runs(**req_copy)

    def test_list_tekton_pipeline_runs_value_error_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_runs_value_error.
        _service.enable_retries()
        self.test_list_tekton_pipeline_runs_value_error()

        # Disable retries and run test_list_tekton_pipeline_runs_value_error.
        _service.disable_retries()
        self.test_list_tekton_pipeline_runs_value_error()

    @responses.activate
    def test_list_tekton_pipeline_runs_with_pager_get_next(self):
        """
        test_list_tekton_pipeline_runs_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"total_count":2,"limit":1,"pipeline_runs":[{"id":"id","user_info":{"iam_id":"iam_id","sub":"sub"},"status":"pending","definition_id":"definition_id","worker":{"name":"name","agent_id":"agent_id","service_id":"service_id","id":"id"},"pipeline_id":"pipeline_id","listener_name":"listener_name","trigger":{"type":"type","name":"start-deploy","href":"href","event_listener":"event_listener","id":"id","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path","href":"href"}],"tags":["tags"],"worker":{"name":"name","type":"type","id":"id"},"max_concurrent_runs":4,"enabled":true},"event_params_blob":"event_params_blob","trigger_headers":"trigger_headers","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path"}],"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","run_url":"run_url","href":"href"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"pipeline_runs":[{"id":"id","user_info":{"iam_id":"iam_id","sub":"sub"},"status":"pending","definition_id":"definition_id","worker":{"name":"name","agent_id":"agent_id","service_id":"service_id","id":"id"},"pipeline_id":"pipeline_id","listener_name":"listener_name","trigger":{"type":"type","name":"start-deploy","href":"href","event_listener":"event_listener","id":"id","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path","href":"href"}],"tags":["tags"],"worker":{"name":"name","type":"type","id":"id"},"max_concurrent_runs":4,"enabled":true},"event_params_blob":"event_params_blob","trigger_headers":"trigger_headers","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path"}],"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","run_url":"run_url","href":"href"}]}'
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
        pager = TektonPipelineRunsPager(
            client=_service,
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            limit=10,
            status='succeeded',
            trigger_name='manual-trigger',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_tekton_pipeline_runs_with_pager_get_all(self):
        """
        test_list_tekton_pipeline_runs_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?start=1"},"total_count":2,"limit":1,"pipeline_runs":[{"id":"id","user_info":{"iam_id":"iam_id","sub":"sub"},"status":"pending","definition_id":"definition_id","worker":{"name":"name","agent_id":"agent_id","service_id":"service_id","id":"id"},"pipeline_id":"pipeline_id","listener_name":"listener_name","trigger":{"type":"type","name":"start-deploy","href":"href","event_listener":"event_listener","id":"id","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path","href":"href"}],"tags":["tags"],"worker":{"name":"name","type":"type","id":"id"},"max_concurrent_runs":4,"enabled":true},"event_params_blob":"event_params_blob","trigger_headers":"trigger_headers","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path"}],"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","run_url":"run_url","href":"href"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"pipeline_runs":[{"id":"id","user_info":{"iam_id":"iam_id","sub":"sub"},"status":"pending","definition_id":"definition_id","worker":{"name":"name","agent_id":"agent_id","service_id":"service_id","id":"id"},"pipeline_id":"pipeline_id","listener_name":"listener_name","trigger":{"type":"type","name":"start-deploy","href":"href","event_listener":"event_listener","id":"id","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path","href":"href"}],"tags":["tags"],"worker":{"name":"name","type":"type","id":"id"},"max_concurrent_runs":4,"enabled":true},"event_params_blob":"event_params_blob","trigger_headers":"trigger_headers","properties":[{"name":"name","value":"value","enum":["enum"],"type":"secure","path":"path"}],"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z","run_url":"run_url","href":"href"}]}'
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
        pager = TektonPipelineRunsPager(
            client=_service,
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            limit=10,
            status='succeeded',
            trigger_name='manual-trigger',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2

class TestCreateTektonPipelineRun():
    """
    Test Class for create_tekton_pipeline_run
    """

    @responses.activate
    def test_create_tekton_pipeline_run_all_params(self):
        """
        create_tekton_pipeline_run()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Property model
        property_model = {}
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['type'] = 'secure'
        property_model['path'] = 'testString'

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_name = 'Generic Webhook Trigger - 0'
        trigger_properties = [property_model]
        secure_trigger_properties = [property_model]
        trigger_headers = {'foo': 'bar'}
        trigger_body = {'foo': 'bar'}

        # Invoke method
        response = _service.create_tekton_pipeline_run(
            pipeline_id,
            trigger_name=trigger_name,
            trigger_properties=trigger_properties,
            secure_trigger_properties=secure_trigger_properties,
            trigger_headers=trigger_headers,
            trigger_body=trigger_body,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['trigger_name'] == 'Generic Webhook Trigger - 0'
        assert req_body['trigger_properties'] == [property_model]
        assert req_body['secure_trigger_properties'] == [property_model]
        assert req_body['trigger_headers'] == {'foo': 'bar'}
        assert req_body['trigger_body'] == {'foo': 'bar'}

    def test_create_tekton_pipeline_run_all_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_run_all_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_run_all_params()

        # Disable retries and run test_create_tekton_pipeline_run_all_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_run_all_params()

    @responses.activate
    def test_create_tekton_pipeline_run_required_params(self):
        """
        test_create_tekton_pipeline_run_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.create_tekton_pipeline_run(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_tekton_pipeline_run_required_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_run_required_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_run_required_params()

        # Disable retries and run test_create_tekton_pipeline_run_required_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_run_required_params()

    @responses.activate
    def test_create_tekton_pipeline_run_value_error(self):
        """
        test_create_tekton_pipeline_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tekton_pipeline_run(**req_copy)

    def test_create_tekton_pipeline_run_value_error_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_run_value_error.
        _service.enable_retries()
        self.test_create_tekton_pipeline_run_value_error()

        # Disable retries and run test_create_tekton_pipeline_run_value_error.
        _service.disable_retries()
        self.test_create_tekton_pipeline_run_value_error()

class TestGetTektonPipelineRun():
    """
    Test Class for get_tekton_pipeline_run
    """

    @responses.activate
    def test_get_tekton_pipeline_run_all_params(self):
        """
        get_tekton_pipeline_run()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'
        includes = 'definitions'

        # Invoke method
        response = _service.get_tekton_pipeline_run(
            pipeline_id,
            id,
            includes=includes,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'includes={}'.format(includes) in query_string

    def test_get_tekton_pipeline_run_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_run_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_run_all_params()

        # Disable retries and run test_get_tekton_pipeline_run_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_run_all_params()

    @responses.activate
    def test_get_tekton_pipeline_run_required_params(self):
        """
        test_get_tekton_pipeline_run_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.get_tekton_pipeline_run(
            pipeline_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_run_required_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_run_required_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_run_required_params()

        # Disable retries and run test_get_tekton_pipeline_run_required_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_run_required_params()

    @responses.activate
    def test_get_tekton_pipeline_run_value_error(self):
        """
        test_get_tekton_pipeline_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline_run(**req_copy)

    def test_get_tekton_pipeline_run_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_run_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_run_value_error()

        # Disable retries and run test_get_tekton_pipeline_run_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_run_value_error()

class TestDeleteTektonPipelineRun():
    """
    Test Class for delete_tekton_pipeline_run
    """

    @responses.activate
    def test_delete_tekton_pipeline_run_all_params(self):
        """
        delete_tekton_pipeline_run()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.delete_tekton_pipeline_run(
            pipeline_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tekton_pipeline_run_all_params_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_run_all_params.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_run_all_params()

        # Disable retries and run test_delete_tekton_pipeline_run_all_params.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_run_all_params()

    @responses.activate
    def test_delete_tekton_pipeline_run_value_error(self):
        """
        test_delete_tekton_pipeline_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tekton_pipeline_run(**req_copy)

    def test_delete_tekton_pipeline_run_value_error_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_run_value_error.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_run_value_error()

        # Disable retries and run test_delete_tekton_pipeline_run_value_error.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_run_value_error()

class TestCancelTektonPipelineRun():
    """
    Test Class for cancel_tekton_pipeline_run
    """

    @responses.activate
    def test_cancel_tekton_pipeline_run_all_params(self):
        """
        cancel_tekton_pipeline_run()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90/cancel')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'
        force = True

        # Invoke method
        response = _service.cancel_tekton_pipeline_run(
            pipeline_id,
            id,
            force=force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['force'] == True

    def test_cancel_tekton_pipeline_run_all_params_with_retries(self):
        # Enable retries and run test_cancel_tekton_pipeline_run_all_params.
        _service.enable_retries()
        self.test_cancel_tekton_pipeline_run_all_params()

        # Disable retries and run test_cancel_tekton_pipeline_run_all_params.
        _service.disable_retries()
        self.test_cancel_tekton_pipeline_run_all_params()

    @responses.activate
    def test_cancel_tekton_pipeline_run_required_params(self):
        """
        test_cancel_tekton_pipeline_run_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90/cancel')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.cancel_tekton_pipeline_run(
            pipeline_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_cancel_tekton_pipeline_run_required_params_with_retries(self):
        # Enable retries and run test_cancel_tekton_pipeline_run_required_params.
        _service.enable_retries()
        self.test_cancel_tekton_pipeline_run_required_params()

        # Disable retries and run test_cancel_tekton_pipeline_run_required_params.
        _service.disable_retries()
        self.test_cancel_tekton_pipeline_run_required_params()

    @responses.activate
    def test_cancel_tekton_pipeline_run_value_error(self):
        """
        test_cancel_tekton_pipeline_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90/cancel')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.cancel_tekton_pipeline_run(**req_copy)

    def test_cancel_tekton_pipeline_run_value_error_with_retries(self):
        # Enable retries and run test_cancel_tekton_pipeline_run_value_error.
        _service.enable_retries()
        self.test_cancel_tekton_pipeline_run_value_error()

        # Disable retries and run test_cancel_tekton_pipeline_run_value_error.
        _service.disable_retries()
        self.test_cancel_tekton_pipeline_run_value_error()

class TestRerunTektonPipelineRun():
    """
    Test Class for rerun_tekton_pipeline_run
    """

    @responses.activate
    def test_rerun_tekton_pipeline_run_all_params(self):
        """
        rerun_tekton_pipeline_run()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90/rerun')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.rerun_tekton_pipeline_run(
            pipeline_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_rerun_tekton_pipeline_run_all_params_with_retries(self):
        # Enable retries and run test_rerun_tekton_pipeline_run_all_params.
        _service.enable_retries()
        self.test_rerun_tekton_pipeline_run_all_params()

        # Disable retries and run test_rerun_tekton_pipeline_run_all_params.
        _service.disable_retries()
        self.test_rerun_tekton_pipeline_run_all_params()

    @responses.activate
    def test_rerun_tekton_pipeline_run_value_error(self):
        """
        test_rerun_tekton_pipeline_run_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90/rerun')
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent_id": "agent_id", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}, "event_params_blob": "event_params_blob", "trigger_headers": "trigger_headers", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}], "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z", "run_url": "run_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.rerun_tekton_pipeline_run(**req_copy)

    def test_rerun_tekton_pipeline_run_value_error_with_retries(self):
        # Enable retries and run test_rerun_tekton_pipeline_run_value_error.
        _service.enable_retries()
        self.test_rerun_tekton_pipeline_run_value_error()

        # Disable retries and run test_rerun_tekton_pipeline_run_value_error.
        _service.disable_retries()
        self.test_rerun_tekton_pipeline_run_value_error()

class TestGetTektonPipelineRunLogs():
    """
    Test Class for get_tekton_pipeline_run_logs
    """

    @responses.activate
    def test_get_tekton_pipeline_run_logs_all_params(self):
        """
        get_tekton_pipeline_run_logs()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90/logs')
        mock_response = '{"logs": [{"href": "href", "id": "id", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.get_tekton_pipeline_run_logs(
            pipeline_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_run_logs_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_run_logs_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_run_logs_all_params()

        # Disable retries and run test_get_tekton_pipeline_run_logs_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_run_logs_all_params()

    @responses.activate
    def test_get_tekton_pipeline_run_logs_value_error(self):
        """
        test_get_tekton_pipeline_run_logs_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/94619026-912b-4d92-8f51-6c74f0692d90/logs')
        mock_response = '{"logs": [{"href": "href", "id": "id", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline_run_logs(**req_copy)

    def test_get_tekton_pipeline_run_logs_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_run_logs_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_run_logs_value_error()

        # Disable retries and run test_get_tekton_pipeline_run_logs_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_run_logs_value_error()

class TestGetTektonPipelineRunLogContent():
    """
    Test Class for get_tekton_pipeline_run_log_content
    """

    @responses.activate
    def test_get_tekton_pipeline_run_log_content_all_params(self):
        """
        get_tekton_pipeline_run_log_content()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/bf4b3abd-0c93-416b-911e-9cf42f1a1085/logs/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"data": "data", "id": "id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        pipeline_run_id = 'bf4b3abd-0c93-416b-911e-9cf42f1a1085'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.get_tekton_pipeline_run_log_content(
            pipeline_id,
            pipeline_run_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_run_log_content_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_run_log_content_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_run_log_content_all_params()

        # Disable retries and run test_get_tekton_pipeline_run_log_content_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_run_log_content_all_params()

    @responses.activate
    def test_get_tekton_pipeline_run_log_content_value_error(self):
        """
        test_get_tekton_pipeline_run_log_content_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/pipeline_runs/bf4b3abd-0c93-416b-911e-9cf42f1a1085/logs/94619026-912b-4d92-8f51-6c74f0692d90')
        mock_response = '{"data": "data", "id": "id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        pipeline_run_id = 'bf4b3abd-0c93-416b-911e-9cf42f1a1085'
        id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "pipeline_run_id": pipeline_run_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline_run_log_content(**req_copy)

    def test_get_tekton_pipeline_run_log_content_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_run_log_content_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_run_log_content_value_error()

        # Disable retries and run test_get_tekton_pipeline_run_log_content_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_run_log_content_value_error()

# endregion
##############################################################################
# End of Service: PipelineRuns
##############################################################################

##############################################################################
# Start of Service: Definitions
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

        service = CdTektonPipelineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdTektonPipelineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdTektonPipelineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListTektonPipelineDefinitions():
    """
    Test Class for list_tekton_pipeline_definitions
    """

    @responses.activate
    def test_list_tekton_pipeline_definitions_all_params(self):
        """
        list_tekton_pipeline_definitions()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions')
        mock_response = '{"definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.list_tekton_pipeline_definitions(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tekton_pipeline_definitions_all_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_definitions_all_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_definitions_all_params()

        # Disable retries and run test_list_tekton_pipeline_definitions_all_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_definitions_all_params()

    @responses.activate
    def test_list_tekton_pipeline_definitions_value_error(self):
        """
        test_list_tekton_pipeline_definitions_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions')
        mock_response = '{"definitions": [{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tekton_pipeline_definitions(**req_copy)

    def test_list_tekton_pipeline_definitions_value_error_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_definitions_value_error.
        _service.enable_retries()
        self.test_list_tekton_pipeline_definitions_value_error()

        # Disable retries and run test_list_tekton_pipeline_definitions_value_error.
        _service.disable_retries()
        self.test_list_tekton_pipeline_definitions_value_error()

class TestCreateTektonPipelineDefinition():
    """
    Test Class for create_tekton_pipeline_definition
    """

    @responses.activate
    def test_create_tekton_pipeline_definition_all_params(self):
        """
        create_tekton_pipeline_definition()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DefinitionSourcePropertiesTool model
        definition_source_properties_tool_model = {}
        definition_source_properties_tool_model['id'] = 'testString'

        # Construct a dict representation of a DefinitionSourceProperties model
        definition_source_properties_model = {}
        definition_source_properties_model['url'] = 'https://github.com/open-toolchain/hello-tekton.git'
        definition_source_properties_model['branch'] = 'master'
        definition_source_properties_model['tag'] = 'testString'
        definition_source_properties_model['path'] = '.tekton'
        definition_source_properties_model['tool'] = definition_source_properties_tool_model

        # Construct a dict representation of a DefinitionSource model
        definition_source_model = {}
        definition_source_model['type'] = 'git'
        definition_source_model['properties'] = definition_source_properties_model

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        source = definition_source_model

        # Invoke method
        response = _service.create_tekton_pipeline_definition(
            pipeline_id,
            source=source,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source'] == definition_source_model

    def test_create_tekton_pipeline_definition_all_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_definition_all_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_definition_all_params()

        # Disable retries and run test_create_tekton_pipeline_definition_all_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_definition_all_params()

    @responses.activate
    def test_create_tekton_pipeline_definition_required_params(self):
        """
        test_create_tekton_pipeline_definition_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.create_tekton_pipeline_definition(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_tekton_pipeline_definition_required_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_definition_required_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_definition_required_params()

        # Disable retries and run test_create_tekton_pipeline_definition_required_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_definition_required_params()

    @responses.activate
    def test_create_tekton_pipeline_definition_value_error(self):
        """
        test_create_tekton_pipeline_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tekton_pipeline_definition(**req_copy)

    def test_create_tekton_pipeline_definition_value_error_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_definition_value_error.
        _service.enable_retries()
        self.test_create_tekton_pipeline_definition_value_error()

        # Disable retries and run test_create_tekton_pipeline_definition_value_error.
        _service.disable_retries()
        self.test_create_tekton_pipeline_definition_value_error()

class TestGetTektonPipelineDefinition():
    """
    Test Class for get_tekton_pipeline_definition
    """

    @responses.activate
    def test_get_tekton_pipeline_definition_all_params(self):
        """
        get_tekton_pipeline_definition()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions/94299034-d45f-4e9a-8ed5-6bd5c7bb7ada')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'

        # Invoke method
        response = _service.get_tekton_pipeline_definition(
            pipeline_id,
            definition_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_definition_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_definition_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_definition_all_params()

        # Disable retries and run test_get_tekton_pipeline_definition_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_definition_all_params()

    @responses.activate
    def test_get_tekton_pipeline_definition_value_error(self):
        """
        test_get_tekton_pipeline_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions/94299034-d45f-4e9a-8ed5-6bd5c7bb7ada')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "definition_id": definition_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline_definition(**req_copy)

    def test_get_tekton_pipeline_definition_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_definition_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_definition_value_error()

        # Disable retries and run test_get_tekton_pipeline_definition_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_definition_value_error()

class TestReplaceTektonPipelineDefinition():
    """
    Test Class for replace_tekton_pipeline_definition
    """

    @responses.activate
    def test_replace_tekton_pipeline_definition_all_params(self):
        """
        replace_tekton_pipeline_definition()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions/94299034-d45f-4e9a-8ed5-6bd5c7bb7ada')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a DefinitionSourcePropertiesTool model
        definition_source_properties_tool_model = {}
        definition_source_properties_tool_model['id'] = 'testString'

        # Construct a dict representation of a DefinitionSourceProperties model
        definition_source_properties_model = {}
        definition_source_properties_model['url'] = 'testString'
        definition_source_properties_model['branch'] = 'testString'
        definition_source_properties_model['tag'] = 'testString'
        definition_source_properties_model['path'] = 'testString'
        definition_source_properties_model['tool'] = definition_source_properties_tool_model

        # Construct a dict representation of a DefinitionSource model
        definition_source_model = {}
        definition_source_model['type'] = 'testString'
        definition_source_model['properties'] = definition_source_properties_model

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
        source = definition_source_model

        # Invoke method
        response = _service.replace_tekton_pipeline_definition(
            pipeline_id,
            definition_id,
            source=source,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source'] == definition_source_model

    def test_replace_tekton_pipeline_definition_all_params_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_definition_all_params.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_definition_all_params()

        # Disable retries and run test_replace_tekton_pipeline_definition_all_params.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_definition_all_params()

    @responses.activate
    def test_replace_tekton_pipeline_definition_required_params(self):
        """
        test_replace_tekton_pipeline_definition_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions/94299034-d45f-4e9a-8ed5-6bd5c7bb7ada')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'

        # Invoke method
        response = _service.replace_tekton_pipeline_definition(
            pipeline_id,
            definition_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_tekton_pipeline_definition_required_params_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_definition_required_params.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_definition_required_params()

        # Disable retries and run test_replace_tekton_pipeline_definition_required_params.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_definition_required_params()

    @responses.activate
    def test_replace_tekton_pipeline_definition_value_error(self):
        """
        test_replace_tekton_pipeline_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions/94299034-d45f-4e9a-8ed5-6bd5c7bb7ada')
        mock_response = '{"source": {"type": "type", "properties": {"url": "url", "branch": "branch", "tag": "tag", "path": "path", "tool": {"id": "id"}}}, "id": "id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "definition_id": definition_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_tekton_pipeline_definition(**req_copy)

    def test_replace_tekton_pipeline_definition_value_error_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_definition_value_error.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_definition_value_error()

        # Disable retries and run test_replace_tekton_pipeline_definition_value_error.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_definition_value_error()

class TestDeleteTektonPipelineDefinition():
    """
    Test Class for delete_tekton_pipeline_definition
    """

    @responses.activate
    def test_delete_tekton_pipeline_definition_all_params(self):
        """
        delete_tekton_pipeline_definition()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions/94299034-d45f-4e9a-8ed5-6bd5c7bb7ada')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'

        # Invoke method
        response = _service.delete_tekton_pipeline_definition(
            pipeline_id,
            definition_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tekton_pipeline_definition_all_params_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_definition_all_params.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_definition_all_params()

        # Disable retries and run test_delete_tekton_pipeline_definition_all_params.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_definition_all_params()

    @responses.activate
    def test_delete_tekton_pipeline_definition_value_error(self):
        """
        test_delete_tekton_pipeline_definition_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/definitions/94299034-d45f-4e9a-8ed5-6bd5c7bb7ada')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "definition_id": definition_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tekton_pipeline_definition(**req_copy)

    def test_delete_tekton_pipeline_definition_value_error_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_definition_value_error.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_definition_value_error()

        # Disable retries and run test_delete_tekton_pipeline_definition_value_error.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_definition_value_error()

# endregion
##############################################################################
# End of Service: Definitions
##############################################################################

##############################################################################
# Start of Service: EnvironmentProperties
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

        service = CdTektonPipelineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdTektonPipelineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdTektonPipelineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListTektonPipelineProperties():
    """
    Test Class for list_tekton_pipeline_properties
    """

    @responses.activate
    def test_list_tekton_pipeline_properties_all_params(self):
        """
        list_tekton_pipeline_properties()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties')
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        name = 'prod'
        type = ['secure', 'text']
        sort = 'name'

        # Invoke method
        response = _service.list_tekton_pipeline_properties(
            pipeline_id,
            name=name,
            type=type,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'name={}'.format(name) in query_string
        assert 'type={}'.format(','.join(type)) in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_tekton_pipeline_properties_all_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_properties_all_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_properties_all_params()

        # Disable retries and run test_list_tekton_pipeline_properties_all_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_properties_all_params()

    @responses.activate
    def test_list_tekton_pipeline_properties_required_params(self):
        """
        test_list_tekton_pipeline_properties_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties')
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.list_tekton_pipeline_properties(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tekton_pipeline_properties_required_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_properties_required_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_properties_required_params()

        # Disable retries and run test_list_tekton_pipeline_properties_required_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_properties_required_params()

    @responses.activate
    def test_list_tekton_pipeline_properties_value_error(self):
        """
        test_list_tekton_pipeline_properties_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties')
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tekton_pipeline_properties(**req_copy)

    def test_list_tekton_pipeline_properties_value_error_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_properties_value_error.
        _service.enable_retries()
        self.test_list_tekton_pipeline_properties_value_error()

        # Disable retries and run test_list_tekton_pipeline_properties_value_error.
        _service.disable_retries()
        self.test_list_tekton_pipeline_properties_value_error()

class TestCreateTektonPipelineProperties():
    """
    Test Class for create_tekton_pipeline_properties
    """

    @responses.activate
    def test_create_tekton_pipeline_properties_all_params(self):
        """
        create_tekton_pipeline_properties()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        name = 'prop1'
        type = 'text'
        value = 'https://github.com/open-toolchain/hello-tekton.git'
        enum = ['testString']
        path = 'testString'

        # Invoke method
        response = _service.create_tekton_pipeline_properties(
            pipeline_id,
            name=name,
            type=type,
            value=value,
            enum=enum,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'prop1'
        assert req_body['type'] == 'text'
        assert req_body['value'] == 'https://github.com/open-toolchain/hello-tekton.git'
        assert req_body['enum'] == ['testString']
        assert req_body['path'] == 'testString'

    def test_create_tekton_pipeline_properties_all_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_properties_all_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_properties_all_params()

        # Disable retries and run test_create_tekton_pipeline_properties_all_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_properties_all_params()

    @responses.activate
    def test_create_tekton_pipeline_properties_required_params(self):
        """
        test_create_tekton_pipeline_properties_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.create_tekton_pipeline_properties(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_tekton_pipeline_properties_required_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_properties_required_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_properties_required_params()

        # Disable retries and run test_create_tekton_pipeline_properties_required_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_properties_required_params()

    @responses.activate
    def test_create_tekton_pipeline_properties_value_error(self):
        """
        test_create_tekton_pipeline_properties_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tekton_pipeline_properties(**req_copy)

    def test_create_tekton_pipeline_properties_value_error_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_properties_value_error.
        _service.enable_retries()
        self.test_create_tekton_pipeline_properties_value_error()

        # Disable retries and run test_create_tekton_pipeline_properties_value_error.
        _service.disable_retries()
        self.test_create_tekton_pipeline_properties_value_error()

class TestGetTektonPipelineProperty():
    """
    Test Class for get_tekton_pipeline_property
    """

    @responses.activate
    def test_get_tekton_pipeline_property_all_params(self):
        """
        get_tekton_pipeline_property()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'

        # Invoke method
        response = _service.get_tekton_pipeline_property(
            pipeline_id,
            property_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_property_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_property_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_property_all_params()

        # Disable retries and run test_get_tekton_pipeline_property_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_property_all_params()

    @responses.activate
    def test_get_tekton_pipeline_property_value_error(self):
        """
        test_get_tekton_pipeline_property_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "property_name": property_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline_property(**req_copy)

    def test_get_tekton_pipeline_property_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_property_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_property_value_error()

        # Disable retries and run test_get_tekton_pipeline_property_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_property_value_error()

class TestReplaceTektonPipelineProperty():
    """
    Test Class for replace_tekton_pipeline_property
    """

    @responses.activate
    def test_replace_tekton_pipeline_property_all_params(self):
        """
        replace_tekton_pipeline_property()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'
        name = 'prop1'
        type = 'text'
        value = 'https://github.com/open-toolchain/hello-tekton.git'
        enum = ['testString']
        path = 'testString'

        # Invoke method
        response = _service.replace_tekton_pipeline_property(
            pipeline_id,
            property_name,
            name=name,
            type=type,
            value=value,
            enum=enum,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'prop1'
        assert req_body['type'] == 'text'
        assert req_body['value'] == 'https://github.com/open-toolchain/hello-tekton.git'
        assert req_body['enum'] == ['testString']
        assert req_body['path'] == 'testString'

    def test_replace_tekton_pipeline_property_all_params_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_property_all_params.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_property_all_params()

        # Disable retries and run test_replace_tekton_pipeline_property_all_params.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_property_all_params()

    @responses.activate
    def test_replace_tekton_pipeline_property_required_params(self):
        """
        test_replace_tekton_pipeline_property_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'

        # Invoke method
        response = _service.replace_tekton_pipeline_property(
            pipeline_id,
            property_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_tekton_pipeline_property_required_params_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_property_required_params.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_property_required_params()

        # Disable retries and run test_replace_tekton_pipeline_property_required_params.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_property_required_params()

    @responses.activate
    def test_replace_tekton_pipeline_property_value_error(self):
        """
        test_replace_tekton_pipeline_property_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "property_name": property_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_tekton_pipeline_property(**req_copy)

    def test_replace_tekton_pipeline_property_value_error_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_property_value_error.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_property_value_error()

        # Disable retries and run test_replace_tekton_pipeline_property_value_error.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_property_value_error()

class TestDeleteTektonPipelineProperty():
    """
    Test Class for delete_tekton_pipeline_property
    """

    @responses.activate
    def test_delete_tekton_pipeline_property_all_params(self):
        """
        delete_tekton_pipeline_property()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties/debug-pipeline')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'

        # Invoke method
        response = _service.delete_tekton_pipeline_property(
            pipeline_id,
            property_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tekton_pipeline_property_all_params_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_property_all_params.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_property_all_params()

        # Disable retries and run test_delete_tekton_pipeline_property_all_params.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_property_all_params()

    @responses.activate
    def test_delete_tekton_pipeline_property_value_error(self):
        """
        test_delete_tekton_pipeline_property_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/properties/debug-pipeline')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "property_name": property_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tekton_pipeline_property(**req_copy)

    def test_delete_tekton_pipeline_property_value_error_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_property_value_error.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_property_value_error()

        # Disable retries and run test_delete_tekton_pipeline_property_value_error.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_property_value_error()

# endregion
##############################################################################
# End of Service: EnvironmentProperties
##############################################################################

##############################################################################
# Start of Service: Triggers
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

        service = CdTektonPipelineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdTektonPipelineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdTektonPipelineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListTektonPipelineTriggers():
    """
    Test Class for list_tekton_pipeline_triggers
    """

    @responses.activate
    def test_list_tekton_pipeline_triggers_all_params(self):
        """
        list_tekton_pipeline_triggers()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers')
        mock_response = '{"triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        type = 'manual,scm'
        name = 'testString'
        event_listener = 'testString'
        worker_id = 'testString'
        worker_name = 'testString'
        disabled = 'true'
        tags = 'tag1,tag2'

        # Invoke method
        response = _service.list_tekton_pipeline_triggers(
            pipeline_id,
            type=type,
            name=name,
            event_listener=event_listener,
            worker_id=worker_id,
            worker_name=worker_name,
            disabled=disabled,
            tags=tags,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'event_listener={}'.format(event_listener) in query_string
        assert 'worker.id={}'.format(worker_id) in query_string
        assert 'worker.name={}'.format(worker_name) in query_string
        assert 'disabled={}'.format(disabled) in query_string
        assert 'tags={}'.format(tags) in query_string

    def test_list_tekton_pipeline_triggers_all_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_triggers_all_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_triggers_all_params()

        # Disable retries and run test_list_tekton_pipeline_triggers_all_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_triggers_all_params()

    @responses.activate
    def test_list_tekton_pipeline_triggers_required_params(self):
        """
        test_list_tekton_pipeline_triggers_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers')
        mock_response = '{"triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.list_tekton_pipeline_triggers(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tekton_pipeline_triggers_required_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_triggers_required_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_triggers_required_params()

        # Disable retries and run test_list_tekton_pipeline_triggers_required_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_triggers_required_params()

    @responses.activate
    def test_list_tekton_pipeline_triggers_value_error(self):
        """
        test_list_tekton_pipeline_triggers_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers')
        mock_response = '{"triggers": [{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tekton_pipeline_triggers(**req_copy)

    def test_list_tekton_pipeline_triggers_value_error_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_triggers_value_error.
        _service.enable_retries()
        self.test_list_tekton_pipeline_triggers_value_error()

        # Disable retries and run test_list_tekton_pipeline_triggers_value_error.
        _service.disable_retries()
        self.test_list_tekton_pipeline_triggers_value_error()

class TestCreateTektonPipelineTrigger():
    """
    Test Class for create_tekton_pipeline_trigger
    """

    @responses.activate
    def test_create_tekton_pipeline_trigger_all_params(self):
        """
        create_tekton_pipeline_trigger()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Worker model
        worker_model = {}
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'public'

        # Construct a dict representation of a GenericSecret model
        generic_secret_model = {}
        generic_secret_model['type'] = 'token_matches'
        generic_secret_model['value'] = 'testString'
        generic_secret_model['source'] = 'header'
        generic_secret_model['key_name'] = 'testString'
        generic_secret_model['algorithm'] = 'md4'

        # Construct a dict representation of a TriggerSourcePropertiesTool model
        trigger_source_properties_tool_model = {}
        trigger_source_properties_tool_model['id'] = 'testString'

        # Construct a dict representation of a TriggerSourceProperties model
        trigger_source_properties_model = {}
        trigger_source_properties_model['url'] = 'testString'
        trigger_source_properties_model['branch'] = 'testString'
        trigger_source_properties_model['pattern'] = 'testString'
        trigger_source_properties_model['blind_connection'] = True
        trigger_source_properties_model['hook_id'] = 'testString'
        trigger_source_properties_model['tool'] = trigger_source_properties_tool_model

        # Construct a dict representation of a TriggerSource model
        trigger_source_model = {}
        trigger_source_model['type'] = 'testString'
        trigger_source_model['properties'] = trigger_source_properties_model

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        type = 'manual'
        name = 'Manual Trigger'
        event_listener = 'pr-listener'
        enabled = True
        tags = ['testString']
        worker = worker_model
        max_concurrent_runs = 3
        secret = generic_secret_model
        cron = 'testString'
        timezone = 'testString'
        source = trigger_source_model
        events = ['push']

        # Invoke method
        response = _service.create_tekton_pipeline_trigger(
            pipeline_id,
            type=type,
            name=name,
            event_listener=event_listener,
            enabled=enabled,
            tags=tags,
            worker=worker,
            max_concurrent_runs=max_concurrent_runs,
            secret=secret,
            cron=cron,
            timezone=timezone,
            source=source,
            events=events,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'manual'
        assert req_body['name'] == 'Manual Trigger'
        assert req_body['event_listener'] == 'pr-listener'
        assert req_body['enabled'] == True
        assert req_body['tags'] == ['testString']
        assert req_body['worker'] == worker_model
        assert req_body['max_concurrent_runs'] == 3
        assert req_body['secret'] == generic_secret_model
        assert req_body['cron'] == 'testString'
        assert req_body['timezone'] == 'testString'
        assert req_body['source'] == trigger_source_model
        assert req_body['events'] == ['push']

    def test_create_tekton_pipeline_trigger_all_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_trigger_all_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_trigger_all_params()

        # Disable retries and run test_create_tekton_pipeline_trigger_all_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_trigger_all_params()

    @responses.activate
    def test_create_tekton_pipeline_trigger_required_params(self):
        """
        test_create_tekton_pipeline_trigger_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Invoke method
        response = _service.create_tekton_pipeline_trigger(
            pipeline_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_tekton_pipeline_trigger_required_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_trigger_required_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_trigger_required_params()

        # Disable retries and run test_create_tekton_pipeline_trigger_required_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_trigger_required_params()

    @responses.activate
    def test_create_tekton_pipeline_trigger_value_error(self):
        """
        test_create_tekton_pipeline_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tekton_pipeline_trigger(**req_copy)

    def test_create_tekton_pipeline_trigger_value_error_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_trigger_value_error.
        _service.enable_retries()
        self.test_create_tekton_pipeline_trigger_value_error()

        # Disable retries and run test_create_tekton_pipeline_trigger_value_error.
        _service.disable_retries()
        self.test_create_tekton_pipeline_trigger_value_error()

class TestGetTektonPipelineTrigger():
    """
    Test Class for get_tekton_pipeline_trigger
    """

    @responses.activate
    def test_get_tekton_pipeline_trigger_all_params(self):
        """
        get_tekton_pipeline_trigger()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Invoke method
        response = _service.get_tekton_pipeline_trigger(
            pipeline_id,
            trigger_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_trigger_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_trigger_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_trigger_all_params()

        # Disable retries and run test_get_tekton_pipeline_trigger_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_trigger_all_params()

    @responses.activate
    def test_get_tekton_pipeline_trigger_value_error(self):
        """
        test_get_tekton_pipeline_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline_trigger(**req_copy)

    def test_get_tekton_pipeline_trigger_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_trigger_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_trigger_value_error()

        # Disable retries and run test_get_tekton_pipeline_trigger_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_trigger_value_error()

class TestUpdateTektonPipelineTrigger():
    """
    Test Class for update_tekton_pipeline_trigger
    """

    @responses.activate
    def test_update_tekton_pipeline_trigger_all_params(self):
        """
        update_tekton_pipeline_trigger()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Worker model
        worker_model = {}
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        # Construct a dict representation of a GenericSecret model
        generic_secret_model = {}
        generic_secret_model['type'] = 'token_matches'
        generic_secret_model['value'] = 'testString'
        generic_secret_model['source'] = 'header'
        generic_secret_model['key_name'] = 'testString'
        generic_secret_model['algorithm'] = 'md4'

        # Construct a dict representation of a TriggerSourcePropertiesTool model
        trigger_source_properties_tool_model = {}
        trigger_source_properties_tool_model['id'] = 'testString'

        # Construct a dict representation of a TriggerSourceProperties model
        trigger_source_properties_model = {}
        trigger_source_properties_model['url'] = 'testString'
        trigger_source_properties_model['branch'] = 'testString'
        trigger_source_properties_model['pattern'] = 'testString'
        trigger_source_properties_model['blind_connection'] = True
        trigger_source_properties_model['hook_id'] = 'testString'
        trigger_source_properties_model['tool'] = trigger_source_properties_tool_model

        # Construct a dict representation of a TriggerSource model
        trigger_source_model = {}
        trigger_source_model['type'] = 'testString'
        trigger_source_model['properties'] = trigger_source_properties_model

        # Construct a dict representation of a TriggerPatch model
        trigger_patch_model = {}
        trigger_patch_model['type'] = 'manual'
        trigger_patch_model['name'] = 'start-deploy'
        trigger_patch_model['event_listener'] = 'testString'
        trigger_patch_model['tags'] = ['testString']
        trigger_patch_model['worker'] = worker_model
        trigger_patch_model['max_concurrent_runs'] = 4
        trigger_patch_model['enabled'] = True
        trigger_patch_model['secret'] = generic_secret_model
        trigger_patch_model['cron'] = 'testString'
        trigger_patch_model['timezone'] = 'America/Los_Angeles, CET, Europe/London, GMT, US/Eastern, or UTC'
        trigger_patch_model['source'] = trigger_source_model
        trigger_patch_model['events'] = ['push', 'pull_request']

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        trigger_patch = trigger_patch_model

        # Invoke method
        response = _service.update_tekton_pipeline_trigger(
            pipeline_id,
            trigger_id,
            trigger_patch=trigger_patch,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == trigger_patch

    def test_update_tekton_pipeline_trigger_all_params_with_retries(self):
        # Enable retries and run test_update_tekton_pipeline_trigger_all_params.
        _service.enable_retries()
        self.test_update_tekton_pipeline_trigger_all_params()

        # Disable retries and run test_update_tekton_pipeline_trigger_all_params.
        _service.disable_retries()
        self.test_update_tekton_pipeline_trigger_all_params()

    @responses.activate
    def test_update_tekton_pipeline_trigger_required_params(self):
        """
        test_update_tekton_pipeline_trigger_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Invoke method
        response = _service.update_tekton_pipeline_trigger(
            pipeline_id,
            trigger_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_tekton_pipeline_trigger_required_params_with_retries(self):
        # Enable retries and run test_update_tekton_pipeline_trigger_required_params.
        _service.enable_retries()
        self.test_update_tekton_pipeline_trigger_required_params()

        # Disable retries and run test_update_tekton_pipeline_trigger_required_params.
        _service.disable_retries()
        self.test_update_tekton_pipeline_trigger_required_params()

    @responses.activate
    def test_update_tekton_pipeline_trigger_value_error(self):
        """
        test_update_tekton_pipeline_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_tekton_pipeline_trigger(**req_copy)

    def test_update_tekton_pipeline_trigger_value_error_with_retries(self):
        # Enable retries and run test_update_tekton_pipeline_trigger_value_error.
        _service.enable_retries()
        self.test_update_tekton_pipeline_trigger_value_error()

        # Disable retries and run test_update_tekton_pipeline_trigger_value_error.
        _service.disable_retries()
        self.test_update_tekton_pipeline_trigger_value_error()

class TestDeleteTektonPipelineTrigger():
    """
    Test Class for delete_tekton_pipeline_trigger
    """

    @responses.activate
    def test_delete_tekton_pipeline_trigger_all_params(self):
        """
        delete_tekton_pipeline_trigger()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Invoke method
        response = _service.delete_tekton_pipeline_trigger(
            pipeline_id,
            trigger_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tekton_pipeline_trigger_all_params_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_trigger_all_params.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_trigger_all_params()

        # Disable retries and run test_delete_tekton_pipeline_trigger_all_params.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_trigger_all_params()

    @responses.activate
    def test_delete_tekton_pipeline_trigger_value_error(self):
        """
        test_delete_tekton_pipeline_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tekton_pipeline_trigger(**req_copy)

    def test_delete_tekton_pipeline_trigger_value_error_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_trigger_value_error.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_trigger_value_error()

        # Disable retries and run test_delete_tekton_pipeline_trigger_value_error.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_trigger_value_error()

class TestDuplicateTektonPipelineTrigger():
    """
    Test Class for duplicate_tekton_pipeline_trigger
    """

    @responses.activate
    def test_duplicate_tekton_pipeline_trigger_all_params(self):
        """
        duplicate_tekton_pipeline_trigger()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/duplicate')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        source_trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        name = 'triggerName'

        # Invoke method
        response = _service.duplicate_tekton_pipeline_trigger(
            pipeline_id,
            source_trigger_id,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'triggerName'

    def test_duplicate_tekton_pipeline_trigger_all_params_with_retries(self):
        # Enable retries and run test_duplicate_tekton_pipeline_trigger_all_params.
        _service.enable_retries()
        self.test_duplicate_tekton_pipeline_trigger_all_params()

        # Disable retries and run test_duplicate_tekton_pipeline_trigger_all_params.
        _service.disable_retries()
        self.test_duplicate_tekton_pipeline_trigger_all_params()

    @responses.activate
    def test_duplicate_tekton_pipeline_trigger_required_params(self):
        """
        test_duplicate_tekton_pipeline_trigger_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/duplicate')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        source_trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Invoke method
        response = _service.duplicate_tekton_pipeline_trigger(
            pipeline_id,
            source_trigger_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_duplicate_tekton_pipeline_trigger_required_params_with_retries(self):
        # Enable retries and run test_duplicate_tekton_pipeline_trigger_required_params.
        _service.enable_retries()
        self.test_duplicate_tekton_pipeline_trigger_required_params()

        # Disable retries and run test_duplicate_tekton_pipeline_trigger_required_params.
        _service.disable_retries()
        self.test_duplicate_tekton_pipeline_trigger_required_params()

    @responses.activate
    def test_duplicate_tekton_pipeline_trigger_value_error(self):
        """
        test_duplicate_tekton_pipeline_trigger_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/duplicate')
        mock_response = '{"type": "type", "name": "start-deploy", "href": "href", "event_listener": "event_listener", "id": "id", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}], "tags": ["tags"], "worker": {"name": "name", "type": "type", "id": "id"}, "max_concurrent_runs": 4, "enabled": true}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        source_trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "source_trigger_id": source_trigger_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.duplicate_tekton_pipeline_trigger(**req_copy)

    def test_duplicate_tekton_pipeline_trigger_value_error_with_retries(self):
        # Enable retries and run test_duplicate_tekton_pipeline_trigger_value_error.
        _service.enable_retries()
        self.test_duplicate_tekton_pipeline_trigger_value_error()

        # Disable retries and run test_duplicate_tekton_pipeline_trigger_value_error.
        _service.disable_retries()
        self.test_duplicate_tekton_pipeline_trigger_value_error()

# endregion
##############################################################################
# End of Service: Triggers
##############################################################################

##############################################################################
# Start of Service: TriggerProperties
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

        service = CdTektonPipelineV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, CdTektonPipelineV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = CdTektonPipelineV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListTektonPipelineTriggerProperties():
    """
    Test Class for list_tekton_pipeline_trigger_properties
    """

    @responses.activate
    def test_list_tekton_pipeline_trigger_properties_all_params(self):
        """
        list_tekton_pipeline_trigger_properties()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties')
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        name = 'prod'
        type = 'secure,text'
        sort = 'name'

        # Invoke method
        response = _service.list_tekton_pipeline_trigger_properties(
            pipeline_id,
            trigger_id,
            name=name,
            type=type,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'name={}'.format(name) in query_string
        assert 'type={}'.format(type) in query_string
        assert 'sort={}'.format(sort) in query_string

    def test_list_tekton_pipeline_trigger_properties_all_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_trigger_properties_all_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_trigger_properties_all_params()

        # Disable retries and run test_list_tekton_pipeline_trigger_properties_all_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_trigger_properties_all_params()

    @responses.activate
    def test_list_tekton_pipeline_trigger_properties_required_params(self):
        """
        test_list_tekton_pipeline_trigger_properties_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties')
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Invoke method
        response = _service.list_tekton_pipeline_trigger_properties(
            pipeline_id,
            trigger_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tekton_pipeline_trigger_properties_required_params_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_trigger_properties_required_params.
        _service.enable_retries()
        self.test_list_tekton_pipeline_trigger_properties_required_params()

        # Disable retries and run test_list_tekton_pipeline_trigger_properties_required_params.
        _service.disable_retries()
        self.test_list_tekton_pipeline_trigger_properties_required_params()

    @responses.activate
    def test_list_tekton_pipeline_trigger_properties_value_error(self):
        """
        test_list_tekton_pipeline_trigger_properties_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties')
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tekton_pipeline_trigger_properties(**req_copy)

    def test_list_tekton_pipeline_trigger_properties_value_error_with_retries(self):
        # Enable retries and run test_list_tekton_pipeline_trigger_properties_value_error.
        _service.enable_retries()
        self.test_list_tekton_pipeline_trigger_properties_value_error()

        # Disable retries and run test_list_tekton_pipeline_trigger_properties_value_error.
        _service.disable_retries()
        self.test_list_tekton_pipeline_trigger_properties_value_error()

class TestCreateTektonPipelineTriggerProperties():
    """
    Test Class for create_tekton_pipeline_trigger_properties
    """

    @responses.activate
    def test_create_tekton_pipeline_trigger_properties_all_params(self):
        """
        create_tekton_pipeline_trigger_properties()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        name = 'prop1'
        type = 'text'
        value = 'https://github.com/open-toolchain/hello-tekton.git'
        enum = ['testString']
        path = 'testString'

        # Invoke method
        response = _service.create_tekton_pipeline_trigger_properties(
            pipeline_id,
            trigger_id,
            name=name,
            type=type,
            value=value,
            enum=enum,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'prop1'
        assert req_body['type'] == 'text'
        assert req_body['value'] == 'https://github.com/open-toolchain/hello-tekton.git'
        assert req_body['enum'] == ['testString']
        assert req_body['path'] == 'testString'

    def test_create_tekton_pipeline_trigger_properties_all_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_trigger_properties_all_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_trigger_properties_all_params()

        # Disable retries and run test_create_tekton_pipeline_trigger_properties_all_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_trigger_properties_all_params()

    @responses.activate
    def test_create_tekton_pipeline_trigger_properties_required_params(self):
        """
        test_create_tekton_pipeline_trigger_properties_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Invoke method
        response = _service.create_tekton_pipeline_trigger_properties(
            pipeline_id,
            trigger_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_tekton_pipeline_trigger_properties_required_params_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_trigger_properties_required_params.
        _service.enable_retries()
        self.test_create_tekton_pipeline_trigger_properties_required_params()

        # Disable retries and run test_create_tekton_pipeline_trigger_properties_required_params.
        _service.disable_retries()
        self.test_create_tekton_pipeline_trigger_properties_required_params()

    @responses.activate
    def test_create_tekton_pipeline_trigger_properties_value_error(self):
        """
        test_create_tekton_pipeline_trigger_properties_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tekton_pipeline_trigger_properties(**req_copy)

    def test_create_tekton_pipeline_trigger_properties_value_error_with_retries(self):
        # Enable retries and run test_create_tekton_pipeline_trigger_properties_value_error.
        _service.enable_retries()
        self.test_create_tekton_pipeline_trigger_properties_value_error()

        # Disable retries and run test_create_tekton_pipeline_trigger_properties_value_error.
        _service.disable_retries()
        self.test_create_tekton_pipeline_trigger_properties_value_error()

class TestGetTektonPipelineTriggerProperty():
    """
    Test Class for get_tekton_pipeline_trigger_property
    """

    @responses.activate
    def test_get_tekton_pipeline_trigger_property_all_params(self):
        """
        get_tekton_pipeline_trigger_property()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'

        # Invoke method
        response = _service.get_tekton_pipeline_trigger_property(
            pipeline_id,
            trigger_id,
            property_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tekton_pipeline_trigger_property_all_params_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_trigger_property_all_params.
        _service.enable_retries()
        self.test_get_tekton_pipeline_trigger_property_all_params()

        # Disable retries and run test_get_tekton_pipeline_trigger_property_all_params.
        _service.disable_retries()
        self.test_get_tekton_pipeline_trigger_property_all_params()

    @responses.activate
    def test_get_tekton_pipeline_trigger_property_value_error(self):
        """
        test_get_tekton_pipeline_trigger_property_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
            "property_name": property_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tekton_pipeline_trigger_property(**req_copy)

    def test_get_tekton_pipeline_trigger_property_value_error_with_retries(self):
        # Enable retries and run test_get_tekton_pipeline_trigger_property_value_error.
        _service.enable_retries()
        self.test_get_tekton_pipeline_trigger_property_value_error()

        # Disable retries and run test_get_tekton_pipeline_trigger_property_value_error.
        _service.disable_retries()
        self.test_get_tekton_pipeline_trigger_property_value_error()

class TestReplaceTektonPipelineTriggerProperty():
    """
    Test Class for replace_tekton_pipeline_trigger_property
    """

    @responses.activate
    def test_replace_tekton_pipeline_trigger_property_all_params(self):
        """
        replace_tekton_pipeline_trigger_property()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'
        name = 'prop1'
        type = 'text'
        value = 'https://github.com/open-toolchain/hello-tekton.git'
        enum = ['testString']
        path = 'testString'

        # Invoke method
        response = _service.replace_tekton_pipeline_trigger_property(
            pipeline_id,
            trigger_id,
            property_name,
            name=name,
            type=type,
            value=value,
            enum=enum,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'prop1'
        assert req_body['type'] == 'text'
        assert req_body['value'] == 'https://github.com/open-toolchain/hello-tekton.git'
        assert req_body['enum'] == ['testString']
        assert req_body['path'] == 'testString'

    def test_replace_tekton_pipeline_trigger_property_all_params_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_trigger_property_all_params.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_trigger_property_all_params()

        # Disable retries and run test_replace_tekton_pipeline_trigger_property_all_params.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_trigger_property_all_params()

    @responses.activate
    def test_replace_tekton_pipeline_trigger_property_required_params(self):
        """
        test_replace_tekton_pipeline_trigger_property_required_params()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'

        # Invoke method
        response = _service.replace_tekton_pipeline_trigger_property(
            pipeline_id,
            trigger_id,
            property_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_tekton_pipeline_trigger_property_required_params_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_trigger_property_required_params.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_trigger_property_required_params()

        # Disable retries and run test_replace_tekton_pipeline_trigger_property_required_params.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_trigger_property_required_params()

    @responses.activate
    def test_replace_tekton_pipeline_trigger_property_value_error(self):
        """
        test_replace_tekton_pipeline_trigger_property_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties/debug-pipeline')
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "type": "secure", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
            "property_name": property_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_tekton_pipeline_trigger_property(**req_copy)

    def test_replace_tekton_pipeline_trigger_property_value_error_with_retries(self):
        # Enable retries and run test_replace_tekton_pipeline_trigger_property_value_error.
        _service.enable_retries()
        self.test_replace_tekton_pipeline_trigger_property_value_error()

        # Disable retries and run test_replace_tekton_pipeline_trigger_property_value_error.
        _service.disable_retries()
        self.test_replace_tekton_pipeline_trigger_property_value_error()

class TestDeleteTektonPipelineTriggerProperty():
    """
    Test Class for delete_tekton_pipeline_trigger_property
    """

    @responses.activate
    def test_delete_tekton_pipeline_trigger_property_all_params(self):
        """
        delete_tekton_pipeline_trigger_property()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties/debug-pipeline')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'

        # Invoke method
        response = _service.delete_tekton_pipeline_trigger_property(
            pipeline_id,
            trigger_id,
            property_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tekton_pipeline_trigger_property_all_params_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_trigger_property_all_params.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_trigger_property_all_params()

        # Disable retries and run test_delete_tekton_pipeline_trigger_property_all_params.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_trigger_property_all_params()

    @responses.activate
    def test_delete_tekton_pipeline_trigger_property_value_error(self):
        """
        test_delete_tekton_pipeline_trigger_property_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties/debug-pipeline')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
            "property_name": property_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tekton_pipeline_trigger_property(**req_copy)

    def test_delete_tekton_pipeline_trigger_property_value_error_with_retries(self):
        # Enable retries and run test_delete_tekton_pipeline_trigger_property_value_error.
        _service.enable_retries()
        self.test_delete_tekton_pipeline_trigger_property_value_error()

        # Disable retries and run test_delete_tekton_pipeline_trigger_property_value_error.
        _service.disable_retries()
        self.test_delete_tekton_pipeline_trigger_property_value_error()

# endregion
##############################################################################
# End of Service: TriggerProperties
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Definition():
    """
    Test Class for Definition
    """

    def test_definition_serialization(self):
        """
        Test serialization/deserialization for Definition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_source_properties_tool_model = {} # DefinitionSourcePropertiesTool
        definition_source_properties_tool_model['id'] = 'testString'

        definition_source_properties_model = {} # DefinitionSourceProperties
        definition_source_properties_model['url'] = 'testString'
        definition_source_properties_model['branch'] = 'testString'
        definition_source_properties_model['tag'] = 'testString'
        definition_source_properties_model['path'] = 'testString'
        definition_source_properties_model['tool'] = definition_source_properties_tool_model

        definition_source_model = {} # DefinitionSource
        definition_source_model['type'] = 'testString'
        definition_source_model['properties'] = definition_source_properties_model

        # Construct a json representation of a Definition model
        definition_model_json = {}
        definition_model_json['source'] = definition_source_model
        definition_model_json['id'] = 'testString'

        # Construct a model instance of Definition by calling from_dict on the json representation
        definition_model = Definition.from_dict(definition_model_json)
        assert definition_model != False

        # Construct a model instance of Definition by calling from_dict on the json representation
        definition_model_dict = Definition.from_dict(definition_model_json).__dict__
        definition_model2 = Definition(**definition_model_dict)

        # Verify the model instances are equivalent
        assert definition_model == definition_model2

        # Convert model instance back to dict and verify no loss of data
        definition_model_json2 = definition_model.to_dict()
        assert definition_model_json2 == definition_model_json

class TestModel_DefinitionSource():
    """
    Test Class for DefinitionSource
    """

    def test_definition_source_serialization(self):
        """
        Test serialization/deserialization for DefinitionSource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_source_properties_tool_model = {} # DefinitionSourcePropertiesTool
        definition_source_properties_tool_model['id'] = 'testString'

        definition_source_properties_model = {} # DefinitionSourceProperties
        definition_source_properties_model['url'] = 'testString'
        definition_source_properties_model['branch'] = 'testString'
        definition_source_properties_model['tag'] = 'testString'
        definition_source_properties_model['path'] = 'testString'
        definition_source_properties_model['tool'] = definition_source_properties_tool_model

        # Construct a json representation of a DefinitionSource model
        definition_source_model_json = {}
        definition_source_model_json['type'] = 'testString'
        definition_source_model_json['properties'] = definition_source_properties_model

        # Construct a model instance of DefinitionSource by calling from_dict on the json representation
        definition_source_model = DefinitionSource.from_dict(definition_source_model_json)
        assert definition_source_model != False

        # Construct a model instance of DefinitionSource by calling from_dict on the json representation
        definition_source_model_dict = DefinitionSource.from_dict(definition_source_model_json).__dict__
        definition_source_model2 = DefinitionSource(**definition_source_model_dict)

        # Verify the model instances are equivalent
        assert definition_source_model == definition_source_model2

        # Convert model instance back to dict and verify no loss of data
        definition_source_model_json2 = definition_source_model.to_dict()
        assert definition_source_model_json2 == definition_source_model_json

class TestModel_DefinitionSourceProperties():
    """
    Test Class for DefinitionSourceProperties
    """

    def test_definition_source_properties_serialization(self):
        """
        Test serialization/deserialization for DefinitionSourceProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_source_properties_tool_model = {} # DefinitionSourcePropertiesTool
        definition_source_properties_tool_model['id'] = 'testString'

        # Construct a json representation of a DefinitionSourceProperties model
        definition_source_properties_model_json = {}
        definition_source_properties_model_json['url'] = 'testString'
        definition_source_properties_model_json['branch'] = 'testString'
        definition_source_properties_model_json['tag'] = 'testString'
        definition_source_properties_model_json['path'] = 'testString'
        definition_source_properties_model_json['tool'] = definition_source_properties_tool_model

        # Construct a model instance of DefinitionSourceProperties by calling from_dict on the json representation
        definition_source_properties_model = DefinitionSourceProperties.from_dict(definition_source_properties_model_json)
        assert definition_source_properties_model != False

        # Construct a model instance of DefinitionSourceProperties by calling from_dict on the json representation
        definition_source_properties_model_dict = DefinitionSourceProperties.from_dict(definition_source_properties_model_json).__dict__
        definition_source_properties_model2 = DefinitionSourceProperties(**definition_source_properties_model_dict)

        # Verify the model instances are equivalent
        assert definition_source_properties_model == definition_source_properties_model2

        # Convert model instance back to dict and verify no loss of data
        definition_source_properties_model_json2 = definition_source_properties_model.to_dict()
        assert definition_source_properties_model_json2 == definition_source_properties_model_json

class TestModel_DefinitionSourcePropertiesTool():
    """
    Test Class for DefinitionSourcePropertiesTool
    """

    def test_definition_source_properties_tool_serialization(self):
        """
        Test serialization/deserialization for DefinitionSourcePropertiesTool
        """

        # Construct a json representation of a DefinitionSourcePropertiesTool model
        definition_source_properties_tool_model_json = {}
        definition_source_properties_tool_model_json['id'] = 'testString'

        # Construct a model instance of DefinitionSourcePropertiesTool by calling from_dict on the json representation
        definition_source_properties_tool_model = DefinitionSourcePropertiesTool.from_dict(definition_source_properties_tool_model_json)
        assert definition_source_properties_tool_model != False

        # Construct a model instance of DefinitionSourcePropertiesTool by calling from_dict on the json representation
        definition_source_properties_tool_model_dict = DefinitionSourcePropertiesTool.from_dict(definition_source_properties_tool_model_json).__dict__
        definition_source_properties_tool_model2 = DefinitionSourcePropertiesTool(**definition_source_properties_tool_model_dict)

        # Verify the model instances are equivalent
        assert definition_source_properties_tool_model == definition_source_properties_tool_model2

        # Convert model instance back to dict and verify no loss of data
        definition_source_properties_tool_model_json2 = definition_source_properties_tool_model.to_dict()
        assert definition_source_properties_tool_model_json2 == definition_source_properties_tool_model_json

class TestModel_DefinitionsCollection():
    """
    Test Class for DefinitionsCollection
    """

    def test_definitions_collection_serialization(self):
        """
        Test serialization/deserialization for DefinitionsCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_source_properties_tool_model = {} # DefinitionSourcePropertiesTool
        definition_source_properties_tool_model['id'] = 'testString'

        definition_source_properties_model = {} # DefinitionSourceProperties
        definition_source_properties_model['url'] = 'testString'
        definition_source_properties_model['branch'] = 'testString'
        definition_source_properties_model['tag'] = 'testString'
        definition_source_properties_model['path'] = 'testString'
        definition_source_properties_model['tool'] = definition_source_properties_tool_model

        definition_source_model = {} # DefinitionSource
        definition_source_model['type'] = 'testString'
        definition_source_model['properties'] = definition_source_properties_model

        definitions_collection_definitions_item_model = {} # DefinitionsCollectionDefinitionsItem
        definitions_collection_definitions_item_model['source'] = definition_source_model
        definitions_collection_definitions_item_model['id'] = 'testString'
        definitions_collection_definitions_item_model['href'] = 'testString'

        # Construct a json representation of a DefinitionsCollection model
        definitions_collection_model_json = {}
        definitions_collection_model_json['definitions'] = [definitions_collection_definitions_item_model]

        # Construct a model instance of DefinitionsCollection by calling from_dict on the json representation
        definitions_collection_model = DefinitionsCollection.from_dict(definitions_collection_model_json)
        assert definitions_collection_model != False

        # Construct a model instance of DefinitionsCollection by calling from_dict on the json representation
        definitions_collection_model_dict = DefinitionsCollection.from_dict(definitions_collection_model_json).__dict__
        definitions_collection_model2 = DefinitionsCollection(**definitions_collection_model_dict)

        # Verify the model instances are equivalent
        assert definitions_collection_model == definitions_collection_model2

        # Convert model instance back to dict and verify no loss of data
        definitions_collection_model_json2 = definitions_collection_model.to_dict()
        assert definitions_collection_model_json2 == definitions_collection_model_json

class TestModel_DefinitionsCollectionDefinitionsItem():
    """
    Test Class for DefinitionsCollectionDefinitionsItem
    """

    def test_definitions_collection_definitions_item_serialization(self):
        """
        Test serialization/deserialization for DefinitionsCollectionDefinitionsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_source_properties_tool_model = {} # DefinitionSourcePropertiesTool
        definition_source_properties_tool_model['id'] = 'testString'

        definition_source_properties_model = {} # DefinitionSourceProperties
        definition_source_properties_model['url'] = 'testString'
        definition_source_properties_model['branch'] = 'testString'
        definition_source_properties_model['tag'] = 'testString'
        definition_source_properties_model['path'] = 'testString'
        definition_source_properties_model['tool'] = definition_source_properties_tool_model

        definition_source_model = {} # DefinitionSource
        definition_source_model['type'] = 'testString'
        definition_source_model['properties'] = definition_source_properties_model

        # Construct a json representation of a DefinitionsCollectionDefinitionsItem model
        definitions_collection_definitions_item_model_json = {}
        definitions_collection_definitions_item_model_json['source'] = definition_source_model
        definitions_collection_definitions_item_model_json['id'] = 'testString'
        definitions_collection_definitions_item_model_json['href'] = 'testString'

        # Construct a model instance of DefinitionsCollectionDefinitionsItem by calling from_dict on the json representation
        definitions_collection_definitions_item_model = DefinitionsCollectionDefinitionsItem.from_dict(definitions_collection_definitions_item_model_json)
        assert definitions_collection_definitions_item_model != False

        # Construct a model instance of DefinitionsCollectionDefinitionsItem by calling from_dict on the json representation
        definitions_collection_definitions_item_model_dict = DefinitionsCollectionDefinitionsItem.from_dict(definitions_collection_definitions_item_model_json).__dict__
        definitions_collection_definitions_item_model2 = DefinitionsCollectionDefinitionsItem(**definitions_collection_definitions_item_model_dict)

        # Verify the model instances are equivalent
        assert definitions_collection_definitions_item_model == definitions_collection_definitions_item_model2

        # Convert model instance back to dict and verify no loss of data
        definitions_collection_definitions_item_model_json2 = definitions_collection_definitions_item_model.to_dict()
        assert definitions_collection_definitions_item_model_json2 == definitions_collection_definitions_item_model_json

class TestModel_GenericSecret():
    """
    Test Class for GenericSecret
    """

    def test_generic_secret_serialization(self):
        """
        Test serialization/deserialization for GenericSecret
        """

        # Construct a json representation of a GenericSecret model
        generic_secret_model_json = {}
        generic_secret_model_json['type'] = 'token_matches'
        generic_secret_model_json['value'] = 'testString'
        generic_secret_model_json['source'] = 'header'
        generic_secret_model_json['key_name'] = 'testString'
        generic_secret_model_json['algorithm'] = 'md4'

        # Construct a model instance of GenericSecret by calling from_dict on the json representation
        generic_secret_model = GenericSecret.from_dict(generic_secret_model_json)
        assert generic_secret_model != False

        # Construct a model instance of GenericSecret by calling from_dict on the json representation
        generic_secret_model_dict = GenericSecret.from_dict(generic_secret_model_json).__dict__
        generic_secret_model2 = GenericSecret(**generic_secret_model_dict)

        # Verify the model instances are equivalent
        assert generic_secret_model == generic_secret_model2

        # Convert model instance back to dict and verify no loss of data
        generic_secret_model_json2 = generic_secret_model.to_dict()
        assert generic_secret_model_json2 == generic_secret_model_json

class TestModel_Log():
    """
    Test Class for Log
    """

    def test_log_serialization(self):
        """
        Test serialization/deserialization for Log
        """

        # Construct a json representation of a Log model
        log_model_json = {}
        log_model_json['href'] = 'testString'
        log_model_json['id'] = 'testString'
        log_model_json['name'] = 'testString'

        # Construct a model instance of Log by calling from_dict on the json representation
        log_model = Log.from_dict(log_model_json)
        assert log_model != False

        # Construct a model instance of Log by calling from_dict on the json representation
        log_model_dict = Log.from_dict(log_model_json).__dict__
        log_model2 = Log(**log_model_dict)

        # Verify the model instances are equivalent
        assert log_model == log_model2

        # Convert model instance back to dict and verify no loss of data
        log_model_json2 = log_model.to_dict()
        assert log_model_json2 == log_model_json

class TestModel_LogsCollection():
    """
    Test Class for LogsCollection
    """

    def test_logs_collection_serialization(self):
        """
        Test serialization/deserialization for LogsCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_model = {} # Log
        log_model['href'] = 'testString'
        log_model['id'] = 'testString'
        log_model['name'] = 'testString'

        # Construct a json representation of a LogsCollection model
        logs_collection_model_json = {}
        logs_collection_model_json['logs'] = [log_model]

        # Construct a model instance of LogsCollection by calling from_dict on the json representation
        logs_collection_model = LogsCollection.from_dict(logs_collection_model_json)
        assert logs_collection_model != False

        # Construct a model instance of LogsCollection by calling from_dict on the json representation
        logs_collection_model_dict = LogsCollection.from_dict(logs_collection_model_json).__dict__
        logs_collection_model2 = LogsCollection(**logs_collection_model_dict)

        # Verify the model instances are equivalent
        assert logs_collection_model == logs_collection_model2

        # Convert model instance back to dict and verify no loss of data
        logs_collection_model_json2 = logs_collection_model.to_dict()
        assert logs_collection_model_json2 == logs_collection_model_json

class TestModel_PipelineRun():
    """
    Test Class for PipelineRun
    """

    def test_pipeline_run_serialization(self):
        """
        Test serialization/deserialization for PipelineRun
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_info_model = {} # UserInfo
        user_info_model['iam_id'] = 'testString'
        user_info_model['sub'] = 'testString'

        pipeline_run_worker_model = {} # PipelineRunWorker
        pipeline_run_worker_model['name'] = 'testString'
        pipeline_run_worker_model['agent_id'] = 'testString'
        pipeline_run_worker_model['service_id'] = 'testString'
        pipeline_run_worker_model['id'] = 'testString'

        trigger_manual_trigger_properties_item_model = {} # TriggerManualTriggerPropertiesItem
        trigger_manual_trigger_properties_item_model['name'] = 'testString'
        trigger_manual_trigger_properties_item_model['value'] = 'testString'
        trigger_manual_trigger_properties_item_model['enum'] = ['testString']
        trigger_manual_trigger_properties_item_model['type'] = 'secure'
        trigger_manual_trigger_properties_item_model['path'] = 'testString'
        trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        trigger_model = {} # TriggerManualTrigger
        trigger_model['type'] = 'testString'
        trigger_model['name'] = 'start-deploy'
        trigger_model['href'] = 'testString'
        trigger_model['event_listener'] = 'testString'
        trigger_model['id'] = 'testString'
        trigger_model['properties'] = [trigger_manual_trigger_properties_item_model]
        trigger_model['tags'] = ['testString']
        trigger_model['worker'] = worker_model
        trigger_model['max_concurrent_runs'] = 4
        trigger_model['enabled'] = True

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['type'] = 'secure'
        property_model['path'] = 'testString'

        # Construct a json representation of a PipelineRun model
        pipeline_run_model_json = {}
        pipeline_run_model_json['id'] = 'testString'
        pipeline_run_model_json['user_info'] = user_info_model
        pipeline_run_model_json['status'] = 'pending'
        pipeline_run_model_json['definition_id'] = 'testString'
        pipeline_run_model_json['worker'] = pipeline_run_worker_model
        pipeline_run_model_json['pipeline_id'] = 'testString'
        pipeline_run_model_json['listener_name'] = 'testString'
        pipeline_run_model_json['trigger'] = trigger_model
        pipeline_run_model_json['event_params_blob'] = 'testString'
        pipeline_run_model_json['trigger_headers'] = 'testString'
        pipeline_run_model_json['properties'] = [property_model]
        pipeline_run_model_json['created_at'] = '2019-01-01T12:00:00Z'
        pipeline_run_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        pipeline_run_model_json['run_url'] = 'testString'

        # Construct a model instance of PipelineRun by calling from_dict on the json representation
        pipeline_run_model = PipelineRun.from_dict(pipeline_run_model_json)
        assert pipeline_run_model != False

        # Construct a model instance of PipelineRun by calling from_dict on the json representation
        pipeline_run_model_dict = PipelineRun.from_dict(pipeline_run_model_json).__dict__
        pipeline_run_model2 = PipelineRun(**pipeline_run_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_run_model == pipeline_run_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_run_model_json2 = pipeline_run_model.to_dict()
        assert pipeline_run_model_json2 == pipeline_run_model_json

class TestModel_PipelineRunWorker():
    """
    Test Class for PipelineRunWorker
    """

    def test_pipeline_run_worker_serialization(self):
        """
        Test serialization/deserialization for PipelineRunWorker
        """

        # Construct a json representation of a PipelineRunWorker model
        pipeline_run_worker_model_json = {}
        pipeline_run_worker_model_json['name'] = 'testString'
        pipeline_run_worker_model_json['agent_id'] = 'testString'
        pipeline_run_worker_model_json['service_id'] = 'testString'
        pipeline_run_worker_model_json['id'] = 'testString'

        # Construct a model instance of PipelineRunWorker by calling from_dict on the json representation
        pipeline_run_worker_model = PipelineRunWorker.from_dict(pipeline_run_worker_model_json)
        assert pipeline_run_worker_model != False

        # Construct a model instance of PipelineRunWorker by calling from_dict on the json representation
        pipeline_run_worker_model_dict = PipelineRunWorker.from_dict(pipeline_run_worker_model_json).__dict__
        pipeline_run_worker_model2 = PipelineRunWorker(**pipeline_run_worker_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_run_worker_model == pipeline_run_worker_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_run_worker_model_json2 = pipeline_run_worker_model.to_dict()
        assert pipeline_run_worker_model_json2 == pipeline_run_worker_model_json

class TestModel_PipelineRunsCollection():
    """
    Test Class for PipelineRunsCollection
    """

    def test_pipeline_runs_collection_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_info_model = {} # UserInfo
        user_info_model['iam_id'] = 'testString'
        user_info_model['sub'] = 'testString'

        pipeline_run_worker_model = {} # PipelineRunWorker
        pipeline_run_worker_model['name'] = 'testString'
        pipeline_run_worker_model['agent_id'] = 'testString'
        pipeline_run_worker_model['service_id'] = 'testString'
        pipeline_run_worker_model['id'] = 'testString'

        trigger_manual_trigger_properties_item_model = {} # TriggerManualTriggerPropertiesItem
        trigger_manual_trigger_properties_item_model['name'] = 'testString'
        trigger_manual_trigger_properties_item_model['value'] = 'testString'
        trigger_manual_trigger_properties_item_model['enum'] = ['testString']
        trigger_manual_trigger_properties_item_model['type'] = 'secure'
        trigger_manual_trigger_properties_item_model['path'] = 'testString'
        trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        trigger_model = {} # TriggerManualTrigger
        trigger_model['type'] = 'testString'
        trigger_model['name'] = 'start-deploy'
        trigger_model['href'] = 'testString'
        trigger_model['event_listener'] = 'testString'
        trigger_model['id'] = 'testString'
        trigger_model['properties'] = [trigger_manual_trigger_properties_item_model]
        trigger_model['tags'] = ['testString']
        trigger_model['worker'] = worker_model
        trigger_model['max_concurrent_runs'] = 4
        trigger_model['enabled'] = True

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['type'] = 'secure'
        property_model['path'] = 'testString'

        pipeline_runs_collection_pipeline_runs_item_model = {} # PipelineRunsCollectionPipelineRunsItem
        pipeline_runs_collection_pipeline_runs_item_model['id'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model['user_info'] = user_info_model
        pipeline_runs_collection_pipeline_runs_item_model['status'] = 'pending'
        pipeline_runs_collection_pipeline_runs_item_model['definition_id'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model['worker'] = pipeline_run_worker_model
        pipeline_runs_collection_pipeline_runs_item_model['pipeline_id'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model['listener_name'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model['trigger'] = trigger_model
        pipeline_runs_collection_pipeline_runs_item_model['event_params_blob'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model['trigger_headers'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model['properties'] = [property_model]
        pipeline_runs_collection_pipeline_runs_item_model['created_at'] = '2019-01-01T12:00:00Z'
        pipeline_runs_collection_pipeline_runs_item_model['updated_at'] = '2019-01-01T12:00:00Z'
        pipeline_runs_collection_pipeline_runs_item_model['run_url'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model['href'] = 'testString'

        pipeline_runs_collection_first_model = {} # PipelineRunsCollectionFirst
        pipeline_runs_collection_first_model['href'] = 'testString'

        pipeline_runs_collection_next_model = {} # PipelineRunsCollectionNext
        pipeline_runs_collection_next_model['href'] = 'testString'

        pipeline_runs_collection_last_model = {} # PipelineRunsCollectionLast
        pipeline_runs_collection_last_model['href'] = 'testString'

        # Construct a json representation of a PipelineRunsCollection model
        pipeline_runs_collection_model_json = {}
        pipeline_runs_collection_model_json['pipeline_runs'] = [pipeline_runs_collection_pipeline_runs_item_model]
        pipeline_runs_collection_model_json['limit'] = 20
        pipeline_runs_collection_model_json['first'] = pipeline_runs_collection_first_model
        pipeline_runs_collection_model_json['next'] = pipeline_runs_collection_next_model
        pipeline_runs_collection_model_json['last'] = pipeline_runs_collection_last_model

        # Construct a model instance of PipelineRunsCollection by calling from_dict on the json representation
        pipeline_runs_collection_model = PipelineRunsCollection.from_dict(pipeline_runs_collection_model_json)
        assert pipeline_runs_collection_model != False

        # Construct a model instance of PipelineRunsCollection by calling from_dict on the json representation
        pipeline_runs_collection_model_dict = PipelineRunsCollection.from_dict(pipeline_runs_collection_model_json).__dict__
        pipeline_runs_collection_model2 = PipelineRunsCollection(**pipeline_runs_collection_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_collection_model == pipeline_runs_collection_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_collection_model_json2 = pipeline_runs_collection_model.to_dict()
        assert pipeline_runs_collection_model_json2 == pipeline_runs_collection_model_json

class TestModel_PipelineRunsCollectionFirst():
    """
    Test Class for PipelineRunsCollectionFirst
    """

    def test_pipeline_runs_collection_first_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsCollectionFirst
        """

        # Construct a json representation of a PipelineRunsCollectionFirst model
        pipeline_runs_collection_first_model_json = {}
        pipeline_runs_collection_first_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunsCollectionFirst by calling from_dict on the json representation
        pipeline_runs_collection_first_model = PipelineRunsCollectionFirst.from_dict(pipeline_runs_collection_first_model_json)
        assert pipeline_runs_collection_first_model != False

        # Construct a model instance of PipelineRunsCollectionFirst by calling from_dict on the json representation
        pipeline_runs_collection_first_model_dict = PipelineRunsCollectionFirst.from_dict(pipeline_runs_collection_first_model_json).__dict__
        pipeline_runs_collection_first_model2 = PipelineRunsCollectionFirst(**pipeline_runs_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_collection_first_model == pipeline_runs_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_collection_first_model_json2 = pipeline_runs_collection_first_model.to_dict()
        assert pipeline_runs_collection_first_model_json2 == pipeline_runs_collection_first_model_json

class TestModel_PipelineRunsCollectionLast():
    """
    Test Class for PipelineRunsCollectionLast
    """

    def test_pipeline_runs_collection_last_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsCollectionLast
        """

        # Construct a json representation of a PipelineRunsCollectionLast model
        pipeline_runs_collection_last_model_json = {}
        pipeline_runs_collection_last_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunsCollectionLast by calling from_dict on the json representation
        pipeline_runs_collection_last_model = PipelineRunsCollectionLast.from_dict(pipeline_runs_collection_last_model_json)
        assert pipeline_runs_collection_last_model != False

        # Construct a model instance of PipelineRunsCollectionLast by calling from_dict on the json representation
        pipeline_runs_collection_last_model_dict = PipelineRunsCollectionLast.from_dict(pipeline_runs_collection_last_model_json).__dict__
        pipeline_runs_collection_last_model2 = PipelineRunsCollectionLast(**pipeline_runs_collection_last_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_collection_last_model == pipeline_runs_collection_last_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_collection_last_model_json2 = pipeline_runs_collection_last_model.to_dict()
        assert pipeline_runs_collection_last_model_json2 == pipeline_runs_collection_last_model_json

class TestModel_PipelineRunsCollectionNext():
    """
    Test Class for PipelineRunsCollectionNext
    """

    def test_pipeline_runs_collection_next_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsCollectionNext
        """

        # Construct a json representation of a PipelineRunsCollectionNext model
        pipeline_runs_collection_next_model_json = {}
        pipeline_runs_collection_next_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunsCollectionNext by calling from_dict on the json representation
        pipeline_runs_collection_next_model = PipelineRunsCollectionNext.from_dict(pipeline_runs_collection_next_model_json)
        assert pipeline_runs_collection_next_model != False

        # Construct a model instance of PipelineRunsCollectionNext by calling from_dict on the json representation
        pipeline_runs_collection_next_model_dict = PipelineRunsCollectionNext.from_dict(pipeline_runs_collection_next_model_json).__dict__
        pipeline_runs_collection_next_model2 = PipelineRunsCollectionNext(**pipeline_runs_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_collection_next_model == pipeline_runs_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_collection_next_model_json2 = pipeline_runs_collection_next_model.to_dict()
        assert pipeline_runs_collection_next_model_json2 == pipeline_runs_collection_next_model_json

class TestModel_PipelineRunsCollectionPipelineRunsItem():
    """
    Test Class for PipelineRunsCollectionPipelineRunsItem
    """

    def test_pipeline_runs_collection_pipeline_runs_item_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsCollectionPipelineRunsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_info_model = {} # UserInfo
        user_info_model['iam_id'] = 'testString'
        user_info_model['sub'] = 'testString'

        pipeline_run_worker_model = {} # PipelineRunWorker
        pipeline_run_worker_model['name'] = 'testString'
        pipeline_run_worker_model['agent_id'] = 'testString'
        pipeline_run_worker_model['service_id'] = 'testString'
        pipeline_run_worker_model['id'] = 'testString'

        trigger_manual_trigger_properties_item_model = {} # TriggerManualTriggerPropertiesItem
        trigger_manual_trigger_properties_item_model['name'] = 'testString'
        trigger_manual_trigger_properties_item_model['value'] = 'testString'
        trigger_manual_trigger_properties_item_model['enum'] = ['testString']
        trigger_manual_trigger_properties_item_model['type'] = 'secure'
        trigger_manual_trigger_properties_item_model['path'] = 'testString'
        trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        trigger_model = {} # TriggerManualTrigger
        trigger_model['type'] = 'testString'
        trigger_model['name'] = 'start-deploy'
        trigger_model['href'] = 'testString'
        trigger_model['event_listener'] = 'testString'
        trigger_model['id'] = 'testString'
        trigger_model['properties'] = [trigger_manual_trigger_properties_item_model]
        trigger_model['tags'] = ['testString']
        trigger_model['worker'] = worker_model
        trigger_model['max_concurrent_runs'] = 4
        trigger_model['enabled'] = True

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['type'] = 'secure'
        property_model['path'] = 'testString'

        # Construct a json representation of a PipelineRunsCollectionPipelineRunsItem model
        pipeline_runs_collection_pipeline_runs_item_model_json = {}
        pipeline_runs_collection_pipeline_runs_item_model_json['id'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model_json['user_info'] = user_info_model
        pipeline_runs_collection_pipeline_runs_item_model_json['status'] = 'pending'
        pipeline_runs_collection_pipeline_runs_item_model_json['definition_id'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model_json['worker'] = pipeline_run_worker_model
        pipeline_runs_collection_pipeline_runs_item_model_json['pipeline_id'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model_json['listener_name'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model_json['trigger'] = trigger_model
        pipeline_runs_collection_pipeline_runs_item_model_json['event_params_blob'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model_json['trigger_headers'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model_json['properties'] = [property_model]
        pipeline_runs_collection_pipeline_runs_item_model_json['created_at'] = '2019-01-01T12:00:00Z'
        pipeline_runs_collection_pipeline_runs_item_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        pipeline_runs_collection_pipeline_runs_item_model_json['run_url'] = 'testString'
        pipeline_runs_collection_pipeline_runs_item_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunsCollectionPipelineRunsItem by calling from_dict on the json representation
        pipeline_runs_collection_pipeline_runs_item_model = PipelineRunsCollectionPipelineRunsItem.from_dict(pipeline_runs_collection_pipeline_runs_item_model_json)
        assert pipeline_runs_collection_pipeline_runs_item_model != False

        # Construct a model instance of PipelineRunsCollectionPipelineRunsItem by calling from_dict on the json representation
        pipeline_runs_collection_pipeline_runs_item_model_dict = PipelineRunsCollectionPipelineRunsItem.from_dict(pipeline_runs_collection_pipeline_runs_item_model_json).__dict__
        pipeline_runs_collection_pipeline_runs_item_model2 = PipelineRunsCollectionPipelineRunsItem(**pipeline_runs_collection_pipeline_runs_item_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_collection_pipeline_runs_item_model == pipeline_runs_collection_pipeline_runs_item_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_collection_pipeline_runs_item_model_json2 = pipeline_runs_collection_pipeline_runs_item_model.to_dict()
        assert pipeline_runs_collection_pipeline_runs_item_model_json2 == pipeline_runs_collection_pipeline_runs_item_model_json

class TestModel_PropertiesCollection():
    """
    Test Class for PropertiesCollection
    """

    def test_properties_collection_serialization(self):
        """
        Test serialization/deserialization for PropertiesCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['type'] = 'secure'
        property_model['path'] = 'testString'

        # Construct a json representation of a PropertiesCollection model
        properties_collection_model_json = {}
        properties_collection_model_json['properties'] = [property_model]

        # Construct a model instance of PropertiesCollection by calling from_dict on the json representation
        properties_collection_model = PropertiesCollection.from_dict(properties_collection_model_json)
        assert properties_collection_model != False

        # Construct a model instance of PropertiesCollection by calling from_dict on the json representation
        properties_collection_model_dict = PropertiesCollection.from_dict(properties_collection_model_json).__dict__
        properties_collection_model2 = PropertiesCollection(**properties_collection_model_dict)

        # Verify the model instances are equivalent
        assert properties_collection_model == properties_collection_model2

        # Convert model instance back to dict and verify no loss of data
        properties_collection_model_json2 = properties_collection_model.to_dict()
        assert properties_collection_model_json2 == properties_collection_model_json

class TestModel_Property():
    """
    Test Class for Property
    """

    def test_property_serialization(self):
        """
        Test serialization/deserialization for Property
        """

        # Construct a json representation of a Property model
        property_model_json = {}
        property_model_json['name'] = 'testString'
        property_model_json['value'] = 'testString'
        property_model_json['enum'] = ['testString']
        property_model_json['type'] = 'secure'
        property_model_json['path'] = 'testString'

        # Construct a model instance of Property by calling from_dict on the json representation
        property_model = Property.from_dict(property_model_json)
        assert property_model != False

        # Construct a model instance of Property by calling from_dict on the json representation
        property_model_dict = Property.from_dict(property_model_json).__dict__
        property_model2 = Property(**property_model_dict)

        # Verify the model instances are equivalent
        assert property_model == property_model2

        # Convert model instance back to dict and verify no loss of data
        property_model_json2 = property_model.to_dict()
        assert property_model_json2 == property_model_json

class TestModel_StepLog():
    """
    Test Class for StepLog
    """

    def test_step_log_serialization(self):
        """
        Test serialization/deserialization for StepLog
        """

        # Construct a json representation of a StepLog model
        step_log_model_json = {}
        step_log_model_json['data'] = 'testString'
        step_log_model_json['id'] = 'testString'

        # Construct a model instance of StepLog by calling from_dict on the json representation
        step_log_model = StepLog.from_dict(step_log_model_json)
        assert step_log_model != False

        # Construct a model instance of StepLog by calling from_dict on the json representation
        step_log_model_dict = StepLog.from_dict(step_log_model_json).__dict__
        step_log_model2 = StepLog(**step_log_model_dict)

        # Verify the model instances are equivalent
        assert step_log_model == step_log_model2

        # Convert model instance back to dict and verify no loss of data
        step_log_model_json2 = step_log_model.to_dict()
        assert step_log_model_json2 == step_log_model_json

class TestModel_TektonPipeline():
    """
    Test Class for TektonPipeline
    """

    def test_tekton_pipeline_serialization(self):
        """
        Test serialization/deserialization for TektonPipeline
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tekton_pipeline_resource_group_model = {} # TektonPipelineResourceGroup
        tekton_pipeline_resource_group_model['id'] = 'testString'

        toolchain_reference_model = {} # ToolchainReference
        toolchain_reference_model['id'] = 'testString'
        toolchain_reference_model['crn'] = 'crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::'

        definition_source_properties_tool_model = {} # DefinitionSourcePropertiesTool
        definition_source_properties_tool_model['id'] = 'testString'

        definition_source_properties_model = {} # DefinitionSourceProperties
        definition_source_properties_model['url'] = 'testString'
        definition_source_properties_model['branch'] = 'testString'
        definition_source_properties_model['tag'] = 'testString'
        definition_source_properties_model['path'] = 'testString'
        definition_source_properties_model['tool'] = definition_source_properties_tool_model

        definition_source_model = {} # DefinitionSource
        definition_source_model['type'] = 'testString'
        definition_source_model['properties'] = definition_source_properties_model

        definition_model = {} # Definition
        definition_model['source'] = definition_source_model
        definition_model['id'] = 'testString'

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['type'] = 'secure'
        property_model['path'] = 'testString'

        trigger_manual_trigger_properties_item_model = {} # TriggerManualTriggerPropertiesItem
        trigger_manual_trigger_properties_item_model['name'] = 'testString'
        trigger_manual_trigger_properties_item_model['value'] = 'testString'
        trigger_manual_trigger_properties_item_model['enum'] = ['testString']
        trigger_manual_trigger_properties_item_model['type'] = 'secure'
        trigger_manual_trigger_properties_item_model['path'] = 'testString'
        trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        trigger_model = {} # TriggerManualTrigger
        trigger_model['type'] = 'testString'
        trigger_model['name'] = 'start-deploy'
        trigger_model['href'] = 'testString'
        trigger_model['event_listener'] = 'testString'
        trigger_model['id'] = 'testString'
        trigger_model['properties'] = [trigger_manual_trigger_properties_item_model]
        trigger_model['tags'] = ['testString']
        trigger_model['worker'] = worker_model
        trigger_model['max_concurrent_runs'] = 4
        trigger_model['enabled'] = True

        # Construct a json representation of a TektonPipeline model
        tekton_pipeline_model_json = {}
        tekton_pipeline_model_json['name'] = 'testString'
        tekton_pipeline_model_json['status'] = 'configured'
        tekton_pipeline_model_json['resource_group'] = tekton_pipeline_resource_group_model
        tekton_pipeline_model_json['toolchain'] = toolchain_reference_model
        tekton_pipeline_model_json['id'] = 'testString'
        tekton_pipeline_model_json['definitions'] = [definition_model]
        tekton_pipeline_model_json['properties'] = [property_model]
        tekton_pipeline_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        tekton_pipeline_model_json['created_at'] = '2019-01-01T12:00:00Z'
        tekton_pipeline_model_json['triggers'] = [trigger_model]
        tekton_pipeline_model_json['worker'] = worker_model
        tekton_pipeline_model_json['runs_url'] = 'testString'
        tekton_pipeline_model_json['build_number'] = 1
        tekton_pipeline_model_json['enable_notifications'] = True
        tekton_pipeline_model_json['enable_partial_cloning'] = True
        tekton_pipeline_model_json['enabled'] = True

        # Construct a model instance of TektonPipeline by calling from_dict on the json representation
        tekton_pipeline_model = TektonPipeline.from_dict(tekton_pipeline_model_json)
        assert tekton_pipeline_model != False

        # Construct a model instance of TektonPipeline by calling from_dict on the json representation
        tekton_pipeline_model_dict = TektonPipeline.from_dict(tekton_pipeline_model_json).__dict__
        tekton_pipeline_model2 = TektonPipeline(**tekton_pipeline_model_dict)

        # Verify the model instances are equivalent
        assert tekton_pipeline_model == tekton_pipeline_model2

        # Convert model instance back to dict and verify no loss of data
        tekton_pipeline_model_json2 = tekton_pipeline_model.to_dict()
        assert tekton_pipeline_model_json2 == tekton_pipeline_model_json

class TestModel_TektonPipelinePatch():
    """
    Test Class for TektonPipelinePatch
    """

    def test_tekton_pipeline_patch_serialization(self):
        """
        Test serialization/deserialization for TektonPipelinePatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        worker_identity_model = {} # WorkerIdentity
        worker_identity_model['id'] = 'testString'

        # Construct a json representation of a TektonPipelinePatch model
        tekton_pipeline_patch_model_json = {}
        tekton_pipeline_patch_model_json['enable_notifications'] = True
        tekton_pipeline_patch_model_json['enable_partial_cloning'] = True
        tekton_pipeline_patch_model_json['worker'] = worker_identity_model

        # Construct a model instance of TektonPipelinePatch by calling from_dict on the json representation
        tekton_pipeline_patch_model = TektonPipelinePatch.from_dict(tekton_pipeline_patch_model_json)
        assert tekton_pipeline_patch_model != False

        # Construct a model instance of TektonPipelinePatch by calling from_dict on the json representation
        tekton_pipeline_patch_model_dict = TektonPipelinePatch.from_dict(tekton_pipeline_patch_model_json).__dict__
        tekton_pipeline_patch_model2 = TektonPipelinePatch(**tekton_pipeline_patch_model_dict)

        # Verify the model instances are equivalent
        assert tekton_pipeline_patch_model == tekton_pipeline_patch_model2

        # Convert model instance back to dict and verify no loss of data
        tekton_pipeline_patch_model_json2 = tekton_pipeline_patch_model.to_dict()
        assert tekton_pipeline_patch_model_json2 == tekton_pipeline_patch_model_json

class TestModel_TektonPipelineResourceGroup():
    """
    Test Class for TektonPipelineResourceGroup
    """

    def test_tekton_pipeline_resource_group_serialization(self):
        """
        Test serialization/deserialization for TektonPipelineResourceGroup
        """

        # Construct a json representation of a TektonPipelineResourceGroup model
        tekton_pipeline_resource_group_model_json = {}
        tekton_pipeline_resource_group_model_json['id'] = 'testString'

        # Construct a model instance of TektonPipelineResourceGroup by calling from_dict on the json representation
        tekton_pipeline_resource_group_model = TektonPipelineResourceGroup.from_dict(tekton_pipeline_resource_group_model_json)
        assert tekton_pipeline_resource_group_model != False

        # Construct a model instance of TektonPipelineResourceGroup by calling from_dict on the json representation
        tekton_pipeline_resource_group_model_dict = TektonPipelineResourceGroup.from_dict(tekton_pipeline_resource_group_model_json).__dict__
        tekton_pipeline_resource_group_model2 = TektonPipelineResourceGroup(**tekton_pipeline_resource_group_model_dict)

        # Verify the model instances are equivalent
        assert tekton_pipeline_resource_group_model == tekton_pipeline_resource_group_model2

        # Convert model instance back to dict and verify no loss of data
        tekton_pipeline_resource_group_model_json2 = tekton_pipeline_resource_group_model.to_dict()
        assert tekton_pipeline_resource_group_model_json2 == tekton_pipeline_resource_group_model_json

class TestModel_ToolchainReference():
    """
    Test Class for ToolchainReference
    """

    def test_toolchain_reference_serialization(self):
        """
        Test serialization/deserialization for ToolchainReference
        """

        # Construct a json representation of a ToolchainReference model
        toolchain_reference_model_json = {}
        toolchain_reference_model_json['id'] = 'testString'
        toolchain_reference_model_json['crn'] = 'crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::'

        # Construct a model instance of ToolchainReference by calling from_dict on the json representation
        toolchain_reference_model = ToolchainReference.from_dict(toolchain_reference_model_json)
        assert toolchain_reference_model != False

        # Construct a model instance of ToolchainReference by calling from_dict on the json representation
        toolchain_reference_model_dict = ToolchainReference.from_dict(toolchain_reference_model_json).__dict__
        toolchain_reference_model2 = ToolchainReference(**toolchain_reference_model_dict)

        # Verify the model instances are equivalent
        assert toolchain_reference_model == toolchain_reference_model2

        # Convert model instance back to dict and verify no loss of data
        toolchain_reference_model_json2 = toolchain_reference_model.to_dict()
        assert toolchain_reference_model_json2 == toolchain_reference_model_json

class TestModel_TriggerGenericTriggerPropertiesItem():
    """
    Test Class for TriggerGenericTriggerPropertiesItem
    """

    def test_trigger_generic_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggerGenericTriggerPropertiesItem
        """

        # Construct a json representation of a TriggerGenericTriggerPropertiesItem model
        trigger_generic_trigger_properties_item_model_json = {}
        trigger_generic_trigger_properties_item_model_json['name'] = 'testString'
        trigger_generic_trigger_properties_item_model_json['value'] = 'testString'
        trigger_generic_trigger_properties_item_model_json['enum'] = ['testString']
        trigger_generic_trigger_properties_item_model_json['type'] = 'secure'
        trigger_generic_trigger_properties_item_model_json['path'] = 'testString'
        trigger_generic_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggerGenericTriggerPropertiesItem by calling from_dict on the json representation
        trigger_generic_trigger_properties_item_model = TriggerGenericTriggerPropertiesItem.from_dict(trigger_generic_trigger_properties_item_model_json)
        assert trigger_generic_trigger_properties_item_model != False

        # Construct a model instance of TriggerGenericTriggerPropertiesItem by calling from_dict on the json representation
        trigger_generic_trigger_properties_item_model_dict = TriggerGenericTriggerPropertiesItem.from_dict(trigger_generic_trigger_properties_item_model_json).__dict__
        trigger_generic_trigger_properties_item_model2 = TriggerGenericTriggerPropertiesItem(**trigger_generic_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert trigger_generic_trigger_properties_item_model == trigger_generic_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_generic_trigger_properties_item_model_json2 = trigger_generic_trigger_properties_item_model.to_dict()
        assert trigger_generic_trigger_properties_item_model_json2 == trigger_generic_trigger_properties_item_model_json

class TestModel_TriggerManualTriggerPropertiesItem():
    """
    Test Class for TriggerManualTriggerPropertiesItem
    """

    def test_trigger_manual_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggerManualTriggerPropertiesItem
        """

        # Construct a json representation of a TriggerManualTriggerPropertiesItem model
        trigger_manual_trigger_properties_item_model_json = {}
        trigger_manual_trigger_properties_item_model_json['name'] = 'testString'
        trigger_manual_trigger_properties_item_model_json['value'] = 'testString'
        trigger_manual_trigger_properties_item_model_json['enum'] = ['testString']
        trigger_manual_trigger_properties_item_model_json['type'] = 'secure'
        trigger_manual_trigger_properties_item_model_json['path'] = 'testString'
        trigger_manual_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggerManualTriggerPropertiesItem by calling from_dict on the json representation
        trigger_manual_trigger_properties_item_model = TriggerManualTriggerPropertiesItem.from_dict(trigger_manual_trigger_properties_item_model_json)
        assert trigger_manual_trigger_properties_item_model != False

        # Construct a model instance of TriggerManualTriggerPropertiesItem by calling from_dict on the json representation
        trigger_manual_trigger_properties_item_model_dict = TriggerManualTriggerPropertiesItem.from_dict(trigger_manual_trigger_properties_item_model_json).__dict__
        trigger_manual_trigger_properties_item_model2 = TriggerManualTriggerPropertiesItem(**trigger_manual_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert trigger_manual_trigger_properties_item_model == trigger_manual_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_manual_trigger_properties_item_model_json2 = trigger_manual_trigger_properties_item_model.to_dict()
        assert trigger_manual_trigger_properties_item_model_json2 == trigger_manual_trigger_properties_item_model_json

class TestModel_TriggerPatch():
    """
    Test Class for TriggerPatch
    """

    def test_trigger_patch_serialization(self):
        """
        Test serialization/deserialization for TriggerPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        generic_secret_model = {} # GenericSecret
        generic_secret_model['type'] = 'token_matches'
        generic_secret_model['value'] = 'testString'
        generic_secret_model['source'] = 'header'
        generic_secret_model['key_name'] = 'testString'
        generic_secret_model['algorithm'] = 'md4'

        trigger_source_properties_tool_model = {} # TriggerSourcePropertiesTool
        trigger_source_properties_tool_model['id'] = 'testString'

        trigger_source_properties_model = {} # TriggerSourceProperties
        trigger_source_properties_model['url'] = 'testString'
        trigger_source_properties_model['branch'] = 'testString'
        trigger_source_properties_model['pattern'] = 'testString'
        trigger_source_properties_model['blind_connection'] = True
        trigger_source_properties_model['hook_id'] = 'testString'
        trigger_source_properties_model['tool'] = trigger_source_properties_tool_model

        trigger_source_model = {} # TriggerSource
        trigger_source_model['type'] = 'testString'
        trigger_source_model['properties'] = trigger_source_properties_model

        # Construct a json representation of a TriggerPatch model
        trigger_patch_model_json = {}
        trigger_patch_model_json['type'] = 'manual'
        trigger_patch_model_json['name'] = 'start-deploy'
        trigger_patch_model_json['event_listener'] = 'testString'
        trigger_patch_model_json['tags'] = ['testString']
        trigger_patch_model_json['worker'] = worker_model
        trigger_patch_model_json['max_concurrent_runs'] = 4
        trigger_patch_model_json['enabled'] = True
        trigger_patch_model_json['secret'] = generic_secret_model
        trigger_patch_model_json['cron'] = 'testString'
        trigger_patch_model_json['timezone'] = 'America/Los_Angeles, CET, Europe/London, GMT, US/Eastern, or UTC'
        trigger_patch_model_json['source'] = trigger_source_model
        trigger_patch_model_json['events'] = ['push', 'pull_request']

        # Construct a model instance of TriggerPatch by calling from_dict on the json representation
        trigger_patch_model = TriggerPatch.from_dict(trigger_patch_model_json)
        assert trigger_patch_model != False

        # Construct a model instance of TriggerPatch by calling from_dict on the json representation
        trigger_patch_model_dict = TriggerPatch.from_dict(trigger_patch_model_json).__dict__
        trigger_patch_model2 = TriggerPatch(**trigger_patch_model_dict)

        # Verify the model instances are equivalent
        assert trigger_patch_model == trigger_patch_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_patch_model_json2 = trigger_patch_model.to_dict()
        assert trigger_patch_model_json2 == trigger_patch_model_json

class TestModel_TriggerPropertiesCollection():
    """
    Test Class for TriggerPropertiesCollection
    """

    def test_trigger_properties_collection_serialization(self):
        """
        Test serialization/deserialization for TriggerPropertiesCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_properties_collection_properties_item_model = {} # TriggerPropertiesCollectionPropertiesItem
        trigger_properties_collection_properties_item_model['name'] = 'testString'
        trigger_properties_collection_properties_item_model['value'] = 'testString'
        trigger_properties_collection_properties_item_model['enum'] = ['testString']
        trigger_properties_collection_properties_item_model['type'] = 'secure'
        trigger_properties_collection_properties_item_model['path'] = 'testString'
        trigger_properties_collection_properties_item_model['href'] = 'testString'

        # Construct a json representation of a TriggerPropertiesCollection model
        trigger_properties_collection_model_json = {}
        trigger_properties_collection_model_json['properties'] = [trigger_properties_collection_properties_item_model]

        # Construct a model instance of TriggerPropertiesCollection by calling from_dict on the json representation
        trigger_properties_collection_model = TriggerPropertiesCollection.from_dict(trigger_properties_collection_model_json)
        assert trigger_properties_collection_model != False

        # Construct a model instance of TriggerPropertiesCollection by calling from_dict on the json representation
        trigger_properties_collection_model_dict = TriggerPropertiesCollection.from_dict(trigger_properties_collection_model_json).__dict__
        trigger_properties_collection_model2 = TriggerPropertiesCollection(**trigger_properties_collection_model_dict)

        # Verify the model instances are equivalent
        assert trigger_properties_collection_model == trigger_properties_collection_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_properties_collection_model_json2 = trigger_properties_collection_model.to_dict()
        assert trigger_properties_collection_model_json2 == trigger_properties_collection_model_json

class TestModel_TriggerPropertiesCollectionPropertiesItem():
    """
    Test Class for TriggerPropertiesCollectionPropertiesItem
    """

    def test_trigger_properties_collection_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggerPropertiesCollectionPropertiesItem
        """

        # Construct a json representation of a TriggerPropertiesCollectionPropertiesItem model
        trigger_properties_collection_properties_item_model_json = {}
        trigger_properties_collection_properties_item_model_json['name'] = 'testString'
        trigger_properties_collection_properties_item_model_json['value'] = 'testString'
        trigger_properties_collection_properties_item_model_json['enum'] = ['testString']
        trigger_properties_collection_properties_item_model_json['type'] = 'secure'
        trigger_properties_collection_properties_item_model_json['path'] = 'testString'
        trigger_properties_collection_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggerPropertiesCollectionPropertiesItem by calling from_dict on the json representation
        trigger_properties_collection_properties_item_model = TriggerPropertiesCollectionPropertiesItem.from_dict(trigger_properties_collection_properties_item_model_json)
        assert trigger_properties_collection_properties_item_model != False

        # Construct a model instance of TriggerPropertiesCollectionPropertiesItem by calling from_dict on the json representation
        trigger_properties_collection_properties_item_model_dict = TriggerPropertiesCollectionPropertiesItem.from_dict(trigger_properties_collection_properties_item_model_json).__dict__
        trigger_properties_collection_properties_item_model2 = TriggerPropertiesCollectionPropertiesItem(**trigger_properties_collection_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert trigger_properties_collection_properties_item_model == trigger_properties_collection_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_properties_collection_properties_item_model_json2 = trigger_properties_collection_properties_item_model.to_dict()
        assert trigger_properties_collection_properties_item_model_json2 == trigger_properties_collection_properties_item_model_json

class TestModel_TriggerProperty():
    """
    Test Class for TriggerProperty
    """

    def test_trigger_property_serialization(self):
        """
        Test serialization/deserialization for TriggerProperty
        """

        # Construct a json representation of a TriggerProperty model
        trigger_property_model_json = {}
        trigger_property_model_json['name'] = 'testString'
        trigger_property_model_json['value'] = 'testString'
        trigger_property_model_json['enum'] = ['testString']
        trigger_property_model_json['type'] = 'secure'
        trigger_property_model_json['path'] = 'testString'

        # Construct a model instance of TriggerProperty by calling from_dict on the json representation
        trigger_property_model = TriggerProperty.from_dict(trigger_property_model_json)
        assert trigger_property_model != False

        # Construct a model instance of TriggerProperty by calling from_dict on the json representation
        trigger_property_model_dict = TriggerProperty.from_dict(trigger_property_model_json).__dict__
        trigger_property_model2 = TriggerProperty(**trigger_property_model_dict)

        # Verify the model instances are equivalent
        assert trigger_property_model == trigger_property_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_property_model_json2 = trigger_property_model.to_dict()
        assert trigger_property_model_json2 == trigger_property_model_json

class TestModel_TriggerScmTriggerPropertiesItem():
    """
    Test Class for TriggerScmTriggerPropertiesItem
    """

    def test_trigger_scm_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggerScmTriggerPropertiesItem
        """

        # Construct a json representation of a TriggerScmTriggerPropertiesItem model
        trigger_scm_trigger_properties_item_model_json = {}
        trigger_scm_trigger_properties_item_model_json['name'] = 'testString'
        trigger_scm_trigger_properties_item_model_json['value'] = 'testString'
        trigger_scm_trigger_properties_item_model_json['enum'] = ['testString']
        trigger_scm_trigger_properties_item_model_json['type'] = 'secure'
        trigger_scm_trigger_properties_item_model_json['path'] = 'testString'
        trigger_scm_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggerScmTriggerPropertiesItem by calling from_dict on the json representation
        trigger_scm_trigger_properties_item_model = TriggerScmTriggerPropertiesItem.from_dict(trigger_scm_trigger_properties_item_model_json)
        assert trigger_scm_trigger_properties_item_model != False

        # Construct a model instance of TriggerScmTriggerPropertiesItem by calling from_dict on the json representation
        trigger_scm_trigger_properties_item_model_dict = TriggerScmTriggerPropertiesItem.from_dict(trigger_scm_trigger_properties_item_model_json).__dict__
        trigger_scm_trigger_properties_item_model2 = TriggerScmTriggerPropertiesItem(**trigger_scm_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert trigger_scm_trigger_properties_item_model == trigger_scm_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_scm_trigger_properties_item_model_json2 = trigger_scm_trigger_properties_item_model.to_dict()
        assert trigger_scm_trigger_properties_item_model_json2 == trigger_scm_trigger_properties_item_model_json

class TestModel_TriggerSource():
    """
    Test Class for TriggerSource
    """

    def test_trigger_source_serialization(self):
        """
        Test serialization/deserialization for TriggerSource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_source_properties_tool_model = {} # TriggerSourcePropertiesTool
        trigger_source_properties_tool_model['id'] = 'testString'

        trigger_source_properties_model = {} # TriggerSourceProperties
        trigger_source_properties_model['url'] = 'testString'
        trigger_source_properties_model['branch'] = 'testString'
        trigger_source_properties_model['pattern'] = 'testString'
        trigger_source_properties_model['blind_connection'] = True
        trigger_source_properties_model['hook_id'] = 'testString'
        trigger_source_properties_model['tool'] = trigger_source_properties_tool_model

        # Construct a json representation of a TriggerSource model
        trigger_source_model_json = {}
        trigger_source_model_json['type'] = 'testString'
        trigger_source_model_json['properties'] = trigger_source_properties_model

        # Construct a model instance of TriggerSource by calling from_dict on the json representation
        trigger_source_model = TriggerSource.from_dict(trigger_source_model_json)
        assert trigger_source_model != False

        # Construct a model instance of TriggerSource by calling from_dict on the json representation
        trigger_source_model_dict = TriggerSource.from_dict(trigger_source_model_json).__dict__
        trigger_source_model2 = TriggerSource(**trigger_source_model_dict)

        # Verify the model instances are equivalent
        assert trigger_source_model == trigger_source_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_source_model_json2 = trigger_source_model.to_dict()
        assert trigger_source_model_json2 == trigger_source_model_json

class TestModel_TriggerSourceProperties():
    """
    Test Class for TriggerSourceProperties
    """

    def test_trigger_source_properties_serialization(self):
        """
        Test serialization/deserialization for TriggerSourceProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_source_properties_tool_model = {} # TriggerSourcePropertiesTool
        trigger_source_properties_tool_model['id'] = 'testString'

        # Construct a json representation of a TriggerSourceProperties model
        trigger_source_properties_model_json = {}
        trigger_source_properties_model_json['url'] = 'testString'
        trigger_source_properties_model_json['branch'] = 'testString'
        trigger_source_properties_model_json['pattern'] = 'testString'
        trigger_source_properties_model_json['blind_connection'] = True
        trigger_source_properties_model_json['hook_id'] = 'testString'
        trigger_source_properties_model_json['tool'] = trigger_source_properties_tool_model

        # Construct a model instance of TriggerSourceProperties by calling from_dict on the json representation
        trigger_source_properties_model = TriggerSourceProperties.from_dict(trigger_source_properties_model_json)
        assert trigger_source_properties_model != False

        # Construct a model instance of TriggerSourceProperties by calling from_dict on the json representation
        trigger_source_properties_model_dict = TriggerSourceProperties.from_dict(trigger_source_properties_model_json).__dict__
        trigger_source_properties_model2 = TriggerSourceProperties(**trigger_source_properties_model_dict)

        # Verify the model instances are equivalent
        assert trigger_source_properties_model == trigger_source_properties_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_source_properties_model_json2 = trigger_source_properties_model.to_dict()
        assert trigger_source_properties_model_json2 == trigger_source_properties_model_json

class TestModel_TriggerSourcePropertiesTool():
    """
    Test Class for TriggerSourcePropertiesTool
    """

    def test_trigger_source_properties_tool_serialization(self):
        """
        Test serialization/deserialization for TriggerSourcePropertiesTool
        """

        # Construct a json representation of a TriggerSourcePropertiesTool model
        trigger_source_properties_tool_model_json = {}
        trigger_source_properties_tool_model_json['id'] = 'testString'

        # Construct a model instance of TriggerSourcePropertiesTool by calling from_dict on the json representation
        trigger_source_properties_tool_model = TriggerSourcePropertiesTool.from_dict(trigger_source_properties_tool_model_json)
        assert trigger_source_properties_tool_model != False

        # Construct a model instance of TriggerSourcePropertiesTool by calling from_dict on the json representation
        trigger_source_properties_tool_model_dict = TriggerSourcePropertiesTool.from_dict(trigger_source_properties_tool_model_json).__dict__
        trigger_source_properties_tool_model2 = TriggerSourcePropertiesTool(**trigger_source_properties_tool_model_dict)

        # Verify the model instances are equivalent
        assert trigger_source_properties_tool_model == trigger_source_properties_tool_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_source_properties_tool_model_json2 = trigger_source_properties_tool_model.to_dict()
        assert trigger_source_properties_tool_model_json2 == trigger_source_properties_tool_model_json

class TestModel_TriggerTimerTriggerPropertiesItem():
    """
    Test Class for TriggerTimerTriggerPropertiesItem
    """

    def test_trigger_timer_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggerTimerTriggerPropertiesItem
        """

        # Construct a json representation of a TriggerTimerTriggerPropertiesItem model
        trigger_timer_trigger_properties_item_model_json = {}
        trigger_timer_trigger_properties_item_model_json['name'] = 'testString'
        trigger_timer_trigger_properties_item_model_json['value'] = 'testString'
        trigger_timer_trigger_properties_item_model_json['enum'] = ['testString']
        trigger_timer_trigger_properties_item_model_json['type'] = 'secure'
        trigger_timer_trigger_properties_item_model_json['path'] = 'testString'
        trigger_timer_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggerTimerTriggerPropertiesItem by calling from_dict on the json representation
        trigger_timer_trigger_properties_item_model = TriggerTimerTriggerPropertiesItem.from_dict(trigger_timer_trigger_properties_item_model_json)
        assert trigger_timer_trigger_properties_item_model != False

        # Construct a model instance of TriggerTimerTriggerPropertiesItem by calling from_dict on the json representation
        trigger_timer_trigger_properties_item_model_dict = TriggerTimerTriggerPropertiesItem.from_dict(trigger_timer_trigger_properties_item_model_json).__dict__
        trigger_timer_trigger_properties_item_model2 = TriggerTimerTriggerPropertiesItem(**trigger_timer_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert trigger_timer_trigger_properties_item_model == trigger_timer_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_timer_trigger_properties_item_model_json2 = trigger_timer_trigger_properties_item_model.to_dict()
        assert trigger_timer_trigger_properties_item_model_json2 == trigger_timer_trigger_properties_item_model_json

class TestModel_TriggersCollection():
    """
    Test Class for TriggersCollection
    """

    def test_triggers_collection_serialization(self):
        """
        Test serialization/deserialization for TriggersCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_manual_trigger_properties_item_model = {} # TriggerManualTriggerPropertiesItem
        trigger_manual_trigger_properties_item_model['name'] = 'testString'
        trigger_manual_trigger_properties_item_model['value'] = 'testString'
        trigger_manual_trigger_properties_item_model['enum'] = ['testString']
        trigger_manual_trigger_properties_item_model['type'] = 'secure'
        trigger_manual_trigger_properties_item_model['path'] = 'testString'
        trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        trigger_model = {} # TriggerManualTrigger
        trigger_model['type'] = 'testString'
        trigger_model['name'] = 'start-deploy'
        trigger_model['href'] = 'testString'
        trigger_model['event_listener'] = 'testString'
        trigger_model['id'] = 'testString'
        trigger_model['properties'] = [trigger_manual_trigger_properties_item_model]
        trigger_model['tags'] = ['testString']
        trigger_model['worker'] = worker_model
        trigger_model['max_concurrent_runs'] = 4
        trigger_model['enabled'] = True

        # Construct a json representation of a TriggersCollection model
        triggers_collection_model_json = {}
        triggers_collection_model_json['triggers'] = [trigger_model]

        # Construct a model instance of TriggersCollection by calling from_dict on the json representation
        triggers_collection_model = TriggersCollection.from_dict(triggers_collection_model_json)
        assert triggers_collection_model != False

        # Construct a model instance of TriggersCollection by calling from_dict on the json representation
        triggers_collection_model_dict = TriggersCollection.from_dict(triggers_collection_model_json).__dict__
        triggers_collection_model2 = TriggersCollection(**triggers_collection_model_dict)

        # Verify the model instances are equivalent
        assert triggers_collection_model == triggers_collection_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_collection_model_json2 = triggers_collection_model.to_dict()
        assert triggers_collection_model_json2 == triggers_collection_model_json

class TestModel_UserInfo():
    """
    Test Class for UserInfo
    """

    def test_user_info_serialization(self):
        """
        Test serialization/deserialization for UserInfo
        """

        # Construct a json representation of a UserInfo model
        user_info_model_json = {}
        user_info_model_json['iam_id'] = 'testString'
        user_info_model_json['sub'] = 'testString'

        # Construct a model instance of UserInfo by calling from_dict on the json representation
        user_info_model = UserInfo.from_dict(user_info_model_json)
        assert user_info_model != False

        # Construct a model instance of UserInfo by calling from_dict on the json representation
        user_info_model_dict = UserInfo.from_dict(user_info_model_json).__dict__
        user_info_model2 = UserInfo(**user_info_model_dict)

        # Verify the model instances are equivalent
        assert user_info_model == user_info_model2

        # Convert model instance back to dict and verify no loss of data
        user_info_model_json2 = user_info_model.to_dict()
        assert user_info_model_json2 == user_info_model_json

class TestModel_Worker():
    """
    Test Class for Worker
    """

    def test_worker_serialization(self):
        """
        Test serialization/deserialization for Worker
        """

        # Construct a json representation of a Worker model
        worker_model_json = {}
        worker_model_json['name'] = 'testString'
        worker_model_json['type'] = 'testString'
        worker_model_json['id'] = 'testString'

        # Construct a model instance of Worker by calling from_dict on the json representation
        worker_model = Worker.from_dict(worker_model_json)
        assert worker_model != False

        # Construct a model instance of Worker by calling from_dict on the json representation
        worker_model_dict = Worker.from_dict(worker_model_json).__dict__
        worker_model2 = Worker(**worker_model_dict)

        # Verify the model instances are equivalent
        assert worker_model == worker_model2

        # Convert model instance back to dict and verify no loss of data
        worker_model_json2 = worker_model.to_dict()
        assert worker_model_json2 == worker_model_json

class TestModel_WorkerIdentity():
    """
    Test Class for WorkerIdentity
    """

    def test_worker_identity_serialization(self):
        """
        Test serialization/deserialization for WorkerIdentity
        """

        # Construct a json representation of a WorkerIdentity model
        worker_identity_model_json = {}
        worker_identity_model_json['id'] = 'testString'

        # Construct a model instance of WorkerIdentity by calling from_dict on the json representation
        worker_identity_model = WorkerIdentity.from_dict(worker_identity_model_json)
        assert worker_identity_model != False

        # Construct a model instance of WorkerIdentity by calling from_dict on the json representation
        worker_identity_model_dict = WorkerIdentity.from_dict(worker_identity_model_json).__dict__
        worker_identity_model2 = WorkerIdentity(**worker_identity_model_dict)

        # Verify the model instances are equivalent
        assert worker_identity_model == worker_identity_model2

        # Convert model instance back to dict and verify no loss of data
        worker_identity_model_json2 = worker_identity_model.to_dict()
        assert worker_identity_model_json2 == worker_identity_model_json

class TestModel_TriggerGenericTrigger():
    """
    Test Class for TriggerGenericTrigger
    """

    def test_trigger_generic_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggerGenericTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_generic_trigger_properties_item_model = {} # TriggerGenericTriggerPropertiesItem
        trigger_generic_trigger_properties_item_model['name'] = 'testString'
        trigger_generic_trigger_properties_item_model['value'] = 'testString'
        trigger_generic_trigger_properties_item_model['enum'] = ['testString']
        trigger_generic_trigger_properties_item_model['type'] = 'secure'
        trigger_generic_trigger_properties_item_model['path'] = 'testString'
        trigger_generic_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        generic_secret_model = {} # GenericSecret
        generic_secret_model['type'] = 'token_matches'
        generic_secret_model['value'] = 'testString'
        generic_secret_model['source'] = 'header'
        generic_secret_model['key_name'] = 'testString'
        generic_secret_model['algorithm'] = 'md4'

        # Construct a json representation of a TriggerGenericTrigger model
        trigger_generic_trigger_model_json = {}
        trigger_generic_trigger_model_json['type'] = 'testString'
        trigger_generic_trigger_model_json['name'] = 'start-deploy'
        trigger_generic_trigger_model_json['href'] = 'testString'
        trigger_generic_trigger_model_json['event_listener'] = 'testString'
        trigger_generic_trigger_model_json['id'] = 'testString'
        trigger_generic_trigger_model_json['properties'] = [trigger_generic_trigger_properties_item_model]
        trigger_generic_trigger_model_json['tags'] = ['testString']
        trigger_generic_trigger_model_json['worker'] = worker_model
        trigger_generic_trigger_model_json['max_concurrent_runs'] = 4
        trigger_generic_trigger_model_json['enabled'] = True
        trigger_generic_trigger_model_json['secret'] = generic_secret_model
        trigger_generic_trigger_model_json['webhook_url'] = 'testString'

        # Construct a model instance of TriggerGenericTrigger by calling from_dict on the json representation
        trigger_generic_trigger_model = TriggerGenericTrigger.from_dict(trigger_generic_trigger_model_json)
        assert trigger_generic_trigger_model != False

        # Construct a model instance of TriggerGenericTrigger by calling from_dict on the json representation
        trigger_generic_trigger_model_dict = TriggerGenericTrigger.from_dict(trigger_generic_trigger_model_json).__dict__
        trigger_generic_trigger_model2 = TriggerGenericTrigger(**trigger_generic_trigger_model_dict)

        # Verify the model instances are equivalent
        assert trigger_generic_trigger_model == trigger_generic_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_generic_trigger_model_json2 = trigger_generic_trigger_model.to_dict()
        assert trigger_generic_trigger_model_json2 == trigger_generic_trigger_model_json

class TestModel_TriggerManualTrigger():
    """
    Test Class for TriggerManualTrigger
    """

    def test_trigger_manual_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggerManualTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_manual_trigger_properties_item_model = {} # TriggerManualTriggerPropertiesItem
        trigger_manual_trigger_properties_item_model['name'] = 'testString'
        trigger_manual_trigger_properties_item_model['value'] = 'testString'
        trigger_manual_trigger_properties_item_model['enum'] = ['testString']
        trigger_manual_trigger_properties_item_model['type'] = 'secure'
        trigger_manual_trigger_properties_item_model['path'] = 'testString'
        trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        # Construct a json representation of a TriggerManualTrigger model
        trigger_manual_trigger_model_json = {}
        trigger_manual_trigger_model_json['type'] = 'testString'
        trigger_manual_trigger_model_json['name'] = 'start-deploy'
        trigger_manual_trigger_model_json['href'] = 'testString'
        trigger_manual_trigger_model_json['event_listener'] = 'testString'
        trigger_manual_trigger_model_json['id'] = 'testString'
        trigger_manual_trigger_model_json['properties'] = [trigger_manual_trigger_properties_item_model]
        trigger_manual_trigger_model_json['tags'] = ['testString']
        trigger_manual_trigger_model_json['worker'] = worker_model
        trigger_manual_trigger_model_json['max_concurrent_runs'] = 4
        trigger_manual_trigger_model_json['enabled'] = True

        # Construct a model instance of TriggerManualTrigger by calling from_dict on the json representation
        trigger_manual_trigger_model = TriggerManualTrigger.from_dict(trigger_manual_trigger_model_json)
        assert trigger_manual_trigger_model != False

        # Construct a model instance of TriggerManualTrigger by calling from_dict on the json representation
        trigger_manual_trigger_model_dict = TriggerManualTrigger.from_dict(trigger_manual_trigger_model_json).__dict__
        trigger_manual_trigger_model2 = TriggerManualTrigger(**trigger_manual_trigger_model_dict)

        # Verify the model instances are equivalent
        assert trigger_manual_trigger_model == trigger_manual_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_manual_trigger_model_json2 = trigger_manual_trigger_model.to_dict()
        assert trigger_manual_trigger_model_json2 == trigger_manual_trigger_model_json

class TestModel_TriggerScmTrigger():
    """
    Test Class for TriggerScmTrigger
    """

    def test_trigger_scm_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggerScmTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_scm_trigger_properties_item_model = {} # TriggerScmTriggerPropertiesItem
        trigger_scm_trigger_properties_item_model['name'] = 'testString'
        trigger_scm_trigger_properties_item_model['value'] = 'testString'
        trigger_scm_trigger_properties_item_model['enum'] = ['testString']
        trigger_scm_trigger_properties_item_model['type'] = 'secure'
        trigger_scm_trigger_properties_item_model['path'] = 'testString'
        trigger_scm_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        trigger_source_properties_tool_model = {} # TriggerSourcePropertiesTool
        trigger_source_properties_tool_model['id'] = 'testString'

        trigger_source_properties_model = {} # TriggerSourceProperties
        trigger_source_properties_model['url'] = 'testString'
        trigger_source_properties_model['branch'] = 'testString'
        trigger_source_properties_model['pattern'] = 'testString'
        trigger_source_properties_model['blind_connection'] = True
        trigger_source_properties_model['hook_id'] = 'testString'
        trigger_source_properties_model['tool'] = trigger_source_properties_tool_model

        trigger_source_model = {} # TriggerSource
        trigger_source_model['type'] = 'testString'
        trigger_source_model['properties'] = trigger_source_properties_model

        # Construct a json representation of a TriggerScmTrigger model
        trigger_scm_trigger_model_json = {}
        trigger_scm_trigger_model_json['type'] = 'testString'
        trigger_scm_trigger_model_json['name'] = 'start-deploy'
        trigger_scm_trigger_model_json['href'] = 'testString'
        trigger_scm_trigger_model_json['event_listener'] = 'testString'
        trigger_scm_trigger_model_json['id'] = 'testString'
        trigger_scm_trigger_model_json['properties'] = [trigger_scm_trigger_properties_item_model]
        trigger_scm_trigger_model_json['tags'] = ['testString']
        trigger_scm_trigger_model_json['worker'] = worker_model
        trigger_scm_trigger_model_json['max_concurrent_runs'] = 4
        trigger_scm_trigger_model_json['enabled'] = True
        trigger_scm_trigger_model_json['source'] = trigger_source_model
        trigger_scm_trigger_model_json['events'] = ['push', 'pull_request']

        # Construct a model instance of TriggerScmTrigger by calling from_dict on the json representation
        trigger_scm_trigger_model = TriggerScmTrigger.from_dict(trigger_scm_trigger_model_json)
        assert trigger_scm_trigger_model != False

        # Construct a model instance of TriggerScmTrigger by calling from_dict on the json representation
        trigger_scm_trigger_model_dict = TriggerScmTrigger.from_dict(trigger_scm_trigger_model_json).__dict__
        trigger_scm_trigger_model2 = TriggerScmTrigger(**trigger_scm_trigger_model_dict)

        # Verify the model instances are equivalent
        assert trigger_scm_trigger_model == trigger_scm_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_scm_trigger_model_json2 = trigger_scm_trigger_model.to_dict()
        assert trigger_scm_trigger_model_json2 == trigger_scm_trigger_model_json

class TestModel_TriggerTimerTrigger():
    """
    Test Class for TriggerTimerTrigger
    """

    def test_trigger_timer_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggerTimerTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_timer_trigger_properties_item_model = {} # TriggerTimerTriggerPropertiesItem
        trigger_timer_trigger_properties_item_model['name'] = 'testString'
        trigger_timer_trigger_properties_item_model['value'] = 'testString'
        trigger_timer_trigger_properties_item_model['enum'] = ['testString']
        trigger_timer_trigger_properties_item_model['type'] = 'secure'
        trigger_timer_trigger_properties_item_model['path'] = 'testString'
        trigger_timer_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'testString'
        worker_model['id'] = 'testString'

        # Construct a json representation of a TriggerTimerTrigger model
        trigger_timer_trigger_model_json = {}
        trigger_timer_trigger_model_json['type'] = 'testString'
        trigger_timer_trigger_model_json['name'] = 'start-deploy'
        trigger_timer_trigger_model_json['href'] = 'testString'
        trigger_timer_trigger_model_json['event_listener'] = 'testString'
        trigger_timer_trigger_model_json['id'] = 'testString'
        trigger_timer_trigger_model_json['properties'] = [trigger_timer_trigger_properties_item_model]
        trigger_timer_trigger_model_json['tags'] = ['testString']
        trigger_timer_trigger_model_json['worker'] = worker_model
        trigger_timer_trigger_model_json['max_concurrent_runs'] = 4
        trigger_timer_trigger_model_json['enabled'] = True
        trigger_timer_trigger_model_json['cron'] = 'testString'
        trigger_timer_trigger_model_json['timezone'] = 'America/Los_Angeles, CET, Europe/London, GMT, US/Eastern, or UTC'

        # Construct a model instance of TriggerTimerTrigger by calling from_dict on the json representation
        trigger_timer_trigger_model = TriggerTimerTrigger.from_dict(trigger_timer_trigger_model_json)
        assert trigger_timer_trigger_model != False

        # Construct a model instance of TriggerTimerTrigger by calling from_dict on the json representation
        trigger_timer_trigger_model_dict = TriggerTimerTrigger.from_dict(trigger_timer_trigger_model_json).__dict__
        trigger_timer_trigger_model2 = TriggerTimerTrigger(**trigger_timer_trigger_model_dict)

        # Verify the model instances are equivalent
        assert trigger_timer_trigger_model == trigger_timer_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_timer_trigger_model_json2 = trigger_timer_trigger_model.to_dict()
        assert trigger_timer_trigger_model_json2 == trigger_timer_trigger_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
