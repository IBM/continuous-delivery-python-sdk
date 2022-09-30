# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.54.2-6c0e29d4-20220824-204545
 
"""
Continuous Delivery Tekton pipeline API definition <br><br> Maximum request payload size
is 512 KB <br><br> All calls require an <strong>Authorization</strong> HTTP header.
<br><br> The following header is the accepted authentication mechanism and required
credentials for each <ul><li><b>Bearer:</b> an IBM Cloud IAM token (authorized for all
endpoints)</li>

API Version: 2.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse, get_query_param
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class CdTektonPipelineV2(BaseService):
    """The CD Tekton Pipeline V2 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.devops.cloud.ibm.com/pipeline/v2'
    DEFAULT_SERVICE_NAME = 'cd_tekton_pipeline'

    REGIONAL_ENDPOINTS = {
        'us-south': 'https://api.us-south.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the us-south region.
        'us-east': 'https://api.us-east.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the us-east region.
        'eu-de': 'https://api.eu-de.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the eu-de region.
        'eu-gb': 'https://api.eu-gb.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the eu-gb region.
        'jp-osa': 'https://api.jp-osa.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the jp-osa region.
        'jp-tok': 'https://api.jp-tok.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the jp-tok region.
        'au-syd': 'https://api.au-syd.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the au-syd region.
        'ca-tor': 'https://api.ca-tor.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the ca-tor region.
        'br-sao': 'https://api.br-sao.devops.cloud.ibm.com/pipeline/v2', # The host URL for Tekton Pipeline Service in the br-sao region.
    }

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CdTektonPipelineV2':
        """
        Return a new client for the CD Tekton Pipeline service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    @classmethod
    def get_service_url_for_region(
        cls,
        region: str,
    ) -> str:
        """
        Returns the service URL associated with the specified region.
        :param str region: a string representing the region
        :return: The service URL associated with the specified region or None
                 if no mapping for the region exists
        :rtype: str
        """
        return cls.REGIONAL_ENDPOINTS.get(region, None)

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the CD Tekton Pipeline service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Pipeline
    #########################


    def create_tekton_pipeline(self,
        *,
        id: str = None,
        enable_slack_notifications: bool = None,
        enable_partial_cloning: bool = None,
        worker: 'WorkerWithId' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create Tekton pipeline.

        This request creates a Tekton pipeline for a Tekton pipeline toolchain
        integration. User must use the toolchain endpoint to create the Tekton pipeline
        toolchain integration first, and then use the generated UUID to create the Tekton
        pipeline.

        :param str id: (optional) UUID.
        :param bool enable_slack_notifications: (optional) Flag whether to enable
               slack notifications for this pipeline. When enabled, pipeline run events
               will be published on all slack integration specified channels in the
               enclosing toolchain.
        :param bool enable_partial_cloning: (optional) Flag whether to enable
               partial cloning for this pipeline. When partial clone is enabled, only the
               files contained within the paths specified in definition repositories will
               be read and cloned. This means symbolic links may not work.
        :param WorkerWithId worker: (optional) Worker object containing worker ID
               only. If omitted the IBM Managed shared workers are used by default.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TektonPipeline` object
        """

        if worker is not None:
            worker = convert_model(worker)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tekton_pipeline')
        headers.update(sdk_headers)

        data = {
            'id': id,
            'enable_slack_notifications': enable_slack_notifications,
            'enable_partial_cloning': enable_partial_cloning,
            'worker': worker
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/tekton_pipelines'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get Tekton pipeline data.

        This request retrieves the Tekton pipeline data for the pipeline identified by
        `{id}`.

        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TektonPipeline` object
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_tekton_pipeline(self,
        id: str,
        *,
        tekton_pipeline_patch: 'TektonPipelinePatch' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update Tekton pipeline data.

        This request updates Tekton pipeline data, but you can only change worker ID in
        this endpoint. Use other endpoints such as /definitions, /triggers, and
        /properties for other configuration updates.

        :param str id: ID of current instance.
        :param TektonPipelinePatch tekton_pipeline_patch: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TektonPipeline` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if  tekton_pipeline_patch is not None and isinstance(tekton_pipeline_patch, TektonPipelinePatch):
            tekton_pipeline_patch = convert_model(tekton_pipeline_patch)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_tekton_pipeline')
        headers.update(sdk_headers)

        data = json.dumps(tekton_pipeline_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_tekton_pipeline(self,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete Tekton pipeline instance.

        This request deletes Tekton pipeline instance that is associated with the pipeline
        toolchain integration.

        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_tekton_pipeline')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # PipelineRuns
    #########################


    def list_tekton_pipeline_runs(self,
        pipeline_id: str,
        *,
        start: str = None,
        limit: int = None,
        offset: int = None,
        status: str = None,
        trigger_name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List pipeline run records.

        This request lists pipeline run records, which has data about the runs, such as
        status, user_info, trigger and other information. Default limit is 50.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str start: (optional) A page token that identifies the start point
               of the list of pipeline runs. This value is computed and included in the
               response body. Cannot be used in combination with `offset`.
        :param int limit: (optional) The number of pipeline runs to return, sorted
               by creation time, most recent first.
        :param int offset: (optional) Skip the specified number of pipeline runs.
               Cannot be used in combination with `start`.
        :param str status: (optional) Filters the collection to resources with the
               specified status.
        :param str trigger_name: (optional) Filters the collection to resources
               with the specified trigger name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRunsCollection` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_tekton_pipeline_runs')
        headers.update(sdk_headers)

        params = {
            'start': start,
            'limit': limit,
            'offset': offset,
            'status': status,
            'trigger.name': trigger_name
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_tekton_pipeline_run(self,
        pipeline_id: str,
        *,
        trigger_name: str = None,
        trigger_properties: dict = None,
        secure_trigger_properties: dict = None,
        trigger_header: dict = None,
        trigger_body: dict = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Trigger a pipeline run.

        Trigger a new pipeline run using the named trigger, using the provided additional
        or override properties.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_name: (optional) Trigger name.
        :param dict trigger_properties: (optional) An object containing string
               values only that provides additional `text` properties, or overrides
               existing pipeline/trigger properties.
        :param dict secure_trigger_properties: (optional) An object containing
               string values only that provides additional `secure` properties, or
               overrides existing `secure` pipeline/trigger properties.
        :param dict trigger_header: (optional) An object containing string values
               only that provides the trigger header. Use `$(header.header_key_name)` to
               access it in triggerBinding.
        :param dict trigger_body: (optional) An object that provides the trigger
               body. Use `$(body.body_key_name)` to access it in triggerBinding.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRun` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tekton_pipeline_run')
        headers.update(sdk_headers)

        data = {
            'trigger_name': trigger_name,
            'trigger_properties': trigger_properties,
            'secure_trigger_properties': secure_trigger_properties,
            'trigger_header': trigger_header,
            'trigger_body': trigger_body
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline_run(self,
        pipeline_id: str,
        id: str,
        *,
        includes: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a pipeline run record.

        This request retrieves details of the pipeline run identified by `{id}`. To get
        the Kubernetes resource list of this pipeline run use the endpoint
        `/tekton_pipelines/{pipeline_id}/tekton_pipelinerun_resource_list/{id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str id: ID of current instance.
        :param str includes: (optional) Defines if response includes definition
               metadata.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRun` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline_run')
        headers.update(sdk_headers)

        params = {
            'includes': includes
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def delete_tekton_pipeline_run(self,
        pipeline_id: str,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a pipeline run record.

        This request deletes the pipeline run record identified by `{id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_tekton_pipeline_run')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def cancel_tekton_pipeline_run(self,
        pipeline_id: str,
        id: str,
        *,
        force: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Cancel a pipeline run.

        This request cancels a running pipeline run identified by `{id}`. Use `force:
        true` in the body if the pipeline run can't be cancelled normally.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str id: ID of current instance.
        :param bool force: (optional) Flag whether force cancel.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRun` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='cancel_tekton_pipeline_run')
        headers.update(sdk_headers)

        data = {
            'force': force
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}/cancel'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def rerun_tekton_pipeline_run(self,
        pipeline_id: str,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Rerun a pipeline run.

        This request reruns a past pipeline run, which is identified by `{id}`, with the
        same data. Request body isn't allowed.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRun` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='rerun_tekton_pipeline_run')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}/rerun'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline_run_logs(self,
        pipeline_id: str,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a list of pipeline run log objects.

        This request fetches a list of log data for a pipeline run identified by `{id}`.
        The `href` in each log entry can be used to fetch that individual log.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogsCollection` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline_run_logs')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}/logs'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline_run_log_content(self,
        pipeline_id: str,
        pipeline_run_id: str,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the log content of a pipeline run step.

        This request retrieves the log content of a pipeline run step, where the step is
        identified by `{id}`. To get the log ID use the endpoint
        `/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}/logs`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str pipeline_run_id: The Tekton pipeline run ID.
        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Log` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if pipeline_run_id is None:
            raise ValueError('pipeline_run_id must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline_run_log_content')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'pipeline_run_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, pipeline_run_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{pipeline_run_id}/logs/{id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Definitions
    #########################


    def list_tekton_pipeline_definitions(self,
        pipeline_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List pipeline definitions.

        This request fetches pipeline definitions, which is a collection of individual
        definition entries. Each entry consists of a repository url, a repository branch
        and a repository path.

        :param str pipeline_id: The Tekton pipeline ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DefinitionsCollection` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_tekton_pipeline_definitions')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_tekton_pipeline_definition(self,
        pipeline_id: str,
        *,
        scm_source: 'DefinitionScmSource' = None,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a single definition.

        This request adds a single definition.

        :param str pipeline_id: The Tekton pipeline ID.
        :param DefinitionScmSource scm_source: (optional) SCM source for Tekton
               pipeline definition.
        :param str id: (optional) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Definition` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if scm_source is not None:
            scm_source = convert_model(scm_source)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tekton_pipeline_definition')
        headers.update(sdk_headers)

        data = {
            'scm_source': scm_source,
            'id': id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline_definition(self,
        pipeline_id: str,
        definition_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve a single definition entry.

        This request fetches a single definition entry, which consists of the definition
        repository URL, branch/tag and path.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str definition_id: The definition ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Definition` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if definition_id is None:
            raise ValueError('definition_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline_definition')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'definition_id']
        path_param_values = self.encode_path_vars(pipeline_id, definition_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions/{definition_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def replace_tekton_pipeline_definition(self,
        pipeline_id: str,
        definition_id: str,
        *,
        scm_source: 'DefinitionScmSource' = None,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Edit a single definition entry.

        This request updates a definition entry identified by `{definition_id}`. The
        service_instance_id property is immutable.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str definition_id: The definition ID.
        :param DefinitionScmSource scm_source: (optional) SCM source for Tekton
               pipeline definition.
        :param str id: (optional) UUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Definition` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if definition_id is None:
            raise ValueError('definition_id must be provided')
        if scm_source is not None:
            scm_source = convert_model(scm_source)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='replace_tekton_pipeline_definition')
        headers.update(sdk_headers)

        data = {
            'scm_source': scm_source,
            'id': id
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'definition_id']
        path_param_values = self.encode_path_vars(pipeline_id, definition_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions/{definition_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_tekton_pipeline_definition(self,
        pipeline_id: str,
        definition_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a single definition entry.

        This request deletes a single definition from the definition list.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str definition_id: The definition ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if definition_id is None:
            raise ValueError('definition_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_tekton_pipeline_definition')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'definition_id']
        path_param_values = self.encode_path_vars(pipeline_id, definition_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions/{definition_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Environment properties
    #########################


    def list_tekton_pipeline_properties(self,
        pipeline_id: str,
        *,
        name: str = None,
        type: List[str] = None,
        sort: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List the pipeline's environment properties.

        This request lists the environment properties the pipeline identified by
        `{pipeline_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str name: (optional) Filters the collection to resources with the
               specified property name.
        :param List[str] type: (optional) Filters the collection to resources with
               the specified property type.
        :param str sort: (optional) Sorts the returned properties by name, in
               ascending order using `name` or in descending order using `-name`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PropertiesCollection` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_tekton_pipeline_properties')
        headers.update(sdk_headers)

        params = {
            'name': name,
            'type': convert_list(type),
            'sort': sort
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_tekton_pipeline_properties(self,
        pipeline_id: str,
        *,
        name: str = None,
        type: str = None,
        value: str = None,
        enum: List[str] = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a pipeline environment property.

        This request creates an environment property.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) Property value.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed when using `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Property` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tekton_pipeline_properties')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'path': path
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline_property(self,
        pipeline_id: str,
        property_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a pipeline environment property.

        This request gets the data of an environment property identified by
        `{property_name}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str property_name: The property name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Property` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if property_name is None:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline_property')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def replace_tekton_pipeline_property(self,
        pipeline_id: str,
        property_name: str,
        *,
        name: str = None,
        type: str = None,
        value: str = None,
        enum: List[str] = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace the value of an environment property.

        This request updates the value of an environment property identified by
        `{property_name}`, its type or name are immutable.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str property_name: The property name.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) Property value.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed when using `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Property` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if property_name is None:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='replace_tekton_pipeline_property')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'path': path
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_tekton_pipeline_property(self,
        pipeline_id: str,
        property_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a single pipeline environment property.

        This request deletes a single pipeline environment property.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str property_name: The property name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if property_name is None:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_tekton_pipeline_property')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Triggers
    #########################


    def list_tekton_pipeline_triggers(self,
        pipeline_id: str,
        *,
        type: str = None,
        name: str = None,
        event_listener: str = None,
        worker_id: str = None,
        worker_name: str = None,
        disabled: str = None,
        tags: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List pipeline triggers.

        This request lists pipeline triggers for the pipeline identified by
        `{pipeline_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str type: (optional) Filter the triggers by "type", accepts a comma
               separated list of types. Valid types are "manual", "scm", "generic", and
               "timer".
        :param str name: (optional) Filter the triggers by "name", accepts a single
               string value.
        :param str event_listener: (optional) Filter the triggers by
               "event_listener", accepts a single string value.
        :param str worker_id: (optional) Filter the triggers by "worker.id",
               accepts a single string value.
        :param str worker_name: (optional) Filter the triggers by "worker.name",
               accepts a single string value.
        :param str disabled: (optional) Filter the triggers by "disabled" flag,
               possible values are "true" or "false".
        :param str tags: (optional) Filter the triggers by "tags", accepts a comma
               separated list of tags. The response lists triggers having at least one
               matching tag.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggersCollection` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_tekton_pipeline_triggers')
        headers.update(sdk_headers)

        params = {
            'type': type,
            'name': name,
            'event_listener': event_listener,
            'worker.id': worker_id,
            'worker.name': worker_name,
            'disabled': disabled,
            'tags': tags
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_tekton_pipeline_trigger(self,
        pipeline_id: str,
        *,
        type: str = None,
        name: str = None,
        event_listener: str = None,
        disabled: bool = None,
        tags: List[str] = None,
        worker: 'Worker' = None,
        max_concurrent_runs: int = None,
        secret: 'GenericSecret' = None,
        cron: str = None,
        timezone: str = None,
        scm_source: 'TriggerScmSource' = None,
        events: 'Events' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a trigger.

        This request creates a trigger.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str type: (optional) Trigger type.
        :param str name: (optional) Trigger name.
        :param str event_listener: (optional) Event listener name. The name of the
               event listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param bool disabled: (optional) Flag whether the trigger is disabled. If
               omitted the trigger is enabled by default.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Worker used to run the trigger. If not
               specified the trigger will use the default pipeline worker.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. Omit this property to disable the
               concurrency limit.
        :param GenericSecret secret: (optional) Only needed for generic webhook
               trigger type. Secret used to start generic webhook trigger.
        :param str cron: (optional) Only needed for timer triggers. Cron expression
               for timer trigger.
        :param str timezone: (optional) Only needed for timer triggers. Timezone
               for timer trigger.
        :param TriggerScmSource scm_source: (optional) SCM source repository for a
               Git trigger. Only needed for Git triggers.
        :param Events events: (optional) Only needed for Git triggers. Events
               object defines the events to which this Git trigger listens.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if worker is not None:
            worker = convert_model(worker)
        if secret is not None:
            secret = convert_model(secret)
        if scm_source is not None:
            scm_source = convert_model(scm_source)
        if events is not None:
            events = convert_model(events)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tekton_pipeline_trigger')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'event_listener': event_listener,
            'disabled': disabled,
            'tags': tags,
            'worker': worker,
            'max_concurrent_runs': max_concurrent_runs,
            'secret': secret,
            'cron': cron,
            'timezone': timezone,
            'scm_source': scm_source,
            'events': events
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline_trigger(self,
        pipeline_id: str,
        trigger_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a single trigger.

        This request retrieves a single trigger identified by `{trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline_trigger')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_tekton_pipeline_trigger(self,
        pipeline_id: str,
        trigger_id: str,
        *,
        trigger_patch: 'TriggerPatch' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Edit a trigger.

        This request changes a single field or many fields of the trigger identified by
        `{trigger_id}`. Note that some fields are immutable, and use `/properties`
        endpoint to update trigger properties.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param TriggerPatch trigger_patch: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        if  trigger_patch is not None and isinstance(trigger_patch, TriggerPatch):
            trigger_patch = convert_model(trigger_patch)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_tekton_pipeline_trigger')
        headers.update(sdk_headers)

        data = json.dumps(trigger_patch)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_tekton_pipeline_trigger(self,
        pipeline_id: str,
        trigger_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a single trigger.

        This request deletes the trigger identified by `{trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_tekton_pipeline_trigger')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def duplicate_tekton_pipeline_trigger(self,
        pipeline_id: str,
        source_trigger_id: str,
        *,
        name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Duplicate a trigger.

        This request duplicates a trigger from an existing trigger identified by
        `{source_trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str source_trigger_id: The ID of the trigger to duplicate.
        :param str name: (optional) Trigger name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if source_trigger_id is None:
            raise ValueError('source_trigger_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='duplicate_tekton_pipeline_trigger')
        headers.update(sdk_headers)

        data = {
            'name': name
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'source_trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, source_trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{source_trigger_id}/duplicate'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Trigger properties
    #########################


    def list_tekton_pipeline_trigger_properties(self,
        pipeline_id: str,
        trigger_id: str,
        name: str,
        type: str,
        sort: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List trigger properties.

        This request lists trigger properties for the trigger identified by
        `{trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str name: Filter properties by `name`.
        :param str type: Filter properties by `type`. Valid types are `secure`,
               `text`, `integration`, `single_select`, `appconfig`.
        :param str sort: Sort properties by name. They can be sorted in ascending
               order using `name` or in descending order using `-name`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerPropertiesCollection` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if sort is None:
            raise ValueError('sort must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_tekton_pipeline_trigger_properties')
        headers.update(sdk_headers)

        params = {
            'name': name,
            'type': type,
            'sort': sort
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_tekton_pipeline_trigger_properties(self,
        pipeline_id: str,
        trigger_id: str,
        *,
        name: str = None,
        type: str = None,
        value: str = None,
        enum: List[str] = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a trigger property.

        This request creates a property in the trigger identified by `{trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) Property value.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerProperty` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tekton_pipeline_trigger_properties')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'path': path
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_tekton_pipeline_trigger_property(self,
        pipeline_id: str,
        trigger_id: str,
        property_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a trigger property.

        This request retrieves a trigger property.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str property_name: The property name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerProperty` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        if property_name is None:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_tekton_pipeline_trigger_property')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def replace_tekton_pipeline_trigger_property(self,
        pipeline_id: str,
        trigger_id: str,
        property_name: str,
        *,
        name: str = None,
        type: str = None,
        value: str = None,
        enum: List[str] = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace a trigger property value.

        This request updates a trigger property value, type and name are immutable.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str property_name: The property name.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) Property value.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerProperty` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        if property_name is None:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='replace_tekton_pipeline_trigger_property')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'path': path
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_tekton_pipeline_trigger_property(self,
        pipeline_id: str,
        trigger_id: str,
        property_name: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a trigger property.

        This request deletes a trigger property.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str property_name: The property name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        if property_name is None:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_tekton_pipeline_trigger_property')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'trigger_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


class ListTektonPipelineRunsEnums:
    """
    Enums for list_tekton_pipeline_runs parameters.
    """

    class Status(str, Enum):
        """
        Filters the collection to resources with the specified status.
        """
        PENDING = 'pending'
        WAITING = 'waiting'
        QUEUED = 'queued'
        RUNNING = 'running'
        CANCELLED = 'cancelled'
        CANCELLING = 'cancelling'
        FAILED = 'failed'
        ERROR = 'error'
        SUCCEEDED = 'succeeded'


class GetTektonPipelineRunEnums:
    """
    Enums for get_tekton_pipeline_run parameters.
    """

    class Includes(str, Enum):
        """
        Defines if response includes definition metadata.
        """
        DEFINITIONS = 'definitions'


class ListTektonPipelinePropertiesEnums:
    """
    Enums for list_tekton_pipeline_properties parameters.
    """

    class Type(str, Enum):
        """
        Filters the collection to resources with the specified property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


##############################################################################
# Models
##############################################################################


class Definition():
    """
    Tekton pipeline definition entry object.

    :attr DefinitionScmSource scm_source: SCM source for Tekton pipeline definition.
    :attr str id: (optional) UUID.
    """

    def __init__(self,
                 scm_source: 'DefinitionScmSource',
                 *,
                 id: str = None) -> None:
        """
        Initialize a Definition object.

        :param DefinitionScmSource scm_source: SCM source for Tekton pipeline
               definition.
        :param str id: (optional) UUID.
        """
        self.scm_source = scm_source
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Definition':
        """Initialize a Definition object from a json dictionary."""
        args = {}
        if 'scm_source' in _dict:
            args['scm_source'] = DefinitionScmSource.from_dict(_dict.get('scm_source'))
        else:
            raise ValueError('Required property \'scm_source\' not present in Definition JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Definition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scm_source') and self.scm_source is not None:
            _dict['scm_source'] = self.scm_source.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Definition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Definition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Definition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DefinitionScmSource():
    """
    SCM source for Tekton pipeline definition.

    :attr str url: URL of the definition repository.
    :attr str branch: (optional) A branch from the repo. One of branch or tag must
          be specified, but only one or the other.
    :attr str tag: (optional) A tag from the repo. One of branch or tag must be
          specified, but only one or the other.
    :attr str path: The path to the definition's yaml files.
    :attr str service_instance_id: (optional) ID of the SCM repository service
          instance.
    """

    def __init__(self,
                 url: str,
                 path: str,
                 *,
                 branch: str = None,
                 tag: str = None,
                 service_instance_id: str = None) -> None:
        """
        Initialize a DefinitionScmSource object.

        :param str url: URL of the definition repository.
        :param str path: The path to the definition's yaml files.
        :param str branch: (optional) A branch from the repo. One of branch or tag
               must be specified, but only one or the other.
        :param str tag: (optional) A tag from the repo. One of branch or tag must
               be specified, but only one or the other.
        :param str service_instance_id: (optional) ID of the SCM repository service
               instance.
        """
        self.url = url
        self.branch = branch
        self.tag = tag
        self.path = path
        self.service_instance_id = service_instance_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefinitionScmSource':
        """Initialize a DefinitionScmSource object from a json dictionary."""
        args = {}
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in DefinitionScmSource JSON')
        if 'branch' in _dict:
            args['branch'] = _dict.get('branch')
        if 'tag' in _dict:
            args['tag'] = _dict.get('tag')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        else:
            raise ValueError('Required property \'path\' not present in DefinitionScmSource JSON')
        if 'service_instance_id' in _dict:
            args['service_instance_id'] = _dict.get('service_instance_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefinitionScmSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'branch') and self.branch is not None:
            _dict['branch'] = self.branch
        if hasattr(self, 'tag') and self.tag is not None:
            _dict['tag'] = self.tag
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'service_instance_id') and self.service_instance_id is not None:
            _dict['service_instance_id'] = self.service_instance_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefinitionScmSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefinitionScmSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefinitionScmSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DefinitionsCollection():
    """
    Pipeline definitions is a collection of individual definition entries, each entry
    consists of a repository URL, branch/tag and path.

    :attr List[DefinitionsCollectionDefinitionsItem] definitions: Definition list.
    """

    def __init__(self,
                 definitions: List['DefinitionsCollectionDefinitionsItem']) -> None:
        """
        Initialize a DefinitionsCollection object.

        :param List[DefinitionsCollectionDefinitionsItem] definitions: Definition
               list.
        """
        self.definitions = definitions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefinitionsCollection':
        """Initialize a DefinitionsCollection object from a json dictionary."""
        args = {}
        if 'definitions' in _dict:
            args['definitions'] = [DefinitionsCollectionDefinitionsItem.from_dict(x) for x in _dict.get('definitions')]
        else:
            raise ValueError('Required property \'definitions\' not present in DefinitionsCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefinitionsCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'definitions') and self.definitions is not None:
            _dict['definitions'] = [x.to_dict() for x in self.definitions]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefinitionsCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefinitionsCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefinitionsCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DefinitionsCollectionDefinitionsItem():
    """
    Tekton pipeline definition entry object.

    :attr DefinitionScmSource scm_source: SCM source for Tekton pipeline definition.
    :attr str id: (optional) UUID.
    :attr str href: (optional) URL of the definition repository.
    """

    def __init__(self,
                 scm_source: 'DefinitionScmSource',
                 *,
                 id: str = None,
                 href: str = None) -> None:
        """
        Initialize a DefinitionsCollectionDefinitionsItem object.

        :param DefinitionScmSource scm_source: SCM source for Tekton pipeline
               definition.
        :param str id: (optional) UUID.
        :param str href: (optional) URL of the definition repository.
        """
        self.scm_source = scm_source
        self.id = id
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefinitionsCollectionDefinitionsItem':
        """Initialize a DefinitionsCollectionDefinitionsItem object from a json dictionary."""
        args = {}
        if 'scm_source' in _dict:
            args['scm_source'] = DefinitionScmSource.from_dict(_dict.get('scm_source'))
        else:
            raise ValueError('Required property \'scm_source\' not present in DefinitionsCollectionDefinitionsItem JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefinitionsCollectionDefinitionsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scm_source') and self.scm_source is not None:
            _dict['scm_source'] = self.scm_source.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefinitionsCollectionDefinitionsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefinitionsCollectionDefinitionsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefinitionsCollectionDefinitionsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Events():
    """
    Only needed for Git triggers. Events object defines the events to which this Git
    trigger listens.

    :attr bool push: (optional) If true, the trigger listens for 'push' Git webhook
          events.
    :attr bool pull_request_closed: (optional) If true, the trigger listens for
          'close pull request' Git webhook events.
    :attr bool pull_request: (optional) If true, the trigger listens for 'open pull
          request' or 'update pull request' Git webhook events.
    """

    def __init__(self,
                 *,
                 push: bool = None,
                 pull_request_closed: bool = None,
                 pull_request: bool = None) -> None:
        """
        Initialize a Events object.

        :param bool push: (optional) If true, the trigger listens for 'push' Git
               webhook events.
        :param bool pull_request_closed: (optional) If true, the trigger listens
               for 'close pull request' Git webhook events.
        :param bool pull_request: (optional) If true, the trigger listens for 'open
               pull request' or 'update pull request' Git webhook events.
        """
        self.push = push
        self.pull_request_closed = pull_request_closed
        self.pull_request = pull_request

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Events':
        """Initialize a Events object from a json dictionary."""
        args = {}
        if 'push' in _dict:
            args['push'] = _dict.get('push')
        if 'pull_request_closed' in _dict:
            args['pull_request_closed'] = _dict.get('pull_request_closed')
        if 'pull_request' in _dict:
            args['pull_request'] = _dict.get('pull_request')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Events object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'push') and self.push is not None:
            _dict['push'] = self.push
        if hasattr(self, 'pull_request_closed') and self.pull_request_closed is not None:
            _dict['pull_request_closed'] = self.pull_request_closed
        if hasattr(self, 'pull_request') and self.pull_request is not None:
            _dict['pull_request'] = self.pull_request
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Events object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Events') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Events') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GenericSecret():
    """
    Only needed for generic webhook trigger type. Secret used to start generic webhook
    trigger.

    :attr str type: (optional) Secret type.
    :attr str value: (optional) Secret value, not needed if secret type is
          `internal_validation`.
    :attr str source: (optional) Secret location, not needed if secret type is
          `internal_validation`.
    :attr str key_name: (optional) Secret name, not needed if type is
          `internal_validation`.
    :attr str algorithm: (optional) Algorithm used for `digest_matches` secret type.
          Only needed for `digest_matches` secret type.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 value: str = None,
                 source: str = None,
                 key_name: str = None,
                 algorithm: str = None) -> None:
        """
        Initialize a GenericSecret object.

        :param str type: (optional) Secret type.
        :param str value: (optional) Secret value, not needed if secret type is
               `internal_validation`.
        :param str source: (optional) Secret location, not needed if secret type is
               `internal_validation`.
        :param str key_name: (optional) Secret name, not needed if type is
               `internal_validation`.
        :param str algorithm: (optional) Algorithm used for `digest_matches` secret
               type. Only needed for `digest_matches` secret type.
        """
        self.type = type
        self.value = value
        self.source = source
        self.key_name = key_name
        self.algorithm = algorithm

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GenericSecret':
        """Initialize a GenericSecret object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        if 'key_name' in _dict:
            args['key_name'] = _dict.get('key_name')
        if 'algorithm' in _dict:
            args['algorithm'] = _dict.get('algorithm')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GenericSecret object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'key_name') and self.key_name is not None:
            _dict['key_name'] = self.key_name
        if hasattr(self, 'algorithm') and self.algorithm is not None:
            _dict['algorithm'] = self.algorithm
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GenericSecret object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GenericSecret') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GenericSecret') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Secret type.
        """
        TOKEN_MATCHES = 'token_matches'
        DIGEST_MATCHES = 'digest_matches'
        INTERNAL_VALIDATION = 'internal_validation'


    class SourceEnum(str, Enum):
        """
        Secret location, not needed if secret type is `internal_validation`.
        """
        HEADER = 'header'
        PAYLOAD = 'payload'
        QUERY = 'query'


    class AlgorithmEnum(str, Enum):
        """
        Algorithm used for `digest_matches` secret type. Only needed for `digest_matches`
        secret type.
        """
        MD4 = 'md4'
        MD5 = 'md5'
        SHA1 = 'sha1'
        SHA256 = 'sha256'
        SHA384 = 'sha384'
        SHA512 = 'sha512'
        SHA512_224 = 'sha512_224'
        SHA512_256 = 'sha512_256'
        RIPEMD160 = 'ripemd160'


class Log():
    """
    Log object for Tekton pipeline run step.

    :attr str data: (optional) The raw log content of step.
    :attr str href: (optional) API for getting log content.
    :attr str id: Step log ID.
    :attr str name: (optional) <podName>/<containerName> of this log.
    """

    def __init__(self,
                 id: str,
                 *,
                 data: str = None,
                 href: str = None,
                 name: str = None) -> None:
        """
        Initialize a Log object.

        :param str id: Step log ID.
        :param str data: (optional) The raw log content of step.
        :param str href: (optional) API for getting log content.
        :param str name: (optional) <podName>/<containerName> of this log.
        """
        self.data = data
        self.href = href
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Log':
        """Initialize a Log object from a json dictionary."""
        args = {}
        if 'data' in _dict:
            args['data'] = _dict.get('data')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Log JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Log object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Log object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Log') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Log') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LogsCollection():
    """
    List of pipeline run log objects.

    :attr List[Log] logs: (optional) The list of pipeline run log objects.
    """

    def __init__(self,
                 *,
                 logs: List['Log'] = None) -> None:
        """
        Initialize a LogsCollection object.

        :param List[Log] logs: (optional) The list of pipeline run log objects.
        """
        self.logs = logs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogsCollection':
        """Initialize a LogsCollection object from a json dictionary."""
        args = {}
        if 'logs' in _dict:
            args['logs'] = [Log.from_dict(x) for x in _dict.get('logs')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogsCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'logs') and self.logs is not None:
            _dict['logs'] = [x.to_dict() for x in self.logs]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogsCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogsCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogsCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRun():
    """
    Single Tekton pipeline run object.

    :attr str id: UUID.
    :attr UserInfo user_info: (optional) User information.
    :attr str status: Status of the pipeline run.
    :attr str definition_id: The aggregated definition ID used for this pipeline
          run.
    :attr PipelineRunWorker worker: worker details used in this pipeline run.
    :attr str pipeline_id: UUID.
    :attr str listener_name: Listener name used to start the run.
    :attr Trigger trigger: Tekton pipeline trigger.
    :attr str event_params_blob: Event parameters object passed to this pipeline run
          in String format, the contents depends on the type of trigger, for example, for
          Git trigger it includes the Git event payload.
    :attr str event_header_params_blob: (optional) Headers passed to this pipeline
          run in String format.
    :attr List[Property] properties: (optional) Properties used in this Tekton
          pipeline run.
    :attr datetime created_at: (optional) Standard RFC 3339 Date Time String.
    :attr datetime updated_at: (optional) Standard RFC 3339 Date Time String.
    :attr str run_url: URL for the details page of this pipeline run.
    """

    def __init__(self,
                 id: str,
                 status: str,
                 definition_id: str,
                 worker: 'PipelineRunWorker',
                 pipeline_id: str,
                 listener_name: str,
                 trigger: 'Trigger',
                 event_params_blob: str,
                 run_url: str,
                 *,
                 user_info: 'UserInfo' = None,
                 event_header_params_blob: str = None,
                 properties: List['Property'] = None,
                 created_at: datetime = None,
                 updated_at: datetime = None) -> None:
        """
        Initialize a PipelineRun object.

        :param str id: UUID.
        :param str status: Status of the pipeline run.
        :param str definition_id: The aggregated definition ID used for this
               pipeline run.
        :param PipelineRunWorker worker: worker details used in this pipeline run.
        :param str pipeline_id: UUID.
        :param str listener_name: Listener name used to start the run.
        :param Trigger trigger: Tekton pipeline trigger.
        :param str event_params_blob: Event parameters object passed to this
               pipeline run in String format, the contents depends on the type of trigger,
               for example, for Git trigger it includes the Git event payload.
        :param str run_url: URL for the details page of this pipeline run.
        :param UserInfo user_info: (optional) User information.
        :param str event_header_params_blob: (optional) Headers passed to this
               pipeline run in String format.
        :param List[Property] properties: (optional) Properties used in this Tekton
               pipeline run.
        :param datetime created_at: (optional) Standard RFC 3339 Date Time String.
        :param datetime updated_at: (optional) Standard RFC 3339 Date Time String.
        """
        self.id = id
        self.user_info = user_info
        self.status = status
        self.definition_id = definition_id
        self.worker = worker
        self.pipeline_id = pipeline_id
        self.listener_name = listener_name
        self.trigger = trigger
        self.event_params_blob = event_params_blob
        self.event_header_params_blob = event_header_params_blob
        self.properties = properties
        self.created_at = created_at
        self.updated_at = updated_at
        self.run_url = run_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRun':
        """Initialize a PipelineRun object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PipelineRun JSON')
        if 'user_info' in _dict:
            args['user_info'] = UserInfo.from_dict(_dict.get('user_info'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in PipelineRun JSON')
        if 'definition_id' in _dict:
            args['definition_id'] = _dict.get('definition_id')
        else:
            raise ValueError('Required property \'definition_id\' not present in PipelineRun JSON')
        if 'worker' in _dict:
            args['worker'] = PipelineRunWorker.from_dict(_dict.get('worker'))
        else:
            raise ValueError('Required property \'worker\' not present in PipelineRun JSON')
        if 'pipeline_id' in _dict:
            args['pipeline_id'] = _dict.get('pipeline_id')
        else:
            raise ValueError('Required property \'pipeline_id\' not present in PipelineRun JSON')
        if 'listener_name' in _dict:
            args['listener_name'] = _dict.get('listener_name')
        else:
            raise ValueError('Required property \'listener_name\' not present in PipelineRun JSON')
        if 'trigger' in _dict:
            args['trigger'] = _dict.get('trigger')
        else:
            raise ValueError('Required property \'trigger\' not present in PipelineRun JSON')
        if 'event_params_blob' in _dict:
            args['event_params_blob'] = _dict.get('event_params_blob')
        else:
            raise ValueError('Required property \'event_params_blob\' not present in PipelineRun JSON')
        if 'event_header_params_blob' in _dict:
            args['event_header_params_blob'] = _dict.get('event_header_params_blob')
        if 'properties' in _dict:
            args['properties'] = [Property.from_dict(x) for x in _dict.get('properties')]
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'run_url' in _dict:
            args['run_url'] = _dict.get('run_url')
        else:
            raise ValueError('Required property \'run_url\' not present in PipelineRun JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRun object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'user_info') and self.user_info is not None:
            _dict['user_info'] = self.user_info.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'definition_id') and self.definition_id is not None:
            _dict['definition_id'] = self.definition_id
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'pipeline_id') and self.pipeline_id is not None:
            _dict['pipeline_id'] = self.pipeline_id
        if hasattr(self, 'listener_name') and self.listener_name is not None:
            _dict['listener_name'] = self.listener_name
        if hasattr(self, 'trigger') and self.trigger is not None:
            if isinstance(self.trigger, dict):
                _dict['trigger'] = self.trigger
            else:
                _dict['trigger'] = self.trigger.to_dict()
        if hasattr(self, 'event_params_blob') and self.event_params_blob is not None:
            _dict['event_params_blob'] = self.event_params_blob
        if hasattr(self, 'event_header_params_blob') and self.event_header_params_blob is not None:
            _dict['event_header_params_blob'] = self.event_header_params_blob
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'run_url') and self.run_url is not None:
            _dict['run_url'] = self.run_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRun object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRun') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRun') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the pipeline run.
        """
        PENDING = 'pending'
        WAITING = 'waiting'
        QUEUED = 'queued'
        RUNNING = 'running'
        CANCELLED = 'cancelled'
        CANCELLING = 'cancelling'
        FAILED = 'failed'
        ERROR = 'error'
        SUCCEEDED = 'succeeded'


class PipelineRunWorker():
    """
    worker details used in this pipeline run.

    :attr str name: (optional) Name of the worker. Computed based on the worker ID.
    :attr str agent: (optional) The agent ID of the corresponding private worker
          integration used for this pipeline run.
    :attr str service_id: (optional) The Service ID of the corresponding private
          worker integration used for this pipeline run.
    :attr str id: UUID.
    """

    def __init__(self,
                 id: str,
                 *,
                 name: str = None,
                 agent: str = None,
                 service_id: str = None) -> None:
        """
        Initialize a PipelineRunWorker object.

        :param str id: UUID.
        :param str name: (optional) Name of the worker. Computed based on the
               worker ID.
        :param str agent: (optional) The agent ID of the corresponding private
               worker integration used for this pipeline run.
        :param str service_id: (optional) The Service ID of the corresponding
               private worker integration used for this pipeline run.
        """
        self.name = name
        self.agent = agent
        self.service_id = service_id
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunWorker':
        """Initialize a PipelineRunWorker object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'agent' in _dict:
            args['agent'] = _dict.get('agent')
        if 'service_id' in _dict:
            args['service_id'] = _dict.get('service_id')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PipelineRunWorker JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunWorker object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'agent') and self.agent is not None:
            _dict['agent'] = self.agent
        if hasattr(self, 'service_id') and self.service_id is not None:
            _dict['service_id'] = self.service_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunWorker object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunWorker') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunWorker') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsCollection():
    """
    Tekton pipeline runs object.

    :attr List[PipelineRunsCollectionPipelineRunsItem] pipeline_runs: Tekton
          pipeline runs list.
    :attr int offset: Skip a specified number of pipeline runs.
    :attr int limit: The number of pipeline runs to return, sorted by creation time,
          most recent first.
    :attr PipelineRunsCollectionFirst first: First page of pipeline runs.
    :attr PipelineRunsCollectionNext next: (optional) Next page of pipeline runs
          relative to the `start` and `limit` params, or relative to the `offset` and
          `limit` params, depending on which of `start` or `offset` were used in the
          request.
    :attr PipelineRunsCollectionLast last: (optional) Last page of pipeline runs
          relative to the `start` and `limit` params, or relative to the `offset` and
          `limit` params, depending on which of `start` or `offset` were used in the
          request.
    """

    def __init__(self,
                 pipeline_runs: List['PipelineRunsCollectionPipelineRunsItem'],
                 offset: int,
                 limit: int,
                 first: 'PipelineRunsCollectionFirst',
                 *,
                 next: 'PipelineRunsCollectionNext' = None,
                 last: 'PipelineRunsCollectionLast' = None) -> None:
        """
        Initialize a PipelineRunsCollection object.

        :param List[PipelineRunsCollectionPipelineRunsItem] pipeline_runs: Tekton
               pipeline runs list.
        :param int offset: Skip a specified number of pipeline runs.
        :param int limit: The number of pipeline runs to return, sorted by creation
               time, most recent first.
        :param PipelineRunsCollectionFirst first: First page of pipeline runs.
        :param PipelineRunsCollectionNext next: (optional) Next page of pipeline
               runs relative to the `start` and `limit` params, or relative to the
               `offset` and `limit` params, depending on which of `start` or `offset` were
               used in the request.
        :param PipelineRunsCollectionLast last: (optional) Last page of pipeline
               runs relative to the `start` and `limit` params, or relative to the
               `offset` and `limit` params, depending on which of `start` or `offset` were
               used in the request.
        """
        self.pipeline_runs = pipeline_runs
        self.offset = offset
        self.limit = limit
        self.first = first
        self.next = next
        self.last = last

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsCollection':
        """Initialize a PipelineRunsCollection object from a json dictionary."""
        args = {}
        if 'pipeline_runs' in _dict:
            args['pipeline_runs'] = [PipelineRunsCollectionPipelineRunsItem.from_dict(x) for x in _dict.get('pipeline_runs')]
        else:
            raise ValueError('Required property \'pipeline_runs\' not present in PipelineRunsCollection JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in PipelineRunsCollection JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in PipelineRunsCollection JSON')
        if 'first' in _dict:
            args['first'] = PipelineRunsCollectionFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in PipelineRunsCollection JSON')
        if 'next' in _dict:
            args['next'] = PipelineRunsCollectionNext.from_dict(_dict.get('next'))
        if 'last' in _dict:
            args['last'] = PipelineRunsCollectionLast.from_dict(_dict.get('last'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pipeline_runs') and self.pipeline_runs is not None:
            _dict['pipeline_runs'] = [x.to_dict() for x in self.pipeline_runs]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunsCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsCollectionFirst():
    """
    First page of pipeline runs.

    :attr str href: General href URL.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a PipelineRunsCollectionFirst object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsCollectionFirst':
        """Initialize a PipelineRunsCollectionFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PipelineRunsCollectionFirst JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsCollectionFirst object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunsCollectionFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsCollectionFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsCollectionFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsCollectionLast():
    """
    Last page of pipeline runs relative to the `start` and `limit` params, or relative to
    the `offset` and `limit` params, depending on which of `start` or `offset` were used
    in the request.

    :attr str href: General href URL.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a PipelineRunsCollectionLast object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsCollectionLast':
        """Initialize a PipelineRunsCollectionLast object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PipelineRunsCollectionLast JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsCollectionLast object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunsCollectionLast object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsCollectionLast') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsCollectionLast') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsCollectionNext():
    """
    Next page of pipeline runs relative to the `start` and `limit` params, or relative to
    the `offset` and `limit` params, depending on which of `start` or `offset` were used
    in the request.

    :attr str href: General href URL.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a PipelineRunsCollectionNext object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsCollectionNext':
        """Initialize a PipelineRunsCollectionNext object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PipelineRunsCollectionNext JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsCollectionNext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunsCollectionNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsCollectionNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsCollectionNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsCollectionPipelineRunsItem():
    """
    Single Tekton pipeline run object.

    :attr str id: UUID.
    :attr UserInfo user_info: (optional) User information.
    :attr str status: Status of the pipeline run.
    :attr str definition_id: The aggregated definition ID used for this pipeline
          run.
    :attr PipelineRunWorker worker: worker details used in this pipeline run.
    :attr str pipeline_id: UUID.
    :attr str listener_name: Listener name used to start the run.
    :attr Trigger trigger: Tekton pipeline trigger.
    :attr str event_params_blob: Event parameters object passed to this pipeline run
          in String format, the contents depends on the type of trigger, for example, for
          Git trigger it includes the Git event payload.
    :attr str event_header_params_blob: (optional) Headers passed to this pipeline
          run in String format.
    :attr List[Property] properties: (optional) Properties used in this Tekton
          pipeline run.
    :attr datetime created_at: (optional) Standard RFC 3339 Date Time String.
    :attr datetime updated_at: (optional) Standard RFC 3339 Date Time String.
    :attr str run_url: URL for the details page of this pipeline run.
    :attr str href: (optional) API URL for interacting with the pipeline run.
    """

    def __init__(self,
                 id: str,
                 status: str,
                 definition_id: str,
                 worker: 'PipelineRunWorker',
                 pipeline_id: str,
                 listener_name: str,
                 trigger: 'Trigger',
                 event_params_blob: str,
                 run_url: str,
                 *,
                 user_info: 'UserInfo' = None,
                 event_header_params_blob: str = None,
                 properties: List['Property'] = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 href: str = None) -> None:
        """
        Initialize a PipelineRunsCollectionPipelineRunsItem object.

        :param str id: UUID.
        :param str status: Status of the pipeline run.
        :param str definition_id: The aggregated definition ID used for this
               pipeline run.
        :param PipelineRunWorker worker: worker details used in this pipeline run.
        :param str pipeline_id: UUID.
        :param str listener_name: Listener name used to start the run.
        :param Trigger trigger: Tekton pipeline trigger.
        :param str event_params_blob: Event parameters object passed to this
               pipeline run in String format, the contents depends on the type of trigger,
               for example, for Git trigger it includes the Git event payload.
        :param str run_url: URL for the details page of this pipeline run.
        :param UserInfo user_info: (optional) User information.
        :param str event_header_params_blob: (optional) Headers passed to this
               pipeline run in String format.
        :param List[Property] properties: (optional) Properties used in this Tekton
               pipeline run.
        :param datetime created_at: (optional) Standard RFC 3339 Date Time String.
        :param datetime updated_at: (optional) Standard RFC 3339 Date Time String.
        :param str href: (optional) API URL for interacting with the pipeline run.
        """
        self.id = id
        self.user_info = user_info
        self.status = status
        self.definition_id = definition_id
        self.worker = worker
        self.pipeline_id = pipeline_id
        self.listener_name = listener_name
        self.trigger = trigger
        self.event_params_blob = event_params_blob
        self.event_header_params_blob = event_header_params_blob
        self.properties = properties
        self.created_at = created_at
        self.updated_at = updated_at
        self.run_url = run_url
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsCollectionPipelineRunsItem':
        """Initialize a PipelineRunsCollectionPipelineRunsItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'user_info' in _dict:
            args['user_info'] = UserInfo.from_dict(_dict.get('user_info'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'definition_id' in _dict:
            args['definition_id'] = _dict.get('definition_id')
        else:
            raise ValueError('Required property \'definition_id\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'worker' in _dict:
            args['worker'] = PipelineRunWorker.from_dict(_dict.get('worker'))
        else:
            raise ValueError('Required property \'worker\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'pipeline_id' in _dict:
            args['pipeline_id'] = _dict.get('pipeline_id')
        else:
            raise ValueError('Required property \'pipeline_id\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'listener_name' in _dict:
            args['listener_name'] = _dict.get('listener_name')
        else:
            raise ValueError('Required property \'listener_name\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'trigger' in _dict:
            args['trigger'] = _dict.get('trigger')
        else:
            raise ValueError('Required property \'trigger\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'event_params_blob' in _dict:
            args['event_params_blob'] = _dict.get('event_params_blob')
        else:
            raise ValueError('Required property \'event_params_blob\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'event_header_params_blob' in _dict:
            args['event_header_params_blob'] = _dict.get('event_header_params_blob')
        if 'properties' in _dict:
            args['properties'] = [Property.from_dict(x) for x in _dict.get('properties')]
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'run_url' in _dict:
            args['run_url'] = _dict.get('run_url')
        else:
            raise ValueError('Required property \'run_url\' not present in PipelineRunsCollectionPipelineRunsItem JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsCollectionPipelineRunsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'user_info') and self.user_info is not None:
            _dict['user_info'] = self.user_info.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'definition_id') and self.definition_id is not None:
            _dict['definition_id'] = self.definition_id
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'pipeline_id') and self.pipeline_id is not None:
            _dict['pipeline_id'] = self.pipeline_id
        if hasattr(self, 'listener_name') and self.listener_name is not None:
            _dict['listener_name'] = self.listener_name
        if hasattr(self, 'trigger') and self.trigger is not None:
            if isinstance(self.trigger, dict):
                _dict['trigger'] = self.trigger
            else:
                _dict['trigger'] = self.trigger.to_dict()
        if hasattr(self, 'event_params_blob') and self.event_params_blob is not None:
            _dict['event_params_blob'] = self.event_params_blob
        if hasattr(self, 'event_header_params_blob') and self.event_header_params_blob is not None:
            _dict['event_header_params_blob'] = self.event_header_params_blob
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'run_url') and self.run_url is not None:
            _dict['run_url'] = self.run_url
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunsCollectionPipelineRunsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsCollectionPipelineRunsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsCollectionPipelineRunsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status of the pipeline run.
        """
        PENDING = 'pending'
        WAITING = 'waiting'
        QUEUED = 'queued'
        RUNNING = 'running'
        CANCELLED = 'cancelled'
        CANCELLING = 'cancelling'
        FAILED = 'failed'
        ERROR = 'error'
        SUCCEEDED = 'succeeded'


class PropertiesCollection():
    """
    Pipeline properties object.

    :attr List[Property] properties: Pipeline properties list.
    """

    def __init__(self,
                 properties: List['Property']) -> None:
        """
        Initialize a PropertiesCollection object.

        :param List[Property] properties: Pipeline properties list.
        """
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PropertiesCollection':
        """Initialize a PropertiesCollection object from a json dictionary."""
        args = {}
        if 'properties' in _dict:
            args['properties'] = [Property.from_dict(x) for x in _dict.get('properties')]
        else:
            raise ValueError('Required property \'properties\' not present in PropertiesCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PropertiesCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PropertiesCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PropertiesCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PropertiesCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Property():
    """
    Property object.

    :attr str name: Property name.
    :attr str value: (optional) Property value.
    :attr List[str] enum: (optional) Options for `single_select` property type. Only
          needed when using `single_select` property type.
    :attr str type: Property type.
    :attr str path: (optional) A dot notation path for `integration` type properties
          to select a value from the tool integration.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 path: str = None) -> None:
        """
        Initialize a Property object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed when using `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.type = type
        self.path = path

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Property':
        """Initialize a Property object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in Property JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in Property JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Property object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Property object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Property') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Property') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


class TektonPipeline():
    """
    Tekton pipeline object.

    :attr str name: String.
    :attr str status: Pipeline status.
    :attr str resource_group_id: ID.
    :attr Toolchain toolchain: Toolchain object.
    :attr str id: UUID.
    :attr List[Definition] definitions: Definition list.
    :attr List[Property] properties: Tekton pipeline's environment properties.
    :attr datetime updated_at: (optional) Standard RFC 3339 Date Time String.
    :attr datetime created_at: (optional) Standard RFC 3339 Date Time String.
    :attr TektonPipelinePipelineDefinition pipeline_definition: (optional) Tekton
          pipeline definition object. If this property is absent or empty, the pipeline
          has no definitions added.
    :attr List[Trigger] triggers: Tekton pipeline triggers list.
    :attr Worker worker: Default pipeline worker used to run the pipeline.
    :attr str runs_url: URL for this pipeline showing the list of pipeline runs.
    :attr int build_number: (optional) The latest pipeline run build number. If this
          property is absent, the pipeline hasn't had any pipeline runs.
    :attr bool enable_slack_notifications: (optional) Flag whether to enable slack
          notifications for this pipeline. When enabled, pipeline run events will be
          published on all slack integration specified channels in the enclosing
          toolchain.
    :attr bool enable_partial_cloning: (optional) Flag whether to enable partial
          cloning for this pipeline. When partial clone is enabled, only the files
          contained within the paths specified in definition repositories will be read and
          cloned. This means symbolic links may not work.
    :attr bool enabled: Flag whether this pipeline is enabled.
    """

    def __init__(self,
                 name: str,
                 status: str,
                 resource_group_id: str,
                 toolchain: 'Toolchain',
                 id: str,
                 definitions: List['Definition'],
                 properties: List['Property'],
                 triggers: List['Trigger'],
                 worker: 'Worker',
                 runs_url: str,
                 enabled: bool,
                 *,
                 updated_at: datetime = None,
                 created_at: datetime = None,
                 pipeline_definition: 'TektonPipelinePipelineDefinition' = None,
                 build_number: int = None,
                 enable_slack_notifications: bool = None,
                 enable_partial_cloning: bool = None) -> None:
        """
        Initialize a TektonPipeline object.

        :param str name: String.
        :param str status: Pipeline status.
        :param str resource_group_id: ID.
        :param Toolchain toolchain: Toolchain object.
        :param str id: UUID.
        :param List[Definition] definitions: Definition list.
        :param List[Property] properties: Tekton pipeline's environment properties.
        :param List[Trigger] triggers: Tekton pipeline triggers list.
        :param Worker worker: Default pipeline worker used to run the pipeline.
        :param str runs_url: URL for this pipeline showing the list of pipeline
               runs.
        :param bool enabled: Flag whether this pipeline is enabled.
        :param datetime updated_at: (optional) Standard RFC 3339 Date Time String.
        :param datetime created_at: (optional) Standard RFC 3339 Date Time String.
        :param TektonPipelinePipelineDefinition pipeline_definition: (optional)
               Tekton pipeline definition object. If this property is absent or empty, the
               pipeline has no definitions added.
        :param int build_number: (optional) The latest pipeline run build number.
               If this property is absent, the pipeline hasn't had any pipeline runs.
        :param bool enable_slack_notifications: (optional) Flag whether to enable
               slack notifications for this pipeline. When enabled, pipeline run events
               will be published on all slack integration specified channels in the
               enclosing toolchain.
        :param bool enable_partial_cloning: (optional) Flag whether to enable
               partial cloning for this pipeline. When partial clone is enabled, only the
               files contained within the paths specified in definition repositories will
               be read and cloned. This means symbolic links may not work.
        """
        self.name = name
        self.status = status
        self.resource_group_id = resource_group_id
        self.toolchain = toolchain
        self.id = id
        self.definitions = definitions
        self.properties = properties
        self.updated_at = updated_at
        self.created_at = created_at
        self.pipeline_definition = pipeline_definition
        self.triggers = triggers
        self.worker = worker
        self.runs_url = runs_url
        self.build_number = build_number
        self.enable_slack_notifications = enable_slack_notifications
        self.enable_partial_cloning = enable_partial_cloning
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TektonPipeline':
        """Initialize a TektonPipeline object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TektonPipeline JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in TektonPipeline JSON')
        if 'resource_group_id' in _dict:
            args['resource_group_id'] = _dict.get('resource_group_id')
        else:
            raise ValueError('Required property \'resource_group_id\' not present in TektonPipeline JSON')
        if 'toolchain' in _dict:
            args['toolchain'] = Toolchain.from_dict(_dict.get('toolchain'))
        else:
            raise ValueError('Required property \'toolchain\' not present in TektonPipeline JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in TektonPipeline JSON')
        if 'definitions' in _dict:
            args['definitions'] = [Definition.from_dict(x) for x in _dict.get('definitions')]
        else:
            raise ValueError('Required property \'definitions\' not present in TektonPipeline JSON')
        if 'properties' in _dict:
            args['properties'] = [Property.from_dict(x) for x in _dict.get('properties')]
        else:
            raise ValueError('Required property \'properties\' not present in TektonPipeline JSON')
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'pipeline_definition' in _dict:
            args['pipeline_definition'] = TektonPipelinePipelineDefinition.from_dict(_dict.get('pipeline_definition'))
        if 'triggers' in _dict:
            args['triggers'] = _dict.get('triggers')
        else:
            raise ValueError('Required property \'triggers\' not present in TektonPipeline JSON')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        else:
            raise ValueError('Required property \'worker\' not present in TektonPipeline JSON')
        if 'runs_url' in _dict:
            args['runs_url'] = _dict.get('runs_url')
        else:
            raise ValueError('Required property \'runs_url\' not present in TektonPipeline JSON')
        if 'build_number' in _dict:
            args['build_number'] = _dict.get('build_number')
        if 'enable_slack_notifications' in _dict:
            args['enable_slack_notifications'] = _dict.get('enable_slack_notifications')
        if 'enable_partial_cloning' in _dict:
            args['enable_partial_cloning'] = _dict.get('enable_partial_cloning')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in TektonPipeline JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TektonPipeline object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'resource_group_id') and self.resource_group_id is not None:
            _dict['resource_group_id'] = self.resource_group_id
        if hasattr(self, 'toolchain') and self.toolchain is not None:
            _dict['toolchain'] = self.toolchain.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'definitions') and self.definitions is not None:
            _dict['definitions'] = [x.to_dict() for x in self.definitions]
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'pipeline_definition') and self.pipeline_definition is not None:
            _dict['pipeline_definition'] = self.pipeline_definition.to_dict()
        if hasattr(self, 'triggers') and self.triggers is not None:
            triggers_list = []
            for x in self.triggers:
                if isinstance(x, dict):
                    triggers_list.append(x)
                else:
                    triggers_list.append(x.to_dict())
            _dict['triggers'] = triggers_list
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'runs_url') and self.runs_url is not None:
            _dict['runs_url'] = self.runs_url
        if hasattr(self, 'build_number') and self.build_number is not None:
            _dict['build_number'] = self.build_number
        if hasattr(self, 'enable_slack_notifications') and self.enable_slack_notifications is not None:
            _dict['enable_slack_notifications'] = self.enable_slack_notifications
        if hasattr(self, 'enable_partial_cloning') and self.enable_partial_cloning is not None:
            _dict['enable_partial_cloning'] = self.enable_partial_cloning
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TektonPipeline object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TektonPipeline') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TektonPipeline') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Pipeline status.
        """
        CONFIGURED = 'configured'
        CONFIGURING = 'configuring'


class TektonPipelinePatch():
    """
    Request body used to update this pipeline.

    :attr bool enable_slack_notifications: (optional) Flag whether to enable slack
          notifications for this pipeline. When enabled, pipeline run events will be
          published on all slack integration specified channels in the enclosing
          toolchain.
    :attr bool enable_partial_cloning: (optional) Flag whether to enable partial
          cloning for this pipeline. When partial clone is enabled, only the files
          contained within the paths specified in definition repositories will be read and
          cloned. This means symbolic links may not work.
    :attr WorkerWithId worker: (optional) Worker object containing worker ID only.
          If omitted the IBM Managed shared workers are used by default.
    """

    def __init__(self,
                 *,
                 enable_slack_notifications: bool = None,
                 enable_partial_cloning: bool = None,
                 worker: 'WorkerWithId' = None) -> None:
        """
        Initialize a TektonPipelinePatch object.

        :param bool enable_slack_notifications: (optional) Flag whether to enable
               slack notifications for this pipeline. When enabled, pipeline run events
               will be published on all slack integration specified channels in the
               enclosing toolchain.
        :param bool enable_partial_cloning: (optional) Flag whether to enable
               partial cloning for this pipeline. When partial clone is enabled, only the
               files contained within the paths specified in definition repositories will
               be read and cloned. This means symbolic links may not work.
        :param WorkerWithId worker: (optional) Worker object containing worker ID
               only. If omitted the IBM Managed shared workers are used by default.
        """
        self.enable_slack_notifications = enable_slack_notifications
        self.enable_partial_cloning = enable_partial_cloning
        self.worker = worker

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TektonPipelinePatch':
        """Initialize a TektonPipelinePatch object from a json dictionary."""
        args = {}
        if 'enable_slack_notifications' in _dict:
            args['enable_slack_notifications'] = _dict.get('enable_slack_notifications')
        if 'enable_partial_cloning' in _dict:
            args['enable_partial_cloning'] = _dict.get('enable_partial_cloning')
        if 'worker' in _dict:
            args['worker'] = WorkerWithId.from_dict(_dict.get('worker'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TektonPipelinePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enable_slack_notifications') and self.enable_slack_notifications is not None:
            _dict['enable_slack_notifications'] = self.enable_slack_notifications
        if hasattr(self, 'enable_partial_cloning') and self.enable_partial_cloning is not None:
            _dict['enable_partial_cloning'] = self.enable_partial_cloning
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TektonPipelinePatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TektonPipelinePatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TektonPipelinePatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TektonPipelinePipelineDefinition():
    """
    Tekton pipeline definition object. If this property is absent or empty, the pipeline
    has no definitions added.

    :attr str status: (optional) The pipeline definition status.
    :attr str id: (optional) UUID.
    """

    def __init__(self,
                 *,
                 status: str = None,
                 id: str = None) -> None:
        """
        Initialize a TektonPipelinePipelineDefinition object.

        :param str status: (optional) The pipeline definition status.
        :param str id: (optional) UUID.
        """
        self.status = status
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TektonPipelinePipelineDefinition':
        """Initialize a TektonPipelinePipelineDefinition object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TektonPipelinePipelineDefinition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TektonPipelinePipelineDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TektonPipelinePipelineDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TektonPipelinePipelineDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The pipeline definition status.
        """
        UPDATED = 'updated'
        OUTDATED = 'outdated'
        UPDATING = 'updating'
        FAILED = 'failed'


class Toolchain():
    """
    Toolchain object.

    :attr str id: UUID.
    :attr str crn: The CRN for the toolchain that contains the Tekton pipeline.
    """

    def __init__(self,
                 id: str,
                 crn: str) -> None:
        """
        Initialize a Toolchain object.

        :param str id: UUID.
        :param str crn: The CRN for the toolchain that contains the Tekton
               pipeline.
        """
        self.id = id
        self.crn = crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Toolchain':
        """Initialize a Toolchain object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Toolchain JSON')
        if 'crn' in _dict:
            args['crn'] = _dict.get('crn')
        else:
            raise ValueError('Required property \'crn\' not present in Toolchain JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Toolchain object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'crn') and self.crn is not None:
            _dict['crn'] = self.crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Toolchain object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Toolchain') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Toolchain') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Trigger():
    """
    Tekton pipeline trigger.

    """

    def __init__(self) -> None:
        """
        Initialize a Trigger object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['TriggerManualTrigger', 'TriggerScmTrigger', 'TriggerTimerTrigger', 'TriggerGenericTrigger']))
        raise Exception(msg)

class TriggerGenericTriggerPropertiesItem():
    """
    Trigger property object.

    :attr str name: Property name.
    :attr str value: (optional) Property value. Can be empty and should be omitted
          for `single_select` property type.
    :attr List[str] enum: (optional) Options for `single_select` property type. Only
          needed for `single_select` property type.
    :attr str type: Property type.
    :attr str path: (optional) A dot notation path for `integration` type properties
          to select a value from the tool integration. If left blank the full tool
          integration data will be used.
    :attr str href: (optional) API URL for interacting with the trigger property.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerGenericTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Can be empty and should be
               omitted for `single_select` property type.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        :param str href: (optional) API URL for interacting with the trigger
               property.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerGenericTriggerPropertiesItem':
        """Initialize a TriggerGenericTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerGenericTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerGenericTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerGenericTriggerPropertiesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerGenericTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerGenericTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerGenericTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


class TriggerManualTriggerPropertiesItem():
    """
    Trigger property object.

    :attr str name: Property name.
    :attr str value: (optional) Property value. Can be empty and should be omitted
          for `single_select` property type.
    :attr List[str] enum: (optional) Options for `single_select` property type. Only
          needed for `single_select` property type.
    :attr str type: Property type.
    :attr str path: (optional) A dot notation path for `integration` type properties
          to select a value from the tool integration. If left blank the full tool
          integration data will be used.
    :attr str href: (optional) API URL for interacting with the trigger property.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerManualTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Can be empty and should be
               omitted for `single_select` property type.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        :param str href: (optional) API URL for interacting with the trigger
               property.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerManualTriggerPropertiesItem':
        """Initialize a TriggerManualTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerManualTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerManualTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerManualTriggerPropertiesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerManualTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerManualTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerManualTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


class TriggerPatch():
    """
    Tekton pipeline trigger object used for updating the trigger.

    :attr str type: (optional) Trigger type.
    :attr str name: (optional) Trigger name.
    :attr str event_listener: (optional) Event listener name. The name of the event
          listener to which the trigger is associated. The event listeners are defined in
          the definition repositories of the Tekton pipeline.
    :attr List[str] tags: (optional) Trigger tags array. Optional tags for the
          trigger.
    :attr Worker worker: (optional) Worker used to run the trigger. If not specified
          the trigger will use the default pipeline worker.
    :attr int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. Omit this property to disable the concurrency
          limit.
    :attr bool disabled: (optional) Defines if this trigger is disabled.
    :attr GenericSecret secret: (optional) Only needed for generic webhook trigger
          type. Secret used to start generic webhook trigger.
    :attr str cron: (optional) Only needed for timer triggers. Cron expression for
          timer trigger.
    :attr str timezone: (optional) Only needed for timer triggers. Timezone for
          timer trigger.
    :attr TriggerScmSource scm_source: (optional) SCM source repository for a Git
          trigger. Only needed for Git triggers.
    :attr Events events: (optional) Only needed for Git triggers. Events object
          defines the events to which this Git trigger listens.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 name: str = None,
                 event_listener: str = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 max_concurrent_runs: int = None,
                 disabled: bool = None,
                 secret: 'GenericSecret' = None,
                 cron: str = None,
                 timezone: str = None,
                 scm_source: 'TriggerScmSource' = None,
                 events: 'Events' = None) -> None:
        """
        Initialize a TriggerPatch object.

        :param str type: (optional) Trigger type.
        :param str name: (optional) Trigger name.
        :param str event_listener: (optional) Event listener name. The name of the
               event listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param List[str] tags: (optional) Trigger tags array. Optional tags for the
               trigger.
        :param Worker worker: (optional) Worker used to run the trigger. If not
               specified the trigger will use the default pipeline worker.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. Omit this property to disable the
               concurrency limit.
        :param bool disabled: (optional) Defines if this trigger is disabled.
        :param GenericSecret secret: (optional) Only needed for generic webhook
               trigger type. Secret used to start generic webhook trigger.
        :param str cron: (optional) Only needed for timer triggers. Cron expression
               for timer trigger.
        :param str timezone: (optional) Only needed for timer triggers. Timezone
               for timer trigger.
        :param TriggerScmSource scm_source: (optional) SCM source repository for a
               Git trigger. Only needed for Git triggers.
        :param Events events: (optional) Only needed for Git triggers. Events
               object defines the events to which this Git trigger listens.
        """
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.tags = tags
        self.worker = worker
        self.max_concurrent_runs = max_concurrent_runs
        self.disabled = disabled
        self.secret = secret
        self.cron = cron
        self.timezone = timezone
        self.scm_source = scm_source
        self.events = events

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerPatch':
        """Initialize a TriggerPatch object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'max_concurrent_runs' in _dict:
            args['max_concurrent_runs'] = _dict.get('max_concurrent_runs')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        if 'secret' in _dict:
            args['secret'] = GenericSecret.from_dict(_dict.get('secret'))
        if 'cron' in _dict:
            args['cron'] = _dict.get('cron')
        if 'timezone' in _dict:
            args['timezone'] = _dict.get('timezone')
        if 'scm_source' in _dict:
            args['scm_source'] = TriggerScmSource.from_dict(_dict.get('scm_source'))
        if 'events' in _dict:
            args['events'] = Events.from_dict(_dict.get('events'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerPatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'event_listener') and self.event_listener is not None:
            _dict['event_listener'] = self.event_listener
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'secret') and self.secret is not None:
            _dict['secret'] = self.secret.to_dict()
        if hasattr(self, 'cron') and self.cron is not None:
            _dict['cron'] = self.cron
        if hasattr(self, 'timezone') and self.timezone is not None:
            _dict['timezone'] = self.timezone
        if hasattr(self, 'scm_source') and self.scm_source is not None:
            _dict['scm_source'] = self.scm_source.to_dict()
        if hasattr(self, 'events') and self.events is not None:
            _dict['events'] = self.events.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerPatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerPatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerPatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Trigger type.
        """
        MANUAL = 'manual'
        SCM = 'scm'
        TIMER = 'timer'
        GENERIC = 'generic'


class TriggerPropertiesCollection():
    """
    Trigger properties object.

    :attr List[TriggerPropertiesCollectionPropertiesItem] properties: Trigger
          properties list.
    """

    def __init__(self,
                 properties: List['TriggerPropertiesCollectionPropertiesItem']) -> None:
        """
        Initialize a TriggerPropertiesCollection object.

        :param List[TriggerPropertiesCollectionPropertiesItem] properties: Trigger
               properties list.
        """
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerPropertiesCollection':
        """Initialize a TriggerPropertiesCollection object from a json dictionary."""
        args = {}
        if 'properties' in _dict:
            args['properties'] = [TriggerPropertiesCollectionPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        else:
            raise ValueError('Required property \'properties\' not present in TriggerPropertiesCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerPropertiesCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerPropertiesCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerPropertiesCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerPropertiesCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerPropertiesCollectionPropertiesItem():
    """
    Trigger property object.

    :attr str name: Property name.
    :attr str value: (optional) Property value. Can be empty and should be omitted
          for `single_select` property type.
    :attr List[str] enum: (optional) Options for `single_select` property type. Only
          needed for `single_select` property type.
    :attr str type: Property type.
    :attr str path: (optional) A dot notation path for `integration` type properties
          to select a value from the tool integration. If left blank the full tool
          integration data will be used.
    :attr str href: (optional) API URL for interacting with the trigger property.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerPropertiesCollectionPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Can be empty and should be
               omitted for `single_select` property type.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        :param str href: (optional) API URL for interacting with the trigger
               property.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerPropertiesCollectionPropertiesItem':
        """Initialize a TriggerPropertiesCollectionPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerPropertiesCollectionPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerPropertiesCollectionPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerPropertiesCollectionPropertiesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerPropertiesCollectionPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerPropertiesCollectionPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerPropertiesCollectionPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


class TriggerProperty():
    """
    Trigger property object.

    :attr str name: Property name.
    :attr str value: (optional) Property value. Can be empty and should be omitted
          for `single_select` property type.
    :attr List[str] enum: (optional) Options for `single_select` property type. Only
          needed for `single_select` property type.
    :attr str type: Property type.
    :attr str path: (optional) A dot notation path for `integration` type properties
          to select a value from the tool integration. If left blank the full tool
          integration data will be used.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 path: str = None) -> None:
        """
        Initialize a TriggerProperty object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Can be empty and should be
               omitted for `single_select` property type.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.type = type
        self.path = path

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerProperty':
        """Initialize a TriggerProperty object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerProperty JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerProperty JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerProperty object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerProperty object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerProperty') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerProperty') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


class TriggerScmSource():
    """
    SCM source repository for a Git trigger. Only needed for Git triggers.

    :attr str url: URL of the repository to which the trigger is listening.
    :attr str branch: (optional) Name of a branch from the repo. One of branch or
          tag must be specified, but only one or the other.
    :attr str pattern: (optional) Git branch or tag pattern to listen to. Please
          refer to https://github.com/micromatch/micromatch for pattern syntax.
    :attr bool blind_connection: (optional) True if the repository server is not
          addressable on the public internet. IBM Cloud will not be able to validate the
          connection details you provide.
    :attr str hook_id: (optional) ID of the webhook from the repo. Computed upon
          creation of the trigger.
    :attr str service_instance_id: (optional) ID of the repository service instance.
    """

    def __init__(self,
                 url: str,
                 *,
                 branch: str = None,
                 pattern: str = None,
                 blind_connection: bool = None,
                 hook_id: str = None,
                 service_instance_id: str = None) -> None:
        """
        Initialize a TriggerScmSource object.

        :param str url: URL of the repository to which the trigger is listening.
        :param str branch: (optional) Name of a branch from the repo. One of branch
               or tag must be specified, but only one or the other.
        :param str pattern: (optional) Git branch or tag pattern to listen to.
               Please refer to https://github.com/micromatch/micromatch for pattern
               syntax.
        :param bool blind_connection: (optional) True if the repository server is
               not addressable on the public internet. IBM Cloud will not be able to
               validate the connection details you provide.
        :param str hook_id: (optional) ID of the webhook from the repo. Computed
               upon creation of the trigger.
        :param str service_instance_id: (optional) ID of the repository service
               instance.
        """
        self.url = url
        self.branch = branch
        self.pattern = pattern
        self.blind_connection = blind_connection
        self.hook_id = hook_id
        self.service_instance_id = service_instance_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerScmSource':
        """Initialize a TriggerScmSource object from a json dictionary."""
        args = {}
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in TriggerScmSource JSON')
        if 'branch' in _dict:
            args['branch'] = _dict.get('branch')
        if 'pattern' in _dict:
            args['pattern'] = _dict.get('pattern')
        if 'blind_connection' in _dict:
            args['blind_connection'] = _dict.get('blind_connection')
        if 'hook_id' in _dict:
            args['hook_id'] = _dict.get('hook_id')
        if 'service_instance_id' in _dict:
            args['service_instance_id'] = _dict.get('service_instance_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerScmSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'branch') and self.branch is not None:
            _dict['branch'] = self.branch
        if hasattr(self, 'pattern') and self.pattern is not None:
            _dict['pattern'] = self.pattern
        if hasattr(self, 'blind_connection') and self.blind_connection is not None:
            _dict['blind_connection'] = self.blind_connection
        if hasattr(self, 'hook_id') and self.hook_id is not None:
            _dict['hook_id'] = self.hook_id
        if hasattr(self, 'service_instance_id') and self.service_instance_id is not None:
            _dict['service_instance_id'] = self.service_instance_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerScmSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerScmSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerScmSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerScmTriggerPropertiesItem():
    """
    Trigger property object.

    :attr str name: Property name.
    :attr str value: (optional) Property value. Can be empty and should be omitted
          for `single_select` property type.
    :attr List[str] enum: (optional) Options for `single_select` property type. Only
          needed for `single_select` property type.
    :attr str type: Property type.
    :attr str path: (optional) A dot notation path for `integration` type properties
          to select a value from the tool integration. If left blank the full tool
          integration data will be used.
    :attr str href: (optional) API URL for interacting with the trigger property.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerScmTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Can be empty and should be
               omitted for `single_select` property type.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        :param str href: (optional) API URL for interacting with the trigger
               property.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerScmTriggerPropertiesItem':
        """Initialize a TriggerScmTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerScmTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerScmTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerScmTriggerPropertiesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerScmTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerScmTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerScmTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


class TriggerTimerTriggerPropertiesItem():
    """
    Trigger property object.

    :attr str name: Property name.
    :attr str value: (optional) Property value. Can be empty and should be omitted
          for `single_select` property type.
    :attr List[str] enum: (optional) Options for `single_select` property type. Only
          needed for `single_select` property type.
    :attr str type: Property type.
    :attr str path: (optional) A dot notation path for `integration` type properties
          to select a value from the tool integration. If left blank the full tool
          integration data will be used.
    :attr str href: (optional) API URL for interacting with the trigger property.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerTimerTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Can be empty and should be
               omitted for `single_select` property type.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties to select a value from the tool integration. If left blank the
               full tool integration data will be used.
        :param str href: (optional) API URL for interacting with the trigger
               property.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerTimerTriggerPropertiesItem':
        """Initialize a TriggerTimerTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerTimerTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerTimerTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerTimerTriggerPropertiesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerTimerTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerTimerTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerTimerTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'secure'
        TEXT = 'text'
        INTEGRATION = 'integration'
        SINGLE_SELECT = 'single_select'
        APPCONFIG = 'appconfig'


class TriggersCollection():
    """
    Tekton pipeline triggers object.

    :attr List[Trigger] triggers: Tekton pipeline triggers list.
    """

    def __init__(self,
                 triggers: List['Trigger']) -> None:
        """
        Initialize a TriggersCollection object.

        :param List[Trigger] triggers: Tekton pipeline triggers list.
        """
        self.triggers = triggers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersCollection':
        """Initialize a TriggersCollection object from a json dictionary."""
        args = {}
        if 'triggers' in _dict:
            args['triggers'] = _dict.get('triggers')
        else:
            raise ValueError('Required property \'triggers\' not present in TriggersCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'triggers') and self.triggers is not None:
            triggers_list = []
            for x in self.triggers:
                if isinstance(x, dict):
                    triggers_list.append(x)
                else:
                    triggers_list.append(x.to_dict())
            _dict['triggers'] = triggers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggersCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UserInfo():
    """
    User information.

    :attr str iam_id: IBM Cloud IAM ID.
    :attr str sub: User email address.
    """

    def __init__(self,
                 iam_id: str,
                 sub: str) -> None:
        """
        Initialize a UserInfo object.

        :param str iam_id: IBM Cloud IAM ID.
        :param str sub: User email address.
        """
        self.iam_id = iam_id
        self.sub = sub

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UserInfo':
        """Initialize a UserInfo object from a json dictionary."""
        args = {}
        if 'iam_id' in _dict:
            args['iam_id'] = _dict.get('iam_id')
        else:
            raise ValueError('Required property \'iam_id\' not present in UserInfo JSON')
        if 'sub' in _dict:
            args['sub'] = _dict.get('sub')
        else:
            raise ValueError('Required property \'sub\' not present in UserInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UserInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'iam_id') and self.iam_id is not None:
            _dict['iam_id'] = self.iam_id
        if hasattr(self, 'sub') and self.sub is not None:
            _dict['sub'] = self.sub
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UserInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UserInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UserInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Worker():
    """
    Default pipeline worker used to run the pipeline.

    :attr str name: (optional) Name of the worker. Computed based on the worker ID.
    :attr str type: (optional) Type of the worker. Computed based on the worker ID.
    :attr str id: ID of the worker.
    """

    def __init__(self,
                 id: str,
                 *,
                 name: str = None,
                 type: str = None) -> None:
        """
        Initialize a Worker object.

        :param str id: ID of the worker.
        :param str name: (optional) Name of the worker. Computed based on the
               worker ID.
        :param str type: (optional) Type of the worker. Computed based on the
               worker ID.
        """
        self.name = name
        self.type = type
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Worker':
        """Initialize a Worker object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Worker JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Worker object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Worker object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Worker') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Worker') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WorkerWithId():
    """
    Worker object containing worker ID only. If omitted the IBM Managed shared workers are
    used by default.

    :attr str id: ID of the worker.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a WorkerWithId object.

        :param str id: ID of the worker.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkerWithId':
        """Initialize a WorkerWithId object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in WorkerWithId JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkerWithId object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WorkerWithId object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkerWithId') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkerWithId') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerGenericTrigger(Trigger):
    """
    Generic webhook trigger, which triggers a pipeline run when the Tekton Pipeline
    Service receives a POST event with secrets.

    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str href: (optional) API URL for interacting with the trigger.
    :attr str event_listener: Event listener name. The name of the event listener to
          which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :attr str id: (optional) ID.
    :attr List[TriggerGenericTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Worker used to run the trigger. If not specified
          the trigger will use the default pipeline worker.
    :attr int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. Omit this property to disable the concurrency
          limit.
    :attr bool disabled: Flag whether the trigger is disabled. If omitted the
          trigger is enabled by default.
    :attr GenericSecret secret: (optional) Only needed for generic webhook trigger
          type. Secret used to start generic webhook trigger.
    :attr str webhook_url: (optional) Webhook URL that can be used to trigger
          pipeline runs.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 href: str = None,
                 id: str = None,
                 properties: List['TriggerGenericTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 max_concurrent_runs: int = None,
                 secret: 'GenericSecret' = None,
                 webhook_url: str = None) -> None:
        """
        Initialize a TriggerGenericTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param bool disabled: Flag whether the trigger is disabled. If omitted the
               trigger is enabled by default.
        :param str href: (optional) API URL for interacting with the trigger.
        :param str id: (optional) ID.
        :param List[TriggerGenericTriggerPropertiesItem] properties: (optional)
               Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Worker used to run the trigger. If not
               specified the trigger will use the default pipeline worker.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. Omit this property to disable the
               concurrency limit.
        :param GenericSecret secret: (optional) Only needed for generic webhook
               trigger type. Secret used to start generic webhook trigger.
        :param str webhook_url: (optional) Webhook URL that can be used to trigger
               pipeline runs.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.href = href
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.max_concurrent_runs = max_concurrent_runs
        self.disabled = disabled
        self.secret = secret
        self.webhook_url = webhook_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerGenericTrigger':
        """Initialize a TriggerGenericTrigger object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerGenericTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerGenericTrigger JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerGenericTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggerGenericTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'max_concurrent_runs' in _dict:
            args['max_concurrent_runs'] = _dict.get('max_concurrent_runs')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggerGenericTrigger JSON')
        if 'secret' in _dict:
            args['secret'] = GenericSecret.from_dict(_dict.get('secret'))
        if 'webhook_url' in _dict:
            args['webhook_url'] = _dict.get('webhook_url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerGenericTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'event_listener') and self.event_listener is not None:
            _dict['event_listener'] = self.event_listener
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'secret') and self.secret is not None:
            _dict['secret'] = self.secret.to_dict()
        if hasattr(self, 'webhook_url') and self.webhook_url is not None:
            _dict['webhook_url'] = self.webhook_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerGenericTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerGenericTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerGenericTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerManualTrigger(Trigger):
    """
    Manual trigger.

    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str href: (optional) API URL for interacting with the trigger.
    :attr str event_listener: Event listener name. The name of the event listener to
          which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :attr str id: (optional) ID.
    :attr List[TriggerManualTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Worker used to run the trigger. If not specified
          the trigger will use the default pipeline worker.
    :attr int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. Omit this property to disable the concurrency
          limit.
    :attr bool disabled: Flag whether the trigger is disabled. If omitted the
          trigger is enabled by default.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 href: str = None,
                 id: str = None,
                 properties: List['TriggerManualTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 max_concurrent_runs: int = None) -> None:
        """
        Initialize a TriggerManualTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param bool disabled: Flag whether the trigger is disabled. If omitted the
               trigger is enabled by default.
        :param str href: (optional) API URL for interacting with the trigger.
        :param str id: (optional) ID.
        :param List[TriggerManualTriggerPropertiesItem] properties: (optional)
               Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Worker used to run the trigger. If not
               specified the trigger will use the default pipeline worker.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. Omit this property to disable the
               concurrency limit.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.href = href
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.max_concurrent_runs = max_concurrent_runs
        self.disabled = disabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerManualTrigger':
        """Initialize a TriggerManualTrigger object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerManualTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerManualTrigger JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerManualTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggerManualTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'max_concurrent_runs' in _dict:
            args['max_concurrent_runs'] = _dict.get('max_concurrent_runs')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggerManualTrigger JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerManualTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'event_listener') and self.event_listener is not None:
            _dict['event_listener'] = self.event_listener
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerManualTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerManualTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerManualTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerScmTrigger(Trigger):
    """
    Git type trigger, which automatically triggers a pipeline run when the Tekton Pipeline
    Service receives a corresponding Git webhook event.

    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str href: (optional) API URL for interacting with the trigger.
    :attr str event_listener: Event listener name. The name of the event listener to
          which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :attr str id: (optional) ID.
    :attr List[TriggerScmTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Worker used to run the trigger. If not specified
          the trigger will use the default pipeline worker.
    :attr int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. Omit this property to disable the concurrency
          limit.
    :attr bool disabled: Flag whether the trigger is disabled. If omitted the
          trigger is enabled by default.
    :attr TriggerScmSource scm_source: (optional) SCM source repository for a Git
          trigger. Only needed for Git triggers.
    :attr Events events: (optional) Only needed for Git triggers. Events object
          defines the events to which this Git trigger listens.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 href: str = None,
                 id: str = None,
                 properties: List['TriggerScmTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 max_concurrent_runs: int = None,
                 scm_source: 'TriggerScmSource' = None,
                 events: 'Events' = None) -> None:
        """
        Initialize a TriggerScmTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param bool disabled: Flag whether the trigger is disabled. If omitted the
               trigger is enabled by default.
        :param str href: (optional) API URL for interacting with the trigger.
        :param str id: (optional) ID.
        :param List[TriggerScmTriggerPropertiesItem] properties: (optional) Trigger
               properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Worker used to run the trigger. If not
               specified the trigger will use the default pipeline worker.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. Omit this property to disable the
               concurrency limit.
        :param TriggerScmSource scm_source: (optional) SCM source repository for a
               Git trigger. Only needed for Git triggers.
        :param Events events: (optional) Only needed for Git triggers. Events
               object defines the events to which this Git trigger listens.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.href = href
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.max_concurrent_runs = max_concurrent_runs
        self.disabled = disabled
        self.scm_source = scm_source
        self.events = events

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerScmTrigger':
        """Initialize a TriggerScmTrigger object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerScmTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerScmTrigger JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerScmTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggerScmTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'max_concurrent_runs' in _dict:
            args['max_concurrent_runs'] = _dict.get('max_concurrent_runs')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggerScmTrigger JSON')
        if 'scm_source' in _dict:
            args['scm_source'] = TriggerScmSource.from_dict(_dict.get('scm_source'))
        if 'events' in _dict:
            args['events'] = Events.from_dict(_dict.get('events'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerScmTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'event_listener') and self.event_listener is not None:
            _dict['event_listener'] = self.event_listener
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'scm_source') and self.scm_source is not None:
            _dict['scm_source'] = self.scm_source.to_dict()
        if hasattr(self, 'events') and self.events is not None:
            _dict['events'] = self.events.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerScmTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerScmTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerScmTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerTimerTrigger(Trigger):
    """
    Timer trigger, which triggers pipeline run according to the cron value and time zone.

    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str href: (optional) API URL for interacting with the trigger.
    :attr str event_listener: Event listener name. The name of the event listener to
          which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :attr str id: (optional) ID.
    :attr List[TriggerTimerTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Worker used to run the trigger. If not specified
          the trigger will use the default pipeline worker.
    :attr int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. Omit this property to disable the concurrency
          limit.
    :attr bool disabled: Flag whether the trigger is disabled. If omitted the
          trigger is enabled by default.
    :attr str cron: (optional) Only needed for timer triggers. Cron expression for
          timer trigger. Maximum frequency is every 5 minutes.
    :attr str timezone: (optional) Only needed for timer triggers. Timezone for
          timer trigger.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 href: str = None,
                 id: str = None,
                 properties: List['TriggerTimerTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 max_concurrent_runs: int = None,
                 cron: str = None,
                 timezone: str = None) -> None:
        """
        Initialize a TriggerTimerTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param bool disabled: Flag whether the trigger is disabled. If omitted the
               trigger is enabled by default.
        :param str href: (optional) API URL for interacting with the trigger.
        :param str id: (optional) ID.
        :param List[TriggerTimerTriggerPropertiesItem] properties: (optional)
               Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Worker used to run the trigger. If not
               specified the trigger will use the default pipeline worker.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. Omit this property to disable the
               concurrency limit.
        :param str cron: (optional) Only needed for timer triggers. Cron expression
               for timer trigger. Maximum frequency is every 5 minutes.
        :param str timezone: (optional) Only needed for timer triggers. Timezone
               for timer trigger.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.href = href
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.max_concurrent_runs = max_concurrent_runs
        self.disabled = disabled
        self.cron = cron
        self.timezone = timezone

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerTimerTrigger':
        """Initialize a TriggerTimerTrigger object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerTimerTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerTimerTrigger JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerTimerTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggerTimerTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'max_concurrent_runs' in _dict:
            args['max_concurrent_runs'] = _dict.get('max_concurrent_runs')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggerTimerTrigger JSON')
        if 'cron' in _dict:
            args['cron'] = _dict.get('cron')
        if 'timezone' in _dict:
            args['timezone'] = _dict.get('timezone')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerTimerTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'event_listener') and self.event_listener is not None:
            _dict['event_listener'] = self.event_listener
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = [x.to_dict() for x in self.properties]
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'cron') and self.cron is not None:
            _dict['cron'] = self.cron
        if hasattr(self, 'timezone') and self.timezone is not None:
            _dict['timezone'] = self.timezone
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerTimerTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerTimerTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerTimerTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

##############################################################################
# Pagers
##############################################################################

class TektonPipelineRunsPager():
    """
    TektonPipelineRunsPager can be used to simplify the use of the "list_tekton_pipeline_runs" method.
    """

    def __init__(self,
                 *,
                 client: CdTektonPipelineV2,
                 pipeline_id: str,
                 limit: int = None,
                 offset: int = None,
                 status: str = None,
                 trigger_name: str = None,
    ) -> None:
        """
        Initialize a TektonPipelineRunsPager object.
        :param str pipeline_id: The Tekton pipeline ID.
        :param int limit: (optional) The number of pipeline runs to return, sorted
               by creation time, most recent first.
        :param int offset: (optional) Skip the specified number of pipeline runs.
               Cannot be used in combination with `start`.
        :param str status: (optional) Filters the collection to resources with the
               specified status.
        :param str trigger_name: (optional) Filters the collection to resources
               with the specified trigger name.
        """
        self._has_next = True
        self._client = client
        self._page_context = { 'next': None }
        self._pipeline_id = pipeline_id
        self._limit = limit
        self._offset = offset
        self._status = status
        self._trigger_name = trigger_name

    def has_next(self) -> bool:
        """
        Returns true if there are potentially more results to be retrieved.
        """
        return self._has_next

    def get_next(self) -> List[dict]:
        """
        Returns the next page of results.
        :return: A List[dict], where each element is a dict that represents an instance of PipelineRunsCollectionPipelineRunsItem.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_tekton_pipeline_runs(
            pipeline_id=self._pipeline_id,
            limit=self._limit,
            offset=self._offset,
            status=self._status,
            trigger_name=self._trigger_name,
            start=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = get_query_param(next_page_link.get('href'), 'start')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('pipeline_runs')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of PipelineRunsCollectionPipelineRunsItem.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
