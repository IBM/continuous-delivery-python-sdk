# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
Examples for CdToolchainV2
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_continuous_delivery.cd_toolchain_v2 import *

#
# This file provides an example of how to use the CD Toolchain service.
#
# The following configuration properties are assumed to be defined:
# CD_TOOLCHAIN_URL=<service base url>
# CD_TOOLCHAIN_AUTH_TYPE=iam
# CD_TOOLCHAIN_APIKEY=<IAM apikey>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = "cd_toolchain_v2.env"

cd_toolchain_service = None

config = None

# Variables to hold link values
tool_id_link = None
toolchain_id_link = None


##############################################################################
# Start of Examples for Service: CdToolchainV2
##############################################################################
# region
class TestCdToolchainV2Examples:
    """
    Example Test Class for CdToolchainV2
    """

    @classmethod
    def setup_class(cls):
        global cd_toolchain_service
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            # begin-common

            cd_toolchain_service = CdToolchainV2.new_instance()

            # end-common
            assert cd_toolchain_service is not None

            # Load the configuration
            global config
            config = read_external_sources(CdToolchainV2.DEFAULT_SERVICE_NAME)

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_create_toolchain_example(self):
        """
        create_toolchain request example
        """
        try:
            global toolchain_id_link
            print("\ncreate_toolchain() result:")
            # begin-create_toolchain

            response = cd_toolchain_service.create_toolchain(
                name="TestToolchainV2",
                resource_group_id="6a9a01f2cff54a7f966f803d92877123",
            )
            toolchain_post = response.get_result()

            print(json.dumps(toolchain_post, indent=2))

            # end-create_toolchain

            toolchain_id_link = toolchain_post["id"]
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_tool_example(self):
        """
        create_tool request example
        """
        try:
            global tool_id_link
            print("\ncreate_tool() result:")
            # begin-create_tool

            response = cd_toolchain_service.create_tool(
                toolchain_id=toolchain_id_link,
                tool_type_id="draservicebroker",
            )
            toolchain_tool_post = response.get_result()

            print(json.dumps(toolchain_tool_post, indent=2))

            # end-create_tool

            tool_id_link = toolchain_tool_post["id"]
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_toolchains_example(self):
        """
        list_toolchains request example
        """
        try:
            print("\nlist_toolchains() result:")
            # begin-list_toolchains

            all_results = []
            pager = ToolchainsPager(
                client=cd_toolchain_service,
                resource_group_id="6a9a01f2cff54a7f966f803d92877123",
                limit=10,
                name="TestToolchainV2",
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_toolchains
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_toolchain_by_id_example(self):
        """
        get_toolchain_by_id request example
        """
        try:
            print("\nget_toolchain_by_id() result:")
            # begin-get_toolchain_by_id

            response = cd_toolchain_service.get_toolchain_by_id(
                toolchain_id=toolchain_id_link,
            )
            toolchain = response.get_result()

            print(json.dumps(toolchain, indent=2))

            # end-get_toolchain_by_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_toolchain_example(self):
        """
        update_toolchain request example
        """
        try:
            print("\nupdate_toolchain() result:")
            # begin-update_toolchain

            toolchain_prototype_patch_model = {}

            response = cd_toolchain_service.update_toolchain(
                toolchain_id=toolchain_id_link,
                toolchain_prototype_patch=toolchain_prototype_patch_model,
            )
            toolchain_patch = response.get_result()

            print(json.dumps(toolchain_patch, indent=2))

            # end-update_toolchain

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_toolchain_event_example(self):
        """
        create_toolchain_event request example
        """
        try:
            print("\ncreate_toolchain_event() result:")
            # begin-create_toolchain_event

            response = cd_toolchain_service.create_toolchain_event(
                toolchain_id=toolchain_id_link,
                title="My-custom-event",
                description="This is my custom event",
                content_type="application/json",
            )
            toolchain_event_post = response.get_result()

            print(json.dumps(toolchain_event_post, indent=2))

            # end-create_toolchain_event

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_tools_example(self):
        """
        list_tools request example
        """
        try:
            print("\nlist_tools() result:")
            # begin-list_tools

            all_results = []
            pager = ToolsPager(
                client=cd_toolchain_service,
                toolchain_id=toolchain_id_link,
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_tools
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tool_by_id_example(self):
        """
        get_tool_by_id request example
        """
        try:
            print("\nget_tool_by_id() result:")
            # begin-get_tool_by_id

            response = cd_toolchain_service.get_tool_by_id(
                toolchain_id=toolchain_id_link,
                tool_id=tool_id_link,
            )
            toolchain_tool = response.get_result()

            print(json.dumps(toolchain_tool, indent=2))

            # end-get_tool_by_id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_tool_example(self):
        """
        update_tool request example
        """
        try:
            print("\nupdate_tool() result:")
            # begin-update_tool

            toolchain_tool_prototype_patch_model = {}

            response = cd_toolchain_service.update_tool(
                toolchain_id=toolchain_id_link,
                tool_id=tool_id_link,
                toolchain_tool_prototype_patch=toolchain_tool_prototype_patch_model,
            )
            toolchain_tool_patch = response.get_result()

            print(json.dumps(toolchain_tool_patch, indent=2))

            # end-update_tool

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tool_example(self):
        """
        delete_tool request example
        """
        try:
            # begin-delete_tool

            response = cd_toolchain_service.delete_tool(
                toolchain_id=toolchain_id_link,
                tool_id=tool_id_link,
            )

            # end-delete_tool
            print("\ndelete_tool() response status code: ", response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_toolchain_example(self):
        """
        delete_toolchain request example
        """
        try:
            # begin-delete_toolchain

            response = cd_toolchain_service.delete_toolchain(
                toolchain_id=toolchain_id_link,
            )

            # end-delete_toolchain
            print(
                "\ndelete_toolchain() response status code: ",
                response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: CdToolchainV2
##############################################################################
