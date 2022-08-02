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

        # Construct a dict representation of a WorkerWithId model
        worker_with_id_model = {
            'id': 'public',
        }

        create_tekton_pipeline_response = self.cd_tekton_pipeline_service.create_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            worker=worker_with_id_model
        )

        assert create_tekton_pipeline_response.get_status_code() == 201
        tekton_pipeline = create_tekton_pipeline_response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_get_tekton_pipeline(self):

        get_tekton_pipeline_response = self.cd_tekton_pipeline_service.get_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert get_tekton_pipeline_response.get_status_code() == 200
        tekton_pipeline = get_tekton_pipeline_response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_update_tekton_pipeline(self):

        # Construct a dict representation of a WorkerWithId model
        worker_with_id_model = {
            'id': 'public',
        }

        update_tekton_pipeline_response = self.cd_tekton_pipeline_service.update_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            worker=worker_with_id_model
        )

        assert update_tekton_pipeline_response.get_status_code() == 200
        tekton_pipeline = update_tekton_pipeline_response.get_result()
        assert tekton_pipeline is not None

    @needscredentials
    def test_list_tekton_pipeline_runs(self):

        list_tekton_pipeline_runs_response = self.cd_tekton_pipeline_service.list_tekton_pipeline_runs(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            limit=1,
            offset=38,
            status='succeeded',
            trigger_name='manual-trigger'
        )

        assert list_tekton_pipeline_runs_response.get_status_code() == 200
        pipeline_runs = list_tekton_pipeline_runs_response.get_result()
        assert pipeline_runs is not None

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
            client=self.ansiform_mock_service,
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

        create_tekton_pipeline_run_response = self.cd_tekton_pipeline_service.create_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_name='Generic Webhook Trigger - 0',
            trigger_properties={'pipeline-debug':'false'},
            secure_trigger_properties={'secure-property-key':'secure value'},
            trigger_header={'source':'api'},
            trigger_body={'message':'hello world','enable':'true','detail':{'name':'example'}}
        )

        assert create_tekton_pipeline_run_response.get_status_code() == 201
        pipeline_run = create_tekton_pipeline_run_response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_get_tekton_pipeline_run(self):

        get_tekton_pipeline_run_response = self.cd_tekton_pipeline_service.get_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            includes='definitions'
        )

        assert get_tekton_pipeline_run_response.get_status_code() == 200
        pipeline_run = get_tekton_pipeline_run_response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_cancel_tekton_pipeline_run(self):

        cancel_tekton_pipeline_run_response = self.cd_tekton_pipeline_service.cancel_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90',
            force=True
        )

        assert cancel_tekton_pipeline_run_response.get_status_code() == 200
        pipeline_run = cancel_tekton_pipeline_run_response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_rerun_tekton_pipeline_run(self):

        rerun_tekton_pipeline_run_response = self.cd_tekton_pipeline_service.rerun_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert rerun_tekton_pipeline_run_response.get_status_code() == 201
        pipeline_run = rerun_tekton_pipeline_run_response.get_result()
        assert pipeline_run is not None

    @needscredentials
    def test_get_tekton_pipeline_run_logs(self):

        get_tekton_pipeline_run_logs_response = self.cd_tekton_pipeline_service.get_tekton_pipeline_run_logs(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert get_tekton_pipeline_run_logs_response.get_status_code() == 200
        pipeline_run_logs = get_tekton_pipeline_run_logs_response.get_result()
        assert pipeline_run_logs is not None

    @needscredentials
    def test_get_tekton_pipeline_run_log_content(self):

        get_tekton_pipeline_run_log_content_response = self.cd_tekton_pipeline_service.get_tekton_pipeline_run_log_content(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            pipeline_run_id='bf4b3abd-0c93-416b-911e-9cf42f1a1085',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert get_tekton_pipeline_run_log_content_response.get_status_code() == 200
        step_log = get_tekton_pipeline_run_log_content_response.get_result()
        assert step_log is not None

    @needscredentials
    def test_list_tekton_pipeline_definitions(self):

        list_tekton_pipeline_definitions_response = self.cd_tekton_pipeline_service.list_tekton_pipeline_definitions(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert list_tekton_pipeline_definitions_response.get_status_code() == 200
        definitions = list_tekton_pipeline_definitions_response.get_result()
        assert definitions is not None

    @needscredentials
    def test_create_tekton_pipeline_definition(self):

        # Construct a dict representation of a DefinitionScmSource model
        definition_scm_source_model = {
            'url': 'https://github.com/IBM/tekton-tutorial.git',
            'branch': 'master',
            'tag': 'testString',
            'path': '.tekton',
        }

        create_tekton_pipeline_definition_response = self.cd_tekton_pipeline_service.create_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            scm_source=definition_scm_source_model
        )

        assert create_tekton_pipeline_definition_response.get_status_code() == 201
        definition = create_tekton_pipeline_definition_response.get_result()
        assert definition is not None

    @needscredentials
    def test_get_tekton_pipeline_definition(self):

        get_tekton_pipeline_definition_response = self.cd_tekton_pipeline_service.get_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
        )

        assert get_tekton_pipeline_definition_response.get_status_code() == 200
        definition = get_tekton_pipeline_definition_response.get_result()
        assert definition is not None

    @needscredentials
    def test_replace_tekton_pipeline_definition(self):

        # Construct a dict representation of a DefinitionScmSource model
        definition_scm_source_model = {
            'url': 'https://github.com/IBM/tekton-tutorial.git',
            'branch': 'master',
            'tag': 'testString',
            'path': '.tekton',
        }

        replace_tekton_pipeline_definition_response = self.cd_tekton_pipeline_service.replace_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada',
            scm_source=definition_scm_source_model,
            service_instance_id='071d8049-d984-4feb-a2ed-2a1e938918ba',
            id='22f92ab1-e0ac-4c65-84e7-8a4cb32dba0f'
        )

        assert replace_tekton_pipeline_definition_response.get_status_code() == 200
        definition = replace_tekton_pipeline_definition_response.get_result()
        assert definition is not None

    @needscredentials
    def test_list_tekton_pipeline_properties(self):

        list_tekton_pipeline_properties_response = self.cd_tekton_pipeline_service.list_tekton_pipeline_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            name='prod',
            type=['SECURE', 'TEXT'],
            sort='name'
        )

        assert list_tekton_pipeline_properties_response.get_status_code() == 200
        env_properties = list_tekton_pipeline_properties_response.get_result()
        assert env_properties is not None

    @needscredentials
    def test_create_tekton_pipeline_properties(self):

        create_tekton_pipeline_properties_response = self.cd_tekton_pipeline_service.create_tekton_pipeline_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            name='key1',
            type='TEXT',
            value='https://github.com/IBM/tekton-tutorial.git',
            enum=['testString'],
            default='testString',
            path='testString'
        )

        assert create_tekton_pipeline_properties_response.get_status_code() == 201
        property = create_tekton_pipeline_properties_response.get_result()
        assert property is not None

    @needscredentials
    def test_get_tekton_pipeline_property(self):

        get_tekton_pipeline_property_response = self.cd_tekton_pipeline_service.get_tekton_pipeline_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            property_name='debug-pipeline'
        )

        assert get_tekton_pipeline_property_response.get_status_code() == 200
        property = get_tekton_pipeline_property_response.get_result()
        assert property is not None

    @needscredentials
    def test_replace_tekton_pipeline_property(self):

        replace_tekton_pipeline_property_response = self.cd_tekton_pipeline_service.replace_tekton_pipeline_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            property_name='debug-pipeline',
            name='key1',
            type='TEXT',
            value='https://github.com/IBM/tekton-tutorial.git',
            enum=['testString'],
            default='testString',
            path='testString'
        )

        assert replace_tekton_pipeline_property_response.get_status_code() == 200
        property = replace_tekton_pipeline_property_response.get_result()
        assert property is not None

    @needscredentials
    def test_list_tekton_pipeline_triggers(self):

        list_tekton_pipeline_triggers_response = self.cd_tekton_pipeline_service.list_tekton_pipeline_triggers(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            type='manual,scm',
            name='testString',
            event_listener='testString',
            worker_id='testString',
            worker_name='testString',
            disabled='true',
            tags='tag1,tag2'
        )

        assert list_tekton_pipeline_triggers_response.get_status_code() == 200
        triggers = list_tekton_pipeline_triggers_response.get_result()
        assert triggers is not None

    @needscredentials
    def test_create_tekton_pipeline_trigger(self):

        # Construct a dict representation of a TriggerDuplicateTrigger model
        trigger_model = {
            'source_trigger_id': 'b3a8228f-1c82-409b-b249-7639166a0300',
            'name': 'Generic Trigger- duplicated',
        }

        create_tekton_pipeline_trigger_response = self.cd_tekton_pipeline_service.create_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger=trigger_model
        )

        assert create_tekton_pipeline_trigger_response.get_status_code() == 201
        trigger = create_tekton_pipeline_trigger_response.get_result()
        assert trigger is not None

    @needscredentials
    def test_get_tekton_pipeline_trigger(self):

        get_tekton_pipeline_trigger_response = self.cd_tekton_pipeline_service.get_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147'
        )

        assert get_tekton_pipeline_trigger_response.get_status_code() == 200
        trigger = get_tekton_pipeline_trigger_response.get_result()
        assert trigger is not None

    @needscredentials
    def test_update_tekton_pipeline_trigger(self):

        # Construct a dict representation of a Worker model
        worker_model = {
            'name': 'testString',
            'type': 'private',
            'id': 'testString',
        }

        # Construct a dict representation of a Concurrency model
        concurrency_model = {
            'max_concurrent_runs': 20,
        }

        # Construct a dict representation of a GenericSecret model
        generic_secret_model = {
            'type': 'tokenMatches',
            'value': 'testString',
            'source': 'header',
            'key_name': 'testString',
            'algorithm': 'md4',
        }

        # Construct a dict representation of a TriggerScmSource model
        trigger_scm_source_model = {
            'url': 'testString',
            'branch': 'testString',
            'pattern': 'testString',
            'blind_connection': True,
            'hook_id': 'testString',
        }

        # Construct a dict representation of a Events model
        events_model = {
            'push': True,
            'pull_request_closed': True,
            'pull_request': True,
        }

        update_tekton_pipeline_trigger_response = self.cd_tekton_pipeline_service.update_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            type='manual',
            name='start-deploy',
            event_listener='testString',
            tags=['testString'],
            worker=worker_model,
            concurrency=concurrency_model,
            disabled=True,
            secret=generic_secret_model,
            cron='testString',
            timezone='Africa/Abidjan',
            scm_source=trigger_scm_source_model,
            events=events_model
        )

        assert update_tekton_pipeline_trigger_response.get_status_code() == 200
        trigger = update_tekton_pipeline_trigger_response.get_result()
        assert trigger is not None

    @needscredentials
    def test_list_tekton_pipeline_trigger_properties(self):

        list_tekton_pipeline_trigger_properties_response = self.cd_tekton_pipeline_service.list_tekton_pipeline_trigger_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            name='prod',
            type='SECURE,TEXT',
            sort='name'
        )

        assert list_tekton_pipeline_trigger_properties_response.get_status_code() == 200
        trigger_properties = list_tekton_pipeline_trigger_properties_response.get_result()
        assert trigger_properties is not None

    @needscredentials
    def test_create_tekton_pipeline_trigger_properties(self):

        create_tekton_pipeline_trigger_properties_response = self.cd_tekton_pipeline_service.create_tekton_pipeline_trigger_properties(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            name='key1',
            type='TEXT',
            value='https://github.com/IBM/tekton-tutorial.git',
            enum=['testString'],
            default='testString',
            path='testString'
        )

        assert create_tekton_pipeline_trigger_properties_response.get_status_code() == 201
        trigger_property = create_tekton_pipeline_trigger_properties_response.get_result()
        assert trigger_property is not None

    @needscredentials
    def test_get_tekton_pipeline_trigger_property(self):

        get_tekton_pipeline_trigger_property_response = self.cd_tekton_pipeline_service.get_tekton_pipeline_trigger_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            property_name='debug-pipeline'
        )

        assert get_tekton_pipeline_trigger_property_response.get_status_code() == 200
        trigger_property = get_tekton_pipeline_trigger_property_response.get_result()
        assert trigger_property is not None

    @needscredentials
    def test_replace_tekton_pipeline_trigger_property(self):

        replace_tekton_pipeline_trigger_property_response = self.cd_tekton_pipeline_service.replace_tekton_pipeline_trigger_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            property_name='debug-pipeline',
            name='key1',
            type='TEXT',
            value='https://github.com/IBM/tekton-tutorial.git',
            enum=['testString'],
            default='testString',
            path='testString'
        )

        assert replace_tekton_pipeline_trigger_property_response.get_status_code() == 200
        trigger_property = replace_tekton_pipeline_trigger_property_response.get_result()
        assert trigger_property is not None

    @needscredentials
    def test_delete_tekton_pipeline_trigger_property(self):

        delete_tekton_pipeline_trigger_property_response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_trigger_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
            property_name='debug-pipeline'
        )

        assert delete_tekton_pipeline_trigger_property_response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_trigger(self):

        delete_tekton_pipeline_trigger_response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_trigger(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            trigger_id='1bb892a1-2e04-4768-a369-b1159eace147'
        )

        assert delete_tekton_pipeline_trigger_response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_run(self):

        delete_tekton_pipeline_run_response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_run(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert delete_tekton_pipeline_run_response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_property(self):

        delete_tekton_pipeline_property_response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_property(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            property_name='debug-pipeline'
        )

        assert delete_tekton_pipeline_property_response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline_definition(self):

        delete_tekton_pipeline_definition_response = self.cd_tekton_pipeline_service.delete_tekton_pipeline_definition(
            pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
            definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
        )

        assert delete_tekton_pipeline_definition_response.get_status_code() == 204

    @needscredentials
    def test_delete_tekton_pipeline(self):

        delete_tekton_pipeline_response = self.cd_tekton_pipeline_service.delete_tekton_pipeline(
            id='94619026-912b-4d92-8f51-6c74f0692d90'
        )

        assert delete_tekton_pipeline_response.get_status_code() == 204
