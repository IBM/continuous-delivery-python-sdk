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
Integration Tests for CdTektonPipelineV2
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from environs import Env
from ibm_continuous_delivery.cd_toolchain_v2 import *
from ibm_continuous_delivery.cd_tekton_pipeline_v2 import *
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Config file name
config_file = 'cd_tekton_pipeline_v2.env'

# Variables to hold link values
toolchain_id_link = None
pipeline_tool_id_link = None
github_tool_id_link = None
definition_id_link = None
trigger_id_link = None
trigger_prop_name_link = None
pipeline_run_id_link = None
rerun_id_link = None
env = Env()

class TestCdTektonPipelineV2():
    """
    Integration Test Class for CdTektonPipelineV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            env.read_env(config_file, recurse=False)
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # Create toolchain service
            cls.cd_toolchain_service = CdToolchainV2.new_instance()
            assert cls.cd_toolchain_service is not None
            cls.config = read_external_sources(CdToolchainV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None
            
            # Create pipeline service
            cls.cd_pipeline_service = CdTektonPipelineV2.new_instance()
            assert cls.cd_pipeline_service is not None
            cls.config = read_external_sources(CdTektonPipelineV2.DEFAULT_SERVICE_NAME)
            print('\n Setup complete.', flush=True)


    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_toolchain(self):
        print('\n Create toolchain.', flush=True)
        global toolchain_id_link
        response = self.cd_toolchain_service.create_toolchain(
            name='PythonPipelineSDKTest',
            resource_group_id=env("CD_TEKTON_PIPELINE_RESOURCE_GROUP_ID"),
            description='A sample toolchain to test the pipeline API'
        )
        assert response.get_status_code() == 201
        toolchain_post = response.get_result()
        assert toolchain_post is not None
        toolchain_id_link = toolchain_post['id']

    @needscredentials
    def test_create_github_tool(self):
        print('\n Create github tool.', flush=True)
        global github_tool_id_link
        response = self.cd_toolchain_service.create_tool(
            toolchain_id=toolchain_id_link,
            tool_type_id='githubconsolidated',
            name='app-repo-1',
            parameters={
                'enable_traceability': False,
                'has_issues': False,
                'repo_url': 'https://github.com/open-toolchain/hello-tekton.git',
                'type': 'link'
            }
        )
        assert response.get_status_code() == 201
        toolchain_github_tool_post = response.get_result()
        assert toolchain_github_tool_post is not None
        github_tool_id_link = toolchain_github_tool_post['id']

    @needscredentials
    def test_create_pipeline_tool(self):
        print('\n Create pipeline tool.', flush=True)
        global pipeline_tool_id_link
        response = self.cd_toolchain_service.create_tool(
            toolchain_id=toolchain_id_link,
            tool_type_id='pipeline',
            name='pipeline-node-test',
            parameters={ 'type': 'tekton' }
        )
        assert response.get_status_code() == 201
        toolchain_pipeline_tool_post = response.get_result()
        assert toolchain_pipeline_tool_post is not None
        pipeline_tool_id_link = toolchain_pipeline_tool_post['id']
        print(f'\n pipeline_tool_id_link: {pipeline_tool_id_link}')
        assert pipeline_tool_id_link is not None

    @needscredentials
    def test_create_tekton_pipeline(self):
        print('\n Create Tekton Pipeline.', flush=True)
        # Construct a dict representation of a WorkerIdentity model
        worker_identity_model = {
            'id': 'public',
        }
        response = self.cd_pipeline_service.create_tekton_pipeline(
            id=pipeline_tool_id_link,
            enable_notifications=False,
            enable_partial_cloning=False,
            worker=worker_identity_model
        )
        assert response.get_status_code() == 201
        tekton_pipeline = response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_get_tekton_pipeline(self):
        print('\n Get Tekton Pipeline.', flush=True)
        response = self.cd_pipeline_service.get_tekton_pipeline(
            id=pipeline_tool_id_link
        )
        assert response.get_status_code() == 200
        tekton_pipeline = response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_update_tekton_pipeline(self):
        print('\n Update Tekton Pipeline.', flush=True)
        # Construct a dict representation of a TektonPipelinePatch model
        tekton_pipeline_patch_model = {
            'enable_notifications': True,
            'enable_partial_cloning': True,
        }
        response = self.cd_pipeline_service.update_tekton_pipeline(
            id=pipeline_tool_id_link,
            tekton_pipeline_patch=tekton_pipeline_patch_model
        )
        assert response.get_status_code() == 200
        tekton_pipeline = response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_create_tekton_pipeline_definition(self):
        print('\n Create definition.', flush=True)
        global definition_id_link
        # Construct a dict representation of a DefinitionSourceProperties model
        definition_source_properties_model = {
            'url': 'https://github.com/open-toolchain/hello-tekton.git',
            'branch': 'master',
            'path': '.tekton',
        }
        # Construct a dict representation of a DefinitionSource model
        definition_source_model = {
            'type': 'git',
            'properties': definition_source_properties_model,
        }
        response = self.cd_pipeline_service.create_tekton_pipeline_definition(
            pipeline_id=pipeline_tool_id_link,
            source=definition_source_model
        )
        assert response.get_status_code() == 201
        definition = response.get_result()
        assert definition is not None
        assert definition["source"] is not None
        assert definition["href"] is not None
        assert definition["source"]["type"] == 'git'
        assert definition["source"]["properties"] is not None
        assert definition["source"]["properties"]["tool"] is not None
        assert definition["source"]["properties"]["path"] == '.tekton'
        assert definition["source"]["properties"]["url"] == 'https://github.com/open-toolchain/hello-tekton.git'
        assert definition["source"]["properties"]["branch"] == 'master'
        assert definition["id"] is not None
        definition_id_link = definition['id']
        assert definition_id_link is not None

    @needscredentials
    def test_get_tekton_pipeline_definition(self):
        print('\n Get definition.', flush=True)
        response = self.cd_pipeline_service.get_tekton_pipeline_definition(
            pipeline_id=pipeline_tool_id_link,
            definition_id=definition_id_link
        )
        assert response.get_status_code() == 200
        definition = response.get_result()
        assert definition is not None

    @needscredentials
    def test_list_tekton_pipeline_definitions(self):
        print('\n List definitions.', flush=True)
        response = self.cd_pipeline_service.list_tekton_pipeline_definitions(
            pipeline_id=pipeline_tool_id_link
        )
        assert response.get_status_code() == 200
        definitions_collection = response.get_result()
        assert definitions_collection is not None
        assert definitions_collection["definitions"][0] is not None
        assert definitions_collection["definitions"][0]["source"] is not None
        assert definitions_collection["definitions"][0]["href"] is not None
        assert definitions_collection["definitions"][0]["source"]["type"] == 'git'
        assert definitions_collection["definitions"][0]["source"]["properties"] is not None
        assert definitions_collection["definitions"][0]["source"]["properties"]["tool"] is not None
        assert definitions_collection["definitions"][0]["source"]["properties"]["path"] == '.tekton'
        assert definitions_collection["definitions"][0]["source"]["properties"]["url"] == 'https://github.com/open-toolchain/hello-tekton.git'
        assert definitions_collection["definitions"][0]["source"]["properties"]["branch"] == 'master'
        assert definitions_collection["definitions"][0]["id"] is not None

    @needscredentials
    def test_create_tekton_pipeline_properties(self):
        print('\n Create property.', flush=True)
        response = self.cd_pipeline_service.create_tekton_pipeline_properties(
            pipeline_id=pipeline_tool_id_link,
            name='prop1',
            type='text',
            value='prop1Value',
        )
        assert response.get_status_code() == 201
        property = response.get_result()
        assert property is not None
        assert property["name"] == 'prop1'
        assert property["type"] == 'text'
        assert property["value"] == 'prop1Value'

    @needscredentials
    def test_get_tekton_pipeline_property(self):
        print('\n Get property definition.', flush=True)
        response = self.cd_pipeline_service.get_tekton_pipeline_property(
            pipeline_id=pipeline_tool_id_link,
            property_name='prop1'
        )
        assert response.get_status_code() == 200
        property = response.get_result()
        assert property is not None

    @needscredentials
    def test_replace_tekton_pipeline_property(self):
        print('\n Update property.', flush=True)
        response = self.cd_pipeline_service.replace_tekton_pipeline_property(
            pipeline_id=pipeline_tool_id_link,
            property_name='prop1',
            name='prop1',
            type='text',
            value='prop1Updated',
        )
        assert response.get_status_code() == 200
        property = response.get_result()
        assert property is not None
        assert property["name"] == 'prop1'
        assert property["type"] == 'text'
        assert property["value"] == 'prop1Updated'

    @needscredentials
    def test_list_tekton_pipeline_properties(self):
        print('\n List properties.', flush=True)
        response = self.cd_pipeline_service.list_tekton_pipeline_properties(
            pipeline_id=pipeline_tool_id_link,
            sort='name'
        )
        assert response.get_status_code() == 200
        properties_collection = response.get_result()
        assert properties_collection is not None
        assert properties_collection is not None
        assert properties_collection["properties"][0] is not None
        assert properties_collection["properties"][0]["name"] == 'prop1'
        assert properties_collection["properties"][0]["type"] == 'text'
        assert properties_collection["properties"][0]["value"] == 'prop1Updated'
        assert properties_collection["properties"][0]["href"] is not None

    @needscredentials
    def test_create_tekton_pipeline_trigger(self):
        print('\n Create trigger.', flush=True)
        global trigger_id_link
        response = self.cd_pipeline_service.create_tekton_pipeline_trigger(
            pipeline_id=pipeline_tool_id_link,
            type='manual',
            name='Manual1',
            event_listener='listener',
            tags=['tag1'],
        )
        assert response.get_status_code() == 201
        trigger = response.get_result()
        assert trigger is not None
        assert trigger["id"] is not None
        trigger_id_link = trigger['id']
        assert trigger["name"] == 'Manual1'
        assert trigger["type"] == 'manual'
        assert trigger["event_listener"] == 'listener'
        assert trigger["enabled"] == True
        assert trigger["href"] is not None
        assert trigger["tags"] is not None

    @needscredentials
    def test_get_tekton_pipeline_trigger(self):
        print('\n Get trigger.', flush=True)
        response = self.cd_pipeline_service.get_tekton_pipeline_trigger(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link
        )
        assert response.get_status_code() == 200
        trigger = response.get_result()
        assert trigger is not None
        assert trigger["id"] is not None
        assert trigger["name"] == 'Manual1'
        assert trigger["type"] == 'manual'
        assert trigger["event_listener"] == 'listener'
        assert trigger["enabled"] == True
        assert trigger["href"] is not None
        assert trigger["tags"] is not None

    @needscredentials
    def test_update_tekton_pipeline_trigger(self):
        print('\n Update trigger.', flush=True)
        # Construct a dict representation of a TriggerPatch model
        trigger_patch_model = {
            'type': 'manual',
            'name': 'start-deploy',
            'tags': ['testString'],
            'max_concurrent_runs': 2,
        }
        response = self.cd_pipeline_service.update_tekton_pipeline_trigger(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link,
            trigger_patch=trigger_patch_model
        )
        assert response.get_status_code() == 200
        trigger = response.get_result()
        assert trigger is not None
        assert trigger["id"] is not None
        assert trigger["name"] == 'start-deploy'
        assert trigger["type"] == 'manual'
        assert trigger["event_listener"] == 'listener'
        assert trigger["max_concurrent_runs"] == 2
        assert trigger["enabled"] == True
        assert trigger["href"] is not None
        assert trigger["tags"] is not None

    @needscredentials
    def test_duplicate_tekton_pipeline_trigger(self):
        print('\n Duplicate trigger.', flush=True)
        response = self.cd_pipeline_service.duplicate_tekton_pipeline_trigger(
            pipeline_id=pipeline_tool_id_link,
            source_trigger_id=trigger_id_link,
            name='duplicateTrigger'
        )
        assert response.get_status_code() == 201
        trigger = response.get_result()
        assert trigger is not None
        assert trigger["id"] is not None
        assert trigger["name"] == 'duplicateTrigger'
        assert trigger["type"] == 'manual'
        assert trigger["event_listener"] == 'listener'
        assert trigger["enabled"] == True
        assert trigger["href"] is not None
        assert trigger["tags"] is not None

    @needscredentials
    def test_list_tekton_pipeline_triggers(self):
        print('\n List triggers.', flush=True)
        response = self.cd_pipeline_service.list_tekton_pipeline_triggers(
            pipeline_id=pipeline_tool_id_link,
            type='manual'
        )
        assert response.get_status_code() == 200
        triggers_collection = response.get_result()
        assert triggers_collection is not None
        assert triggers_collection["triggers"][0] is not None
        assert triggers_collection["triggers"][0]["href"] is not None
        assert triggers_collection["triggers"][0]["id"] is not None
        assert triggers_collection["triggers"][0]["name"] == 'start-deploy'
        assert triggers_collection["triggers"][0]["type"] == 'manual'
        assert triggers_collection["triggers"][0]["event_listener"] == 'listener'
        assert triggers_collection["triggers"][0]["max_concurrent_runs"] == 2
        assert triggers_collection["triggers"][0]["enabled"] == True
        assert triggers_collection["triggers"][0]["href"] is not None
        assert triggers_collection["triggers"][0]["tags"] is not None

    @needscredentials
    def test_create_tekton_pipeline_trigger_properties(self):
        print('\n Create trigger property.', flush=True)
        global trigger_prop_name_link
        response = self.cd_pipeline_service.create_tekton_pipeline_trigger_properties(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link,
            name='trigProp1',
            type='text',
            value='testValue'
        )
        assert response.get_status_code() == 201
        trigger_property = response.get_result()
        trigger_prop_name_link = trigger_property['name']
        assert trigger_property is not None
        assert trigger_property["name"] == 'trigProp1'
        assert trigger_property["type"] == 'text'
        assert trigger_property["value"] == 'testValue'

    @needscredentials
    def test_get_tekton_pipeline_trigger_property(self):
        print('\n Get trigger property.', flush=True)
        response = self.cd_pipeline_service.get_tekton_pipeline_trigger_property(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link,
            property_name='trigProp1'
        )
        assert response.get_status_code() == 200
        trigger_property = response.get_result()
        assert trigger_property is not None
        assert trigger_property["name"] == 'trigProp1'
        assert trigger_property["type"] == 'text'
        assert trigger_property["value"] == 'testValue'

    @needscredentials
    def test_replace_tekton_pipeline_trigger_property(self):
        print('\n Update trigger property.', flush=True)
        response = self.cd_pipeline_service.replace_tekton_pipeline_trigger_property(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link,
            property_name='trigProp1',
            name='trigProp1',
            type='text',
            value='editedValue'
        )
        assert response.get_status_code() == 200
        trigger_property = response.get_result()
        assert trigger_property is not None
        assert trigger_property["name"] == 'trigProp1'
        assert trigger_property["type"] == 'text'
        assert trigger_property["value"] == 'editedValue'

    @needscredentials
    def test_list_tekton_pipeline_trigger_properties(self):
        print('\n List trigger properties.', flush=True)
        response = self.cd_pipeline_service.list_tekton_pipeline_trigger_properties(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link,
            name='trigProp1'
        )
        assert response.get_status_code() == 200
        trigger_properties_collection = response.get_result()
        assert trigger_properties_collection is not None
        assert trigger_properties_collection["properties"][0] is not None
        assert trigger_properties_collection["properties"][0]["href"] is not None
        assert trigger_properties_collection["properties"][0]["name"] == 'trigProp1'
        assert trigger_properties_collection["properties"][0]["type"] == 'text'
        assert trigger_properties_collection["properties"][0]["value"] == 'editedValue'

    @needscredentials
    def test_create_tekton_pipeline_run(self):
        print('\n Create PipelineRun.', flush=True)
        global pipeline_run_id_link
        # Construct a dict representation of a Trigger model
        trigger_model = {
            'name': 'start-deploy',
            'properties': {'addedProp1': 'addedProp123'},
            'secure_properties': {'addedSecProp1': 'addedSecProp123'},
            'headers': {'source':'api'},
            'body': {'message':'hello world','enable':'true','detail':{'name':'example'}},
        }
        response = self.cd_pipeline_service.create_tekton_pipeline_run(
            pipeline_id=pipeline_tool_id_link,
            trigger=trigger_model
        )
        assert response.get_status_code() == 201
        pipeline_run = response.get_result()
        assert pipeline_run is not None
        assert pipeline_run["id"] is not None
        pipeline_run_id_link = pipeline_run["id"]
        assert pipeline_run["href"] is not None
        assert pipeline_run["run_url"] is not None
        assert pipeline_run["status"] is not None
        assert pipeline_run["listener_name"] == 'listener'
        assert pipeline_run["trigger"] is not None
        assert pipeline_run["trigger"]["name"] == 'start-deploy'
        assert pipeline_run["type"] == 'pipeline_run'
        assert pipeline_run["properties"] is not None
        assert pipeline_run["properties"][0]["name"] == 'addedProp1'
        assert pipeline_run["properties"][1]["name"] == 'addedSecProp1'
        assert pipeline_run["properties"][2]["name"] == 'trigProp1'
        assert pipeline_run["properties"][3]["name"] == 'prop1'

    @needscredentials
    def test_get_tekton_pipeline_run(self):
        print('\n Get PipelineRun.', flush=True)
        response = self.cd_pipeline_service.get_tekton_pipeline_run(
            pipeline_id=pipeline_tool_id_link,
            id=pipeline_run_id_link
        )
        assert response.get_status_code() == 200
        pipeline_run = response.get_result()
        assert pipeline_run is not None
        assert pipeline_run["id"] is not None
        assert pipeline_run["href"] is not None
        assert pipeline_run["run_url"] is not None
        assert pipeline_run["status"] is not None
        assert pipeline_run["listener_name"] == 'listener'
        assert pipeline_run["trigger"] is not None
        assert pipeline_run["trigger"]["name"] == 'start-deploy'
        assert pipeline_run["type"] == 'pipeline_run'
        assert pipeline_run["properties"] is not None
        assert pipeline_run["properties"][0]["name"] == 'addedProp1'
        assert pipeline_run["properties"][1]["name"] == 'addedSecProp1'
        assert pipeline_run["properties"][2]["name"] == 'trigProp1'
        assert pipeline_run["properties"][3]["name"] == 'prop1'

    @needscredentials
    def test_rerun_tekton_pipeline_run(self):
        print('\n Rerun PipelineRun.', flush=True)
        global rerun_id_link
        response = self.cd_pipeline_service.rerun_tekton_pipeline_run(
            pipeline_id=pipeline_tool_id_link,
            id=pipeline_run_id_link
        )
        assert response.get_status_code() == 201
        pipeline_rerun = response.get_result()
        assert pipeline_rerun is not None
        assert pipeline_rerun["id"] is not None
        rerun_id_link = pipeline_rerun["id"]
        assert pipeline_rerun["href"] is not None
        assert pipeline_rerun["run_url"] is not None
        assert pipeline_rerun["status"] is not None
        assert pipeline_rerun["listener_name"] == 'listener'
        assert pipeline_rerun["trigger"] is not None
        assert pipeline_rerun["trigger"]["name"] == 'start-deploy'
        assert pipeline_rerun["type"] == 'pipeline_run'
        assert pipeline_rerun["properties"] is not None
        assert pipeline_rerun["properties"][0]["name"] == 'addedProp1'
        assert pipeline_rerun["properties"][1]["name"] == 'addedSecProp1'
        assert pipeline_rerun["properties"][2]["name"] == 'trigProp1'
        assert pipeline_rerun["properties"][3]["name"] == 'prop1'

    @needscredentials
    def test_list_tekton_pipeline_runs(self):
        print('\n List PipelineRuns.', flush=True)
        response = self.cd_pipeline_service.list_tekton_pipeline_runs(
            pipeline_id=pipeline_tool_id_link,
            limit=5
        )
        assert response.get_status_code() == 200
        pipeline_runs_collection = response.get_result()
        assert pipeline_runs_collection is not None
        assert pipeline_runs_collection["pipeline_runs"] is not None
        assert len(pipeline_runs_collection["pipeline_runs"]) == 2

    @needscredentials
    def test_list_tekton_pipeline_runs_with_pager(self):
        all_results = []
        # Test get_next().
        pager = TektonPipelineRunsPager(
            client=self.cd_pipeline_service,
            pipeline_id=pipeline_tool_id_link,
            limit=1,
            trigger_name='start-deploy'
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        # Test get_all().
        pager = TektonPipelineRunsPager(
            client=self.cd_pipeline_service,
            pipeline_id=pipeline_tool_id_link,
            limit=10,
            trigger_name='start-deploy',
        )
        all_items = pager.get_all()
        assert all_items is not None
        assert len(all_results) == len(all_items)
        print(f'\n list_tekton_pipeline_runs() returned a total of {len(all_results)} items(s) using TektonPipelineRunsPager.')

    # @needscredentials
    # def test_get_tekton_pipeline_run_logs(self):
    #     global run_log_id_link
    #     response = self.cd_pipeline_service.get_tekton_pipeline_run_logs(
    #         pipeline_id=pipeline_tool_id_link,
    #         id=pipeline_run_id_link
    #     )
    #     assert response.get_status_code() == 200
    #     logs_collection = response.get_result()
    #     assert logs_collection is not None
    #     print(f'\n logs_collection: {logs_collection}')
    #     print(f'\n len(logs_collection): {len(logs_collection)}')

    # @needscredentials
    # def test_get_tekton_pipeline_run_log_content(self):
    #     response = self.cd_pipeline_service.get_tekton_pipeline_run_log_content(
    #         pipeline_id=pipeline_tool_id_link,
    #         pipeline_run_id='bf4b3abd-0c93-416b-911e-9cf42f1a1085',
    #         id=pipeline_tool_id_link
    #     )
    #     assert response.get_status_code() == 200
    #     step_log = response.get_result()
    #     assert step_log is not None

    @needscredentials
    def test_delete_tekton_pipeline_run(self):
        print('\n Delete PipelineRun.', flush=True)
        response = self.cd_pipeline_service.delete_tekton_pipeline_run(
            pipeline_id=pipeline_tool_id_link,
            id=pipeline_run_id_link
        )
        assert response.get_status_code() == 204
        print(f'\n pipeline_run deleted')

    @needscredentials
    def test_delete_tekton_pipeline_definition(self):
        print('\n Delete definition.', flush=True)
        response = self.cd_pipeline_service.delete_tekton_pipeline_definition(
            pipeline_id=pipeline_tool_id_link,
            definition_id=definition_id_link
        )
        assert response.get_status_code() == 204
        print(f'\n definition deleted')

    @needscredentials
    def test_delete_tekton_pipeline_property(self):
        print('\n Delete property.', flush=True)
        response = self.cd_pipeline_service.delete_tekton_pipeline_property(
            pipeline_id=pipeline_tool_id_link,
            property_name='prop1'
        )
        assert response.get_status_code() == 204
        print(f'\n property deleted')

    @needscredentials
    def test_delete_tekton_pipeline_trigger_property(self):
        print('\n Delete trigger property.', flush=True)
        response = self.cd_pipeline_service.delete_tekton_pipeline_trigger_property(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link,
            property_name=trigger_prop_name_link
        )
        assert response.get_status_code() == 204
        print(f'\n trigger property deleted')

    @needscredentials
    def test_delete_tekton_pipeline_trigger(self):
        print('\n Delete trigger.', flush=True)
        response = self.cd_pipeline_service.delete_tekton_pipeline_trigger(
            pipeline_id=pipeline_tool_id_link,
            trigger_id=trigger_id_link
        )
        assert response.get_status_code() == 204
        print(f'\n trigger deleted')

    @needscredentials
    def test_delete_tekton_pipeline(self):
        print('\n Delete tekton pipeline.', flush=True)
        response = self.cd_pipeline_service.delete_tekton_pipeline(
            id=pipeline_tool_id_link
        )
        assert response.get_status_code() == 204
        print(f'\n pipeline deleted')

    @needscredentials
    def test_delete_toolchain(self):
        print('\n Delete toolchain.', flush=True)
        response = self.cd_toolchain_service.delete_toolchain(
            toolchain_id=toolchain_id_link
        )
        assert response.get_status_code() == 204
        print(f'\n toolchain deleted')
        print(f'\n All tests complete')
