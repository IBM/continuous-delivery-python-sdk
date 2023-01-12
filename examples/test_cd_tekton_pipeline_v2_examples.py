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
Examples for CdTektonPipelineV2
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from ibm_continuous_delivery.cd_tekton_pipeline_v2 import *

#
# This file provides an example of how to use the CD Tekton Pipeline service.
#
# The following configuration properties are assumed to be defined:
# CD_TEKTON_PIPELINE_URL=<service base url>
# CD_TEKTON_PIPELINE_AUTH_TYPE=iam
# CD_TEKTON_PIPELINE_APIKEY=<IAM apikey>
# CD_TEKTON_PIPELINE_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = 'cd_tekton_pipeline_v2.env'

cd_tekton_pipeline_service = None

config = None


##############################################################################
# Start of Examples for Service: CdTektonPipelineV2
##############################################################################
# region
class TestCdTektonPipelineV2Examples():
    """
    Example Test Class for CdTektonPipelineV2
    """

    @classmethod
    def setup_class(cls):
        global cd_tekton_pipeline_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            cd_tekton_pipeline_service = CdTektonPipelineV2.new_instance(
            )

            # end-common
            assert cd_tekton_pipeline_service is not None

            # Load the configuration
            global config
            config = read_external_sources(CdTektonPipelineV2.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_tekton_pipeline_example(self):
        """
        create_tekton_pipeline request example
        """
        try:
            print('\ncreate_tekton_pipeline() result:')
            # begin-create_tekton_pipeline

            worker_identity_model = {
                'id': 'public',
            }

            response = cd_tekton_pipeline_service.create_tekton_pipeline(
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                worker=worker_identity_model
            )
            tekton_pipeline = response.get_result()

            print(json.dumps(tekton_pipeline, indent=2))

            # end-create_tekton_pipeline

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_example(self):
        """
        get_tekton_pipeline request example
        """
        try:
            print('\nget_tekton_pipeline() result:')
            # begin-get_tekton_pipeline

            response = cd_tekton_pipeline_service.get_tekton_pipeline(
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            )
            tekton_pipeline = response.get_result()

            print(json.dumps(tekton_pipeline, indent=2))

            # end-get_tekton_pipeline

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_tekton_pipeline_example(self):
        """
        update_tekton_pipeline request example
        """
        try:
            print('\nupdate_tekton_pipeline() result:')
            # begin-update_tekton_pipeline

            worker_identity_model = {
                'id': 'public',
            }

            tekton_pipeline_patch_model = {
                'worker': worker_identity_model,
            }

            response = cd_tekton_pipeline_service.update_tekton_pipeline(
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                tekton_pipeline_patch=tekton_pipeline_patch_model
            )
            tekton_pipeline = response.get_result()

            print(json.dumps(tekton_pipeline, indent=2))

            # end-update_tekton_pipeline

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_tekton_pipeline_runs_example(self):
        """
        list_tekton_pipeline_runs request example
        """
        try:
            print('\nlist_tekton_pipeline_runs() result:')
            # begin-list_tekton_pipeline_runs

            all_results = []
            pager = TektonPipelineRunsPager(
                client=cd_tekton_pipeline_service,
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                limit=10,
                status='succeeded',
                trigger_name='manual-trigger',
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_tekton_pipeline_runs
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_tekton_pipeline_run_example(self):
        """
        create_tekton_pipeline_run request example
        """
        try:
            print('\ncreate_tekton_pipeline_run() result:')
            # begin-create_tekton_pipeline_run

            property_model = {
                'name': 'testString',
                'href': 'testString',
                'type': 'secure',
            }

            pipeline_run_trigger_model = {
                'name': 'Generic Webhook Trigger - 0',
                'properties': [property_model],
                'secure_properties': [property_model],
                'headers': {'source':'api'},
                'body': {'message':'hello world','enable':'true','detail':{'name':'example'}},
            }

            response = cd_tekton_pipeline_service.create_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger=pipeline_run_trigger_model
            )
            pipeline_run = response.get_result()

            print(json.dumps(pipeline_run, indent=2))

            # end-create_tekton_pipeline_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_run_example(self):
        """
        get_tekton_pipeline_run request example
        """
        try:
            print('\nget_tekton_pipeline_run() result:')
            # begin-get_tekton_pipeline_run

            response = cd_tekton_pipeline_service.get_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                includes='definitions'
            )
            pipeline_run = response.get_result()

            print(json.dumps(pipeline_run, indent=2))

            # end-get_tekton_pipeline_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_cancel_tekton_pipeline_run_example(self):
        """
        cancel_tekton_pipeline_run request example
        """
        try:
            print('\ncancel_tekton_pipeline_run() result:')
            # begin-cancel_tekton_pipeline_run

            response = cd_tekton_pipeline_service.cancel_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                force=True
            )
            pipeline_run = response.get_result()

            print(json.dumps(pipeline_run, indent=2))

            # end-cancel_tekton_pipeline_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_rerun_tekton_pipeline_run_example(self):
        """
        rerun_tekton_pipeline_run request example
        """
        try:
            print('\nrerun_tekton_pipeline_run() result:')
            # begin-rerun_tekton_pipeline_run

            response = cd_tekton_pipeline_service.rerun_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            )
            pipeline_run = response.get_result()

            print(json.dumps(pipeline_run, indent=2))

            # end-rerun_tekton_pipeline_run

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_run_logs_example(self):
        """
        get_tekton_pipeline_run_logs request example
        """
        try:
            print('\nget_tekton_pipeline_run_logs() result:')
            # begin-get_tekton_pipeline_run_logs

            response = cd_tekton_pipeline_service.get_tekton_pipeline_run_logs(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            )
            logs_collection = response.get_result()

            print(json.dumps(logs_collection, indent=2))

            # end-get_tekton_pipeline_run_logs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_run_log_content_example(self):
        """
        get_tekton_pipeline_run_log_content request example
        """
        try:
            print('\nget_tekton_pipeline_run_log_content() result:')
            # begin-get_tekton_pipeline_run_log_content

            response = cd_tekton_pipeline_service.get_tekton_pipeline_run_log_content(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                pipeline_run_id='bf4b3abd-0c93-416b-911e-9cf42f1a1085',
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            )
            step_log = response.get_result()

            print(json.dumps(step_log, indent=2))

            # end-get_tekton_pipeline_run_log_content

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_tekton_pipeline_definitions_example(self):
        """
        list_tekton_pipeline_definitions request example
        """
        try:
            print('\nlist_tekton_pipeline_definitions() result:')
            # begin-list_tekton_pipeline_definitions

            response = cd_tekton_pipeline_service.list_tekton_pipeline_definitions(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90'
            )
            definitions_collection = response.get_result()

            print(json.dumps(definitions_collection, indent=2))

            # end-list_tekton_pipeline_definitions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_tekton_pipeline_definition_example(self):
        """
        create_tekton_pipeline_definition request example
        """
        try:
            print('\ncreate_tekton_pipeline_definition() result:')
            # begin-create_tekton_pipeline_definition

            definition_source_properties_model = {
                'url': 'https://github.com/open-toolchain/hello-tekton.git',
                'branch': 'master',
                'path': '.tekton',
            }

            definition_source_model = {
                'type': 'git',
                'properties': definition_source_properties_model,
            }

            response = cd_tekton_pipeline_service.create_tekton_pipeline_definition(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                source=definition_source_model
            )
            definition = response.get_result()

            print(json.dumps(definition, indent=2))

            # end-create_tekton_pipeline_definition

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_definition_example(self):
        """
        get_tekton_pipeline_definition request example
        """
        try:
            print('\nget_tekton_pipeline_definition() result:')
            # begin-get_tekton_pipeline_definition

            response = cd_tekton_pipeline_service.get_tekton_pipeline_definition(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
            )
            definition = response.get_result()

            print(json.dumps(definition, indent=2))

            # end-get_tekton_pipeline_definition

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_tekton_pipeline_definition_example(self):
        """
        replace_tekton_pipeline_definition request example
        """
        try:
            print('\nreplace_tekton_pipeline_definition() result:')
            # begin-replace_tekton_pipeline_definition

            definition_source_properties_model = {
                'url': 'testString',
                'path': 'testString',
            }

            definition_source_model = {
                'type': 'testString',
                'properties': definition_source_properties_model,
            }

            response = cd_tekton_pipeline_service.replace_tekton_pipeline_definition(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada',
                source=definition_source_model
            )
            definition = response.get_result()

            print(json.dumps(definition, indent=2))

            # end-replace_tekton_pipeline_definition

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_tekton_pipeline_properties_example(self):
        """
        list_tekton_pipeline_properties request example
        """
        try:
            print('\nlist_tekton_pipeline_properties() result:')
            # begin-list_tekton_pipeline_properties

            response = cd_tekton_pipeline_service.list_tekton_pipeline_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                name='prod',
                type=['secure', 'text'],
                sort='name'
            )
            properties_collection = response.get_result()

            print(json.dumps(properties_collection, indent=2))

            # end-list_tekton_pipeline_properties

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_tekton_pipeline_properties_example(self):
        """
        create_tekton_pipeline_properties request example
        """
        try:
            print('\ncreate_tekton_pipeline_properties() result:')
            # begin-create_tekton_pipeline_properties

            response = cd_tekton_pipeline_service.create_tekton_pipeline_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                name='prop1',
                type='text',
                value='https://github.com/open-toolchain/hello-tekton.git'
            )
            property = response.get_result()

            print(json.dumps(property, indent=2))

            # end-create_tekton_pipeline_properties

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_property_example(self):
        """
        get_tekton_pipeline_property request example
        """
        try:
            print('\nget_tekton_pipeline_property() result:')
            # begin-get_tekton_pipeline_property

            response = cd_tekton_pipeline_service.get_tekton_pipeline_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                property_name='debug-pipeline'
            )
            property = response.get_result()

            print(json.dumps(property, indent=2))

            # end-get_tekton_pipeline_property

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_tekton_pipeline_property_example(self):
        """
        replace_tekton_pipeline_property request example
        """
        try:
            print('\nreplace_tekton_pipeline_property() result:')
            # begin-replace_tekton_pipeline_property

            response = cd_tekton_pipeline_service.replace_tekton_pipeline_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                property_name='debug-pipeline',
                name='prop1',
                type='text',
                value='https://github.com/open-toolchain/hello-tekton.git'
            )
            property = response.get_result()

            print(json.dumps(property, indent=2))

            # end-replace_tekton_pipeline_property

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_tekton_pipeline_triggers_example(self):
        """
        list_tekton_pipeline_triggers request example
        """
        try:
            print('\nlist_tekton_pipeline_triggers() result:')
            # begin-list_tekton_pipeline_triggers

            response = cd_tekton_pipeline_service.list_tekton_pipeline_triggers(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                type='manual,scm',
                disabled='true',
                tags='tag1,tag2'
            )
            triggers_collection = response.get_result()

            print(json.dumps(triggers_collection, indent=2))

            # end-list_tekton_pipeline_triggers

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_tekton_pipeline_trigger_example(self):
        """
        create_tekton_pipeline_trigger request example
        """
        try:
            print('\ncreate_tekton_pipeline_trigger() result:')
            # begin-create_tekton_pipeline_trigger

            worker_model = {
                'id': 'public',
            }

            response = cd_tekton_pipeline_service.create_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                type='manual',
                name='Manual Trigger',
                event_listener='pr-listener',
                worker=worker_model,
                max_concurrent_runs=3,
                enabled=True
            )
            trigger = response.get_result()

            print(json.dumps(trigger, indent=2))

            # end-create_tekton_pipeline_trigger

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_trigger_example(self):
        """
        get_tekton_pipeline_trigger request example
        """
        try:
            print('\nget_tekton_pipeline_trigger() result:')
            # begin-get_tekton_pipeline_trigger

            response = cd_tekton_pipeline_service.get_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147'
            )
            trigger = response.get_result()

            print(json.dumps(trigger, indent=2))

            # end-get_tekton_pipeline_trigger

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_tekton_pipeline_trigger_example(self):
        """
        update_tekton_pipeline_trigger request example
        """
        try:
            print('\nupdate_tekton_pipeline_trigger() result:')
            # begin-update_tekton_pipeline_trigger

            trigger_patch_model = {
                'name': 'start-deploy',
            }

            response = cd_tekton_pipeline_service.update_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                trigger_patch=trigger_patch_model
            )
            trigger = response.get_result()

            print(json.dumps(trigger, indent=2))

            # end-update_tekton_pipeline_trigger

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_duplicate_tekton_pipeline_trigger_example(self):
        """
        duplicate_tekton_pipeline_trigger request example
        """
        try:
            print('\nduplicate_tekton_pipeline_trigger() result:')
            # begin-duplicate_tekton_pipeline_trigger

            response = cd_tekton_pipeline_service.duplicate_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                source_trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                name='triggerName'
            )
            trigger = response.get_result()

            print(json.dumps(trigger, indent=2))

            # end-duplicate_tekton_pipeline_trigger

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_tekton_pipeline_trigger_properties_example(self):
        """
        list_tekton_pipeline_trigger_properties request example
        """
        try:
            print('\nlist_tekton_pipeline_trigger_properties() result:')
            # begin-list_tekton_pipeline_trigger_properties

            response = cd_tekton_pipeline_service.list_tekton_pipeline_trigger_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                name='prod',
                type='secure,text',
                sort='name'
            )
            trigger_properties_collection = response.get_result()

            print(json.dumps(trigger_properties_collection, indent=2))

            # end-list_tekton_pipeline_trigger_properties

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_tekton_pipeline_trigger_properties_example(self):
        """
        create_tekton_pipeline_trigger_properties request example
        """
        try:
            print('\ncreate_tekton_pipeline_trigger_properties() result:')
            # begin-create_tekton_pipeline_trigger_properties

            response = cd_tekton_pipeline_service.create_tekton_pipeline_trigger_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                name='prop1',
                type='text',
                value='https://github.com/open-toolchain/hello-tekton.git'
            )
            trigger_property = response.get_result()

            print(json.dumps(trigger_property, indent=2))

            # end-create_tekton_pipeline_trigger_properties

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_tekton_pipeline_trigger_property_example(self):
        """
        get_tekton_pipeline_trigger_property request example
        """
        try:
            print('\nget_tekton_pipeline_trigger_property() result:')
            # begin-get_tekton_pipeline_trigger_property

            response = cd_tekton_pipeline_service.get_tekton_pipeline_trigger_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                property_name='debug-pipeline'
            )
            trigger_property = response.get_result()

            print(json.dumps(trigger_property, indent=2))

            # end-get_tekton_pipeline_trigger_property

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_tekton_pipeline_trigger_property_example(self):
        """
        replace_tekton_pipeline_trigger_property request example
        """
        try:
            print('\nreplace_tekton_pipeline_trigger_property() result:')
            # begin-replace_tekton_pipeline_trigger_property

            response = cd_tekton_pipeline_service.replace_tekton_pipeline_trigger_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                property_name='debug-pipeline',
                name='prop1',
                type='text',
                value='https://github.com/open-toolchain/hello-tekton.git'
            )
            trigger_property = response.get_result()

            print(json.dumps(trigger_property, indent=2))

            # end-replace_tekton_pipeline_trigger_property

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tekton_pipeline_example(self):
        """
        delete_tekton_pipeline request example
        """
        try:
            # begin-delete_tekton_pipeline

            response = cd_tekton_pipeline_service.delete_tekton_pipeline(
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            )

            # end-delete_tekton_pipeline
            print('\ndelete_tekton_pipeline() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tekton_pipeline_run_example(self):
        """
        delete_tekton_pipeline_run request example
        """
        try:
            # begin-delete_tekton_pipeline_run

            response = cd_tekton_pipeline_service.delete_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            )

            # end-delete_tekton_pipeline_run
            print('\ndelete_tekton_pipeline_run() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tekton_pipeline_definition_example(self):
        """
        delete_tekton_pipeline_definition request example
        """
        try:
            # begin-delete_tekton_pipeline_definition

            response = cd_tekton_pipeline_service.delete_tekton_pipeline_definition(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
            )

            # end-delete_tekton_pipeline_definition
            print('\ndelete_tekton_pipeline_definition() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tekton_pipeline_property_example(self):
        """
        delete_tekton_pipeline_property request example
        """
        try:
            # begin-delete_tekton_pipeline_property

            response = cd_tekton_pipeline_service.delete_tekton_pipeline_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                property_name='debug-pipeline'
            )

            # end-delete_tekton_pipeline_property
            print('\ndelete_tekton_pipeline_property() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tekton_pipeline_trigger_example(self):
        """
        delete_tekton_pipeline_trigger request example
        """
        try:
            # begin-delete_tekton_pipeline_trigger

            response = cd_tekton_pipeline_service.delete_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147'
            )

            # end-delete_tekton_pipeline_trigger
            print('\ndelete_tekton_pipeline_trigger() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_tekton_pipeline_trigger_property_example(self):
        """
        delete_tekton_pipeline_trigger_property request example
        """
        try:
            # begin-delete_tekton_pipeline_trigger_property

            response = cd_tekton_pipeline_service.delete_tekton_pipeline_trigger_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                property_name='debug-pipeline'
            )

            # end-delete_tekton_pipeline_trigger_property
            print('\ndelete_tekton_pipeline_trigger_property() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: CdTektonPipelineV2
##############################################################################
