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
Integration Tests for CdToolchainV2
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_continuous_delivery.cd_toolchain_v2 import *

# Config file name
config_file = "cd_toolchain_v2.env"

# Variables to hold link values
tool_id_link = None
toolchain_id_link = None


class TestCdToolchainV2:
    """
    Integration Test Class for CdToolchainV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            cls.cd_toolchain_service = CdToolchainV2.new_instance()
            assert cls.cd_toolchain_service is not None

            cls.config = read_external_sources(CdToolchainV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.cd_toolchain_service.enable_retries()

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_create_toolchain(self):
        global toolchain_id_link

        response = self.cd_toolchain_service.create_toolchain(
            name="TestToolchainV2",
            resource_group_id="6a9a01f2cff54a7f966f803d92877123",
            description="A sample toolchain to test the API",
        )

        assert response.get_status_code() == 201
        toolchain_post = response.get_result()
        assert toolchain_post is not None

        toolchain_id_link = toolchain_post["id"]

    @needscredentials
    def test_create_tool(self):
        global tool_id_link

        response = self.cd_toolchain_service.create_tool(
            toolchain_id=toolchain_id_link,
            tool_type_id="draservicebroker",
            name="testString",
            parameters={"anyKey": "anyValue"},
        )

        assert response.get_status_code() == 201
        toolchain_tool_post = response.get_result()
        assert toolchain_tool_post is not None

        tool_id_link = toolchain_tool_post["id"]

    @needscredentials
    def test_list_toolchains(self):
        response = self.cd_toolchain_service.list_toolchains(
            resource_group_id="6a9a01f2cff54a7f966f803d92877123",
            limit=20,
            start="testString",
            name="TestToolchainV2",
        )

        assert response.get_status_code() == 200
        toolchain_collection = response.get_result()
        assert toolchain_collection is not None

    @needscredentials
    def test_list_toolchains_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ToolchainsPager(
            client=self.cd_toolchain_service,
            resource_group_id="6a9a01f2cff54a7f966f803d92877123",
            limit=10,
            name="TestToolchainV2",
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ToolchainsPager(
            client=self.cd_toolchain_service,
            resource_group_id="6a9a01f2cff54a7f966f803d92877123",
            limit=10,
            name="TestToolchainV2",
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f"\nlist_toolchains() returned a total of {len(all_results)} items(s) using ToolchainsPager.")

    @needscredentials
    def test_get_toolchain_by_id(self):
        response = self.cd_toolchain_service.get_toolchain_by_id(
            toolchain_id=toolchain_id_link,
        )

        assert response.get_status_code() == 200
        toolchain = response.get_result()
        assert toolchain is not None

    @needscredentials
    def test_update_toolchain(self):
        # Construct a dict representation of a ToolchainPrototypePatch model
        toolchain_prototype_patch_model = {
            "name": "newToolchainName",
            "description": "New toolchain description",
        }

        response = self.cd_toolchain_service.update_toolchain(
            toolchain_id=toolchain_id_link,
            toolchain_prototype_patch=toolchain_prototype_patch_model,
        )

        assert response.get_status_code() == 200
        toolchain_patch = response.get_result()
        assert toolchain_patch is not None

    @needscredentials
    def test_create_toolchain_event(self):
        # Construct a dict representation of a ToolchainEventPrototypeDataApplicationJson model
        toolchain_event_prototype_data_application_json_model = {
            "content": {
                "customKey1": "myCustomData",
                "customKey2": 123,
                "customKey3": {"nestedKey": "moreData"},
            },
        }
        # Construct a dict representation of a ToolchainEventPrototypeData model
        toolchain_event_prototype_data_model = {
            "application_json": toolchain_event_prototype_data_application_json_model,
            "text_plain": "This event is dispatched because the pipeline failed",
        }

        response = self.cd_toolchain_service.create_toolchain_event(
            toolchain_id=toolchain_id_link,
            title="My-custom-event",
            description="This is my custom event",
            content_type="application/json",
            data=toolchain_event_prototype_data_model,
        )

        assert response.get_status_code() == 200
        toolchain_event_post = response.get_result()
        assert toolchain_event_post is not None

    @needscredentials
    def test_list_tools(self):
        response = self.cd_toolchain_service.list_tools(
            toolchain_id=toolchain_id_link,
            limit=20,
            start="testString",
        )

        assert response.get_status_code() == 200
        toolchain_tool_collection = response.get_result()
        assert toolchain_tool_collection is not None

    @needscredentials
    def test_list_tools_with_pager(self):
        all_results = []

        # Test get_next().
        pager = ToolsPager(
            client=self.cd_toolchain_service,
            toolchain_id=toolchain_id_link,
            limit=10,
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = ToolsPager(
            client=self.cd_toolchain_service,
            toolchain_id=toolchain_id_link,
            limit=10,
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f"\nlist_tools() returned a total of {len(all_results)} items(s) using ToolsPager.")

    @needscredentials
    def test_get_tool_by_id(self):
        response = self.cd_toolchain_service.get_tool_by_id(
            toolchain_id=toolchain_id_link,
            tool_id=tool_id_link,
        )

        assert response.get_status_code() == 200
        toolchain_tool = response.get_result()
        assert toolchain_tool is not None

    @needscredentials
    def test_update_tool(self):
        # Construct a dict representation of a ToolchainToolPrototypePatch model
        toolchain_tool_prototype_patch_model = {
            "name": "MyTool",
            "tool_type_id": "draservicebroker",
            "parameters": {"anyKey": "anyValue"},
        }

        response = self.cd_toolchain_service.update_tool(
            toolchain_id=toolchain_id_link,
            tool_id=tool_id_link,
            toolchain_tool_prototype_patch=toolchain_tool_prototype_patch_model,
        )

        assert response.get_status_code() == 200
        toolchain_tool_patch = response.get_result()
        assert toolchain_tool_patch is not None

    @needscredentials
    def test_delete_tool(self):
        response = self.cd_toolchain_service.delete_tool(
            toolchain_id=toolchain_id_link,
            tool_id=tool_id_link,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_toolchain(self):
        response = self.cd_toolchain_service.delete_toolchain(
            toolchain_id=toolchain_id_link,
        )

        assert response.get_status_code() == 204
