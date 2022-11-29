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
Integration Tests for CdTektonPipelineV2
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from ibm_continuous_delivery.cd_tekton_pipeline_v2 import *

# Config file name
config_file = 'cd_tekton_pipeline_v2.env'

class TestCdTektonPipelineV2():
    """
    Integration Test Class for CdTektonPipelineV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.cd_tekton_pipeline_service = CdTektonPipelineV2.new_instance(
            )
            assert cls.cd_tekton_pipeline_service is not None

            cls.config = read_external_sources(
                CdTektonPipelineV2.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.cd_tekton_pipeline_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_tekton_pipeline(self):

        # Construct a dict representation of a WorkerIdentity model
        worker_identity_model = {
            'id': 'public',
        }

        response = self.cd_tekton_pipeline_service.create_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            enable_notifications=False,
            enable_partial_cloning=False,
            worker=worker_identity_model
        )

        assert response.get_status_code() == 201
        tekton_pipeline = response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_get_tekton_pipeline(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert response.get_status_code() == 200
        tekton_pipeline = response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_update_tekton_pipeline(self):

        # Construct a dict representation of a WorkerIdentity model
        worker_identity_model = {
            'id': 'public',
        }

        # Construct a dict representation of a TektonPipelinePatch model
        tekton_pipeline_patch_model = {
            'enable_notifications': True,
            'enable_partial_cloning': True,
            'worker': worker_identity_model,
        }

        response = self.cd_tekton_pipeline_service.update_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            tekton_pipeline_patch=tekton_pipeline_patch_model
        )

        assert response.get_status_code() == 200
        tekton_pipeline = response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_list_tekton_pipeline_runs(self):

        response = self.cd_tekton_pipeline_service.list_tekton_pipeline_runs(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            start='testString',
            limit=1,
            status='succeeded',
            trigger_name='manual-trigger'
        )

        assert response.get_status_code() == 200
        pipeline_runs_collection = response.get_result()
        assert pipeline_runs_collection is not None

    @needscredentials
    def test_list_tekton_pipeline_runs_with_pager(self):
        all_results = []

        # Test get_next().
        pager = TektonPipelineRunsPager(
            client=self.cd_tekton_pipeline_service,
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            limit=10,
            status='succeeded',
            trigger_name='manual-trigger',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)

        # Test get_all().
        pager = TektonPipelineRunsPager(
            client=self.cd_tekton_pipeline_service,
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            limit=10,
            status='succeeded',
            trigger_name='manual-trigger',
        )
        all_items = pager.get_all()
        assert all_items is not None

        assert len(all_results) == len(all_items)
        print(f'\nlist_tekton_pipeline_runs() returned a total of {len(all_results)} items(s) using TektonPipelineRunsPager.')

    @needscredentials
    def test_create_tekton_pipeline_run(self):

        # Construct a dict representation of a Property model
        property_model = {
            'name': 'testString',
            'value': 'testString',
            'enum': ['testString'],
            'type': 'secure',
            'path': 'testString',
        }

        response = self.cd_tekton_pipeline_service.create_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_name='Generic Webhook Trigger - 0',
            trigger_properties=[property_model],
            secure_trigger_properties=[property_model],
            trigger_headers={'source':'api'},
            trigger_body={'message':'hello world','enable':'true','detail':{'name':'example'}}
        )

        assert response.get_status_code() == 201
        pipeline_run = response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_get_tekton_pipeline_run(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            includes='definitions'
        )

        assert response.get_status_code() == 200
        pipeline_run = response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_cancel_tekton_pipeline_run(self):

        response = self.cd_tekton_pipeline_service.cancel_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            force=True
        )

        assert response.get_status_code() == 202
        pipeline_run = response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_rerun_tekton_pipeline_run(self):

        response = self.cd_tekton_pipeline_service.rerun_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert response.get_status_code() == 201
        pipeline_run = response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_get_tekton_pipeline_run_logs(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline_run_logs(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert response.get_status_code() == 200
        logs_collection = response.get_result()
        assert logs_collection is not None

    @needscredentials
    def test_get_tekton_pipeline_run_log_content(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline_run_log_content(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            pipeline_run_id='bf4b3abd-0c93-416b-911e-9cf42f1a1085',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert response.get_status_code() == 200
        step_log = response.get_result()
        assert step_log is not None

    @needscredentials
    def test_list_tekton_pipeline_definitions(self):

        response = self.cd_tekton_pipeline_service.list_tekton_pipeline_definitions(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert response.get_status_code() == 200
        definitions_collection = response.get_result()
        assert definitions_collection is not None

    @needscredentials
    def test_create_tekton_pipeline_definition(self):

        # Construct a dict representation of a DefinitionSourcePropertiesTool model
        definition_source_properties_tool_model = {
            'id': 'testString',
        }

        # Construct a dict representation of a DefinitionSourceProperties model
        definition_source_properties_model = {
            'url': 'https://github.com/open-toolchain/hello-tekton.git',
            'branch': 'master',
            'tag': 'testString',
            'path': '.tekton',
            'tool': definition_source_properties_tool_model,
        }

        # Construct a dict representation of a DefinitionSource model
        definition_source_model = {
            'type': 'git',
            'properties': definition_source_properties_model,
        }

        response = self.cd_tekton_pipeline_service.create_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            source=definition_source_model
        )

        assert response.get_status_code() == 201
        definition = response.get_result()
        assert definition is not None

    @needscredentials
    def test_get_tekton_pipeline_definition(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
        )

        assert response.get_status_code() == 200
        definition = response.get_result()
        assert definition is not None

    @needscredentials
    def test_replace_tekton_pipeline_definition(self):

        # Construct a dict representation of a DefinitionSourcePropertiesTool model
        definition_source_properties_tool_model = {
            'id': 'testString',
        }

        # Construct a dict representation of a DefinitionSourceProperties model
        definition_source_properties_model = {
            'url': 'testString',
            'branch': 'testString',
            'tag': 'testString',
            'path': 'testString',
            'tool': definition_source_properties_tool_model,
        }

        # Construct a dict representation of a DefinitionSource model
        definition_source_model = {
            'type': 'testString',
            'properties': definition_source_properties_model,
        }

        response = self.cd_tekton_pipeline_service.replace_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada',
            source=definition_source_model
        )

        assert response.get_status_code() == 200
        definition = response.get_result()
        assert definition is not None

    @needscredentials
    def test_list_tekton_pipeline_properties(self):

        response = self.cd_tekton_pipeline_service.list_tekton_pipeline_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            name='prod',
            type=['secure', 'text'],
            sort='name'
        )

        assert response.get_status_code() == 200
        properties_collection = response.get_result()
        assert properties_collection is not None

    @needscredentials
    def test_create_tekton_pipeline_properties(self):

        response = self.cd_tekton_pipeline_service.create_tekton_pipeline_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            name='prop1',
            type='text',
            value='https://github.com/open-toolchain/hello-tekton.git',
            enum=['testString'],
            path='testString'
        )

        assert response.get_status_code() == 201
        property = response.get_result()
        assert property is not None

    @needscredentials
    def test_get_tekton_pipeline_property(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            property_name='debug-pipeline'
        )

        assert response.get_status_code() == 200
        property = response.get_result()
        assert property is not None

    @needscredentials
    def test_replace_tekton_pipeline_property(self):

        response = self.cd_tekton_pipeline_service.replace_tekton_pipeline_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            property_name='debug-pipeline',
            name='prop1',
            type='text',
            value='https://github.com/open-toolchain/hello-tekton.git',
            enum=['testString'],
            path='testString'
        )

        assert response.get_status_code() == 200
        property = response.get_result()
        assert property is not None

    @needscredentials
    def test_list_tekton_pipeline_triggers(self):

        response = self.cd_tekton_pipeline_service.list_tekton_pipeline_triggers(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            type='manual,scm',
            name='testString',
            event_listener='testString',
            worker_id='testString',
            worker_name='testString',
            disabled='true',
            tags='tag1,tag2'
        )

        assert response.get_status_code() == 200
        triggers_collection = response.get_result()
        assert triggers_collection is not None

    @needscredentials
    def test_create_tekton_pipeline_trigger(self):

        # Construct a dict representation of a Worker model
        worker_model = {
            'name': 'testString',
            'type': 'testString',
            'id': 'public',
        }

        # Construct a dict representation of a GenericSecret model
        generic_secret_model = {
            'type': 'token_matches',
            'value': 'testString',
            'source': 'header',
            'key_name': 'testString',
            'algorithm': 'md4',
        }

        # Construct a dict representation of a TriggerSourcePropertiesTool model
        trigger_source_properties_tool_model = {
            'id': 'testString',
        }

        # Construct a dict representation of a TriggerSourceProperties model
        trigger_source_properties_model = {
            'url': 'testString',
            'branch': 'testString',
            'pattern': 'testString',
            'blind_connection': True,
            'hook_id': 'testString',
            'tool': trigger_source_properties_tool_model,
        }

        # Construct a dict representation of a TriggerSource model
        trigger_source_model = {
            'type': 'testString',
            'properties': trigger_source_properties_model,
        }

        response = self.cd_tekton_pipeline_service.create_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            type='manual',
            name='Manual Trigger',
            event_listener='pr-listener',
            enabled=True,
            tags=['testString'],
            worker=worker_model,
            max_concurrent_runs=3,
            secret=generic_secret_model,
            cron='testString',
            timezone='testString',
            source=trigger_source_model,
            events=['push']
        )

        assert response.get_status_code() == 201
        trigger = response.get_result()
        assert trigger is not None

    @needscredentials
    def test_get_tekton_pipeline_trigger(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147'
        )

        assert response.get_status_code() == 200
        trigger = response.get_result()
        assert trigger is not None

    @needscredentials
    def test_update_tekton_pipeline_trigger(self):

        # Construct a dict representation of a Worker model
        worker_model = {
            'name': 'testString',
            'type': 'testString',
            'id': 'testString',
        }

        # Construct a dict representation of a GenericSecret model
        generic_secret_model = {
            'type': 'token_matches',
            'value': 'testString',
            'source': 'header',
            'key_name': 'testString',
            'algorithm': 'md4',
        }

        # Construct a dict representation of a TriggerSourcePropertiesTool model
        trigger_source_properties_tool_model = {
            'id': 'testString',
        }

        # Construct a dict representation of a TriggerSourceProperties model
        trigger_source_properties_model = {
            'url': 'testString',
            'branch': 'testString',
            'pattern': 'testString',
            'blind_connection': True,
            'hook_id': 'testString',
            'tool': trigger_source_properties_tool_model,
        }

        # Construct a dict representation of a TriggerSource model
        trigger_source_model = {
            'type': 'testString',
            'properties': trigger_source_properties_model,
        }

        # Construct a dict representation of a TriggerPatch model
        trigger_patch_model = {
            'type': 'manual',
            'name': 'start-deploy',
            'event_listener': 'testString',
            'tags': ['testString'],
            'worker': worker_model,
            'max_concurrent_runs': 4,
            'enabled': True,
            'secret': generic_secret_model,
            'cron': 'testString',
            'timezone': 'America/Los_Angeles, CET, Europe/London, GMT, US/Eastern, or UTC',
            'source': trigger_source_model,
            'events': ['push', 'pull_request'],
        }

        response = self.cd_tekton_pipeline_service.update_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            trigger_patch=trigger_patch_model
        )

        assert response.get_status_code() == 200
        trigger = response.get_result()
        assert trigger is not None

    @needscredentials
    def test_duplicate_tekton_pipeline_trigger(self):

        response = self.cd_tekton_pipeline_service.duplicate_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            source_trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            name='triggerName'
        )

        assert response.get_status_code() == 201
        trigger = response.get_result()
        assert trigger is not None

    @needscredentials
    def test_list_tekton_pipeline_trigger_properties(self):

        response = self.cd_tekton_pipeline_service.list_tekton_pipeline_trigger_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            name='prod',
            type='secure,text',
            sort='name'
        )

        assert response.get_status_code() == 200
        trigger_properties_collection = response.get_result()
        assert trigger_properties_collection is not None

    @needscredentials
    def test_create_tekton_pipeline_trigger_properties(self):

        response = self.cd_tekton_pipeline_service.create_tekton_pipeline_trigger_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            name='prop1',
            type='text',
            value='https://github.com/open-toolchain/hello-tekton.git',
            enum=['testString'],
            path='testString'
        )

        assert response.get_status_code() == 201
        trigger_property = response.get_result()
        assert trigger_property is not None

    @needscredentials
    def test_get_tekton_pipeline_trigger_property(self):

        response = self.cd_tekton_pipeline_service.get_tekton_pipeline_trigger_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            property_name='debug-pipeline'
        )

        assert response.get_status_code() == 200
        trigger_property = response.get_result()
        assert trigger_property is not None

    @needscredentials
    def test_replace_tekton_pipeline_trigger_property(self):

        response = self.cd_tekton_pipeline_service.replace_tekton_pipeline_trigger_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            property_name='debug-pipeline',
            name='prop1',
            type='text',
            value='https://github.com/open-toolchain/hello-tekton.git',
            enum=['testString'],
            path='testString'
        )

        assert response.get_status_code() == 200
        trigger_property = response.get_result()
        assert trigger_property is not None

    @needscredentials
    def test_delete_tekton_pipeline_trigger_property(self):

        response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_trigger_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            property_name='debug-pipeline'
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_trigger(self):

        response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147'
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_run(self):

        response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_property(self):

        response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            property_name='debug-pipeline'
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_definition(self):

        response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline(self):

        response = self.cd_tekton_pipeline_service.delete_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert response.get_status_code() == 204
