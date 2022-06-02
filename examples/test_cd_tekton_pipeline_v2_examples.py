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
Examples for CdTektonPipelineV2
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from github.com/IBM/continuous-delivery-pipeline-python-sdk.cd_tekton_pipeline_v2 import *

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

            worker_with_id_model = {
                'id': 'public',
            }

            tekton_pipeline = cd_tekton_pipeline_service.create_tekton_pipeline(
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                worker=worker_with_id_model
            ).get_result()

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

            tekton_pipeline = cd_tekton_pipeline_service.get_tekton_pipeline(
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            ).get_result()

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

            worker_with_id_model = {
                'id': 'public',
            }

            tekton_pipeline = cd_tekton_pipeline_service.update_tekton_pipeline(
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                worker=worker_with_id_model
            ).get_result()

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

            pipeline_runs = cd_tekton_pipeline_service.list_tekton_pipeline_runs(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                status='succeeded',
                trigger_name='manual-trigger'
            ).get_result()

            print(json.dumps(pipeline_runs, indent=2))

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

            pipeline_run = cd_tekton_pipeline_service.create_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_name='Generic Webhook Trigger - 0',
                trigger_properties={'pipeline-debug':'false'},
                secure_trigger_properties={'secure-property-key':'secure value'},
                trigger_header={'source':'api'},
                trigger_body={'message':'hello world','enable':'true','detail':{'name':'example'}}
            ).get_result()

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

            pipeline_run = cd_tekton_pipeline_service.get_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                includes='definitions'
            ).get_result()

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

            pipeline_run = cd_tekton_pipeline_service.cancel_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90',
                force=True
            ).get_result()

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

            pipeline_run = cd_tekton_pipeline_service.rerun_tekton_pipeline_run(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            ).get_result()

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

            pipeline_run_logs = cd_tekton_pipeline_service.get_tekton_pipeline_run_logs(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            ).get_result()

            print(json.dumps(pipeline_run_logs, indent=2))

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

            step_log = cd_tekton_pipeline_service.get_tekton_pipeline_run_log_content(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                pipeline_run_id='bf4b3abd-0c93-416b-911e-9cf42f1a1085',
                id='94619026-912b-4d92-8f51-6c74f0692d90'
            ).get_result()

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

            definitions = cd_tekton_pipeline_service.list_tekton_pipeline_definitions(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90'
            ).get_result()

            print(json.dumps(definitions, indent=2))

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

            definition_scm_source_model = {
                'url': 'https://github.com/IBM/tekton-tutorial.git',
                'branch': 'master',
                'path': '.tekton',
            }

            definition = cd_tekton_pipeline_service.create_tekton_pipeline_definition(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                scm_source=definition_scm_source_model
            ).get_result()

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

            definition = cd_tekton_pipeline_service.get_tekton_pipeline_definition(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada'
            ).get_result()

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

            definition_scm_source_model = {
                'url': 'https://github.com/IBM/tekton-tutorial.git',
                'branch': 'master',
                'path': '.tekton',
            }

            definition = cd_tekton_pipeline_service.replace_tekton_pipeline_definition(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                definition_id='94299034-d45f-4e9a-8ed5-6bd5c7bb7ada',
                scm_source=definition_scm_source_model,
                service_instance_id='071d8049-d984-4feb-a2ed-2a1e938918ba',
                id='22f92ab1-e0ac-4c65-84e7-8a4cb32dba0f'
            ).get_result()

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

            env_properties = cd_tekton_pipeline_service.list_tekton_pipeline_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                name='prod',
                type=['SECURE', 'TEXT'],
                sort='name'
            ).get_result()

            print(json.dumps(env_properties, indent=2))

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

            property = cd_tekton_pipeline_service.create_tekton_pipeline_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                name='key1',
                type='TEXT',
                value='https://github.com/IBM/tekton-tutorial.git'
            ).get_result()

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

            property = cd_tekton_pipeline_service.get_tekton_pipeline_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                property_name='debug-pipeline'
            ).get_result()

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

            property = cd_tekton_pipeline_service.replace_tekton_pipeline_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                property_name='debug-pipeline',
                name='key1',
                type='TEXT',
                value='https://github.com/IBM/tekton-tutorial.git'
            ).get_result()

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

            triggers = cd_tekton_pipeline_service.list_tekton_pipeline_triggers(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                type='manual,scm',
                disabled='true',
                tags='tag1,tag2'
            ).get_result()

            print(json.dumps(triggers, indent=2))

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

            trigger_model = {
                'source_trigger_id': 'b3a8228f-1c82-409b-b249-7639166a0300',
                'name': 'Generic Trigger- duplicated',
            }

            trigger = cd_tekton_pipeline_service.create_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger=trigger_model
            ).get_result()

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

            trigger = cd_tekton_pipeline_service.get_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147'
            ).get_result()

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

            trigger = cd_tekton_pipeline_service.update_tekton_pipeline_trigger(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                name='start-deploy',
                disabled=True
            ).get_result()

            print(json.dumps(trigger, indent=2))

            # end-update_tekton_pipeline_trigger

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

            trigger_properties = cd_tekton_pipeline_service.list_tekton_pipeline_trigger_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                name='prod',
                type='SECURE,TEXT',
                sort='name'
            ).get_result()

            print(json.dumps(trigger_properties, indent=2))

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

            trigger_property = cd_tekton_pipeline_service.create_tekton_pipeline_trigger_properties(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                name='key1',
                type='TEXT',
                value='https://github.com/IBM/tekton-tutorial.git'
            ).get_result()

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

            trigger_property = cd_tekton_pipeline_service.get_tekton_pipeline_trigger_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                property_name='debug-pipeline'
            ).get_result()

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

            trigger_property = cd_tekton_pipeline_service.replace_tekton_pipeline_trigger_property(
                pipeline_id='94619026-912b-4d92-8f51-6c74f0692d90',
                trigger_id='1bb892a1-2e04-4768-a369-b1159eace147',
                property_name='debug-pipeline',
                name='key1',
                type='TEXT',
                value='https://github.com/IBM/tekton-tutorial.git'
            ).get_result()

            print(json.dumps(trigger_property, indent=2))

            # end-replace_tekton_pipeline_trigger_property

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

# endregion
##############################################################################
# End of Examples for Service: CdTektonPipelineV2
##############################################################################
