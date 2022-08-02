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

# IBM OpenAPI SDK Code Generator Version: 3.53.0-9710cac3-20220713-193508
 
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

    DEFAULT_SERVICE_URL = 'https://api.us-south.devops.cloud.ibm.com/v2'
    DEFAULT_SERVICE_NAME = 'cd_tekton_pipeline'

    REGIONAL_ENDPOINTS = {
        'us-south': 'https://api.us-south.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the us-south region.
        'us-east': 'https://api.us-east.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the us-east region.
        'eu-de': 'https://api.eu-de.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the eu-de region.
        'eu-gb': 'https://api.eu-gb.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the eu-gb region.
        'jp-osa': 'https://api.jp-osa.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the jp-osa region.
        'jp-tok': 'https://api.jp-tok.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the jp-tok region.
        'au-syd': 'https://api.au-syd.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the au-syd region.
        'ca-tor': 'https://api.ca-tor.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the ca-tor region.
        'br-sao': 'https://api.br-sao.devops.cloud.ibm.com/v2', # The host URL for Tekton Pipeline Service in the br-sao region.
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
        worker: 'WorkerWithId' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create tekton pipeline.

        This request creates a tekton pipeline for a tekton pipeline toolchain
        integration, user has to use the toolchain endpoint to create the tekton pipeline
        toolchain integration first and then use the generated UUID to create the tekton
        pipeline with or without a specified worker.

        :param str id: (optional) UUID.
        :param WorkerWithId worker: (optional) Worker object with worker ID only.
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
        Get tekton pipeline data.

        This request retrieves whole tekton pipeline data.

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
        worker: 'WorkerWithId' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update tekton pipeline data.

        This request updates tekton pipeline data, but you can only change worker ID in
        this endpoint. Use other endpoints such as /definitions, /triggers, and
        /properties for detailed updated.

        :param str id: ID of current instance.
        :param WorkerWithId worker: (optional) Worker object with worker ID only.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TektonPipeline` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if worker is not None:
            worker = convert_model(worker)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_tekton_pipeline')
        headers.update(sdk_headers)

        data = {
            'worker': worker
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

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
        Delete tekton pipeline instance.

        This request deletes tekton pipeline instance that associated with the pipeline
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
        limit: int = None,
        offset: int = None,
        status: str = None,
        trigger_name: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List pipeline run records.

        This request list pipeline run records, which has data of that run, such as
        status, user_info, trigger and other information. Default limit is 50.

        :param str pipeline_id: The tekton pipeline ID.
        :param int limit: (optional) The number of pipeline runs to return, sorted
               by creation time, most recent first.
        :param int offset: (optional) Skip the specified number of pipeline runs.
        :param str status: (optional) Filters the collection to resources with the
               specified status.
        :param str trigger_name: (optional) Filters the collection to resources
               with the specified trigger name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRuns` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_tekton_pipeline_runs')
        headers.update(sdk_headers)

        params = {
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
        Start a trigger to create a pipelineRun.

        This request executes a trigger to create a pipelineRun.

        :param str pipeline_id: The tekton pipeline ID.
        :param str trigger_name: (optional) Trigger name.
        :param dict trigger_properties: (optional) A valid single dictionary object
               containing string values only to provide extra TEXT trigger properties or
               override defined TEXT type trigger properties.
        :param dict secure_trigger_properties: (optional) A valid single dictionary
               object containing string values only to provide extra SECURE type trigger
               properties or override defined SECURE type trigger properties.
        :param dict trigger_header: (optional) A valid single dictionary object
               with only string values to provide header, use $(header.header_key_name) to
               access it in triggerBinding.
        :param dict trigger_body: (optional) A valid object to provide body, use
               $(body.body_key_name) to access it in triggerBinding.
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

        This request retrieves detail of requested pipeline run, to get Kubernetes
        Resources List of this pipeline run use endpoint
        /tekton_pipelines/{pipeline_id}/tekton_pipelinerun_resource_list/{id}.

        :param str pipeline_id: The tekton pipeline ID.
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

        This request deletes the requested pipeline run record.

        :param str pipeline_id: The tekton pipeline ID.
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

        This request cancels a running pipeline run, use 'force' payload in case you can't
        cancel a pipeline run normally.

        :param str pipeline_id: The tekton pipeline ID.
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

        This request reruns a past pipeline run with same data. Request body isn't
        allowed.

        :param str pipeline_id: The tekton pipeline ID.
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
        Get a list of pipeline run log IDs.

        This request fetches list of log IDs of a pipeline run.

        :param str pipeline_id: The tekton pipeline ID.
        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRunLogs` object
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
        Get the log content of a pipeline run step by using the step log ID.

        This request retrieves log content of a pipeline run step, to get the log ID use
        endpoint /tekton_pipelines/{pipeline_id}/pipeline_runs/{id}/logs.

        :param str pipeline_id: The tekton pipeline ID.
        :param str pipeline_run_id: The tekton pipeline run ID.
        :param str id: ID of current instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StepLog` object
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

        This request fetches pipeline definitions, which is the a collection of individual
        definition entries, each entry is a composition of a repo url, a repo branch and a
        repo path.

        :param str pipeline_id: The tekton pipeline ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Definitions` object
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
        **kwargs
    ) -> DetailedResponse:
        """
        Create a single definition.

        This request adds a single definition.

        :param str pipeline_id: The tekton pipeline ID.
        :param DefinitionScmSource scm_source: (optional) Scm source for tekton
               pipeline defintion.
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
            'scm_source': scm_source
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

        This request fetches a single definition entry, which is a composition of the
        definition repo's url, branch and directory path.

        :param str pipeline_id: The tekton pipeline ID.
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
        service_instance_id: str = None,
        id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Edit a single definition entry.

        This request replaces a single definition's repo directory path or repo branch.
        Its scm_source.url and service_instance_id are immutable.

        :param str pipeline_id: The tekton pipeline ID.
        :param str definition_id: The definition ID.
        :param DefinitionScmSource scm_source: (optional) Scm source for tekton
               pipeline defintion.
        :param str service_instance_id: (optional) UUID.
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
            'service_instance_id': service_instance_id,
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

        This request deletes a single definition from definition list.

        :param str pipeline_id: The tekton pipeline ID.
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
        List pipeline environment properties.

        This request lists the pipeline environment properties which every pipelineRun
        execution has access to.

        :param str pipeline_id: The tekton pipeline ID.
        :param str name: (optional) Filters the collection to resources with the
               specified property name.
        :param List[str] type: (optional) Filters the collection to resources with
               the specified property type.
        :param str sort: (optional) Sorts the returned properties by a property
               field, for properties you can sort them alphabetically by "name" in
               ascending order or with "-name" in descending order.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnvProperties` object
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
        default: str = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create pipeline environment property.

        This request creates a single pipeline environment property.

        :param str pipeline_id: The tekton pipeline ID.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
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
            'default': default,
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
        Get a single pipeline environment property.

        This request gets a single pipeline environment property data.

        :param str pipeline_id: The tekton pipeline ID.
        :param str property_name: The property's name.
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
        default: str = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace a single pipeline environment property value.

        This request updates a single pipeline environment property value, its type or
        name are immutable. For any property type, the entered value replaces the existing
        value.

        :param str pipeline_id: The tekton pipeline ID.
        :param str property_name: The property's name.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
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
            'default': default,
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

        :param str pipeline_id: The tekton pipeline ID.
        :param str property_name: The property's name.
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

        This request lists pipeline triggers.

        :param str pipeline_id: The tekton pipeline ID.
        :param str type: (optional) filter the triggers by trigger "type", possible
               values are "manual", "scm", "generic", "timer".
        :param str name: (optional) filter the triggers by trigger "name", accept
               single string value.
        :param str event_listener: (optional) filter the triggers by trigger
               "event_listener", accept single string value.
        :param str worker_id: (optional) filter the triggers by trigger
               "worker.id", accept single string value.
        :param str worker_name: (optional) filter the triggers by trigger
               "worker.name", accept single string value.
        :param str disabled: (optional) filter the triggers by trigger "disabled"
               flag, possbile state are "true" and "false".
        :param str tags: (optional) filter the triggers by trigger "tags", the
               response lists triggers if it has one matching tag.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Triggers` object
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
        trigger: 'Trigger' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a trigger or duplicate a trigger.

        This request creates a trigger or duplicate a trigger from an existing trigger.

        :param str pipeline_id: The tekton pipeline ID.
        :param Trigger trigger: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if  trigger is not None and isinstance(trigger, Trigger):
            trigger = convert_model(trigger)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_tekton_pipeline_trigger')
        headers.update(sdk_headers)

        data = json.dumps(trigger)
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

        This request retrieves a single trigger detail.

        :param str pipeline_id: The tekton pipeline ID.
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
        type: str = None,
        name: str = None,
        event_listener: str = None,
        tags: List[str] = None,
        worker: 'Worker' = None,
        concurrency: 'Concurrency' = None,
        disabled: bool = None,
        secret: 'GenericSecret' = None,
        cron: str = None,
        timezone: str = None,
        scm_source: 'TriggerScmSource' = None,
        events: 'Events' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Edit a single trigger entry.

        This request changes a single field or many fields of a trigger, note that some
        fields are immutable, and use /properties to update trigger properties.

        :param str pipeline_id: The tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str type: (optional) Trigger type.
        :param str name: (optional) Trigger name.
        :param str event_listener: (optional) Event listener name.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        :param bool disabled: (optional) Defines if this trigger is disabled.
        :param GenericSecret secret: (optional) Needed only for generic trigger
               type. Secret used to start generic trigger.
        :param str cron: (optional) Needed only for timer trigger type. Cron
               expression for timer trigger.
        :param str timezone: (optional) Needed only for timer trigger type.
               Timezones for timer trigger.
        :param TriggerScmSource scm_source: (optional) Scm source for git type
               tekton pipeline trigger.
        :param Events events: (optional) Needed only for git trigger type. Events
               object defines the events this git trigger listening to.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if pipeline_id is None:
            raise ValueError('pipeline_id must be provided')
        if trigger_id is None:
            raise ValueError('trigger_id must be provided')
        if worker is not None:
            worker = convert_model(worker)
        if concurrency is not None:
            concurrency = convert_model(concurrency)
        if secret is not None:
            secret = convert_model(secret)
        if scm_source is not None:
            scm_source = convert_model(scm_source)
        if events is not None:
            events = convert_model(events)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_tekton_pipeline_trigger')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'event_listener': event_listener,
            'tags': tags,
            'worker': worker,
            'concurrency': concurrency,
            'disabled': disabled,
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

        This request deletes a single trigger.

        :param str pipeline_id: The tekton pipeline ID.
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
        List trigger environment properties.

        This request lists trigger environment properties.

        :param str pipeline_id: The tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str name: filter properties by the name of property.
        :param str type: filter properties by the type of property, avaialble types
               are "SECURE","TEXT","INTEGRATION","SINGLE_SELECT","APPCONFIG".
        :param str sort: sort properties by the a property field, for properties
               you can only sort them by "name" or "-name".
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerProperties` object
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
        default: str = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create trigger's environment property.

        This request creates a trigger's property.

        :param str pipeline_id: The tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
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
            'default': default,
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
        Get a trigger's environment property.

        This request retrieves a trigger's environment property.

        :param str pipeline_id: The tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str property_name: The property's name.
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
        default: str = None,
        path: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace a trigger's environment property value.

        This request updates a trigger's environment property value, its type or name are
        immutable. For any property type, the entered value replaces the existing value.

        :param str pipeline_id: The tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str property_name: The property's name.
        :param str name: (optional) Property name.
        :param str type: (optional) Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
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
            'default': default,
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
        Delete a trigger's property.

        this request deletes a trigger's property.

        :param str pipeline_id: The tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str property_name: The property's name.
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
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


##############################################################################
# Models
##############################################################################


class Concurrency():
    """
    Concurrency object.

    :attr int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger.
    """

    def __init__(self,
                 *,
                 max_concurrent_runs: int = None) -> None:
        """
        Initialize a Concurrency object.

        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger.
        """
        self.max_concurrent_runs = max_concurrent_runs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Concurrency':
        """Initialize a Concurrency object from a json dictionary."""
        args = {}
        if 'max_concurrent_runs' in _dict:
            args['max_concurrent_runs'] = _dict.get('max_concurrent_runs')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Concurrency object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Concurrency object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Concurrency') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Concurrency') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Definition():
    """
    Tekton pipeline definition entry object.

    :attr DefinitionScmSource scm_source: Scm source for tekton pipeline defintion.
    :attr str service_instance_id: UUID.
    :attr str id: (optional) UUID.
    """

    def __init__(self,
                 scm_source: 'DefinitionScmSource',
                 service_instance_id: str,
                 *,
                 id: str = None) -> None:
        """
        Initialize a Definition object.

        :param DefinitionScmSource scm_source: Scm source for tekton pipeline
               defintion.
        :param str service_instance_id: UUID.
        :param str id: (optional) UUID.
        """
        self.scm_source = scm_source
        self.service_instance_id = service_instance_id
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Definition':
        """Initialize a Definition object from a json dictionary."""
        args = {}
        if 'scm_source' in _dict:
            args['scm_source'] = DefinitionScmSource.from_dict(_dict.get('scm_source'))
        else:
            raise ValueError('Required property \'scm_source\' not present in Definition JSON')
        if 'service_instance_id' in _dict:
            args['service_instance_id'] = _dict.get('service_instance_id')
        else:
            raise ValueError('Required property \'service_instance_id\' not present in Definition JSON')
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
        if hasattr(self, 'service_instance_id') and self.service_instance_id is not None:
            _dict['service_instance_id'] = self.service_instance_id
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
    Scm source for tekton pipeline defintion.

    :attr str url: General href URL.
    :attr str branch: (optional) A branch of the repo, branch field doesn't coexist
          with tag field.
    :attr str tag: (optional) A tag of the repo.
    :attr str path: The path to the definitions yaml files.
    """

    def __init__(self,
                 url: str,
                 path: str,
                 *,
                 branch: str = None,
                 tag: str = None) -> None:
        """
        Initialize a DefinitionScmSource object.

        :param str url: General href URL.
        :param str path: The path to the definitions yaml files.
        :param str branch: (optional) A branch of the repo, branch field doesn't
               coexist with tag field.
        :param str tag: (optional) A tag of the repo.
        """
        self.url = url
        self.branch = branch
        self.tag = tag
        self.path = path

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

class Definitions():
    """
    Pipeline definitions is a collection of individual definition entries, each entry is a
    composition of a repo url, repo branch/tag and a certain directory path.

    :attr List[DefinitionsDefinitionsItem] definitions: Definition list.
    """

    def __init__(self,
                 definitions: List['DefinitionsDefinitionsItem']) -> None:
        """
        Initialize a Definitions object.

        :param List[DefinitionsDefinitionsItem] definitions: Definition list.
        """
        self.definitions = definitions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Definitions':
        """Initialize a Definitions object from a json dictionary."""
        args = {}
        if 'definitions' in _dict:
            args['definitions'] = [DefinitionsDefinitionsItem.from_dict(x) for x in _dict.get('definitions')]
        else:
            raise ValueError('Required property \'definitions\' not present in Definitions JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Definitions object from a json dictionary."""
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
        """Return a `str` version of this Definitions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Definitions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Definitions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DefinitionsDefinitionsItem():
    """
    Tekton pipeline definition entry object.

    :attr DefinitionScmSource scm_source: Scm source for tekton pipeline defintion.
    :attr str service_instance_id: UUID.
    :attr str id: (optional) UUID.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 scm_source: 'DefinitionScmSource',
                 service_instance_id: str,
                 *,
                 id: str = None,
                 href: str = None) -> None:
        """
        Initialize a DefinitionsDefinitionsItem object.

        :param DefinitionScmSource scm_source: Scm source for tekton pipeline
               defintion.
        :param str service_instance_id: UUID.
        :param str id: (optional) UUID.
        :param str href: (optional) General href URL.
        """
        self.scm_source = scm_source
        self.service_instance_id = service_instance_id
        self.id = id
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefinitionsDefinitionsItem':
        """Initialize a DefinitionsDefinitionsItem object from a json dictionary."""
        args = {}
        if 'scm_source' in _dict:
            args['scm_source'] = DefinitionScmSource.from_dict(_dict.get('scm_source'))
        else:
            raise ValueError('Required property \'scm_source\' not present in DefinitionsDefinitionsItem JSON')
        if 'service_instance_id' in _dict:
            args['service_instance_id'] = _dict.get('service_instance_id')
        else:
            raise ValueError('Required property \'service_instance_id\' not present in DefinitionsDefinitionsItem JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefinitionsDefinitionsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'scm_source') and self.scm_source is not None:
            _dict['scm_source'] = self.scm_source.to_dict()
        if hasattr(self, 'service_instance_id') and self.service_instance_id is not None:
            _dict['service_instance_id'] = self.service_instance_id
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefinitionsDefinitionsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefinitionsDefinitionsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefinitionsDefinitionsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class EnvProperties():
    """
    Pipeline properties object.

    :attr List[Property] properties: Pipeline properties list.
    """

    def __init__(self,
                 properties: List['Property']) -> None:
        """
        Initialize a EnvProperties object.

        :param List[Property] properties: Pipeline properties list.
        """
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvProperties':
        """Initialize a EnvProperties object from a json dictionary."""
        args = {}
        if 'properties' in _dict:
            args['properties'] = [Property.from_dict(x) for x in _dict.get('properties')]
        else:
            raise ValueError('Required property \'properties\' not present in EnvProperties JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvProperties object from a json dictionary."""
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
        """Return a `str` version of this EnvProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Events():
    """
    Needed only for git trigger type. Events object defines the events this git trigger
    listening to.

    :attr bool push: (optional) If true, the trigger starts when tekton pipeline
          service receive a repo's 'push' git webhook event.
    :attr bool pull_request_closed: (optional) If true, the trigger starts when
          tekton pipeline service receive a repo pull reqeust's 'close' git webhook event.
    :attr bool pull_request: (optional) If true, the trigger starts when tekton
          pipeline service receive a repo pull reqeust's 'open' or 'update' git webhook
          event.
    """

    def __init__(self,
                 *,
                 push: bool = None,
                 pull_request_closed: bool = None,
                 pull_request: bool = None) -> None:
        """
        Initialize a Events object.

        :param bool push: (optional) If true, the trigger starts when tekton
               pipeline service receive a repo's 'push' git webhook event.
        :param bool pull_request_closed: (optional) If true, the trigger starts
               when tekton pipeline service receive a repo pull reqeust's 'close' git
               webhook event.
        :param bool pull_request: (optional) If true, the trigger starts when
               tekton pipeline service receive a repo pull reqeust's 'open' or 'update'
               git webhook event.
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
    Needed only for generic trigger type. Secret used to start generic trigger.

    :attr str type: (optional) Secret type.
    :attr str value: (optional) Secret value, not needed if secret type is
          "internalValidation".
    :attr str source: (optional) Secret location, not needed if secret type is
          "internalValidation".
    :attr str key_name: (optional) Secret name, not needed if type is
          "internalValidation".
    :attr str algorithm: (optional) Algorithm used for "digestMatches" secret type.
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
               "internalValidation".
        :param str source: (optional) Secret location, not needed if secret type is
               "internalValidation".
        :param str key_name: (optional) Secret name, not needed if type is
               "internalValidation".
        :param str algorithm: (optional) Algorithm used for "digestMatches" secret
               type.
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
        TOKENMATCHES = 'tokenMatches'
        DIGESTMATCHES = 'digestMatches'
        INTERNALVALIDATION = 'internalValidation'


    class SourceEnum(str, Enum):
        """
        Secret location, not needed if secret type is "internalValidation".
        """
        HEADER = 'header'
        PAYLOAD = 'payload'
        QUERY = 'query'


    class AlgorithmEnum(str, Enum):
        """
        Algorithm used for "digestMatches" secret type.
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


class PipelineRun():
    """
    Single tekton pipeline run object.

    :attr str id: UUID.
    :attr UserInfo user_info: (optional) User information.
    :attr str status: Status of the pipeline run.
    :attr str definition_id: The aggregated definition ID used for this pipelineRun.
    :attr PipelineRunWorker worker: worker details used in this pipelineRun.
    :attr str pipeline_id: UUID.
    :attr str listener_name: Listener name used to start the run.
    :attr Trigger trigger: Tekton pipeline trigger object.
    :attr str event_params_blob: Event parameters object passed to this pipeline run
          in String format, the contents depends on the type of trigger, for example, for
          git trigger it includes the git event payload.
    :attr str event_header_params_blob: (optional) Heads passed to this pipeline run
          in String format, tekton pipeline service can't control the shape of the
          contents.
    :attr List[Property] properties: (optional) Properties used in this tekton
          pipeline run.
    :attr datetime created: Standard RFC 3339 Date Time String.
    :attr datetime updated: (optional) Standard RFC 3339 Date Time String.
    :attr str html_url: Dashboard URL for this pipeline run.
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
                 created: datetime,
                 html_url: str,
                 *,
                 user_info: 'UserInfo' = None,
                 event_header_params_blob: str = None,
                 properties: List['Property'] = None,
                 updated: datetime = None) -> None:
        """
        Initialize a PipelineRun object.

        :param str id: UUID.
        :param str status: Status of the pipeline run.
        :param str definition_id: The aggregated definition ID used for this
               pipelineRun.
        :param PipelineRunWorker worker: worker details used in this pipelineRun.
        :param str pipeline_id: UUID.
        :param str listener_name: Listener name used to start the run.
        :param Trigger trigger: Tekton pipeline trigger object.
        :param str event_params_blob: Event parameters object passed to this
               pipeline run in String format, the contents depends on the type of trigger,
               for example, for git trigger it includes the git event payload.
        :param datetime created: Standard RFC 3339 Date Time String.
        :param str html_url: Dashboard URL for this pipeline run.
        :param UserInfo user_info: (optional) User information.
        :param str event_header_params_blob: (optional) Heads passed to this
               pipeline run in String format, tekton pipeline service can't control the
               shape of the contents.
        :param List[Property] properties: (optional) Properties used in this tekton
               pipeline run.
        :param datetime updated: (optional) Standard RFC 3339 Date Time String.
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
        self.created = created
        self.updated = updated
        self.html_url = html_url

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
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        else:
            raise ValueError('Required property \'created\' not present in PipelineRun JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'html_url' in _dict:
            args['html_url'] = _dict.get('html_url')
        else:
            raise ValueError('Required property \'html_url\' not present in PipelineRun JSON')
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'html_url') and self.html_url is not None:
            _dict['html_url'] = self.html_url
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


class PipelineRunLog():
    """
    Pipeline run logId object.

    :attr str name: (optional) <podName>/<containerName> of this log.
    :attr str id: (optional) Generated log ID.
    :attr str href: (optional) API for getting log content.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 id: str = None,
                 href: str = None) -> None:
        """
        Initialize a PipelineRunLog object.

        :param str name: (optional) <podName>/<containerName> of this log.
        :param str id: (optional) Generated log ID.
        :param str href: (optional) API for getting log content.
        """
        self.name = name
        self.id = id
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunLog':
        """Initialize a PipelineRunLog object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunLog object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunLog object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunLog') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunLog') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunLogs():
    """
    List of pipeline run log ID object.

    :attr List[PipelineRunLog] logs: (optional)
    """

    def __init__(self,
                 *,
                 logs: List['PipelineRunLog'] = None) -> None:
        """
        Initialize a PipelineRunLogs object.

        :param List[PipelineRunLog] logs: (optional)
        """
        self.logs = logs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunLogs':
        """Initialize a PipelineRunLogs object from a json dictionary."""
        args = {}
        if 'logs' in _dict:
            args['logs'] = [PipelineRunLog.from_dict(x) for x in _dict.get('logs')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunLogs object from a json dictionary."""
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
        """Return a `str` version of this PipelineRunLogs object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunLogs') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunLogs') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunWorker():
    """
    worker details used in this pipelineRun.

    :attr str name: (optional) Worker name.
    :attr str agent: (optional) The agent ID of the corresponding private worker
          integration used for this pipelineRun.
    :attr str service_id: (optional) The Service ID of the corresponding private
          worker integration used for this pipelineRun.
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
        :param str name: (optional) Worker name.
        :param str agent: (optional) The agent ID of the corresponding private
               worker integration used for this pipelineRun.
        :param str service_id: (optional) The Service ID of the corresponding
               private worker integration used for this pipelineRun.
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

class PipelineRuns():
    """
    Tekton pipeline runs object.

    :attr List[PipelineRunsPipelineRunsItem] pipeline_runs: Tekton pipeline runs
          list.
    :attr int offset: Skip a specified number of pipeline runs.
    :attr int limit: The number of pipeline runs to return, sorted by creation time,
          most recent first.
    :attr PipelineRunsFirst first: First page of pipeline runs.
    :attr PipelineRunsNext next: (optional) Next page of pipeline runs relative to
          the offset and limit.
    """

    def __init__(self,
                 pipeline_runs: List['PipelineRunsPipelineRunsItem'],
                 offset: int,
                 limit: int,
                 first: 'PipelineRunsFirst',
                 *,
                 next: 'PipelineRunsNext' = None) -> None:
        """
        Initialize a PipelineRuns object.

        :param List[PipelineRunsPipelineRunsItem] pipeline_runs: Tekton pipeline
               runs list.
        :param int offset: Skip a specified number of pipeline runs.
        :param int limit: The number of pipeline runs to return, sorted by creation
               time, most recent first.
        :param PipelineRunsFirst first: First page of pipeline runs.
        :param PipelineRunsNext next: (optional) Next page of pipeline runs
               relative to the offset and limit.
        """
        self.pipeline_runs = pipeline_runs
        self.offset = offset
        self.limit = limit
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRuns':
        """Initialize a PipelineRuns object from a json dictionary."""
        args = {}
        if 'pipeline_runs' in _dict:
            args['pipeline_runs'] = [PipelineRunsPipelineRunsItem.from_dict(x) for x in _dict.get('pipeline_runs')]
        else:
            raise ValueError('Required property \'pipeline_runs\' not present in PipelineRuns JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in PipelineRuns JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in PipelineRuns JSON')
        if 'first' in _dict:
            args['first'] = PipelineRunsFirst.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in PipelineRuns JSON')
        if 'next' in _dict:
            args['next'] = PipelineRunsNext.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRuns object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRuns object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRuns') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRuns') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsFirst():
    """
    First page of pipeline runs.

    :attr str href: General href URL.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a PipelineRunsFirst object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsFirst':
        """Initialize a PipelineRunsFirst object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PipelineRunsFirst JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsFirst object from a json dictionary."""
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
        """Return a `str` version of this PipelineRunsFirst object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsFirst') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsFirst') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsNext():
    """
    Next page of pipeline runs relative to the offset and limit.

    :attr str href: General href URL.
    """

    def __init__(self,
                 href: str) -> None:
        """
        Initialize a PipelineRunsNext object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsNext':
        """Initialize a PipelineRunsNext object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        else:
            raise ValueError('Required property \'href\' not present in PipelineRunsNext JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsNext object from a json dictionary."""
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
        """Return a `str` version of this PipelineRunsNext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsNext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsNext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PipelineRunsPipelineRunsItem():
    """
    Single tekton pipeline run object.

    :attr str id: UUID.
    :attr UserInfo user_info: (optional) User information.
    :attr str status: Status of the pipeline run.
    :attr str definition_id: The aggregated definition ID used for this pipelineRun.
    :attr PipelineRunWorker worker: worker details used in this pipelineRun.
    :attr str pipeline_id: UUID.
    :attr str listener_name: Listener name used to start the run.
    :attr Trigger trigger: Tekton pipeline trigger object.
    :attr str event_params_blob: Event parameters object passed to this pipeline run
          in String format, the contents depends on the type of trigger, for example, for
          git trigger it includes the git event payload.
    :attr str event_header_params_blob: (optional) Heads passed to this pipeline run
          in String format, tekton pipeline service can't control the shape of the
          contents.
    :attr List[Property] properties: (optional) Properties used in this tekton
          pipeline run.
    :attr datetime created: Standard RFC 3339 Date Time String.
    :attr datetime updated: (optional) Standard RFC 3339 Date Time String.
    :attr str html_url: Dashboard URL for this pipeline run.
    :attr str href: (optional) General href URL.
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
                 created: datetime,
                 html_url: str,
                 *,
                 user_info: 'UserInfo' = None,
                 event_header_params_blob: str = None,
                 properties: List['Property'] = None,
                 updated: datetime = None,
                 href: str = None) -> None:
        """
        Initialize a PipelineRunsPipelineRunsItem object.

        :param str id: UUID.
        :param str status: Status of the pipeline run.
        :param str definition_id: The aggregated definition ID used for this
               pipelineRun.
        :param PipelineRunWorker worker: worker details used in this pipelineRun.
        :param str pipeline_id: UUID.
        :param str listener_name: Listener name used to start the run.
        :param Trigger trigger: Tekton pipeline trigger object.
        :param str event_params_blob: Event parameters object passed to this
               pipeline run in String format, the contents depends on the type of trigger,
               for example, for git trigger it includes the git event payload.
        :param datetime created: Standard RFC 3339 Date Time String.
        :param str html_url: Dashboard URL for this pipeline run.
        :param UserInfo user_info: (optional) User information.
        :param str event_header_params_blob: (optional) Heads passed to this
               pipeline run in String format, tekton pipeline service can't control the
               shape of the contents.
        :param List[Property] properties: (optional) Properties used in this tekton
               pipeline run.
        :param datetime updated: (optional) Standard RFC 3339 Date Time String.
        :param str href: (optional) General href URL.
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
        self.created = created
        self.updated = updated
        self.html_url = html_url
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsPipelineRunsItem':
        """Initialize a PipelineRunsPipelineRunsItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'user_info' in _dict:
            args['user_info'] = UserInfo.from_dict(_dict.get('user_info'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'definition_id' in _dict:
            args['definition_id'] = _dict.get('definition_id')
        else:
            raise ValueError('Required property \'definition_id\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'worker' in _dict:
            args['worker'] = PipelineRunWorker.from_dict(_dict.get('worker'))
        else:
            raise ValueError('Required property \'worker\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'pipeline_id' in _dict:
            args['pipeline_id'] = _dict.get('pipeline_id')
        else:
            raise ValueError('Required property \'pipeline_id\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'listener_name' in _dict:
            args['listener_name'] = _dict.get('listener_name')
        else:
            raise ValueError('Required property \'listener_name\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'trigger' in _dict:
            args['trigger'] = _dict.get('trigger')
        else:
            raise ValueError('Required property \'trigger\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'event_params_blob' in _dict:
            args['event_params_blob'] = _dict.get('event_params_blob')
        else:
            raise ValueError('Required property \'event_params_blob\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'event_header_params_blob' in _dict:
            args['event_header_params_blob'] = _dict.get('event_header_params_blob')
        if 'properties' in _dict:
            args['properties'] = [Property.from_dict(x) for x in _dict.get('properties')]
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        else:
            raise ValueError('Required property \'created\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'html_url' in _dict:
            args['html_url'] = _dict.get('html_url')
        else:
            raise ValueError('Required property \'html_url\' not present in PipelineRunsPipelineRunsItem JSON')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsPipelineRunsItem object from a json dictionary."""
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'html_url') and self.html_url is not None:
            _dict['html_url'] = self.html_url
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunsPipelineRunsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunsPipelineRunsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunsPipelineRunsItem') -> bool:
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


class Property():
    """
    Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None) -> None:
        """
        Initialize a Property object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
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
        if 'default' in _dict:
            args['default'] = _dict.get('default')
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class StepLog():
    """
    Log object for tekton pipeline run step.

    :attr str id: Step log ID.
    :attr str data: The raw log content of step.
    """

    def __init__(self,
                 id: str,
                 data: str) -> None:
        """
        Initialize a StepLog object.

        :param str id: Step log ID.
        :param str data: The raw log content of step.
        """
        self.id = id
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StepLog':
        """Initialize a StepLog object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in StepLog JSON')
        if 'data' in _dict:
            args['data'] = _dict.get('data')
        else:
            raise ValueError('Required property \'data\' not present in StepLog JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StepLog object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StepLog object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StepLog') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StepLog') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

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
    :attr datetime updated_at: Standard RFC 3339 Date Time String.
    :attr datetime created: Standard RFC 3339 Date Time String.
    :attr TektonPipelinePipelineDefinition pipeline_definition: (optional) Tekton
          pipeline definition document detail object. If this property is absent, the
          pipeline has no definitions added.
    :attr List[Trigger] triggers: Tekton pipeline triggers list.
    :attr Worker worker: Default pipeline worker used to run the pipeline.
    :attr str html_url: Dashboard URL of this pipeline.
    :attr int build_number: (optional) The latest pipeline run build number. If this
          property is absent, the pipeline hasn't had any pipelineRuns.
    :attr bool enabled: Flag whether this pipeline enabled.
    """

    def __init__(self,
                 name: str,
                 status: str,
                 resource_group_id: str,
                 toolchain: 'Toolchain',
                 id: str,
                 definitions: List['Definition'],
                 properties: List['Property'],
                 updated_at: datetime,
                 created: datetime,
                 triggers: List['Trigger'],
                 worker: 'Worker',
                 html_url: str,
                 enabled: bool,
                 *,
                 pipeline_definition: 'TektonPipelinePipelineDefinition' = None,
                 build_number: int = None) -> None:
        """
        Initialize a TektonPipeline object.

        :param str name: String.
        :param str status: Pipeline status.
        :param str resource_group_id: ID.
        :param Toolchain toolchain: Toolchain object.
        :param str id: UUID.
        :param List[Definition] definitions: Definition list.
        :param List[Property] properties: Tekton pipeline's environment properties.
        :param datetime updated_at: Standard RFC 3339 Date Time String.
        :param datetime created: Standard RFC 3339 Date Time String.
        :param List[Trigger] triggers: Tekton pipeline triggers list.
        :param Worker worker: Default pipeline worker used to run the pipeline.
        :param str html_url: Dashboard URL of this pipeline.
        :param bool enabled: Flag whether this pipeline enabled.
        :param TektonPipelinePipelineDefinition pipeline_definition: (optional)
               Tekton pipeline definition document detail object. If this property is
               absent, the pipeline has no definitions added.
        :param int build_number: (optional) The latest pipeline run build number.
               If this property is absent, the pipeline hasn't had any pipelineRuns.
        """
        self.name = name
        self.status = status
        self.resource_group_id = resource_group_id
        self.toolchain = toolchain
        self.id = id
        self.definitions = definitions
        self.properties = properties
        self.updated_at = updated_at
        self.created = created
        self.pipeline_definition = pipeline_definition
        self.triggers = triggers
        self.worker = worker
        self.html_url = html_url
        self.build_number = build_number
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
        else:
            raise ValueError('Required property \'updated_at\' not present in TektonPipeline JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        else:
            raise ValueError('Required property \'created\' not present in TektonPipeline JSON')
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
        if 'html_url' in _dict:
            args['html_url'] = _dict.get('html_url')
        else:
            raise ValueError('Required property \'html_url\' not present in TektonPipeline JSON')
        if 'build_number' in _dict:
            args['build_number'] = _dict.get('build_number')
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
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
        if hasattr(self, 'html_url') and self.html_url is not None:
            _dict['html_url'] = self.html_url
        if hasattr(self, 'build_number') and self.build_number is not None:
            _dict['build_number'] = self.build_number
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


class TektonPipelinePipelineDefinition():
    """
    Tekton pipeline definition document detail object. If this property is absent, the
    pipeline has no definitions added.

    :attr str status: (optional) The state of pipeline definition status.
    :attr str id: (optional) UUID.
    """

    def __init__(self,
                 *,
                 status: str = None,
                 id: str = None) -> None:
        """
        Initialize a TektonPipelinePipelineDefinition object.

        :param str status: (optional) The state of pipeline definition status.
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
        The state of pipeline definition status.
        """
        UPDATED = 'updated'
        OUTDATED = 'outdated'
        UPDATING = 'updating'
        FAILED = 'failed'


class Toolchain():
    """
    Toolchain object.

    :attr str id: UUID.
    :attr str crn: The CRN for the toolchain that containing the tekton pipeline.
    """

    def __init__(self,
                 id: str,
                 crn: str) -> None:
        """
        Initialize a Toolchain object.

        :param str id: UUID.
        :param str crn: The CRN for the toolchain that containing the tekton
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
    Tekton pipeline trigger object.

    """

    def __init__(self) -> None:
        """
        Initialize a Trigger object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['TriggerDuplicateTrigger', 'TriggerManualTrigger', 'TriggerScmTrigger', 'TriggerTimerTrigger', 'TriggerGenericTrigger']))
        raise Exception(msg)

class TriggerGenericTriggerPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerGenericTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
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
        if 'default' in _dict:
            args['default'] = _dict.get('default')
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggerManualTriggerPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerManualTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
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
        if 'default' in _dict:
            args['default'] = _dict.get('default')
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggerProperties():
    """
    Trigger properties object.

    :attr List[TriggerPropertiesPropertiesItem] properties: Trigger properties list.
    """

    def __init__(self,
                 properties: List['TriggerPropertiesPropertiesItem']) -> None:
        """
        Initialize a TriggerProperties object.

        :param List[TriggerPropertiesPropertiesItem] properties: Trigger properties
               list.
        """
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerProperties':
        """Initialize a TriggerProperties object from a json dictionary."""
        args = {}
        if 'properties' in _dict:
            args['properties'] = [TriggerPropertiesPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        else:
            raise ValueError('Required property \'properties\' not present in TriggerProperties JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerProperties object from a json dictionary."""
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
        """Return a `str` version of this TriggerProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerPropertiesPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerPropertiesPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerPropertiesPropertiesItem':
        """Initialize a TriggerPropertiesPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerPropertiesPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'default' in _dict:
            args['default'] = _dict.get('default')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggerPropertiesPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerPropertiesPropertiesItem object from a json dictionary."""
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        """Return a `str` version of this TriggerPropertiesPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerPropertiesPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerPropertiesPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggerProperty():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None) -> None:
        """
        Initialize a TriggerProperty object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
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
        if 'default' in _dict:
            args['default'] = _dict.get('default')
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggerScmSource():
    """
    Scm source for git type tekton pipeline trigger.

    :attr str url: Needed only for git trigger type. Repo URL that listening to.
    :attr str branch: (optional) Needed only for git trigger type. Branch name of
          the repo. Branch field doesn't coexist with pattern field.
    :attr str pattern: (optional) Needed only for git trigger type. Git branch or
          tag pattern to listen to. Please refer to
          https://github.com/micromatch/micromatch for pattern syntax.
    :attr bool blind_connection: (optional) Needed only for git trigger type. Branch
          name of the repo.
    :attr str hook_id: (optional) Webhook ID.
    """

    def __init__(self,
                 url: str,
                 *,
                 branch: str = None,
                 pattern: str = None,
                 blind_connection: bool = None,
                 hook_id: str = None) -> None:
        """
        Initialize a TriggerScmSource object.

        :param str url: Needed only for git trigger type. Repo URL that listening
               to.
        :param str branch: (optional) Needed only for git trigger type. Branch name
               of the repo. Branch field doesn't coexist with pattern field.
        :param str pattern: (optional) Needed only for git trigger type. Git branch
               or tag pattern to listen to. Please refer to
               https://github.com/micromatch/micromatch for pattern syntax.
        :param bool blind_connection: (optional) Needed only for git trigger type.
               Branch name of the repo.
        :param str hook_id: (optional) Webhook ID.
        """
        self.url = url
        self.branch = branch
        self.pattern = pattern
        self.blind_connection = blind_connection
        self.hook_id = hook_id

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
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerScmTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
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
        if 'default' in _dict:
            args['default'] = _dict.get('default')
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggerTimerTriggerPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggerTimerTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
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
        if 'default' in _dict:
            args['default'] = _dict.get('default')
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class Triggers():
    """
    Tekton pipeline triggers object.

    :attr List[TriggersTriggersItem] triggers: Tekton pipeline triggers list.
    """

    def __init__(self,
                 triggers: List['TriggersTriggersItem']) -> None:
        """
        Initialize a Triggers object.

        :param List[TriggersTriggersItem] triggers: Tekton pipeline triggers list.
        """
        self.triggers = triggers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Triggers':
        """Initialize a Triggers object from a json dictionary."""
        args = {}
        if 'triggers' in _dict:
            args['triggers'] = _dict.get('triggers')
        else:
            raise ValueError('Required property \'triggers\' not present in Triggers JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Triggers object from a json dictionary."""
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
        """Return a `str` version of this Triggers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Triggers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Triggers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggersTriggersItem():
    """
    Tekton pipeline trigger object.

    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a TriggersTriggersItem object.

        :param str href: (optional) General href URL.
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['TriggersTriggersItemTriggerDuplicateTrigger', 'TriggersTriggersItemTriggerManualTrigger', 'TriggersTriggersItemTriggerScmTrigger', 'TriggersTriggersItemTriggerTimerTrigger', 'TriggersTriggersItemTriggerGenericTrigger']))
        raise Exception(msg)

class TriggersTriggersItemTriggerGenericTriggerPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerGenericTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerGenericTriggerPropertiesItem':
        """Initialize a TriggersTriggersItemTriggerGenericTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerGenericTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'default' in _dict:
            args['default'] = _dict.get('default')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerGenericTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerGenericTriggerPropertiesItem object from a json dictionary."""
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        """Return a `str` version of this TriggersTriggersItemTriggerGenericTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerGenericTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerGenericTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggersTriggersItemTriggerManualTriggerPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerManualTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerManualTriggerPropertiesItem':
        """Initialize a TriggersTriggersItemTriggerManualTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerManualTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'default' in _dict:
            args['default'] = _dict.get('default')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerManualTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerManualTriggerPropertiesItem object from a json dictionary."""
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        """Return a `str` version of this TriggersTriggersItemTriggerManualTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerManualTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerManualTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggersTriggersItemTriggerScmTriggerPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerScmTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerScmTriggerPropertiesItem':
        """Initialize a TriggersTriggersItemTriggerScmTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerScmTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'default' in _dict:
            args['default'] = _dict.get('default')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerScmTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerScmTriggerPropertiesItem object from a json dictionary."""
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        """Return a `str` version of this TriggersTriggersItemTriggerScmTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerScmTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerScmTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class TriggersTriggersItemTriggerTimerTriggerPropertiesItem():
    """
    Trigger Property object.

    :attr str name: Property name.
    :attr str value: (optional) String format property value.
    :attr List[str] enum: (optional) Options for SINGLE_SELECT property type.
    :attr str default: (optional) Default option for SINGLE_SELECT property type.
    :attr str type: Property type.
    :attr str path: (optional) property path for INTEGRATION type properties.
    :attr str href: (optional) General href URL.
    """

    def __init__(self,
                 name: str,
                 type: str,
                 *,
                 value: str = None,
                 enum: List[str] = None,
                 default: str = None,
                 path: str = None,
                 href: str = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerTimerTriggerPropertiesItem object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) String format property value.
        :param List[str] enum: (optional) Options for SINGLE_SELECT property type.
        :param str default: (optional) Default option for SINGLE_SELECT property
               type.
        :param str path: (optional) property path for INTEGRATION type properties.
        :param str href: (optional) General href URL.
        """
        self.name = name
        self.value = value
        self.enum = enum
        self.default = default
        self.type = type
        self.path = path
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerTimerTriggerPropertiesItem':
        """Initialize a TriggersTriggersItemTriggerTimerTriggerPropertiesItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerTimerTriggerPropertiesItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'enum' in _dict:
            args['enum'] = _dict.get('enum')
        if 'default' in _dict:
            args['default'] = _dict.get('default')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerTimerTriggerPropertiesItem JSON')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerTimerTriggerPropertiesItem object from a json dictionary."""
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
        if hasattr(self, 'default') and self.default is not None:
            _dict['default'] = self.default
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
        """Return a `str` version of this TriggersTriggersItemTriggerTimerTriggerPropertiesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerTimerTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerTimerTriggerPropertiesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Property type.
        """
        SECURE = 'SECURE'
        TEXT = 'TEXT'
        INTEGRATION = 'INTEGRATION'
        SINGLE_SELECT = 'SINGLE_SELECT'
        APPCONFIG = 'APPCONFIG'


class UserInfo():
    """
    User information.

    :attr str iam_id: IBM Cloud IAM ID.
    :attr str sub: User Email address.
    """

    def __init__(self,
                 iam_id: str,
                 sub: str) -> None:
        """
        Initialize a UserInfo object.

        :param str iam_id: IBM Cloud IAM ID.
        :param str sub: User Email address.
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

    :attr str name: (optional) worker name.
    :attr str type: (optional) worker type.
    :attr str id: Id.
    """

    def __init__(self,
                 id: str,
                 *,
                 name: str = None,
                 type: str = None) -> None:
        """
        Initialize a Worker object.

        :param str id: Id.
        :param str name: (optional) worker name.
        :param str type: (optional) worker type.
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

    class TypeEnum(str, Enum):
        """
        worker type.
        """
        PRIVATE = 'private'
        PUBLIC = 'public'


class WorkerWithId():
    """
    Worker object with worker ID only.

    :attr str id:
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a WorkerWithId object.

        :param str id:
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

class TriggerDuplicateTrigger(Trigger):
    """
    request body to duplicate trigger.

    :attr str source_trigger_id: source trigger ID to clone from.
    :attr str name: name of the duplicated trigger.
    """

    def __init__(self,
                 source_trigger_id: str,
                 name: str) -> None:
        """
        Initialize a TriggerDuplicateTrigger object.

        :param str source_trigger_id: source trigger ID to clone from.
        :param str name: name of the duplicated trigger.
        """
        # pylint: disable=super-init-not-called
        self.source_trigger_id = source_trigger_id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerDuplicateTrigger':
        """Initialize a TriggerDuplicateTrigger object from a json dictionary."""
        args = {}
        if 'source_trigger_id' in _dict:
            args['source_trigger_id'] = _dict.get('source_trigger_id')
        else:
            raise ValueError('Required property \'source_trigger_id\' not present in TriggerDuplicateTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggerDuplicateTrigger JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerDuplicateTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source_trigger_id') and self.source_trigger_id is not None:
            _dict['source_trigger_id'] = self.source_trigger_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerDuplicateTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerDuplicateTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerDuplicateTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggerGenericTrigger(Trigger):
    """
    Generic trigger, which triggers pipeline when tekton pipeline service receive a valie
    POST event with secrets.

    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggerGenericTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    :attr GenericSecret secret: (optional) Needed only for generic trigger type.
          Secret used to start generic trigger.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 id: str = None,
                 properties: List['TriggerGenericTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None,
                 secret: 'GenericSecret' = None) -> None:
        """
        Initialize a TriggerGenericTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str id: (optional) Id.
        :param List[TriggerGenericTriggerPropertiesItem] properties: (optional)
               Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        :param GenericSecret secret: (optional) Needed only for generic trigger
               type. Secret used to start generic trigger.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
        self.disabled = disabled
        self.secret = secret

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
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggerGenericTrigger JSON')
        if 'secret' in _dict:
            args['secret'] = GenericSecret.from_dict(_dict.get('secret'))
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'secret') and self.secret is not None:
            _dict['secret'] = self.secret.to_dict()
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
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggerManualTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 id: str = None,
                 properties: List['TriggerManualTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None) -> None:
        """
        Initialize a TriggerManualTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str id: (optional) Id.
        :param List[TriggerManualTriggerPropertiesItem] properties: (optional)
               Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
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
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
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
    Git type trigger, which automatically triggers pipelineRun when tekton pipeline
    service receive a valid corresponding git event.

    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggerScmTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    :attr TriggerScmSource scm_source: (optional) Scm source for git type tekton
          pipeline trigger.
    :attr Events events: (optional) Needed only for git trigger type. Events object
          defines the events this git trigger listening to.
    :attr str service_instance_id: (optional) UUID.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 id: str = None,
                 properties: List['TriggerScmTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None,
                 scm_source: 'TriggerScmSource' = None,
                 events: 'Events' = None,
                 service_instance_id: str = None) -> None:
        """
        Initialize a TriggerScmTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str id: (optional) Id.
        :param List[TriggerScmTriggerPropertiesItem] properties: (optional) Trigger
               properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        :param TriggerScmSource scm_source: (optional) Scm source for git type
               tekton pipeline trigger.
        :param Events events: (optional) Needed only for git trigger type. Events
               object defines the events this git trigger listening to.
        :param str service_instance_id: (optional) UUID.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
        self.disabled = disabled
        self.scm_source = scm_source
        self.events = events
        self.service_instance_id = service_instance_id

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
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggerScmTrigger JSON')
        if 'scm_source' in _dict:
            args['scm_source'] = TriggerScmSource.from_dict(_dict.get('scm_source'))
        if 'events' in _dict:
            args['events'] = Events.from_dict(_dict.get('events'))
        if 'service_instance_id' in _dict:
            args['service_instance_id'] = _dict.get('service_instance_id')
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'scm_source') and self.scm_source is not None:
            _dict['scm_source'] = self.scm_source.to_dict()
        if hasattr(self, 'events') and self.events is not None:
            _dict['events'] = self.events.to_dict()
        if hasattr(self, 'service_instance_id') and self.service_instance_id is not None:
            _dict['service_instance_id'] = self.service_instance_id
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
    Timer trigger, which triggers pipelineRun according to the cron value and time zone.

    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggerTimerTriggerPropertiesItem] properties: (optional) Trigger
          properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    :attr str cron: (optional) Needed only for timer trigger type. Cron expression
          for timer trigger. Maximum frequency is every 5 minutes.
    :attr str timezone: (optional) Needed only for timer trigger type. Timezones for
          timer trigger.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 id: str = None,
                 properties: List['TriggerTimerTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None,
                 cron: str = None,
                 timezone: str = None) -> None:
        """
        Initialize a TriggerTimerTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str id: (optional) Id.
        :param List[TriggerTimerTriggerPropertiesItem] properties: (optional)
               Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        :param str cron: (optional) Needed only for timer trigger type. Cron
               expression for timer trigger. Maximum frequency is every 5 minutes.
        :param str timezone: (optional) Needed only for timer trigger type.
               Timezones for timer trigger.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
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
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
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

class TriggersTriggersItemTriggerDuplicateTrigger(TriggersTriggersItem):
    """
    request body to duplicate trigger.

    :attr str href: (optional) General href URL.
    :attr str source_trigger_id: source trigger ID to clone from.
    :attr str name: name of the duplicated trigger.
    """

    def __init__(self,
                 source_trigger_id: str,
                 name: str,
                 *,
                 href: str = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerDuplicateTrigger object.

        :param str source_trigger_id: source trigger ID to clone from.
        :param str name: name of the duplicated trigger.
        :param str href: (optional) General href URL.
        """
        # pylint: disable=super-init-not-called
        self.href = href
        self.source_trigger_id = source_trigger_id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerDuplicateTrigger':
        """Initialize a TriggersTriggersItemTriggerDuplicateTrigger object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'source_trigger_id' in _dict:
            args['source_trigger_id'] = _dict.get('source_trigger_id')
        else:
            raise ValueError('Required property \'source_trigger_id\' not present in TriggersTriggersItemTriggerDuplicateTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerDuplicateTrigger JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerDuplicateTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'source_trigger_id') and self.source_trigger_id is not None:
            _dict['source_trigger_id'] = self.source_trigger_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggersTriggersItemTriggerDuplicateTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerDuplicateTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerDuplicateTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggersTriggersItemTriggerGenericTrigger(TriggersTriggersItem):
    """
    Generic trigger, which triggers pipeline when tekton pipeline service receive a valie
    POST event with secrets.

    :attr str href: (optional) General href URL.
    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggersTriggersItemTriggerGenericTriggerPropertiesItem] properties:
          (optional) Trigger properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    :attr GenericSecret secret: (optional) Needed only for generic trigger type.
          Secret used to start generic trigger.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 href: str = None,
                 id: str = None,
                 properties: List['TriggersTriggersItemTriggerGenericTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None,
                 secret: 'GenericSecret' = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerGenericTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str href: (optional) General href URL.
        :param str id: (optional) Id.
        :param List[TriggersTriggersItemTriggerGenericTriggerPropertiesItem]
               properties: (optional) Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        :param GenericSecret secret: (optional) Needed only for generic trigger
               type. Secret used to start generic trigger.
        """
        # pylint: disable=super-init-not-called
        self.href = href
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
        self.disabled = disabled
        self.secret = secret

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerGenericTrigger':
        """Initialize a TriggersTriggersItemTriggerGenericTrigger object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerGenericTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerGenericTrigger JSON')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggersTriggersItemTriggerGenericTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggersTriggersItemTriggerGenericTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggersTriggersItemTriggerGenericTrigger JSON')
        if 'secret' in _dict:
            args['secret'] = GenericSecret.from_dict(_dict.get('secret'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerGenericTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'secret') and self.secret is not None:
            _dict['secret'] = self.secret.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggersTriggersItemTriggerGenericTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerGenericTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerGenericTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggersTriggersItemTriggerManualTrigger(TriggersTriggersItem):
    """
    Manual trigger.

    :attr str href: (optional) General href URL.
    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggersTriggersItemTriggerManualTriggerPropertiesItem] properties:
          (optional) Trigger properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 href: str = None,
                 id: str = None,
                 properties: List['TriggersTriggersItemTriggerManualTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerManualTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str href: (optional) General href URL.
        :param str id: (optional) Id.
        :param List[TriggersTriggersItemTriggerManualTriggerPropertiesItem]
               properties: (optional) Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        """
        # pylint: disable=super-init-not-called
        self.href = href
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
        self.disabled = disabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerManualTrigger':
        """Initialize a TriggersTriggersItemTriggerManualTrigger object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerManualTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerManualTrigger JSON')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggersTriggersItemTriggerManualTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggersTriggersItemTriggerManualTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggersTriggersItemTriggerManualTrigger JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerManualTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggersTriggersItemTriggerManualTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerManualTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerManualTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggersTriggersItemTriggerScmTrigger(TriggersTriggersItem):
    """
    Git type trigger, which automatically triggers pipelineRun when tekton pipeline
    service receive a valid corresponding git event.

    :attr str href: (optional) General href URL.
    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggersTriggersItemTriggerScmTriggerPropertiesItem] properties:
          (optional) Trigger properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    :attr TriggerScmSource scm_source: (optional) Scm source for git type tekton
          pipeline trigger.
    :attr Events events: (optional) Needed only for git trigger type. Events object
          defines the events this git trigger listening to.
    :attr str service_instance_id: (optional) UUID.
    """

    def __init__(self,
                 type: str,
                 name: str,
                 event_listener: str,
                 disabled: bool,
                 *,
                 href: str = None,
                 id: str = None,
                 properties: List['TriggersTriggersItemTriggerScmTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None,
                 scm_source: 'TriggerScmSource' = None,
                 events: 'Events' = None,
                 service_instance_id: str = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerScmTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str href: (optional) General href URL.
        :param str id: (optional) Id.
        :param List[TriggersTriggersItemTriggerScmTriggerPropertiesItem]
               properties: (optional) Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        :param TriggerScmSource scm_source: (optional) Scm source for git type
               tekton pipeline trigger.
        :param Events events: (optional) Needed only for git trigger type. Events
               object defines the events this git trigger listening to.
        :param str service_instance_id: (optional) UUID.
        """
        # pylint: disable=super-init-not-called
        self.href = href
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
        self.disabled = disabled
        self.scm_source = scm_source
        self.events = events
        self.service_instance_id = service_instance_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerScmTrigger':
        """Initialize a TriggersTriggersItemTriggerScmTrigger object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerScmTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerScmTrigger JSON')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggersTriggersItemTriggerScmTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggersTriggersItemTriggerScmTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggersTriggersItemTriggerScmTrigger JSON')
        if 'scm_source' in _dict:
            args['scm_source'] = TriggerScmSource.from_dict(_dict.get('scm_source'))
        if 'events' in _dict:
            args['events'] = Events.from_dict(_dict.get('events'))
        if 'service_instance_id' in _dict:
            args['service_instance_id'] = _dict.get('service_instance_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerScmTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'scm_source') and self.scm_source is not None:
            _dict['scm_source'] = self.scm_source.to_dict()
        if hasattr(self, 'events') and self.events is not None:
            _dict['events'] = self.events.to_dict()
        if hasattr(self, 'service_instance_id') and self.service_instance_id is not None:
            _dict['service_instance_id'] = self.service_instance_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggersTriggersItemTriggerScmTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerScmTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerScmTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TriggersTriggersItemTriggerTimerTrigger(TriggersTriggersItem):
    """
    Timer trigger, which triggers pipelineRun according to the cron value and time zone.

    :attr str href: (optional) General href URL.
    :attr str type: Trigger type.
    :attr str name: Trigger name.
    :attr str event_listener: Event listener name.
    :attr str id: (optional) Id.
    :attr List[TriggersTriggersItemTriggerTimerTriggerPropertiesItem] properties:
          (optional) Trigger properties.
    :attr List[str] tags: (optional) Trigger tags array.
    :attr Worker worker: (optional) Trigger worker used to run the trigger, the
          trigger worker overrides the default pipeline worker.If not exist, this trigger
          uses default pipeline worker.
    :attr Concurrency concurrency: (optional) Concurrency object.
    :attr bool disabled: flag whether the trigger is disabled.
    :attr str cron: (optional) Needed only for timer trigger type. Cron expression
          for timer trigger. Maximum frequency is every 5 minutes.
    :attr str timezone: (optional) Needed only for timer trigger type. Timezones for
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
                 properties: List['TriggersTriggersItemTriggerTimerTriggerPropertiesItem'] = None,
                 tags: List[str] = None,
                 worker: 'Worker' = None,
                 concurrency: 'Concurrency' = None,
                 cron: str = None,
                 timezone: str = None) -> None:
        """
        Initialize a TriggersTriggersItemTriggerTimerTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name.
        :param bool disabled: flag whether the trigger is disabled.
        :param str href: (optional) General href URL.
        :param str id: (optional) Id.
        :param List[TriggersTriggersItemTriggerTimerTriggerPropertiesItem]
               properties: (optional) Trigger properties.
        :param List[str] tags: (optional) Trigger tags array.
        :param Worker worker: (optional) Trigger worker used to run the trigger,
               the trigger worker overrides the default pipeline worker.If not exist, this
               trigger uses default pipeline worker.
        :param Concurrency concurrency: (optional) Concurrency object.
        :param str cron: (optional) Needed only for timer trigger type. Cron
               expression for timer trigger. Maximum frequency is every 5 minutes.
        :param str timezone: (optional) Needed only for timer trigger type.
               Timezones for timer trigger.
        """
        # pylint: disable=super-init-not-called
        self.href = href
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.id = id
        self.properties = properties
        self.tags = tags
        self.worker = worker
        self.concurrency = concurrency
        self.disabled = disabled
        self.cron = cron
        self.timezone = timezone

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersTriggersItemTriggerTimerTrigger':
        """Initialize a TriggersTriggersItemTriggerTimerTrigger object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in TriggersTriggersItemTriggerTimerTrigger JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in TriggersTriggersItemTriggerTimerTrigger JSON')
        if 'event_listener' in _dict:
            args['event_listener'] = _dict.get('event_listener')
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggersTriggersItemTriggerTimerTrigger JSON')
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'properties' in _dict:
            args['properties'] = [TriggersTriggersItemTriggerTimerTriggerPropertiesItem.from_dict(x) for x in _dict.get('properties')]
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'worker' in _dict:
            args['worker'] = Worker.from_dict(_dict.get('worker'))
        if 'concurrency' in _dict:
            args['concurrency'] = Concurrency.from_dict(_dict.get('concurrency'))
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in TriggersTriggersItemTriggerTimerTrigger JSON')
        if 'cron' in _dict:
            args['cron'] = _dict.get('cron')
        if 'timezone' in _dict:
            args['timezone'] = _dict.get('timezone')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggersTriggersItemTriggerTimerTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
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
        if hasattr(self, 'concurrency') and self.concurrency is not None:
            _dict['concurrency'] = self.concurrency.to_dict()
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
        """Return a `str` version of this TriggersTriggersItemTriggerTimerTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggersTriggersItemTriggerTimerTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggersTriggersItemTriggerTimerTrigger') -> bool:
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
                 status: str = None,
                 trigger_name: str = None,
    ) -> None:
        """
        Initialize a TektonPipelineRunsPager object.
        :param str pipeline_id: The tekton pipeline ID.
        :param int limit: (optional) The number of pipeline runs to return, sorted
               by creation time, most recent first.
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
        :return: A List[dict], where each element is a dict that represents an instance of PipelineRunsPipelineRunsItem.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_tekton_pipeline_runs(
            pipeline_id=self._pipeline_id,
            limit=self._limit,
            status=self._status,
            trigger_name=self._trigger_name,
            offset=self._page_context.get('next'),
        ).get_result()

        next = None
        next_page_link = result.get('next')
        if next_page_link is not None:
            next = get_query_param(next_page_link.get('href'), 'offset')
        self._page_context['next'] = next
        if next is None:
            self._has_next = False

        return result.get('pipeline_runs')

    def get_all(self) -> List[dict]:
        """
        Returns all results by invoking get_next() repeatedly
        until all pages of results have been retrieved.
        :return: A List[dict], where each element is a dict that represents an instance of PipelineRunsPipelineRunsItem.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
