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
Integration Tests for ExampleServiceV1
This class contains an integration test for the example service.

 Notes:

 1. This example integration test shows how to automatically skip tests if the required config file
    is not available.

 2. Before running this test:
    a. "cp example-service.env.hide example-service.env"
    b. start up the ExampleService service by following the instructions here:
    https://github.ibm.com/CloudEngineering/java-sdk-template/blob/main/README_FIRST.md#integration-tests
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from mysdk.example_service_v1 import *

# Config file name
config_file = 'example_service_v1.env'

# Variables to hold link values
get_resource_link = None

class TestExampleServiceV1():
    """
    Integration Test Class for ExampleServiceV1
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.example_service_service = ExampleServiceV1.new_instance(
            )
            assert cls.example_service_service is not None

            cls.config = read_external_sources(
                ExampleServiceV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.example_service_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_resource(self):

        create_resource_response = self.example_service_service.create_resource(
            name='The Hunt for Red October',
            tag='Book',
        )

        assert create_resource_response.get_status_code() == 201
        resource = create_resource_response.get_result()
        assert resource is not None

        # Store get_resource_link value for later test cases
        global get_resource_link
        get_resource_link = resource['resource_id']

    @needscredentials
    def test_list_resources(self):

        list_resources_response = self.example_service_service.list_resources(
            limit=1
        )

        assert list_resources_response.get_status_code() == 200
        resources = list_resources_response.get_result()
        assert resources is not None

    @needscredentials
    def test_get_resource(self):

        get_resource_response = self.example_service_service.get_resource(
            resource_id=get_resource_link
        )

        assert get_resource_response.get_status_code() == 200
        resource = get_resource_response.get_result()
        assert resource is not None

    @needscredentials
    def test_get_resource_encoded(self):

        create_resource_response = self.example_service_service.create_resource(
            name='Debt of Honor',
            tag='Book',
            resource_id='url%3encoded%3resource%3id'
        )

        assert create_resource_response.get_status_code() == 201
        resource = create_resource_response.get_result()
        assert resource is not None

        get_resource_encoded_response = self.example_service_service.get_resource_encoded(
            url_encoded_resource_id='url%3encoded%3resource%3id'
        )

        assert get_resource_encoded_response.get_status_code() == 200
        resource = get_resource_encoded_response.get_result()
        assert resource is not None

