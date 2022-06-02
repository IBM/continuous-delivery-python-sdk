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
from github.com/IBM/continuous-delivery-pipeline-python-sdk.cd_tekton_pipeline_v2 import *


_service = CdTektonPipelineV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://devops-api.us-south.devops.cloud.ibm.com/v2'
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
    assert CdTektonPipelineV2.get_service_url_for_region('us-south') == 'https://devops-api.us-south.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('us-east') == 'https://devops-api.us-east.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('eu-de') == 'https://devops-api.eu-de.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('eu-gb') == 'https://devops-api.eu-gb.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('jp-osa') == 'https://devops-api.jp-osa.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('jp-tok') == 'https://devops-api.jp-tok.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('au-syd') == 'https://devops-api.au-syd.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('ca-tor') == 'https://devops-api.ca-tor.devops.cloud.ibm.com/v2'
    assert CdTektonPipelineV2.get_service_url_for_region('br-sao') == 'https://devops-api.br-sao.devops.cloud.ibm.com/v2'


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
        mock_response = '{"name": "name", "status": "configured", "resource_group_id": "resource_group_id", "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "pipeline_definition": {"status": "updated", "id": "id"}, "triggers": [{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}], "worker": {"name": "name", "type": "private", "id": "id"}, "html_url": "html_url", "build_number": 1, "enabled": false}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a WorkerWithId model
        worker_with_id_model = {}
        worker_with_id_model['id'] = 'public'

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'
        worker = worker_with_id_model

        # Invoke method
        response = _service.create_tekton_pipeline(
            id=id,
            worker=worker,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['id'] == '94619026-912b-4d92-8f51-6c74f0692d90'
        assert req_body['worker'] == worker_with_id_model

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
        mock_response = '{"name": "name", "status": "configured", "resource_group_id": "resource_group_id", "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "pipeline_definition": {"status": "updated", "id": "id"}, "triggers": [{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}], "worker": {"name": "name", "type": "private", "id": "id"}, "html_url": "html_url", "build_number": 1, "enabled": false}'
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
        mock_response = '{"name": "name", "status": "configured", "resource_group_id": "resource_group_id", "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "pipeline_definition": {"status": "updated", "id": "id"}, "triggers": [{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}], "worker": {"name": "name", "type": "private", "id": "id"}, "html_url": "html_url", "build_number": 1, "enabled": false}'
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
        mock_response = '{"name": "name", "status": "configured", "resource_group_id": "resource_group_id", "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "pipeline_definition": {"status": "updated", "id": "id"}, "triggers": [{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}], "worker": {"name": "name", "type": "private", "id": "id"}, "html_url": "html_url", "build_number": 1, "enabled": false}'
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
        mock_response = '{"name": "name", "status": "configured", "resource_group_id": "resource_group_id", "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "pipeline_definition": {"status": "updated", "id": "id"}, "triggers": [{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}], "worker": {"name": "name", "type": "private", "id": "id"}, "html_url": "html_url", "build_number": 1, "enabled": false}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a WorkerWithId model
        worker_with_id_model = {}
        worker_with_id_model['id'] = 'public'

        # Set up parameter values
        id = '94619026-912b-4d92-8f51-6c74f0692d90'
        worker = worker_with_id_model

        # Invoke method
        response = _service.update_tekton_pipeline(
            id,
            worker=worker,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['worker'] == worker_with_id_model

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
        mock_response = '{"name": "name", "status": "configured", "resource_group_id": "resource_group_id", "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "pipeline_definition": {"status": "updated", "id": "id"}, "triggers": [{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}], "worker": {"name": "name", "type": "private", "id": "id"}, "html_url": "html_url", "build_number": 1, "enabled": false}'
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
        mock_response = '{"name": "name", "status": "configured", "resource_group_id": "resource_group_id", "toolchain": {"id": "id", "crn": "crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::"}, "id": "id", "definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}], "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "updated_at": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "pipeline_definition": {"status": "updated", "id": "id"}, "triggers": [{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}], "worker": {"name": "name", "type": "private", "id": "id"}, "html_url": "html_url", "build_number": 1, "enabled": false}'
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
        mock_response = '{"pipeline_runs": [{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url", "href": "href"}], "offset": 20, "limit": 20, "first": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        limit = 1
        offset = 38
        status = 'succeeded'
        trigger_name = 'manual-trigger'

        # Invoke method
        response = _service.list_tekton_pipeline_runs(
            pipeline_id,
            limit=limit,
            offset=offset,
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
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
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
        mock_response = '{"pipeline_runs": [{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url", "href": "href"}], "offset": 20, "limit": 20, "first": {"href": "href"}, "next": {"href": "href"}}'
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
        mock_response = '{"pipeline_runs": [{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url", "href": "href"}], "offset": 20, "limit": 20, "first": {"href": "href"}, "next": {"href": "href"}}'
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_name = 'Generic Webhook Trigger - 0'
        trigger_properties = {'key1': 'testString'}
        secure_trigger_properties = {'key1': 'testString'}
        trigger_header = {'key1': 'testString'}
        trigger_body = {'key1': 'testString'}

        # Invoke method
        response = _service.create_tekton_pipeline_run(
            pipeline_id,
            trigger_name=trigger_name,
            trigger_properties=trigger_properties,
            secure_trigger_properties=secure_trigger_properties,
            trigger_header=trigger_header,
            trigger_body=trigger_body,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['trigger_name'] == 'Generic Webhook Trigger - 0'
        assert req_body['trigger_properties'] == {'key1': 'testString'}
        assert req_body['secure_trigger_properties'] == {'key1': 'testString'}
        assert req_body['trigger_header'] == {'key1': 'testString'}
        assert req_body['trigger_body'] == {'key1': 'testString'}

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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
        assert response.status_code == 200
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

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
        assert response.status_code == 200

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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
        responses.add(responses.POST,
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
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
        mock_response = '{"id": "id", "user_info": {"iam_id": "iam_id", "sub": "sub"}, "status": "pending", "definition_id": "definition_id", "worker": {"name": "name", "agent": "agent", "service_id": "service_id", "id": "id"}, "pipeline_id": "pipeline_id", "listener_name": "listener_name", "trigger": {"source_trigger_id": "source_trigger_id", "name": "start-deploy"}, "event_params_blob": "event_params_blob", "event_header_params_blob": "event_header_params_blob", "properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "html_url": "html_url"}'
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
        mock_response = '{"logs": [{"name": "name", "id": "id", "href": "href"}]}'
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
        mock_response = '{"logs": [{"name": "name", "id": "id", "href": "href"}]}'
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
        mock_response = '{"id": "id", "data": "data"}'
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
        mock_response = '{"id": "id", "data": "data"}'
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
        mock_response = '{"definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id", "href": "href"}]}'
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
        mock_response = '{"definitions": [{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id", "href": "href"}]}'
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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DefinitionScmSource model
        definition_scm_source_model = {}
        definition_scm_source_model['url'] = 'https://github.com/IBM/tekton-tutorial.git'
        definition_scm_source_model['branch'] = 'master'
        definition_scm_source_model['tag'] = 'testString'
        definition_scm_source_model['path'] = '.tekton'

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        scm_source = definition_scm_source_model

        # Invoke method
        response = _service.create_tekton_pipeline_definition(
            pipeline_id,
            scm_source=scm_source,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['scm_source'] == definition_scm_source_model

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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a DefinitionScmSource model
        definition_scm_source_model = {}
        definition_scm_source_model['url'] = 'https://github.com/IBM/tekton-tutorial.git'
        definition_scm_source_model['branch'] = 'master'
        definition_scm_source_model['tag'] = 'testString'
        definition_scm_source_model['path'] = '.tekton'

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        definition_id = '94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
        scm_source = definition_scm_source_model
        service_instance_id = '071d8049-d984-4feb-a2ed-2a1e938918ba'
        id = '22f92ab1-e0ac-4c65-84e7-8a4cb32dba0f'

        # Invoke method
        response = _service.replace_tekton_pipeline_definition(
            pipeline_id,
            definition_id,
            scm_source=scm_source,
            service_instance_id=service_instance_id,
            id=id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['scm_source'] == definition_scm_source_model
        assert req_body['service_instance_id'] == '071d8049-d984-4feb-a2ed-2a1e938918ba'
        assert req_body['id'] == '22f92ab1-e0ac-4c65-84e7-8a4cb32dba0f'

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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
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
        mock_response = '{"scm_source": {"url": "url", "branch": "branch", "tag": "tag", "path": "path"}, "service_instance_id": "service_instance_id", "id": "id"}'
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
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        name = 'prod'
        type = ['SECURE', 'TEXT']
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
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}]}'
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
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}]}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        name = 'key1'
        type = 'TEXT'
        value = 'https://github.com/IBM/tekton-tutorial.git'
        enum = ['testString']
        default = 'testString'
        path = 'testString'

        # Invoke method
        response = _service.create_tekton_pipeline_properties(
            pipeline_id,
            name=name,
            type=type,
            value=value,
            enum=enum,
            default=default,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'key1'
        assert req_body['type'] == 'TEXT'
        assert req_body['value'] == 'https://github.com/IBM/tekton-tutorial.git'
        assert req_body['enum'] == ['testString']
        assert req_body['default'] == 'testString'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        property_name = 'debug-pipeline'
        name = 'key1'
        type = 'TEXT'
        value = 'https://github.com/IBM/tekton-tutorial.git'
        enum = ['testString']
        default = 'testString'
        path = 'testString'

        # Invoke method
        response = _service.replace_tekton_pipeline_property(
            pipeline_id,
            property_name,
            name=name,
            type=type,
            value=value,
            enum=enum,
            default=default,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'key1'
        assert req_body['type'] == 'TEXT'
        assert req_body['value'] == 'https://github.com/IBM/tekton-tutorial.git'
        assert req_body['enum'] == ['testString']
        assert req_body['default'] == 'testString'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"triggers": [{"href": "href", "source_trigger_id": "source_trigger_id", "name": "start-deploy"}]}'
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
        mock_response = '{"triggers": [{"href": "href", "source_trigger_id": "source_trigger_id", "name": "start-deploy"}]}'
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
        mock_response = '{"triggers": [{"href": "href", "source_trigger_id": "source_trigger_id", "name": "start-deploy"}]}'
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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a TriggerDuplicateTrigger model
        trigger_model = {}
        trigger_model['source_trigger_id'] = 'b3a8228f-1c82-409b-b249-7639166a0300'
        trigger_model['name'] = 'Generic Trigger- duplicated'

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger = trigger_model

        # Invoke method
        response = _service.create_tekton_pipeline_trigger(
            pipeline_id,
            trigger=trigger,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == trigger

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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Worker model
        worker_model = {}
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        # Construct a dict representation of a Concurrency model
        concurrency_model = {}
        concurrency_model['max_concurrent_runs'] = 20

        # Construct a dict representation of a GenericSecret model
        generic_secret_model = {}
        generic_secret_model['type'] = 'tokenMatches'
        generic_secret_model['value'] = 'testString'
        generic_secret_model['source'] = 'header'
        generic_secret_model['key_name'] = 'testString'
        generic_secret_model['algorithm'] = 'md4'

        # Construct a dict representation of a TriggerScmSource model
        trigger_scm_source_model = {}
        trigger_scm_source_model['url'] = 'testString'
        trigger_scm_source_model['branch'] = 'testString'
        trigger_scm_source_model['pattern'] = 'testString'
        trigger_scm_source_model['blind_connection'] = True
        trigger_scm_source_model['hook_id'] = 'testString'

        # Construct a dict representation of a Events model
        events_model = {}
        events_model['push'] = True
        events_model['pull_request_closed'] = True
        events_model['pull_request'] = True

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        type = 'manual'
        name = 'start-deploy'
        event_listener = 'testString'
        tags = ['testString']
        worker = worker_model
        concurrency = concurrency_model
        disabled = True
        secret = generic_secret_model
        cron = 'testString'
        timezone = 'Africa/Abidjan'
        scm_source = trigger_scm_source_model
        events = events_model

        # Invoke method
        response = _service.update_tekton_pipeline_trigger(
            pipeline_id,
            trigger_id,
            type=type,
            name=name,
            event_listener=event_listener,
            tags=tags,
            worker=worker,
            concurrency=concurrency,
            disabled=disabled,
            secret=secret,
            cron=cron,
            timezone=timezone,
            scm_source=scm_source,
            events=events,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'manual'
        assert req_body['name'] == 'start-deploy'
        assert req_body['event_listener'] == 'testString'
        assert req_body['tags'] == ['testString']
        assert req_body['worker'] == worker_model
        assert req_body['concurrency'] == concurrency_model
        assert req_body['disabled'] == True
        assert req_body['secret'] == generic_secret_model
        assert req_body['cron'] == 'testString'
        assert req_body['timezone'] == 'Africa/Abidjan'
        assert req_body['scm_source'] == trigger_scm_source_model
        assert req_body['events'] == events_model

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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
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
        mock_response = '{"source_trigger_id": "source_trigger_id", "name": "start-deploy"}'
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
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        name = 'prod'
        type = 'SECURE,TEXT'
        sort = 'name'

        # Invoke method
        response = _service.list_tekton_pipeline_trigger_properties(
            pipeline_id,
            trigger_id,
            name,
            type,
            sort,
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
    def test_list_tekton_pipeline_trigger_properties_value_error(self):
        """
        test_list_tekton_pipeline_trigger_properties_value_error()
        """
        # Set up mock
        url = preprocess_url('/tekton_pipelines/94619026-912b-4d92-8f51-6c74f0692d90/triggers/1bb892a1-2e04-4768-a369-b1159eace147/properties')
        mock_response = '{"properties": [{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path", "href": "href"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        name = 'prod'
        type = 'SECURE,TEXT'
        sort = 'name'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pipeline_id": pipeline_id,
            "trigger_id": trigger_id,
            "name": name,
            "type": type,
            "sort": sort,
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        name = 'key1'
        type = 'TEXT'
        value = 'https://github.com/IBM/tekton-tutorial.git'
        enum = ['testString']
        default = 'testString'
        path = 'testString'

        # Invoke method
        response = _service.create_tekton_pipeline_trigger_properties(
            pipeline_id,
            trigger_id,
            name=name,
            type=type,
            value=value,
            enum=enum,
            default=default,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'key1'
        assert req_body['type'] == 'TEXT'
        assert req_body['value'] == 'https://github.com/IBM/tekton-tutorial.git'
        assert req_body['enum'] == ['testString']
        assert req_body['default'] == 'testString'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pipeline_id = '94619026-912b-4d92-8f51-6c74f0692d90'
        trigger_id = '1bb892a1-2e04-4768-a369-b1159eace147'
        property_name = 'debug-pipeline'
        name = 'key1'
        type = 'TEXT'
        value = 'https://github.com/IBM/tekton-tutorial.git'
        enum = ['testString']
        default = 'testString'
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
            default=default,
            path=path,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'key1'
        assert req_body['type'] == 'TEXT'
        assert req_body['value'] == 'https://github.com/IBM/tekton-tutorial.git'
        assert req_body['enum'] == ['testString']
        assert req_body['default'] == 'testString'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
        mock_response = '{"name": "name", "value": "value", "enum": ["enum"], "default": "default", "type": "SECURE", "path": "path"}'
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
class TestModel_Concurrency():
    """
    Test Class for Concurrency
    """

    def test_concurrency_serialization(self):
        """
        Test serialization/deserialization for Concurrency
        """

        # Construct a json representation of a Concurrency model
        concurrency_model_json = {}
        concurrency_model_json['max_concurrent_runs'] = 20

        # Construct a model instance of Concurrency by calling from_dict on the json representation
        concurrency_model = Concurrency.from_dict(concurrency_model_json)
        assert concurrency_model != False

        # Construct a model instance of Concurrency by calling from_dict on the json representation
        concurrency_model_dict = Concurrency.from_dict(concurrency_model_json).__dict__
        concurrency_model2 = Concurrency(**concurrency_model_dict)

        # Verify the model instances are equivalent
        assert concurrency_model == concurrency_model2

        # Convert model instance back to dict and verify no loss of data
        concurrency_model_json2 = concurrency_model.to_dict()
        assert concurrency_model_json2 == concurrency_model_json

class TestModel_Definition():
    """
    Test Class for Definition
    """

    def test_definition_serialization(self):
        """
        Test serialization/deserialization for Definition
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_scm_source_model = {} # DefinitionScmSource
        definition_scm_source_model['url'] = 'testString'
        definition_scm_source_model['branch'] = 'testString'
        definition_scm_source_model['tag'] = 'testString'
        definition_scm_source_model['path'] = 'testString'

        # Construct a json representation of a Definition model
        definition_model_json = {}
        definition_model_json['scm_source'] = definition_scm_source_model
        definition_model_json['service_instance_id'] = 'testString'
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

class TestModel_DefinitionScmSource():
    """
    Test Class for DefinitionScmSource
    """

    def test_definition_scm_source_serialization(self):
        """
        Test serialization/deserialization for DefinitionScmSource
        """

        # Construct a json representation of a DefinitionScmSource model
        definition_scm_source_model_json = {}
        definition_scm_source_model_json['url'] = 'testString'
        definition_scm_source_model_json['branch'] = 'testString'
        definition_scm_source_model_json['tag'] = 'testString'
        definition_scm_source_model_json['path'] = 'testString'

        # Construct a model instance of DefinitionScmSource by calling from_dict on the json representation
        definition_scm_source_model = DefinitionScmSource.from_dict(definition_scm_source_model_json)
        assert definition_scm_source_model != False

        # Construct a model instance of DefinitionScmSource by calling from_dict on the json representation
        definition_scm_source_model_dict = DefinitionScmSource.from_dict(definition_scm_source_model_json).__dict__
        definition_scm_source_model2 = DefinitionScmSource(**definition_scm_source_model_dict)

        # Verify the model instances are equivalent
        assert definition_scm_source_model == definition_scm_source_model2

        # Convert model instance back to dict and verify no loss of data
        definition_scm_source_model_json2 = definition_scm_source_model.to_dict()
        assert definition_scm_source_model_json2 == definition_scm_source_model_json

class TestModel_Definitions():
    """
    Test Class for Definitions
    """

    def test_definitions_serialization(self):
        """
        Test serialization/deserialization for Definitions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_scm_source_model = {} # DefinitionScmSource
        definition_scm_source_model['url'] = 'testString'
        definition_scm_source_model['branch'] = 'testString'
        definition_scm_source_model['tag'] = 'testString'
        definition_scm_source_model['path'] = 'testString'

        definitions_definitions_item_model = {} # DefinitionsDefinitionsItem
        definitions_definitions_item_model['scm_source'] = definition_scm_source_model
        definitions_definitions_item_model['service_instance_id'] = 'testString'
        definitions_definitions_item_model['id'] = 'testString'
        definitions_definitions_item_model['href'] = 'testString'

        # Construct a json representation of a Definitions model
        definitions_model_json = {}
        definitions_model_json['definitions'] = [definitions_definitions_item_model]

        # Construct a model instance of Definitions by calling from_dict on the json representation
        definitions_model = Definitions.from_dict(definitions_model_json)
        assert definitions_model != False

        # Construct a model instance of Definitions by calling from_dict on the json representation
        definitions_model_dict = Definitions.from_dict(definitions_model_json).__dict__
        definitions_model2 = Definitions(**definitions_model_dict)

        # Verify the model instances are equivalent
        assert definitions_model == definitions_model2

        # Convert model instance back to dict and verify no loss of data
        definitions_model_json2 = definitions_model.to_dict()
        assert definitions_model_json2 == definitions_model_json

class TestModel_DefinitionsDefinitionsItem():
    """
    Test Class for DefinitionsDefinitionsItem
    """

    def test_definitions_definitions_item_serialization(self):
        """
        Test serialization/deserialization for DefinitionsDefinitionsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        definition_scm_source_model = {} # DefinitionScmSource
        definition_scm_source_model['url'] = 'testString'
        definition_scm_source_model['branch'] = 'testString'
        definition_scm_source_model['tag'] = 'testString'
        definition_scm_source_model['path'] = 'testString'

        # Construct a json representation of a DefinitionsDefinitionsItem model
        definitions_definitions_item_model_json = {}
        definitions_definitions_item_model_json['scm_source'] = definition_scm_source_model
        definitions_definitions_item_model_json['service_instance_id'] = 'testString'
        definitions_definitions_item_model_json['id'] = 'testString'
        definitions_definitions_item_model_json['href'] = 'testString'

        # Construct a model instance of DefinitionsDefinitionsItem by calling from_dict on the json representation
        definitions_definitions_item_model = DefinitionsDefinitionsItem.from_dict(definitions_definitions_item_model_json)
        assert definitions_definitions_item_model != False

        # Construct a model instance of DefinitionsDefinitionsItem by calling from_dict on the json representation
        definitions_definitions_item_model_dict = DefinitionsDefinitionsItem.from_dict(definitions_definitions_item_model_json).__dict__
        definitions_definitions_item_model2 = DefinitionsDefinitionsItem(**definitions_definitions_item_model_dict)

        # Verify the model instances are equivalent
        assert definitions_definitions_item_model == definitions_definitions_item_model2

        # Convert model instance back to dict and verify no loss of data
        definitions_definitions_item_model_json2 = definitions_definitions_item_model.to_dict()
        assert definitions_definitions_item_model_json2 == definitions_definitions_item_model_json

class TestModel_EnvProperties():
    """
    Test Class for EnvProperties
    """

    def test_env_properties_serialization(self):
        """
        Test serialization/deserialization for EnvProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['default'] = 'testString'
        property_model['type'] = 'SECURE'
        property_model['path'] = 'testString'

        # Construct a json representation of a EnvProperties model
        env_properties_model_json = {}
        env_properties_model_json['properties'] = [property_model]

        # Construct a model instance of EnvProperties by calling from_dict on the json representation
        env_properties_model = EnvProperties.from_dict(env_properties_model_json)
        assert env_properties_model != False

        # Construct a model instance of EnvProperties by calling from_dict on the json representation
        env_properties_model_dict = EnvProperties.from_dict(env_properties_model_json).__dict__
        env_properties_model2 = EnvProperties(**env_properties_model_dict)

        # Verify the model instances are equivalent
        assert env_properties_model == env_properties_model2

        # Convert model instance back to dict and verify no loss of data
        env_properties_model_json2 = env_properties_model.to_dict()
        assert env_properties_model_json2 == env_properties_model_json

class TestModel_Events():
    """
    Test Class for Events
    """

    def test_events_serialization(self):
        """
        Test serialization/deserialization for Events
        """

        # Construct a json representation of a Events model
        events_model_json = {}
        events_model_json['push'] = True
        events_model_json['pull_request_closed'] = True
        events_model_json['pull_request'] = True

        # Construct a model instance of Events by calling from_dict on the json representation
        events_model = Events.from_dict(events_model_json)
        assert events_model != False

        # Construct a model instance of Events by calling from_dict on the json representation
        events_model_dict = Events.from_dict(events_model_json).__dict__
        events_model2 = Events(**events_model_dict)

        # Verify the model instances are equivalent
        assert events_model == events_model2

        # Convert model instance back to dict and verify no loss of data
        events_model_json2 = events_model.to_dict()
        assert events_model_json2 == events_model_json

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
        generic_secret_model_json['type'] = 'tokenMatches'
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
        pipeline_run_worker_model['agent'] = 'testString'
        pipeline_run_worker_model['service_id'] = 'testString'
        pipeline_run_worker_model['id'] = 'testString'

        trigger_model = {} # TriggerDuplicateTrigger
        trigger_model['source_trigger_id'] = 'testString'
        trigger_model['name'] = 'start-deploy'

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['default'] = 'testString'
        property_model['type'] = 'SECURE'
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
        pipeline_run_model_json['event_header_params_blob'] = 'testString'
        pipeline_run_model_json['properties'] = [property_model]
        pipeline_run_model_json['created'] = '2019-01-01T12:00:00Z'
        pipeline_run_model_json['updated'] = '2019-01-01T12:00:00Z'
        pipeline_run_model_json['html_url'] = 'testString'

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

class TestModel_PipelineRunLog():
    """
    Test Class for PipelineRunLog
    """

    def test_pipeline_run_log_serialization(self):
        """
        Test serialization/deserialization for PipelineRunLog
        """

        # Construct a json representation of a PipelineRunLog model
        pipeline_run_log_model_json = {}
        pipeline_run_log_model_json['name'] = 'testString'
        pipeline_run_log_model_json['id'] = 'testString'
        pipeline_run_log_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunLog by calling from_dict on the json representation
        pipeline_run_log_model = PipelineRunLog.from_dict(pipeline_run_log_model_json)
        assert pipeline_run_log_model != False

        # Construct a model instance of PipelineRunLog by calling from_dict on the json representation
        pipeline_run_log_model_dict = PipelineRunLog.from_dict(pipeline_run_log_model_json).__dict__
        pipeline_run_log_model2 = PipelineRunLog(**pipeline_run_log_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_run_log_model == pipeline_run_log_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_run_log_model_json2 = pipeline_run_log_model.to_dict()
        assert pipeline_run_log_model_json2 == pipeline_run_log_model_json

class TestModel_PipelineRunLogs():
    """
    Test Class for PipelineRunLogs
    """

    def test_pipeline_run_logs_serialization(self):
        """
        Test serialization/deserialization for PipelineRunLogs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pipeline_run_log_model = {} # PipelineRunLog
        pipeline_run_log_model['name'] = 'testString'
        pipeline_run_log_model['id'] = 'testString'
        pipeline_run_log_model['href'] = 'testString'

        # Construct a json representation of a PipelineRunLogs model
        pipeline_run_logs_model_json = {}
        pipeline_run_logs_model_json['logs'] = [pipeline_run_log_model]

        # Construct a model instance of PipelineRunLogs by calling from_dict on the json representation
        pipeline_run_logs_model = PipelineRunLogs.from_dict(pipeline_run_logs_model_json)
        assert pipeline_run_logs_model != False

        # Construct a model instance of PipelineRunLogs by calling from_dict on the json representation
        pipeline_run_logs_model_dict = PipelineRunLogs.from_dict(pipeline_run_logs_model_json).__dict__
        pipeline_run_logs_model2 = PipelineRunLogs(**pipeline_run_logs_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_run_logs_model == pipeline_run_logs_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_run_logs_model_json2 = pipeline_run_logs_model.to_dict()
        assert pipeline_run_logs_model_json2 == pipeline_run_logs_model_json

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
        pipeline_run_worker_model_json['agent'] = 'testString'
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

class TestModel_PipelineRuns():
    """
    Test Class for PipelineRuns
    """

    def test_pipeline_runs_serialization(self):
        """
        Test serialization/deserialization for PipelineRuns
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_info_model = {} # UserInfo
        user_info_model['iam_id'] = 'testString'
        user_info_model['sub'] = 'testString'

        pipeline_run_worker_model = {} # PipelineRunWorker
        pipeline_run_worker_model['name'] = 'testString'
        pipeline_run_worker_model['agent'] = 'testString'
        pipeline_run_worker_model['service_id'] = 'testString'
        pipeline_run_worker_model['id'] = 'testString'

        trigger_model = {} # TriggerDuplicateTrigger
        trigger_model['source_trigger_id'] = 'testString'
        trigger_model['name'] = 'start-deploy'

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['default'] = 'testString'
        property_model['type'] = 'SECURE'
        property_model['path'] = 'testString'

        pipeline_runs_pipeline_runs_item_model = {} # PipelineRunsPipelineRunsItem
        pipeline_runs_pipeline_runs_item_model['id'] = 'testString'
        pipeline_runs_pipeline_runs_item_model['user_info'] = user_info_model
        pipeline_runs_pipeline_runs_item_model['status'] = 'pending'
        pipeline_runs_pipeline_runs_item_model['definition_id'] = 'testString'
        pipeline_runs_pipeline_runs_item_model['worker'] = pipeline_run_worker_model
        pipeline_runs_pipeline_runs_item_model['pipeline_id'] = 'testString'
        pipeline_runs_pipeline_runs_item_model['listener_name'] = 'testString'
        pipeline_runs_pipeline_runs_item_model['trigger'] = trigger_model
        pipeline_runs_pipeline_runs_item_model['event_params_blob'] = 'testString'
        pipeline_runs_pipeline_runs_item_model['event_header_params_blob'] = 'testString'
        pipeline_runs_pipeline_runs_item_model['properties'] = [property_model]
        pipeline_runs_pipeline_runs_item_model['created'] = '2019-01-01T12:00:00Z'
        pipeline_runs_pipeline_runs_item_model['updated'] = '2019-01-01T12:00:00Z'
        pipeline_runs_pipeline_runs_item_model['html_url'] = 'testString'
        pipeline_runs_pipeline_runs_item_model['href'] = 'testString'

        pipeline_runs_first_model = {} # PipelineRunsFirst
        pipeline_runs_first_model['href'] = 'testString'

        pipeline_runs_next_model = {} # PipelineRunsNext
        pipeline_runs_next_model['href'] = 'testString'

        # Construct a json representation of a PipelineRuns model
        pipeline_runs_model_json = {}
        pipeline_runs_model_json['pipeline_runs'] = [pipeline_runs_pipeline_runs_item_model]
        pipeline_runs_model_json['offset'] = 20
        pipeline_runs_model_json['limit'] = 20
        pipeline_runs_model_json['first'] = pipeline_runs_first_model
        pipeline_runs_model_json['next'] = pipeline_runs_next_model

        # Construct a model instance of PipelineRuns by calling from_dict on the json representation
        pipeline_runs_model = PipelineRuns.from_dict(pipeline_runs_model_json)
        assert pipeline_runs_model != False

        # Construct a model instance of PipelineRuns by calling from_dict on the json representation
        pipeline_runs_model_dict = PipelineRuns.from_dict(pipeline_runs_model_json).__dict__
        pipeline_runs_model2 = PipelineRuns(**pipeline_runs_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_model == pipeline_runs_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_model_json2 = pipeline_runs_model.to_dict()
        assert pipeline_runs_model_json2 == pipeline_runs_model_json

class TestModel_PipelineRunsFirst():
    """
    Test Class for PipelineRunsFirst
    """

    def test_pipeline_runs_first_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsFirst
        """

        # Construct a json representation of a PipelineRunsFirst model
        pipeline_runs_first_model_json = {}
        pipeline_runs_first_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunsFirst by calling from_dict on the json representation
        pipeline_runs_first_model = PipelineRunsFirst.from_dict(pipeline_runs_first_model_json)
        assert pipeline_runs_first_model != False

        # Construct a model instance of PipelineRunsFirst by calling from_dict on the json representation
        pipeline_runs_first_model_dict = PipelineRunsFirst.from_dict(pipeline_runs_first_model_json).__dict__
        pipeline_runs_first_model2 = PipelineRunsFirst(**pipeline_runs_first_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_first_model == pipeline_runs_first_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_first_model_json2 = pipeline_runs_first_model.to_dict()
        assert pipeline_runs_first_model_json2 == pipeline_runs_first_model_json

class TestModel_PipelineRunsNext():
    """
    Test Class for PipelineRunsNext
    """

    def test_pipeline_runs_next_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsNext
        """

        # Construct a json representation of a PipelineRunsNext model
        pipeline_runs_next_model_json = {}
        pipeline_runs_next_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunsNext by calling from_dict on the json representation
        pipeline_runs_next_model = PipelineRunsNext.from_dict(pipeline_runs_next_model_json)
        assert pipeline_runs_next_model != False

        # Construct a model instance of PipelineRunsNext by calling from_dict on the json representation
        pipeline_runs_next_model_dict = PipelineRunsNext.from_dict(pipeline_runs_next_model_json).__dict__
        pipeline_runs_next_model2 = PipelineRunsNext(**pipeline_runs_next_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_next_model == pipeline_runs_next_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_next_model_json2 = pipeline_runs_next_model.to_dict()
        assert pipeline_runs_next_model_json2 == pipeline_runs_next_model_json

class TestModel_PipelineRunsPipelineRunsItem():
    """
    Test Class for PipelineRunsPipelineRunsItem
    """

    def test_pipeline_runs_pipeline_runs_item_serialization(self):
        """
        Test serialization/deserialization for PipelineRunsPipelineRunsItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        user_info_model = {} # UserInfo
        user_info_model['iam_id'] = 'testString'
        user_info_model['sub'] = 'testString'

        pipeline_run_worker_model = {} # PipelineRunWorker
        pipeline_run_worker_model['name'] = 'testString'
        pipeline_run_worker_model['agent'] = 'testString'
        pipeline_run_worker_model['service_id'] = 'testString'
        pipeline_run_worker_model['id'] = 'testString'

        trigger_model = {} # TriggerDuplicateTrigger
        trigger_model['source_trigger_id'] = 'testString'
        trigger_model['name'] = 'start-deploy'

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['default'] = 'testString'
        property_model['type'] = 'SECURE'
        property_model['path'] = 'testString'

        # Construct a json representation of a PipelineRunsPipelineRunsItem model
        pipeline_runs_pipeline_runs_item_model_json = {}
        pipeline_runs_pipeline_runs_item_model_json['id'] = 'testString'
        pipeline_runs_pipeline_runs_item_model_json['user_info'] = user_info_model
        pipeline_runs_pipeline_runs_item_model_json['status'] = 'pending'
        pipeline_runs_pipeline_runs_item_model_json['definition_id'] = 'testString'
        pipeline_runs_pipeline_runs_item_model_json['worker'] = pipeline_run_worker_model
        pipeline_runs_pipeline_runs_item_model_json['pipeline_id'] = 'testString'
        pipeline_runs_pipeline_runs_item_model_json['listener_name'] = 'testString'
        pipeline_runs_pipeline_runs_item_model_json['trigger'] = trigger_model
        pipeline_runs_pipeline_runs_item_model_json['event_params_blob'] = 'testString'
        pipeline_runs_pipeline_runs_item_model_json['event_header_params_blob'] = 'testString'
        pipeline_runs_pipeline_runs_item_model_json['properties'] = [property_model]
        pipeline_runs_pipeline_runs_item_model_json['created'] = '2019-01-01T12:00:00Z'
        pipeline_runs_pipeline_runs_item_model_json['updated'] = '2019-01-01T12:00:00Z'
        pipeline_runs_pipeline_runs_item_model_json['html_url'] = 'testString'
        pipeline_runs_pipeline_runs_item_model_json['href'] = 'testString'

        # Construct a model instance of PipelineRunsPipelineRunsItem by calling from_dict on the json representation
        pipeline_runs_pipeline_runs_item_model = PipelineRunsPipelineRunsItem.from_dict(pipeline_runs_pipeline_runs_item_model_json)
        assert pipeline_runs_pipeline_runs_item_model != False

        # Construct a model instance of PipelineRunsPipelineRunsItem by calling from_dict on the json representation
        pipeline_runs_pipeline_runs_item_model_dict = PipelineRunsPipelineRunsItem.from_dict(pipeline_runs_pipeline_runs_item_model_json).__dict__
        pipeline_runs_pipeline_runs_item_model2 = PipelineRunsPipelineRunsItem(**pipeline_runs_pipeline_runs_item_model_dict)

        # Verify the model instances are equivalent
        assert pipeline_runs_pipeline_runs_item_model == pipeline_runs_pipeline_runs_item_model2

        # Convert model instance back to dict and verify no loss of data
        pipeline_runs_pipeline_runs_item_model_json2 = pipeline_runs_pipeline_runs_item_model.to_dict()
        assert pipeline_runs_pipeline_runs_item_model_json2 == pipeline_runs_pipeline_runs_item_model_json

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
        property_model_json['default'] = 'testString'
        property_model_json['type'] = 'SECURE'
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
        step_log_model_json['id'] = 'testString'
        step_log_model_json['data'] = 'testString'

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

        toolchain_model = {} # Toolchain
        toolchain_model['id'] = 'testString'
        toolchain_model['crn'] = 'crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::'

        definition_scm_source_model = {} # DefinitionScmSource
        definition_scm_source_model['url'] = 'testString'
        definition_scm_source_model['branch'] = 'testString'
        definition_scm_source_model['tag'] = 'testString'
        definition_scm_source_model['path'] = 'testString'

        definition_model = {} # Definition
        definition_model['scm_source'] = definition_scm_source_model
        definition_model['service_instance_id'] = 'testString'
        definition_model['id'] = 'testString'

        property_model = {} # Property
        property_model['name'] = 'testString'
        property_model['value'] = 'testString'
        property_model['enum'] = ['testString']
        property_model['default'] = 'testString'
        property_model['type'] = 'SECURE'
        property_model['path'] = 'testString'

        tekton_pipeline_pipeline_definition_model = {} # TektonPipelinePipelineDefinition
        tekton_pipeline_pipeline_definition_model['status'] = 'updated'
        tekton_pipeline_pipeline_definition_model['id'] = 'testString'

        trigger_model = {} # TriggerDuplicateTrigger
        trigger_model['source_trigger_id'] = 'testString'
        trigger_model['name'] = 'start-deploy'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        # Construct a json representation of a TektonPipeline model
        tekton_pipeline_model_json = {}
        tekton_pipeline_model_json['name'] = 'testString'
        tekton_pipeline_model_json['status'] = 'configured'
        tekton_pipeline_model_json['resource_group_id'] = 'testString'
        tekton_pipeline_model_json['toolchain'] = toolchain_model
        tekton_pipeline_model_json['id'] = 'testString'
        tekton_pipeline_model_json['definitions'] = [definition_model]
        tekton_pipeline_model_json['properties'] = [property_model]
        tekton_pipeline_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        tekton_pipeline_model_json['created'] = '2019-01-01T12:00:00Z'
        tekton_pipeline_model_json['pipeline_definition'] = tekton_pipeline_pipeline_definition_model
        tekton_pipeline_model_json['triggers'] = [trigger_model]
        tekton_pipeline_model_json['worker'] = worker_model
        tekton_pipeline_model_json['html_url'] = 'testString'
        tekton_pipeline_model_json['build_number'] = 1
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

class TestModel_TektonPipelinePipelineDefinition():
    """
    Test Class for TektonPipelinePipelineDefinition
    """

    def test_tekton_pipeline_pipeline_definition_serialization(self):
        """
        Test serialization/deserialization for TektonPipelinePipelineDefinition
        """

        # Construct a json representation of a TektonPipelinePipelineDefinition model
        tekton_pipeline_pipeline_definition_model_json = {}
        tekton_pipeline_pipeline_definition_model_json['status'] = 'updated'
        tekton_pipeline_pipeline_definition_model_json['id'] = 'testString'

        # Construct a model instance of TektonPipelinePipelineDefinition by calling from_dict on the json representation
        tekton_pipeline_pipeline_definition_model = TektonPipelinePipelineDefinition.from_dict(tekton_pipeline_pipeline_definition_model_json)
        assert tekton_pipeline_pipeline_definition_model != False

        # Construct a model instance of TektonPipelinePipelineDefinition by calling from_dict on the json representation
        tekton_pipeline_pipeline_definition_model_dict = TektonPipelinePipelineDefinition.from_dict(tekton_pipeline_pipeline_definition_model_json).__dict__
        tekton_pipeline_pipeline_definition_model2 = TektonPipelinePipelineDefinition(**tekton_pipeline_pipeline_definition_model_dict)

        # Verify the model instances are equivalent
        assert tekton_pipeline_pipeline_definition_model == tekton_pipeline_pipeline_definition_model2

        # Convert model instance back to dict and verify no loss of data
        tekton_pipeline_pipeline_definition_model_json2 = tekton_pipeline_pipeline_definition_model.to_dict()
        assert tekton_pipeline_pipeline_definition_model_json2 == tekton_pipeline_pipeline_definition_model_json

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
        toolchain_model_json['crn'] = 'crn:v1:staging:public:toolchain:us-south:a/0ba224679d6c697f9baee5e14ade83ac:bf5fa00f-ddef-4298-b87b-aa8b6da0e1a6::'

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
        trigger_generic_trigger_properties_item_model_json['default'] = 'testString'
        trigger_generic_trigger_properties_item_model_json['type'] = 'SECURE'
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
        trigger_manual_trigger_properties_item_model_json['default'] = 'testString'
        trigger_manual_trigger_properties_item_model_json['type'] = 'SECURE'
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

class TestModel_TriggerProperties():
    """
    Test Class for TriggerProperties
    """

    def test_trigger_properties_serialization(self):
        """
        Test serialization/deserialization for TriggerProperties
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trigger_properties_properties_item_model = {} # TriggerPropertiesPropertiesItem
        trigger_properties_properties_item_model['name'] = 'testString'
        trigger_properties_properties_item_model['value'] = 'testString'
        trigger_properties_properties_item_model['enum'] = ['testString']
        trigger_properties_properties_item_model['default'] = 'testString'
        trigger_properties_properties_item_model['type'] = 'SECURE'
        trigger_properties_properties_item_model['path'] = 'testString'
        trigger_properties_properties_item_model['href'] = 'testString'

        # Construct a json representation of a TriggerProperties model
        trigger_properties_model_json = {}
        trigger_properties_model_json['properties'] = [trigger_properties_properties_item_model]

        # Construct a model instance of TriggerProperties by calling from_dict on the json representation
        trigger_properties_model = TriggerProperties.from_dict(trigger_properties_model_json)
        assert trigger_properties_model != False

        # Construct a model instance of TriggerProperties by calling from_dict on the json representation
        trigger_properties_model_dict = TriggerProperties.from_dict(trigger_properties_model_json).__dict__
        trigger_properties_model2 = TriggerProperties(**trigger_properties_model_dict)

        # Verify the model instances are equivalent
        assert trigger_properties_model == trigger_properties_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_properties_model_json2 = trigger_properties_model.to_dict()
        assert trigger_properties_model_json2 == trigger_properties_model_json

class TestModel_TriggerPropertiesPropertiesItem():
    """
    Test Class for TriggerPropertiesPropertiesItem
    """

    def test_trigger_properties_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggerPropertiesPropertiesItem
        """

        # Construct a json representation of a TriggerPropertiesPropertiesItem model
        trigger_properties_properties_item_model_json = {}
        trigger_properties_properties_item_model_json['name'] = 'testString'
        trigger_properties_properties_item_model_json['value'] = 'testString'
        trigger_properties_properties_item_model_json['enum'] = ['testString']
        trigger_properties_properties_item_model_json['default'] = 'testString'
        trigger_properties_properties_item_model_json['type'] = 'SECURE'
        trigger_properties_properties_item_model_json['path'] = 'testString'
        trigger_properties_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggerPropertiesPropertiesItem by calling from_dict on the json representation
        trigger_properties_properties_item_model = TriggerPropertiesPropertiesItem.from_dict(trigger_properties_properties_item_model_json)
        assert trigger_properties_properties_item_model != False

        # Construct a model instance of TriggerPropertiesPropertiesItem by calling from_dict on the json representation
        trigger_properties_properties_item_model_dict = TriggerPropertiesPropertiesItem.from_dict(trigger_properties_properties_item_model_json).__dict__
        trigger_properties_properties_item_model2 = TriggerPropertiesPropertiesItem(**trigger_properties_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert trigger_properties_properties_item_model == trigger_properties_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_properties_properties_item_model_json2 = trigger_properties_properties_item_model.to_dict()
        assert trigger_properties_properties_item_model_json2 == trigger_properties_properties_item_model_json

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
        trigger_property_model_json['default'] = 'testString'
        trigger_property_model_json['type'] = 'SECURE'
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

class TestModel_TriggerScmSource():
    """
    Test Class for TriggerScmSource
    """

    def test_trigger_scm_source_serialization(self):
        """
        Test serialization/deserialization for TriggerScmSource
        """

        # Construct a json representation of a TriggerScmSource model
        trigger_scm_source_model_json = {}
        trigger_scm_source_model_json['url'] = 'testString'
        trigger_scm_source_model_json['branch'] = 'testString'
        trigger_scm_source_model_json['pattern'] = 'testString'
        trigger_scm_source_model_json['blind_connection'] = True
        trigger_scm_source_model_json['hook_id'] = 'testString'

        # Construct a model instance of TriggerScmSource by calling from_dict on the json representation
        trigger_scm_source_model = TriggerScmSource.from_dict(trigger_scm_source_model_json)
        assert trigger_scm_source_model != False

        # Construct a model instance of TriggerScmSource by calling from_dict on the json representation
        trigger_scm_source_model_dict = TriggerScmSource.from_dict(trigger_scm_source_model_json).__dict__
        trigger_scm_source_model2 = TriggerScmSource(**trigger_scm_source_model_dict)

        # Verify the model instances are equivalent
        assert trigger_scm_source_model == trigger_scm_source_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_scm_source_model_json2 = trigger_scm_source_model.to_dict()
        assert trigger_scm_source_model_json2 == trigger_scm_source_model_json

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
        trigger_scm_trigger_properties_item_model_json['default'] = 'testString'
        trigger_scm_trigger_properties_item_model_json['type'] = 'SECURE'
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
        trigger_timer_trigger_properties_item_model_json['default'] = 'testString'
        trigger_timer_trigger_properties_item_model_json['type'] = 'SECURE'
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

class TestModel_Triggers():
    """
    Test Class for Triggers
    """

    def test_triggers_serialization(self):
        """
        Test serialization/deserialization for Triggers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        triggers_triggers_item_model = {} # TriggersTriggersItemTriggerDuplicateTrigger
        triggers_triggers_item_model['href'] = 'testString'
        triggers_triggers_item_model['source_trigger_id'] = 'testString'
        triggers_triggers_item_model['name'] = 'start-deploy'

        # Construct a json representation of a Triggers model
        triggers_model_json = {}
        triggers_model_json['triggers'] = [triggers_triggers_item_model]

        # Construct a model instance of Triggers by calling from_dict on the json representation
        triggers_model = Triggers.from_dict(triggers_model_json)
        assert triggers_model != False

        # Construct a model instance of Triggers by calling from_dict on the json representation
        triggers_model_dict = Triggers.from_dict(triggers_model_json).__dict__
        triggers_model2 = Triggers(**triggers_model_dict)

        # Verify the model instances are equivalent
        assert triggers_model == triggers_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_model_json2 = triggers_model.to_dict()
        assert triggers_model_json2 == triggers_model_json

class TestModel_TriggersTriggersItemTriggerGenericTriggerPropertiesItem():
    """
    Test Class for TriggersTriggersItemTriggerGenericTriggerPropertiesItem
    """

    def test_triggers_triggers_item_trigger_generic_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerGenericTriggerPropertiesItem
        """

        # Construct a json representation of a TriggersTriggersItemTriggerGenericTriggerPropertiesItem model
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json = {}
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json['name'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json['value'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json['enum'] = ['testString']
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json['default'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json['type'] = 'SECURE'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json['path'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggersTriggersItemTriggerGenericTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_generic_trigger_properties_item_model = TriggersTriggersItemTriggerGenericTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_generic_trigger_properties_item_model_json)
        assert triggers_triggers_item_trigger_generic_trigger_properties_item_model != False

        # Construct a model instance of TriggersTriggersItemTriggerGenericTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_dict = TriggersTriggersItemTriggerGenericTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_generic_trigger_properties_item_model_json).__dict__
        triggers_triggers_item_trigger_generic_trigger_properties_item_model2 = TriggersTriggersItemTriggerGenericTriggerPropertiesItem(**triggers_triggers_item_trigger_generic_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_generic_trigger_properties_item_model == triggers_triggers_item_trigger_generic_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_generic_trigger_properties_item_model_json2 = triggers_triggers_item_trigger_generic_trigger_properties_item_model.to_dict()
        assert triggers_triggers_item_trigger_generic_trigger_properties_item_model_json2 == triggers_triggers_item_trigger_generic_trigger_properties_item_model_json

class TestModel_TriggersTriggersItemTriggerManualTriggerPropertiesItem():
    """
    Test Class for TriggersTriggersItemTriggerManualTriggerPropertiesItem
    """

    def test_triggers_triggers_item_trigger_manual_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerManualTriggerPropertiesItem
        """

        # Construct a json representation of a TriggersTriggersItemTriggerManualTriggerPropertiesItem model
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json = {}
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json['name'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json['value'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json['enum'] = ['testString']
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json['default'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json['type'] = 'SECURE'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json['path'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggersTriggersItemTriggerManualTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_manual_trigger_properties_item_model = TriggersTriggersItemTriggerManualTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_manual_trigger_properties_item_model_json)
        assert triggers_triggers_item_trigger_manual_trigger_properties_item_model != False

        # Construct a model instance of TriggersTriggersItemTriggerManualTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_dict = TriggersTriggersItemTriggerManualTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_manual_trigger_properties_item_model_json).__dict__
        triggers_triggers_item_trigger_manual_trigger_properties_item_model2 = TriggersTriggersItemTriggerManualTriggerPropertiesItem(**triggers_triggers_item_trigger_manual_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_manual_trigger_properties_item_model == triggers_triggers_item_trigger_manual_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_manual_trigger_properties_item_model_json2 = triggers_triggers_item_trigger_manual_trigger_properties_item_model.to_dict()
        assert triggers_triggers_item_trigger_manual_trigger_properties_item_model_json2 == triggers_triggers_item_trigger_manual_trigger_properties_item_model_json

class TestModel_TriggersTriggersItemTriggerScmTriggerPropertiesItem():
    """
    Test Class for TriggersTriggersItemTriggerScmTriggerPropertiesItem
    """

    def test_triggers_triggers_item_trigger_scm_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerScmTriggerPropertiesItem
        """

        # Construct a json representation of a TriggersTriggersItemTriggerScmTriggerPropertiesItem model
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json = {}
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json['name'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json['value'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json['enum'] = ['testString']
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json['default'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json['type'] = 'SECURE'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json['path'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggersTriggersItemTriggerScmTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_scm_trigger_properties_item_model = TriggersTriggersItemTriggerScmTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_scm_trigger_properties_item_model_json)
        assert triggers_triggers_item_trigger_scm_trigger_properties_item_model != False

        # Construct a model instance of TriggersTriggersItemTriggerScmTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_dict = TriggersTriggersItemTriggerScmTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_scm_trigger_properties_item_model_json).__dict__
        triggers_triggers_item_trigger_scm_trigger_properties_item_model2 = TriggersTriggersItemTriggerScmTriggerPropertiesItem(**triggers_triggers_item_trigger_scm_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_scm_trigger_properties_item_model == triggers_triggers_item_trigger_scm_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_scm_trigger_properties_item_model_json2 = triggers_triggers_item_trigger_scm_trigger_properties_item_model.to_dict()
        assert triggers_triggers_item_trigger_scm_trigger_properties_item_model_json2 == triggers_triggers_item_trigger_scm_trigger_properties_item_model_json

class TestModel_TriggersTriggersItemTriggerTimerTriggerPropertiesItem():
    """
    Test Class for TriggersTriggersItemTriggerTimerTriggerPropertiesItem
    """

    def test_triggers_triggers_item_trigger_timer_trigger_properties_item_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerTimerTriggerPropertiesItem
        """

        # Construct a json representation of a TriggersTriggersItemTriggerTimerTriggerPropertiesItem model
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json = {}
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json['name'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json['value'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json['enum'] = ['testString']
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json['default'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json['type'] = 'SECURE'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json['path'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json['href'] = 'testString'

        # Construct a model instance of TriggersTriggersItemTriggerTimerTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_timer_trigger_properties_item_model = TriggersTriggersItemTriggerTimerTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_timer_trigger_properties_item_model_json)
        assert triggers_triggers_item_trigger_timer_trigger_properties_item_model != False

        # Construct a model instance of TriggersTriggersItemTriggerTimerTriggerPropertiesItem by calling from_dict on the json representation
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_dict = TriggersTriggersItemTriggerTimerTriggerPropertiesItem.from_dict(triggers_triggers_item_trigger_timer_trigger_properties_item_model_json).__dict__
        triggers_triggers_item_trigger_timer_trigger_properties_item_model2 = TriggersTriggersItemTriggerTimerTriggerPropertiesItem(**triggers_triggers_item_trigger_timer_trigger_properties_item_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_timer_trigger_properties_item_model == triggers_triggers_item_trigger_timer_trigger_properties_item_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_timer_trigger_properties_item_model_json2 = triggers_triggers_item_trigger_timer_trigger_properties_item_model.to_dict()
        assert triggers_triggers_item_trigger_timer_trigger_properties_item_model_json2 == triggers_triggers_item_trigger_timer_trigger_properties_item_model_json

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
        worker_model_json['type'] = 'private'
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

class TestModel_WorkerWithId():
    """
    Test Class for WorkerWithId
    """

    def test_worker_with_id_serialization(self):
        """
        Test serialization/deserialization for WorkerWithId
        """

        # Construct a json representation of a WorkerWithId model
        worker_with_id_model_json = {}
        worker_with_id_model_json['id'] = 'testString'

        # Construct a model instance of WorkerWithId by calling from_dict on the json representation
        worker_with_id_model = WorkerWithId.from_dict(worker_with_id_model_json)
        assert worker_with_id_model != False

        # Construct a model instance of WorkerWithId by calling from_dict on the json representation
        worker_with_id_model_dict = WorkerWithId.from_dict(worker_with_id_model_json).__dict__
        worker_with_id_model2 = WorkerWithId(**worker_with_id_model_dict)

        # Verify the model instances are equivalent
        assert worker_with_id_model == worker_with_id_model2

        # Convert model instance back to dict and verify no loss of data
        worker_with_id_model_json2 = worker_with_id_model.to_dict()
        assert worker_with_id_model_json2 == worker_with_id_model_json

class TestModel_TriggerDuplicateTrigger():
    """
    Test Class for TriggerDuplicateTrigger
    """

    def test_trigger_duplicate_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggerDuplicateTrigger
        """

        # Construct a json representation of a TriggerDuplicateTrigger model
        trigger_duplicate_trigger_model_json = {}
        trigger_duplicate_trigger_model_json['source_trigger_id'] = 'testString'
        trigger_duplicate_trigger_model_json['name'] = 'start-deploy'

        # Construct a model instance of TriggerDuplicateTrigger by calling from_dict on the json representation
        trigger_duplicate_trigger_model = TriggerDuplicateTrigger.from_dict(trigger_duplicate_trigger_model_json)
        assert trigger_duplicate_trigger_model != False

        # Construct a model instance of TriggerDuplicateTrigger by calling from_dict on the json representation
        trigger_duplicate_trigger_model_dict = TriggerDuplicateTrigger.from_dict(trigger_duplicate_trigger_model_json).__dict__
        trigger_duplicate_trigger_model2 = TriggerDuplicateTrigger(**trigger_duplicate_trigger_model_dict)

        # Verify the model instances are equivalent
        assert trigger_duplicate_trigger_model == trigger_duplicate_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        trigger_duplicate_trigger_model_json2 = trigger_duplicate_trigger_model.to_dict()
        assert trigger_duplicate_trigger_model_json2 == trigger_duplicate_trigger_model_json

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
        trigger_generic_trigger_properties_item_model['default'] = 'testString'
        trigger_generic_trigger_properties_item_model['type'] = 'SECURE'
        trigger_generic_trigger_properties_item_model['path'] = 'testString'
        trigger_generic_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        generic_secret_model = {} # GenericSecret
        generic_secret_model['type'] = 'tokenMatches'
        generic_secret_model['value'] = 'testString'
        generic_secret_model['source'] = 'header'
        generic_secret_model['key_name'] = 'testString'
        generic_secret_model['algorithm'] = 'md4'

        # Construct a json representation of a TriggerGenericTrigger model
        trigger_generic_trigger_model_json = {}
        trigger_generic_trigger_model_json['type'] = 'testString'
        trigger_generic_trigger_model_json['name'] = 'start-deploy'
        trigger_generic_trigger_model_json['event_listener'] = 'testString'
        trigger_generic_trigger_model_json['id'] = 'testString'
        trigger_generic_trigger_model_json['properties'] = [trigger_generic_trigger_properties_item_model]
        trigger_generic_trigger_model_json['tags'] = ['testString']
        trigger_generic_trigger_model_json['worker'] = worker_model
        trigger_generic_trigger_model_json['concurrency'] = concurrency_model
        trigger_generic_trigger_model_json['disabled'] = True
        trigger_generic_trigger_model_json['secret'] = generic_secret_model

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
        trigger_manual_trigger_properties_item_model['default'] = 'testString'
        trigger_manual_trigger_properties_item_model['type'] = 'SECURE'
        trigger_manual_trigger_properties_item_model['path'] = 'testString'
        trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        # Construct a json representation of a TriggerManualTrigger model
        trigger_manual_trigger_model_json = {}
        trigger_manual_trigger_model_json['type'] = 'testString'
        trigger_manual_trigger_model_json['name'] = 'start-deploy'
        trigger_manual_trigger_model_json['event_listener'] = 'testString'
        trigger_manual_trigger_model_json['id'] = 'testString'
        trigger_manual_trigger_model_json['properties'] = [trigger_manual_trigger_properties_item_model]
        trigger_manual_trigger_model_json['tags'] = ['testString']
        trigger_manual_trigger_model_json['worker'] = worker_model
        trigger_manual_trigger_model_json['concurrency'] = concurrency_model
        trigger_manual_trigger_model_json['disabled'] = True

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
        trigger_scm_trigger_properties_item_model['default'] = 'testString'
        trigger_scm_trigger_properties_item_model['type'] = 'SECURE'
        trigger_scm_trigger_properties_item_model['path'] = 'testString'
        trigger_scm_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        trigger_scm_source_model = {} # TriggerScmSource
        trigger_scm_source_model['url'] = 'testString'
        trigger_scm_source_model['branch'] = 'testString'
        trigger_scm_source_model['pattern'] = 'testString'
        trigger_scm_source_model['blind_connection'] = True
        trigger_scm_source_model['hook_id'] = 'testString'

        events_model = {} # Events
        events_model['push'] = True
        events_model['pull_request_closed'] = True
        events_model['pull_request'] = True

        # Construct a json representation of a TriggerScmTrigger model
        trigger_scm_trigger_model_json = {}
        trigger_scm_trigger_model_json['type'] = 'testString'
        trigger_scm_trigger_model_json['name'] = 'start-deploy'
        trigger_scm_trigger_model_json['event_listener'] = 'testString'
        trigger_scm_trigger_model_json['id'] = 'testString'
        trigger_scm_trigger_model_json['properties'] = [trigger_scm_trigger_properties_item_model]
        trigger_scm_trigger_model_json['tags'] = ['testString']
        trigger_scm_trigger_model_json['worker'] = worker_model
        trigger_scm_trigger_model_json['concurrency'] = concurrency_model
        trigger_scm_trigger_model_json['disabled'] = True
        trigger_scm_trigger_model_json['scm_source'] = trigger_scm_source_model
        trigger_scm_trigger_model_json['events'] = events_model
        trigger_scm_trigger_model_json['service_instance_id'] = 'testString'

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
        trigger_timer_trigger_properties_item_model['default'] = 'testString'
        trigger_timer_trigger_properties_item_model['type'] = 'SECURE'
        trigger_timer_trigger_properties_item_model['path'] = 'testString'
        trigger_timer_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        # Construct a json representation of a TriggerTimerTrigger model
        trigger_timer_trigger_model_json = {}
        trigger_timer_trigger_model_json['type'] = 'testString'
        trigger_timer_trigger_model_json['name'] = 'start-deploy'
        trigger_timer_trigger_model_json['event_listener'] = 'testString'
        trigger_timer_trigger_model_json['id'] = 'testString'
        trigger_timer_trigger_model_json['properties'] = [trigger_timer_trigger_properties_item_model]
        trigger_timer_trigger_model_json['tags'] = ['testString']
        trigger_timer_trigger_model_json['worker'] = worker_model
        trigger_timer_trigger_model_json['concurrency'] = concurrency_model
        trigger_timer_trigger_model_json['disabled'] = True
        trigger_timer_trigger_model_json['cron'] = 'testString'
        trigger_timer_trigger_model_json['timezone'] = 'Africa/Abidjan'

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

class TestModel_TriggersTriggersItemTriggerDuplicateTrigger():
    """
    Test Class for TriggersTriggersItemTriggerDuplicateTrigger
    """

    def test_triggers_triggers_item_trigger_duplicate_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerDuplicateTrigger
        """

        # Construct a json representation of a TriggersTriggersItemTriggerDuplicateTrigger model
        triggers_triggers_item_trigger_duplicate_trigger_model_json = {}
        triggers_triggers_item_trigger_duplicate_trigger_model_json['href'] = 'testString'
        triggers_triggers_item_trigger_duplicate_trigger_model_json['source_trigger_id'] = 'testString'
        triggers_triggers_item_trigger_duplicate_trigger_model_json['name'] = 'start-deploy'

        # Construct a model instance of TriggersTriggersItemTriggerDuplicateTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_duplicate_trigger_model = TriggersTriggersItemTriggerDuplicateTrigger.from_dict(triggers_triggers_item_trigger_duplicate_trigger_model_json)
        assert triggers_triggers_item_trigger_duplicate_trigger_model != False

        # Construct a model instance of TriggersTriggersItemTriggerDuplicateTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_duplicate_trigger_model_dict = TriggersTriggersItemTriggerDuplicateTrigger.from_dict(triggers_triggers_item_trigger_duplicate_trigger_model_json).__dict__
        triggers_triggers_item_trigger_duplicate_trigger_model2 = TriggersTriggersItemTriggerDuplicateTrigger(**triggers_triggers_item_trigger_duplicate_trigger_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_duplicate_trigger_model == triggers_triggers_item_trigger_duplicate_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_duplicate_trigger_model_json2 = triggers_triggers_item_trigger_duplicate_trigger_model.to_dict()
        assert triggers_triggers_item_trigger_duplicate_trigger_model_json2 == triggers_triggers_item_trigger_duplicate_trigger_model_json

class TestModel_TriggersTriggersItemTriggerGenericTrigger():
    """
    Test Class for TriggersTriggersItemTriggerGenericTrigger
    """

    def test_triggers_triggers_item_trigger_generic_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerGenericTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        triggers_triggers_item_trigger_generic_trigger_properties_item_model = {} # TriggersTriggersItemTriggerGenericTriggerPropertiesItem
        triggers_triggers_item_trigger_generic_trigger_properties_item_model['name'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model['value'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model['enum'] = ['testString']
        triggers_triggers_item_trigger_generic_trigger_properties_item_model['default'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model['type'] = 'SECURE'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model['path'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        generic_secret_model = {} # GenericSecret
        generic_secret_model['type'] = 'tokenMatches'
        generic_secret_model['value'] = 'testString'
        generic_secret_model['source'] = 'header'
        generic_secret_model['key_name'] = 'testString'
        generic_secret_model['algorithm'] = 'md4'

        # Construct a json representation of a TriggersTriggersItemTriggerGenericTrigger model
        triggers_triggers_item_trigger_generic_trigger_model_json = {}
        triggers_triggers_item_trigger_generic_trigger_model_json['href'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_model_json['type'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_model_json['name'] = 'start-deploy'
        triggers_triggers_item_trigger_generic_trigger_model_json['event_listener'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_model_json['id'] = 'testString'
        triggers_triggers_item_trigger_generic_trigger_model_json['properties'] = [triggers_triggers_item_trigger_generic_trigger_properties_item_model]
        triggers_triggers_item_trigger_generic_trigger_model_json['tags'] = ['testString']
        triggers_triggers_item_trigger_generic_trigger_model_json['worker'] = worker_model
        triggers_triggers_item_trigger_generic_trigger_model_json['concurrency'] = concurrency_model
        triggers_triggers_item_trigger_generic_trigger_model_json['disabled'] = True
        triggers_triggers_item_trigger_generic_trigger_model_json['secret'] = generic_secret_model

        # Construct a model instance of TriggersTriggersItemTriggerGenericTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_generic_trigger_model = TriggersTriggersItemTriggerGenericTrigger.from_dict(triggers_triggers_item_trigger_generic_trigger_model_json)
        assert triggers_triggers_item_trigger_generic_trigger_model != False

        # Construct a model instance of TriggersTriggersItemTriggerGenericTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_generic_trigger_model_dict = TriggersTriggersItemTriggerGenericTrigger.from_dict(triggers_triggers_item_trigger_generic_trigger_model_json).__dict__
        triggers_triggers_item_trigger_generic_trigger_model2 = TriggersTriggersItemTriggerGenericTrigger(**triggers_triggers_item_trigger_generic_trigger_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_generic_trigger_model == triggers_triggers_item_trigger_generic_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_generic_trigger_model_json2 = triggers_triggers_item_trigger_generic_trigger_model.to_dict()
        assert triggers_triggers_item_trigger_generic_trigger_model_json2 == triggers_triggers_item_trigger_generic_trigger_model_json

class TestModel_TriggersTriggersItemTriggerManualTrigger():
    """
    Test Class for TriggersTriggersItemTriggerManualTrigger
    """

    def test_triggers_triggers_item_trigger_manual_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerManualTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        triggers_triggers_item_trigger_manual_trigger_properties_item_model = {} # TriggersTriggersItemTriggerManualTriggerPropertiesItem
        triggers_triggers_item_trigger_manual_trigger_properties_item_model['name'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model['value'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model['enum'] = ['testString']
        triggers_triggers_item_trigger_manual_trigger_properties_item_model['default'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model['type'] = 'SECURE'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model['path'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        # Construct a json representation of a TriggersTriggersItemTriggerManualTrigger model
        triggers_triggers_item_trigger_manual_trigger_model_json = {}
        triggers_triggers_item_trigger_manual_trigger_model_json['href'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_model_json['type'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_model_json['name'] = 'start-deploy'
        triggers_triggers_item_trigger_manual_trigger_model_json['event_listener'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_model_json['id'] = 'testString'
        triggers_triggers_item_trigger_manual_trigger_model_json['properties'] = [triggers_triggers_item_trigger_manual_trigger_properties_item_model]
        triggers_triggers_item_trigger_manual_trigger_model_json['tags'] = ['testString']
        triggers_triggers_item_trigger_manual_trigger_model_json['worker'] = worker_model
        triggers_triggers_item_trigger_manual_trigger_model_json['concurrency'] = concurrency_model
        triggers_triggers_item_trigger_manual_trigger_model_json['disabled'] = True

        # Construct a model instance of TriggersTriggersItemTriggerManualTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_manual_trigger_model = TriggersTriggersItemTriggerManualTrigger.from_dict(triggers_triggers_item_trigger_manual_trigger_model_json)
        assert triggers_triggers_item_trigger_manual_trigger_model != False

        # Construct a model instance of TriggersTriggersItemTriggerManualTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_manual_trigger_model_dict = TriggersTriggersItemTriggerManualTrigger.from_dict(triggers_triggers_item_trigger_manual_trigger_model_json).__dict__
        triggers_triggers_item_trigger_manual_trigger_model2 = TriggersTriggersItemTriggerManualTrigger(**triggers_triggers_item_trigger_manual_trigger_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_manual_trigger_model == triggers_triggers_item_trigger_manual_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_manual_trigger_model_json2 = triggers_triggers_item_trigger_manual_trigger_model.to_dict()
        assert triggers_triggers_item_trigger_manual_trigger_model_json2 == triggers_triggers_item_trigger_manual_trigger_model_json

class TestModel_TriggersTriggersItemTriggerScmTrigger():
    """
    Test Class for TriggersTriggersItemTriggerScmTrigger
    """

    def test_triggers_triggers_item_trigger_scm_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerScmTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        triggers_triggers_item_trigger_scm_trigger_properties_item_model = {} # TriggersTriggersItemTriggerScmTriggerPropertiesItem
        triggers_triggers_item_trigger_scm_trigger_properties_item_model['name'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model['value'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model['enum'] = ['testString']
        triggers_triggers_item_trigger_scm_trigger_properties_item_model['default'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model['type'] = 'SECURE'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model['path'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        trigger_scm_source_model = {} # TriggerScmSource
        trigger_scm_source_model['url'] = 'testString'
        trigger_scm_source_model['branch'] = 'testString'
        trigger_scm_source_model['pattern'] = 'testString'
        trigger_scm_source_model['blind_connection'] = True
        trigger_scm_source_model['hook_id'] = 'testString'

        events_model = {} # Events
        events_model['push'] = True
        events_model['pull_request_closed'] = True
        events_model['pull_request'] = True

        # Construct a json representation of a TriggersTriggersItemTriggerScmTrigger model
        triggers_triggers_item_trigger_scm_trigger_model_json = {}
        triggers_triggers_item_trigger_scm_trigger_model_json['href'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_model_json['type'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_model_json['name'] = 'start-deploy'
        triggers_triggers_item_trigger_scm_trigger_model_json['event_listener'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_model_json['id'] = 'testString'
        triggers_triggers_item_trigger_scm_trigger_model_json['properties'] = [triggers_triggers_item_trigger_scm_trigger_properties_item_model]
        triggers_triggers_item_trigger_scm_trigger_model_json['tags'] = ['testString']
        triggers_triggers_item_trigger_scm_trigger_model_json['worker'] = worker_model
        triggers_triggers_item_trigger_scm_trigger_model_json['concurrency'] = concurrency_model
        triggers_triggers_item_trigger_scm_trigger_model_json['disabled'] = True
        triggers_triggers_item_trigger_scm_trigger_model_json['scm_source'] = trigger_scm_source_model
        triggers_triggers_item_trigger_scm_trigger_model_json['events'] = events_model
        triggers_triggers_item_trigger_scm_trigger_model_json['service_instance_id'] = 'testString'

        # Construct a model instance of TriggersTriggersItemTriggerScmTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_scm_trigger_model = TriggersTriggersItemTriggerScmTrigger.from_dict(triggers_triggers_item_trigger_scm_trigger_model_json)
        assert triggers_triggers_item_trigger_scm_trigger_model != False

        # Construct a model instance of TriggersTriggersItemTriggerScmTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_scm_trigger_model_dict = TriggersTriggersItemTriggerScmTrigger.from_dict(triggers_triggers_item_trigger_scm_trigger_model_json).__dict__
        triggers_triggers_item_trigger_scm_trigger_model2 = TriggersTriggersItemTriggerScmTrigger(**triggers_triggers_item_trigger_scm_trigger_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_scm_trigger_model == triggers_triggers_item_trigger_scm_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_scm_trigger_model_json2 = triggers_triggers_item_trigger_scm_trigger_model.to_dict()
        assert triggers_triggers_item_trigger_scm_trigger_model_json2 == triggers_triggers_item_trigger_scm_trigger_model_json

class TestModel_TriggersTriggersItemTriggerTimerTrigger():
    """
    Test Class for TriggersTriggersItemTriggerTimerTrigger
    """

    def test_triggers_triggers_item_trigger_timer_trigger_serialization(self):
        """
        Test serialization/deserialization for TriggersTriggersItemTriggerTimerTrigger
        """

        # Construct dict forms of any model objects needed in order to build this model.

        triggers_triggers_item_trigger_timer_trigger_properties_item_model = {} # TriggersTriggersItemTriggerTimerTriggerPropertiesItem
        triggers_triggers_item_trigger_timer_trigger_properties_item_model['name'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model['value'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model['enum'] = ['testString']
        triggers_triggers_item_trigger_timer_trigger_properties_item_model['default'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model['type'] = 'SECURE'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model['path'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_properties_item_model['href'] = 'testString'

        worker_model = {} # Worker
        worker_model['name'] = 'testString'
        worker_model['type'] = 'private'
        worker_model['id'] = 'testString'

        concurrency_model = {} # Concurrency
        concurrency_model['max_concurrent_runs'] = 20

        # Construct a json representation of a TriggersTriggersItemTriggerTimerTrigger model
        triggers_triggers_item_trigger_timer_trigger_model_json = {}
        triggers_triggers_item_trigger_timer_trigger_model_json['href'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_model_json['type'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_model_json['name'] = 'start-deploy'
        triggers_triggers_item_trigger_timer_trigger_model_json['event_listener'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_model_json['id'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_model_json['properties'] = [triggers_triggers_item_trigger_timer_trigger_properties_item_model]
        triggers_triggers_item_trigger_timer_trigger_model_json['tags'] = ['testString']
        triggers_triggers_item_trigger_timer_trigger_model_json['worker'] = worker_model
        triggers_triggers_item_trigger_timer_trigger_model_json['concurrency'] = concurrency_model
        triggers_triggers_item_trigger_timer_trigger_model_json['disabled'] = True
        triggers_triggers_item_trigger_timer_trigger_model_json['cron'] = 'testString'
        triggers_triggers_item_trigger_timer_trigger_model_json['timezone'] = 'Africa/Abidjan'

        # Construct a model instance of TriggersTriggersItemTriggerTimerTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_timer_trigger_model = TriggersTriggersItemTriggerTimerTrigger.from_dict(triggers_triggers_item_trigger_timer_trigger_model_json)
        assert triggers_triggers_item_trigger_timer_trigger_model != False

        # Construct a model instance of TriggersTriggersItemTriggerTimerTrigger by calling from_dict on the json representation
        triggers_triggers_item_trigger_timer_trigger_model_dict = TriggersTriggersItemTriggerTimerTrigger.from_dict(triggers_triggers_item_trigger_timer_trigger_model_json).__dict__
        triggers_triggers_item_trigger_timer_trigger_model2 = TriggersTriggersItemTriggerTimerTrigger(**triggers_triggers_item_trigger_timer_trigger_model_dict)

        # Verify the model instances are equivalent
        assert triggers_triggers_item_trigger_timer_trigger_model == triggers_triggers_item_trigger_timer_trigger_model2

        # Convert model instance back to dict and verify no loss of data
        triggers_triggers_item_trigger_timer_trigger_model_json2 = triggers_triggers_item_trigger_timer_trigger_model.to_dict()
        assert triggers_triggers_item_trigger_timer_trigger_model_json2 == triggers_triggers_item_trigger_timer_trigger_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
