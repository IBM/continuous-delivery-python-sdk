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
Examples for ExampleServiceV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from mysdk.example_service_v1 import *

#
# This file provides an example of how to use the ExampleService service.
#
# The following configuration properties are assumed to be defined:
# EXAMPLE_SERVICE_URL=<service base url>
# EXAMPLE_SERVICE_AUTH_TYPE=iam
# EXAMPLE_SERVICE_APIKEY=<IAM apikey>
# EXAMPLE_SERVICE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'example_service_v1.env'

example_service_service = None

config = None

# Variables to hold link values
get_resource_link = None


##############################################################################
# Start of Examples for Service: ExampleServiceV1
##############################################################################
# region
class TestExampleServiceV1Examples():
    """
    Example Test Class for ExampleServiceV1
    """

    @classmethod
    def setup_class(cls):
        global example_service_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            example_service_service = ExampleServiceV1.new_instance(
            )

            # end-common
            assert example_service_service is not None

            # Load the configuration
            global config
            config = read_external_sources(ExampleServiceV1.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_resource_example(self):
        """
        create_resource request example
        """
        try:
            print('\ncreate_resource() result:')
            # begin-create_resource

            resource = example_service_service.create_resource(
                name='The Hunt for Red October',
                tag='Book'
            ).get_result()

            print(json.dumps(resource, indent=2))

            # end-create_resource

            global get_resource_link
            get_resource_link = resource['resource_id']
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_resources_example(self):
        """
        list_resources request example
        """
        try:
            print('\nlist_resources() result:')
            # begin-list_resources

            resources = example_service_service.list_resources(
                limit=1
            ).get_result()

            print(json.dumps(resources, indent=2))

            # end-list_resources

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_example(self):
        """
        get_resource request example
        """
        try:
            print('\nget_resource() result:')
            # begin-get_resource

            resource = example_service_service.get_resource(
                resource_id=get_resource_link
            ).get_result()

            print(json.dumps(resource, indent=2))

            # end-get_resource

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_encoded_example(self):
        """
        get_resource_encoded request example
        """
        try:
            print('\nget_resource_encoded() result:')
            # begin-get_resource_encoded

            resource = example_service_service.get_resource_encoded(
                url_encoded_resource_id='url%3encoded%3resource%3id'
            ).get_result()

            print(json.dumps(resource, indent=2))

            # end-get_resource_encoded

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: ExampleServiceV1
##############################################################################
