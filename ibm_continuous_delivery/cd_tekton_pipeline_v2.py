# coding: utf-8

# (C) Copyright IBM Corp. 2025.
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

# IBM OpenAPI SDK Code Generator Version: 3.103.0-e8b84313-20250402-201816

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
from typing import Dict, List, Optional
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
        'us-south': 'https://api.us-south.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the us-south region.
        'us-east': 'https://api.us-east.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the us-east region.
        'eu-de': 'https://api.eu-de.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the eu-de region.
        'eu-gb': 'https://api.eu-gb.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the eu-gb region.
        'eu-es': 'https://api.eu-es.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the eu-es region.
        'jp-osa': 'https://api.jp-osa.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the jp-osa region.
        'jp-tok': 'https://api.jp-tok.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the jp-tok region.
        'au-syd': 'https://api.au-syd.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the au-syd region.
        'ca-tor': 'https://api.ca-tor.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the ca-tor region.
        'br-sao': 'https://api.br-sao.devops.cloud.ibm.com/pipeline/v2',  # The host URL for Tekton Pipeline Service in the br-sao region.
    }

    @classmethod
    def new_instance(
        cls,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'CdTektonPipelineV2':
        """
        Return a new client for the CD Tekton Pipeline service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(authenticator)
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

    def __init__(
        self,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the CD Tekton Pipeline service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)

    #########################
    # Pipeline
    #########################

    def create_tekton_pipeline(
        self,
        id: str,
        *,
        next_build_number: Optional[int] = None,
        enable_notifications: Optional[bool] = None,
        enable_partial_cloning: Optional[bool] = None,
        worker: Optional['WorkerIdentity'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create Tekton pipeline.

        This request creates a Tekton pipeline. Requires a pipeline tool already created
        in the toolchain using the toolchain API
        https://cloud.ibm.com/apidocs/toolchain#create-tool, and use the tool ID to create
        the Tekton pipeline.

        :param str id: The ID for the associated pipeline tool, which was already
               created in the target toolchain. To get the pipeline ID call the toolchain
               API https://cloud.ibm.com/apidocs/toolchain#list-tools and find the
               pipeline tool.
        :param int next_build_number: (optional) Specify the build number that will
               be used for the next pipeline run. Build numbers can be any positive whole
               number between 0 and 100000000000000.
        :param bool enable_notifications: (optional) Flag to enable notifications
               for this pipeline. If enabled, the Tekton pipeline run events will be
               published to all the destinations specified by the Slack and Event
               Notifications integrations in the parent toolchain.
        :param bool enable_partial_cloning: (optional) Flag to enable partial
               cloning for this pipeline. When partial clone is enabled, only the files
               contained within the paths specified in definition repositories are read
               and cloned, this means that symbolic links might not work.
        :param WorkerIdentity worker: (optional) Specify the worker that is to be
               used to run the trigger, indicated by a worker object with only the worker
               ID. If not specified or set as `worker: { id: 'public' }`, the IBM Managed
               shared workers are used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TektonPipeline` object
        """

        if id is None:
            raise ValueError('id must be provided')
        if worker is not None:
            worker = convert_model(worker)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_tekton_pipeline',
        )
        headers.update(sdk_headers)

        data = {
            'id': id,
            'next_build_number': next_build_number,
            'enable_notifications': enable_notifications,
            'enable_partial_cloning': enable_partial_cloning,
            'worker': worker,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/tekton_pipelines'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline(
        self,
        id: str,
        **kwargs,
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

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_tekton_pipeline(
        self,
        id: str,
        *,
        tekton_pipeline_patch: Optional['TektonPipelinePatch'] = None,
        **kwargs,
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

        if not id:
            raise ValueError('id must be provided')
        if tekton_pipeline_patch is not None and isinstance(tekton_pipeline_patch, TektonPipelinePatch):
            tekton_pipeline_patch = convert_model(tekton_pipeline_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_tekton_pipeline',
        )
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
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_tekton_pipeline(
        self,
        id: str,
        **kwargs,
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

        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_tekton_pipeline',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['id']
        path_param_values = self.encode_path_vars(id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # PipelineRuns
    #########################

    def list_tekton_pipeline_runs(
        self,
        pipeline_id: str,
        *,
        start: Optional[str] = None,
        limit: Optional[int] = None,
        status: Optional[str] = None,
        trigger_name: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List pipeline run records.

        This request lists pipeline run records, which has data about the runs, such as
        status, user_info, trigger and other information. Default limit is 50.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str start: (optional) A page token that identifies the start point
               of the list of pipeline runs. This value is included in the response body
               of each request to fetch pipeline runs.
        :param int limit: (optional) The number of pipeline runs to return, sorted
               by creation time, most recent first.
        :param str status: (optional) Filters the collection to resources with the
               specified status.
        :param str trigger_name: (optional) Filters the collection to resources
               with the specified trigger name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRunsCollection` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_tekton_pipeline_runs',
        )
        headers.update(sdk_headers)

        params = {
            'start': start,
            'limit': limit,
            'status': status,
            'trigger.name': trigger_name,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_tekton_pipeline_run(
        self,
        pipeline_id: str,
        *,
        description: Optional[str] = None,
        trigger_name: Optional[str] = None,
        trigger_properties: Optional[dict] = None,
        secure_trigger_properties: Optional[dict] = None,
        trigger_headers: Optional[dict] = None,
        trigger_body: Optional[dict] = None,
        trigger: Optional['PipelineRunTrigger'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Trigger a pipeline run.

        Trigger a new pipeline run using either the manual or the timed trigger,
        specifying the additional properties or overriding existing ones as needed.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str description: (optional) Optional description for the created
               PipelineRun.
        :param str trigger_name: (optional) Trigger name.
        :param dict trigger_properties: (optional) An object containing string
               values only. It provides additional 'text' properties or overrides existing
               pipeline/trigger properties that can be used in the created run.
        :param dict secure_trigger_properties: (optional) An object containing
               string values only. It provides additional `secure` properties or overrides
               existing `secure` pipeline/trigger properties that can be used in the
               created run.
        :param dict trigger_headers: (optional) An object containing string values
               only that provides the request headers. Use `$(header.header_key_name)` to
               access it in a TriggerBinding. Most commonly used as part of a Generic
               Webhook to provide a verification token or signature in the request
               headers.
        :param dict trigger_body: (optional) An object that provides the request
               body. Use `$(body.body_key_name)` to access it in a TriggerBinding. Most
               commonly used to pass in additional properties or override properties for
               the pipeline run that is created.
        :param PipelineRunTrigger trigger: (optional) Trigger details passed when
               triggering a Tekton pipeline run.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRun` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if trigger is not None:
            trigger = convert_model(trigger)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_tekton_pipeline_run',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
            'trigger_name': trigger_name,
            'trigger_properties': trigger_properties,
            'secure_trigger_properties': secure_trigger_properties,
            'trigger_headers': trigger_headers,
            'trigger_body': trigger_body,
            'trigger': trigger,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline_run(
        self,
        pipeline_id: str,
        id: str,
        *,
        includes: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a pipeline run record.

        This request retrieves details of the pipeline run identified by `{id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str id: ID of current instance.
        :param str includes: (optional) Defines if response includes definition
               metadata.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRun` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline_run',
        )
        headers.update(sdk_headers)

        params = {
            'includes': includes,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_tekton_pipeline_run(
        self,
        pipeline_id: str,
        id: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_tekton_pipeline_run',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def cancel_tekton_pipeline_run(
        self,
        pipeline_id: str,
        id: str,
        *,
        force: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Cancel a pipeline run.

        This request cancels a running pipeline run identified by `{id}`. Use `force:
        true` in the body if the pipeline run can't be cancelled normally.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str id: ID of current instance.
        :param bool force: (optional) Flag indicating whether the pipeline
               cancellation action is forced or not.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PipelineRun` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='cancel_tekton_pipeline_run',
        )
        headers.update(sdk_headers)

        data = {
            'force': force,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def rerun_tekton_pipeline_run(
        self,
        pipeline_id: str,
        id: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='rerun_tekton_pipeline_run',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}/rerun'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline_run_logs(
        self,
        pipeline_id: str,
        id: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline_run_logs',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{id}/logs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline_run_log_content(
        self,
        pipeline_id: str,
        pipeline_run_id: str,
        id: str,
        **kwargs,
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
        :rtype: DetailedResponse with `dict` result representing a `StepLog` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not pipeline_run_id:
            raise ValueError('pipeline_run_id must be provided')
        if not id:
            raise ValueError('id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline_run_log_content',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'pipeline_run_id', 'id']
        path_param_values = self.encode_path_vars(pipeline_id, pipeline_run_id, id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/pipeline_runs/{pipeline_run_id}/logs/{id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Definitions
    #########################

    def list_tekton_pipeline_definitions(
        self,
        pipeline_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List pipeline definitions.

        This request fetches pipeline definitions, which is a collection of individual
        definition entries. Each entry consists of a repository url, a repository path and
        a branch or tag. The referenced repository URL must match the URL of a repository
        tool integration in the parent toolchain. Obtain the list of integrations from the
        toolchain API https://cloud.ibm.com/apidocs/toolchain#list-tools. The branch or
        tag of the definition must match against a corresponding branch or tag in the
        chosen repository, and the path must match a subfolder in the repository.

        :param str pipeline_id: The Tekton pipeline ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DefinitionsCollection` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_tekton_pipeline_definitions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_tekton_pipeline_definition(
        self,
        pipeline_id: str,
        source: 'DefinitionSource',
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a single definition.

        This request adds a single definition. The source properties should consist of a
        repository url, a repository path and a branch or tag. The referenced repository
        URL must match the URL of a repository tool integration in the parent toolchain.
        Obtain the list of integrations from the toolchain API
        https://cloud.ibm.com/apidocs/toolchain#list-tools. The branch or tag of the
        definition must match against a corresponding branch or tag in the chosen
        repository, and the path must match a subfolder in the repository.

        :param str pipeline_id: The Tekton pipeline ID.
        :param DefinitionSource source: Source repository containing the Tekton
               pipeline definition.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Definition` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if source is None:
            raise ValueError('source must be provided')
        source = convert_model(source)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_tekton_pipeline_definition',
        )
        headers.update(sdk_headers)

        data = {
            'source': source,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline_definition(
        self,
        pipeline_id: str,
        definition_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Retrieve a single definition entry.

        This request fetches a single definition entry, which consists of the definition
        repository URL, a repository path, and a branch or tag.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str definition_id: The definition ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Definition` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not definition_id:
            raise ValueError('definition_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline_definition',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'definition_id']
        path_param_values = self.encode_path_vars(pipeline_id, definition_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions/{definition_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_tekton_pipeline_definition(
        self,
        pipeline_id: str,
        definition_id: str,
        source: 'DefinitionSource',
        **kwargs,
    ) -> DetailedResponse:
        """
        Edit a single definition entry.

        This request updates a definition entry identified by `{definition_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str definition_id: The definition ID.
        :param DefinitionSource source: Source repository containing the Tekton
               pipeline definition.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Definition` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not definition_id:
            raise ValueError('definition_id must be provided')
        if source is None:
            raise ValueError('source must be provided')
        source = convert_model(source)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_tekton_pipeline_definition',
        )
        headers.update(sdk_headers)

        data = {
            'source': source,
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
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_tekton_pipeline_definition(
        self,
        pipeline_id: str,
        definition_id: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not definition_id:
            raise ValueError('definition_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_tekton_pipeline_definition',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'definition_id']
        path_param_values = self.encode_path_vars(pipeline_id, definition_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/definitions/{definition_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Environment properties
    #########################

    def list_tekton_pipeline_properties(
        self,
        pipeline_id: str,
        *,
        name: Optional[str] = None,
        type: Optional[List[str]] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List the pipeline's environment properties.

        This request lists the environment properties of the pipeline identified by
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_tekton_pipeline_properties',
        )
        headers.update(sdk_headers)

        params = {
            'name': name,
            'type': convert_list(type),
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_tekton_pipeline_properties(
        self,
        pipeline_id: str,
        name: str,
        type: str,
        *,
        value: Optional[str] = None,
        enum: Optional[List[str]] = None,
        locked: Optional[bool] = None,
        path: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a pipeline environment property.

        This request creates an environment property.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Any string value is valid.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed when using `single_select` property type.
        :param bool locked: (optional) When true, this property cannot be
               overridden by a trigger property or at runtime. Attempting to override it
               will result in run requests being rejected. The default is false.
        :param str path: (optional) A dot notation path for `integration` type
               properties only, to select a value from the tool integration. If left blank
               the full tool integration data will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Property` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_tekton_pipeline_properties',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'locked': locked,
            'path': path,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline_property(
        self,
        pipeline_id: str,
        property_name: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not property_name:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline_property',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_tekton_pipeline_property(
        self,
        pipeline_id: str,
        property_name: str,
        name: str,
        type: str,
        *,
        value: Optional[str] = None,
        enum: Optional[List[str]] = None,
        locked: Optional[bool] = None,
        path: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Replace the value of an environment property.

        This request updates the value of an environment property identified by
        `{property_name}`, its type and name are immutable.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str property_name: The property name.
        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Any string value is valid.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed when using `single_select` property type.
        :param bool locked: (optional) When true, this property cannot be
               overridden by a trigger property or at runtime. Attempting to override it
               will result in run requests being rejected. The default is false.
        :param str path: (optional) A dot notation path for `integration` type
               properties only, to select a value from the tool integration. If left blank
               the full tool integration data will be used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Property` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not property_name:
            raise ValueError('property_name must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_tekton_pipeline_property',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'locked': locked,
            'path': path,
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
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_tekton_pipeline_property(
        self,
        pipeline_id: str,
        property_name: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not property_name:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_tekton_pipeline_property',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/properties/{property_name}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Triggers
    #########################

    def list_tekton_pipeline_triggers(
        self,
        pipeline_id: str,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        event_listener: Optional[str] = None,
        worker_id: Optional[str] = None,
        worker_name: Optional[str] = None,
        disabled: Optional[str] = None,
        tags: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List pipeline triggers.

        This request lists pipeline triggers for the pipeline identified by
        `{pipeline_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str type: (optional) Optional filter by "type", accepts a comma
               separated list of types. Valid types are "manual", "scm", "generic", and
               "timer".
        :param str name: (optional) Optional filter by "name", accepts a single
               string value.
        :param str event_listener: (optional) Optional filter by "event_listener",
               accepts a single string value.
        :param str worker_id: (optional) Optional filter by "worker.id", accepts a
               single string value.
        :param str worker_name: (optional) Optional filter by "worker.name",
               accepts a single string value.
        :param str disabled: (optional) Optional filter by "disabled" state,
               possible values are "true" or "false".
        :param str tags: (optional) Optional filter by "tags", accepts a comma
               separated list of tags. The response lists triggers having at least one
               matching tag.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggersCollection` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_tekton_pipeline_triggers',
        )
        headers.update(sdk_headers)

        params = {
            'type': type,
            'name': name,
            'event_listener': event_listener,
            'worker.id': worker_id,
            'worker.name': worker_name,
            'disabled': disabled,
            'tags': tags,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id']
        path_param_values = self.encode_path_vars(pipeline_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_tekton_pipeline_trigger(
        self,
        pipeline_id: str,
        type: str,
        name: str,
        event_listener: str,
        *,
        tags: Optional[List[str]] = None,
        worker: Optional['WorkerIdentity'] = None,
        max_concurrent_runs: Optional[int] = None,
        limit_waiting_runs: Optional[bool] = None,
        enabled: Optional[bool] = None,
        secret: Optional['GenericSecret'] = None,
        cron: Optional[str] = None,
        timezone: Optional[str] = None,
        source: Optional['TriggerSourcePrototype'] = None,
        events: Optional[List[str]] = None,
        filter: Optional[str] = None,
        favorite: Optional[bool] = None,
        enable_events_from_forks: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a trigger.

        This request creates a trigger.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param List[str] tags: (optional) Trigger tags array.
        :param WorkerIdentity worker: (optional) Specify the worker used to run the
               trigger. Use `worker: { id: 'public' }` to use the IBM Managed workers. The
               default is to inherit the worker set in the pipeline settings, which can
               also be explicitly set using `worker: { id: 'inherit' }`.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. If omitted then the concurrency limit is
               disabled for this trigger.
        :param bool limit_waiting_runs: (optional) Only used for SCM triggers. Flag
               that will limit the trigger to a maximum of one waiting run. A newly
               triggered run will cause waiting run(s) to be automatically cancelled.
        :param bool enabled: (optional) Flag to check if the trigger is enabled. If
               omitted the trigger is enabled by default.
        :param GenericSecret secret: (optional) Only needed for Generic Webhook
               trigger type. The secret is used to start the Generic Webhook trigger.
        :param str cron: (optional) Only needed for timer triggers. CRON expression
               that indicates when this trigger will activate. Maximum frequency is every
               5 minutes. The string is based on UNIX crontab syntax: minute, hour, day of
               month, month, day of week. Example: The CRON expression 0 */2 * * * -
               translates to - every 2 hours.
        :param str timezone: (optional) Only used for timer triggers. Specify the
               timezone used for this timer trigger, which will ensure the CRON activates
               this trigger relative to the specified timezone. If no timezone is
               specified, the default timezone used is UTC. Valid timezones are those
               listed in the IANA timezone database, https://www.iana.org/time-zones.
        :param TriggerSourcePrototype source: (optional) Source repository for a
               Git trigger. Only required for Git triggers. The referenced repository URL
               must match the URL of a repository tool integration in the parent
               toolchain. Obtain the list of integrations from the toolchain API
               https://cloud.ibm.com/apidocs/toolchain#list-tools.
        :param List[str] events: (optional) Either 'events' or 'filter' is required
               specifically for Git triggers. Stores a list of events that a Git trigger
               listens to. Choose one or more from 'push', 'pull_request', and
               'pull_request_closed'. If SCM repositories use the 'merge request' term,
               they correspond to the generic term i.e. 'pull request'.
        :param str filter: (optional) Either 'events' or 'filter' can be used.
               Stores the CEL (Common Expression Language) expression value which is used
               for event filtering against the Git webhook payloads.
        :param bool favorite: (optional) Mark the trigger as a favorite.
        :param bool enable_events_from_forks: (optional) Only used for SCM
               triggers. When enabled, pull request events from forks of the selected
               repository will trigger a pipeline run.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if type is None:
            raise ValueError('type must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if event_listener is None:
            raise ValueError('event_listener must be provided')
        if worker is not None:
            worker = convert_model(worker)
        if secret is not None:
            secret = convert_model(secret)
        if source is not None:
            source = convert_model(source)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_tekton_pipeline_trigger',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'event_listener': event_listener,
            'tags': tags,
            'worker': worker,
            'max_concurrent_runs': max_concurrent_runs,
            'limit_waiting_runs': limit_waiting_runs,
            'enabled': enabled,
            'secret': secret,
            'cron': cron,
            'timezone': timezone,
            'source': source,
            'events': events,
            'filter': filter,
            'favorite': favorite,
            'enable_events_from_forks': enable_events_from_forks,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline_trigger(
        self,
        pipeline_id: str,
        trigger_id: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline_trigger',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_tekton_pipeline_trigger(
        self,
        pipeline_id: str,
        trigger_id: str,
        *,
        trigger_patch: Optional['TriggerPatch'] = None,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        if trigger_patch is not None and isinstance(trigger_patch, TriggerPatch):
            trigger_patch = convert_model(trigger_patch)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_tekton_pipeline_trigger',
        )
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
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_tekton_pipeline_trigger(
        self,
        pipeline_id: str,
        trigger_id: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_tekton_pipeline_trigger',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def duplicate_tekton_pipeline_trigger(
        self,
        pipeline_id: str,
        source_trigger_id: str,
        name: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Duplicate a trigger.

        This request duplicates a trigger from an existing trigger identified by
        `{source_trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str source_trigger_id: The ID of the trigger to duplicate.
        :param str name: Trigger name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Trigger` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not source_trigger_id:
            raise ValueError('source_trigger_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='duplicate_tekton_pipeline_trigger',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Trigger properties
    #########################

    def list_tekton_pipeline_trigger_properties(
        self,
        pipeline_id: str,
        trigger_id: str,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List trigger properties.

        This request lists trigger properties for the trigger identified by
        `{trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str name: (optional) Filter properties by `name`.
        :param str type: (optional) Filter properties by `type`. Valid types are
               `secure`, `text`, `integration`, `single_select`, `appconfig`.
        :param str sort: (optional) Sort properties by name. They can be sorted in
               ascending order using `name` or in descending order using `-name`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerPropertiesCollection` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_tekton_pipeline_trigger_properties',
        )
        headers.update(sdk_headers)

        params = {
            'name': name,
            'type': type,
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_tekton_pipeline_trigger_properties(
        self,
        pipeline_id: str,
        trigger_id: str,
        name: str,
        type: str,
        *,
        value: Optional[str] = None,
        enum: Optional[List[str]] = None,
        path: Optional[str] = None,
        locked: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a trigger property.

        This request creates a property in the trigger identified by `{trigger_id}`.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Any string value is valid.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties only, to select a value from the tool integration. If left blank
               the full tool integration data will be used.
        :param bool locked: (optional) When true, this property cannot be
               overridden at runtime. Attempting to override it will result in run
               requests being rejected. The default is false.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerProperty` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_tekton_pipeline_trigger_properties',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'path': path,
            'locked': locked,
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
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_tekton_pipeline_trigger_property(
        self,
        pipeline_id: str,
        trigger_id: str,
        property_name: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        if not property_name:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_tekton_pipeline_trigger_property',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['pipeline_id', 'trigger_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties/{property_name}'.format(
            **path_param_dict
        )
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def replace_tekton_pipeline_trigger_property(
        self,
        pipeline_id: str,
        trigger_id: str,
        property_name: str,
        name: str,
        type: str,
        *,
        value: Optional[str] = None,
        enum: Optional[List[str]] = None,
        path: Optional[str] = None,
        locked: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Replace a trigger property value.

        This request updates a trigger property value, type and name are immutable.

        :param str pipeline_id: The Tekton pipeline ID.
        :param str trigger_id: The trigger ID.
        :param str property_name: The property name.
        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Any string value is valid.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties only, to select a value from the tool integration. If left blank
               the full tool integration data will be used.
        :param bool locked: (optional) When true, this property cannot be
               overridden at runtime. Attempting to override it will result in run
               requests being rejected. The default is false.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TriggerProperty` object
        """

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        if not property_name:
            raise ValueError('property_name must be provided')
        if name is None:
            raise ValueError('name must be provided')
        if type is None:
            raise ValueError('type must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='replace_tekton_pipeline_trigger_property',
        )
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'value': value,
            'enum': enum,
            'path': path,
            'locked': locked,
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
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties/{property_name}'.format(
            **path_param_dict
        )
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_tekton_pipeline_trigger_property(
        self,
        pipeline_id: str,
        trigger_id: str,
        property_name: str,
        **kwargs,
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

        if not pipeline_id:
            raise ValueError('pipeline_id must be provided')
        if not trigger_id:
            raise ValueError('trigger_id must be provided')
        if not property_name:
            raise ValueError('property_name must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_tekton_pipeline_trigger_property',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['pipeline_id', 'trigger_id', 'property_name']
        path_param_values = self.encode_path_vars(pipeline_id, trigger_id, property_name)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/tekton_pipelines/{pipeline_id}/triggers/{trigger_id}/properties/{property_name}'.format(
            **path_param_dict
        )
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

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


class Definition:
    """
    Tekton pipeline definition entry object, consisting of a repository url, a repository
    path and a branch or tag. The referenced repository URL must match the URL of a
    repository tool integration in the parent toolchain. Obtain the list of integrations
    from the toolchain API https://cloud.ibm.com/apidocs/toolchain#list-tools. The branch
    or tag of the definition must match against a corresponding branch or tag in the
    chosen repository, and the path must match a subfolder in the repository.

    :param DefinitionSource source: Source repository containing the Tekton pipeline
          definition.
    :param str href: (optional) API URL for interacting with the definition.
    :param str id: The aggregated definition ID.
    """

    def __init__(
        self,
        source: 'DefinitionSource',
        id: str,
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a Definition object.

        :param DefinitionSource source: Source repository containing the Tekton
               pipeline definition.
        :param str id: The aggregated definition ID.
        :param str href: (optional) API URL for interacting with the definition.
        """
        self.source = source
        self.href = href
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Definition':
        """Initialize a Definition object from a json dictionary."""
        args = {}
        if (source := _dict.get('source')) is not None:
            args['source'] = DefinitionSource.from_dict(source)
        else:
            raise ValueError('Required property \'source\' not present in Definition JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Definition JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Definition object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
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


class DefinitionSource:
    """
    Source repository containing the Tekton pipeline definition.

    :param str type: The only supported source type is "git", indicating that the
          source is a git repository.
    :param DefinitionSourceProperties properties: Properties of the source, which
          define the URL of the repository and a branch or tag.
    """

    def __init__(
        self,
        type: str,
        properties: 'DefinitionSourceProperties',
    ) -> None:
        """
        Initialize a DefinitionSource object.

        :param str type: The only supported source type is "git", indicating that
               the source is a git repository.
        :param DefinitionSourceProperties properties: Properties of the source,
               which define the URL of the repository and a branch or tag.
        """
        self.type = type
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefinitionSource':
        """Initialize a DefinitionSource object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in DefinitionSource JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = DefinitionSourceProperties.from_dict(properties)
        else:
            raise ValueError('Required property \'properties\' not present in DefinitionSource JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefinitionSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'properties') and self.properties is not None:
            if isinstance(self.properties, dict):
                _dict['properties'] = self.properties
            else:
                _dict['properties'] = self.properties.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefinitionSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefinitionSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefinitionSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefinitionSourceProperties:
    """
    Properties of the source, which define the URL of the repository and a branch or tag.

    :param str url: URL of the definition repository.
    :param str branch: (optional) A branch from the repo, specify one of branch or
          tag only.
    :param str tag: (optional) A tag from the repo, specify one of branch or tag
          only.
    :param str path: The path to the definition's YAML files.
    :param Tool tool: (optional) Reference to the repository tool in the parent
          toolchain.
    """

    def __init__(
        self,
        url: str,
        path: str,
        *,
        branch: Optional[str] = None,
        tag: Optional[str] = None,
        tool: Optional['Tool'] = None,
    ) -> None:
        """
        Initialize a DefinitionSourceProperties object.

        :param str url: URL of the definition repository.
        :param str path: The path to the definition's YAML files.
        :param str branch: (optional) A branch from the repo, specify one of branch
               or tag only.
        :param str tag: (optional) A tag from the repo, specify one of branch or
               tag only.
        :param Tool tool: (optional) Reference to the repository tool in the parent
               toolchain.
        """
        self.url = url
        self.branch = branch
        self.tag = tag
        self.path = path
        self.tool = tool

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefinitionSourceProperties':
        """Initialize a DefinitionSourceProperties object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in DefinitionSourceProperties JSON')
        if (branch := _dict.get('branch')) is not None:
            args['branch'] = branch
        if (tag := _dict.get('tag')) is not None:
            args['tag'] = tag
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        else:
            raise ValueError('Required property \'path\' not present in DefinitionSourceProperties JSON')
        if (tool := _dict.get('tool')) is not None:
            args['tool'] = Tool.from_dict(tool)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DefinitionSourceProperties object from a json dictionary."""
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
        if hasattr(self, 'tool') and self.tool is not None:
            if isinstance(self.tool, dict):
                _dict['tool'] = self.tool
            else:
                _dict['tool'] = self.tool.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DefinitionSourceProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DefinitionSourceProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DefinitionSourceProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DefinitionsCollection:
    """
    Pipeline definitions is a collection of individual definition entries, each entry
    consists of a repository URL, a repository path, and a branch or tag.

    :param List[Definition] definitions: The list of all definitions in the
          pipeline.
    """

    def __init__(
        self,
        definitions: List['Definition'],
    ) -> None:
        """
        Initialize a DefinitionsCollection object.

        :param List[Definition] definitions: The list of all definitions in the
               pipeline.
        """
        self.definitions = definitions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DefinitionsCollection':
        """Initialize a DefinitionsCollection object from a json dictionary."""
        args = {}
        if (definitions := _dict.get('definitions')) is not None:
            args['definitions'] = [Definition.from_dict(v) for v in definitions]
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
            definitions_list = []
            for v in self.definitions:
                if isinstance(v, dict):
                    definitions_list.append(v)
                else:
                    definitions_list.append(v.to_dict())
            _dict['definitions'] = definitions_list
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


class GenericSecret:
    """
    Only needed for Generic Webhook trigger type. The secret is used to start the Generic
    Webhook trigger.

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

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
        source: Optional[str] = None,
        key_name: Optional[str] = None,
        algorithm: Optional[str] = None,
    ) -> None:
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
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        if (key_name := _dict.get('key_name')) is not None:
            args['key_name'] = key_name
        if (algorithm := _dict.get('algorithm')) is not None:
            args['algorithm'] = algorithm
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


class Log:
    """
    Log data for Tekton pipeline run steps.

    :param str href: (optional) API for getting log content.
    :param str id: Step log ID.
    :param str name: <podName>/<containerName> of this log.
    """

    def __init__(
        self,
        id: str,
        name: str,
        *,
        href: Optional[str] = None,
    ) -> None:
        """
        Initialize a Log object.

        :param str id: Step log ID.
        :param str name: <podName>/<containerName> of this log.
        :param str href: (optional) API for getting log content.
        """
        self.href = href
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Log':
        """Initialize a Log object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Log JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Log JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Log object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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


class LogsCollection:
    """
    List of pipeline run log objects.

    :param List[Log] logs: The list of pipeline run log objects.
    """

    def __init__(
        self,
        logs: List['Log'],
    ) -> None:
        """
        Initialize a LogsCollection object.

        :param List[Log] logs: The list of pipeline run log objects.
        """
        self.logs = logs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogsCollection':
        """Initialize a LogsCollection object from a json dictionary."""
        args = {}
        if (logs := _dict.get('logs')) is not None:
            args['logs'] = [Log.from_dict(v) for v in logs]
        else:
            raise ValueError('Required property \'logs\' not present in LogsCollection JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogsCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'logs') and self.logs is not None:
            logs_list = []
            for v in self.logs:
                if isinstance(v, dict):
                    logs_list.append(v)
                else:
                    logs_list.append(v.to_dict())
            _dict['logs'] = logs_list
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


class PipelineRun:
    """
    Single Tekton pipeline run object.

    :param str id: Universally Unique Identifier.
    :param str href: (optional) General href URL.
    :param UserInfo user_info: (optional) Information about the user that triggered
          a pipeline run. Only included for pipeline runs that were manually triggered.
    :param str status: Status of the pipeline run.
    :param str definition_id: The aggregated definition ID.
    :param RunDefinition definition: (optional) Reference to the pipeline definition
          of a pipeline run.
    :param str description: (optional) Optional description for the created
          PipelineRun.
    :param PipelineRunWorker worker: Worker details used in this pipeline run.
    :param str pipeline_id: The ID of the pipeline to which this pipeline run
          belongs.
    :param RunPipeline pipeline: (optional) Reference to the pipeline to which a
          pipeline run belongs.
    :param str listener_name: Listener name used to start the run.
    :param Trigger trigger: Tekton pipeline trigger.
    :param str event_params_blob: Event parameters object in String format that was
          passed in upon creation of this pipeline run, the contents depends on the type
          of trigger. For example, the Git event payload is included for Git triggers, or
          in the case of a manual trigger the override and added properties are included.
    :param str trigger_headers: (optional) Trigger headers object in String format
          that was passed in upon creation of this pipeline run. Omitted if no
          trigger_headers object was provided when creating the pipeline run.
    :param List[Property] properties: (optional) Properties used in this Tekton
          pipeline run. Not included when fetching the list of pipeline runs.
    :param datetime created_at: Standard RFC 3339 Date Time String.
    :param datetime updated_at: (optional) Standard RFC 3339 Date Time String. Only
          included if the run has been updated since it was created.
    :param str run_url: URL for the details page of this pipeline run.
    :param str error_message: (optional) Error message that provides details when a
          pipeline run encounters an error.
    """

    def __init__(
        self,
        id: str,
        status: str,
        definition_id: str,
        worker: 'PipelineRunWorker',
        pipeline_id: str,
        listener_name: str,
        trigger: 'Trigger',
        event_params_blob: str,
        created_at: datetime,
        run_url: str,
        *,
        href: Optional[str] = None,
        user_info: Optional['UserInfo'] = None,
        definition: Optional['RunDefinition'] = None,
        description: Optional[str] = None,
        pipeline: Optional['RunPipeline'] = None,
        trigger_headers: Optional[str] = None,
        properties: Optional[List['Property']] = None,
        updated_at: Optional[datetime] = None,
        error_message: Optional[str] = None,
    ) -> None:
        """
        Initialize a PipelineRun object.

        :param str id: Universally Unique Identifier.
        :param str status: Status of the pipeline run.
        :param str definition_id: The aggregated definition ID.
        :param PipelineRunWorker worker: Worker details used in this pipeline run.
        :param str pipeline_id: The ID of the pipeline to which this pipeline run
               belongs.
        :param str listener_name: Listener name used to start the run.
        :param Trigger trigger: Tekton pipeline trigger.
        :param str event_params_blob: Event parameters object in String format that
               was passed in upon creation of this pipeline run, the contents depends on
               the type of trigger. For example, the Git event payload is included for Git
               triggers, or in the case of a manual trigger the override and added
               properties are included.
        :param datetime created_at: Standard RFC 3339 Date Time String.
        :param str run_url: URL for the details page of this pipeline run.
        :param str href: (optional) General href URL.
        :param UserInfo user_info: (optional) Information about the user that
               triggered a pipeline run. Only included for pipeline runs that were
               manually triggered.
        :param RunDefinition definition: (optional) Reference to the pipeline
               definition of a pipeline run.
        :param str description: (optional) Optional description for the created
               PipelineRun.
        :param RunPipeline pipeline: (optional) Reference to the pipeline to which
               a pipeline run belongs.
        :param str trigger_headers: (optional) Trigger headers object in String
               format that was passed in upon creation of this pipeline run. Omitted if no
               trigger_headers object was provided when creating the pipeline run.
        :param List[Property] properties: (optional) Properties used in this Tekton
               pipeline run. Not included when fetching the list of pipeline runs.
        :param datetime updated_at: (optional) Standard RFC 3339 Date Time String.
               Only included if the run has been updated since it was created.
        :param str error_message: (optional) Error message that provides details
               when a pipeline run encounters an error.
        """
        self.id = id
        self.href = href
        self.user_info = user_info
        self.status = status
        self.definition_id = definition_id
        self.definition = definition
        self.description = description
        self.worker = worker
        self.pipeline_id = pipeline_id
        self.pipeline = pipeline
        self.listener_name = listener_name
        self.trigger = trigger
        self.event_params_blob = event_params_blob
        self.trigger_headers = trigger_headers
        self.properties = properties
        self.created_at = created_at
        self.updated_at = updated_at
        self.run_url = run_url
        self.error_message = error_message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRun':
        """Initialize a PipelineRun object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in PipelineRun JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (user_info := _dict.get('user_info')) is not None:
            args['user_info'] = UserInfo.from_dict(user_info)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in PipelineRun JSON')
        if (definition_id := _dict.get('definition_id')) is not None:
            args['definition_id'] = definition_id
        else:
            raise ValueError('Required property \'definition_id\' not present in PipelineRun JSON')
        if (definition := _dict.get('definition')) is not None:
            args['definition'] = RunDefinition.from_dict(definition)
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = PipelineRunWorker.from_dict(worker)
        else:
            raise ValueError('Required property \'worker\' not present in PipelineRun JSON')
        if (pipeline_id := _dict.get('pipeline_id')) is not None:
            args['pipeline_id'] = pipeline_id
        else:
            raise ValueError('Required property \'pipeline_id\' not present in PipelineRun JSON')
        if (pipeline := _dict.get('pipeline')) is not None:
            args['pipeline'] = RunPipeline.from_dict(pipeline)
        if (listener_name := _dict.get('listener_name')) is not None:
            args['listener_name'] = listener_name
        else:
            raise ValueError('Required property \'listener_name\' not present in PipelineRun JSON')
        if (trigger := _dict.get('trigger')) is not None:
            args['trigger'] = trigger
        else:
            raise ValueError('Required property \'trigger\' not present in PipelineRun JSON')
        if (event_params_blob := _dict.get('event_params_blob')) is not None:
            args['event_params_blob'] = event_params_blob
        else:
            raise ValueError('Required property \'event_params_blob\' not present in PipelineRun JSON')
        if (trigger_headers := _dict.get('trigger_headers')) is not None:
            args['trigger_headers'] = trigger_headers
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [Property.from_dict(v) for v in properties]
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in PipelineRun JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        if (run_url := _dict.get('run_url')) is not None:
            args['run_url'] = run_url
        else:
            raise ValueError('Required property \'run_url\' not present in PipelineRun JSON')
        if (error_message := _dict.get('error_message')) is not None:
            args['error_message'] = error_message
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
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'user_info') and self.user_info is not None:
            if isinstance(self.user_info, dict):
                _dict['user_info'] = self.user_info
            else:
                _dict['user_info'] = self.user_info.to_dict()
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'definition_id') and self.definition_id is not None:
            _dict['definition_id'] = self.definition_id
        if hasattr(self, 'definition') and self.definition is not None:
            if isinstance(self.definition, dict):
                _dict['definition'] = self.definition
            else:
                _dict['definition'] = self.definition.to_dict()
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'worker') and self.worker is not None:
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
                _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'pipeline_id') and self.pipeline_id is not None:
            _dict['pipeline_id'] = self.pipeline_id
        if hasattr(self, 'pipeline') and self.pipeline is not None:
            if isinstance(self.pipeline, dict):
                _dict['pipeline'] = self.pipeline
            else:
                _dict['pipeline'] = self.pipeline.to_dict()
        if hasattr(self, 'listener_name') and self.listener_name is not None:
            _dict['listener_name'] = self.listener_name
        if hasattr(self, 'trigger') and self.trigger is not None:
            if isinstance(self.trigger, dict):
                _dict['trigger'] = self.trigger
            else:
                _dict['trigger'] = self.trigger.to_dict()
        if hasattr(self, 'event_params_blob') and self.event_params_blob is not None:
            _dict['event_params_blob'] = self.event_params_blob
        if hasattr(self, 'trigger_headers') and self.trigger_headers is not None:
            _dict['trigger_headers'] = self.trigger_headers
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'run_url') and self.run_url is not None:
            _dict['run_url'] = self.run_url
        if hasattr(self, 'error_message') and self.error_message is not None:
            _dict['error_message'] = self.error_message
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
        FAILED = 'failed'
        ERROR = 'error'
        SUCCEEDED = 'succeeded'


class PipelineRunTrigger:
    """
    Trigger details passed when triggering a Tekton pipeline run.

    :param str name: Trigger name.
    :param dict properties: (optional) An object containing string values only. It
          provides additional 'text' properties or overrides existing pipeline/trigger
          properties that can be used in the created run.
    :param dict secure_properties: (optional) An object containing string values
          only. It provides additional `secure` properties or overrides existing `secure`
          pipeline/trigger properties that can be used in the created run.
    :param dict headers_: (optional) An object containing string values only that
          provides the request headers. Use `$(header.header_key_name)` to access it in a
          TriggerBinding. Most commonly used as part of a Generic Webhook to provide a
          verification token or signature in the request headers.
    :param dict body: (optional) An object that provides the request body. Use
          `$(body.body_key_name)` to access it in a TriggerBinding. Most commonly used to
          pass in additional properties or override properties for the pipeline run that
          is created.
    """

    def __init__(
        self,
        name: str,
        *,
        properties: Optional[dict] = None,
        secure_properties: Optional[dict] = None,
        headers_: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> None:
        """
        Initialize a PipelineRunTrigger object.

        :param str name: Trigger name.
        :param dict properties: (optional) An object containing string values only.
               It provides additional 'text' properties or overrides existing
               pipeline/trigger properties that can be used in the created run.
        :param dict secure_properties: (optional) An object containing string
               values only. It provides additional `secure` properties or overrides
               existing `secure` pipeline/trigger properties that can be used in the
               created run.
        :param dict headers_: (optional) An object containing string values only
               that provides the request headers. Use `$(header.header_key_name)` to
               access it in a TriggerBinding. Most commonly used as part of a Generic
               Webhook to provide a verification token or signature in the request
               headers.
        :param dict body: (optional) An object that provides the request body. Use
               `$(body.body_key_name)` to access it in a TriggerBinding. Most commonly
               used to pass in additional properties or override properties for the
               pipeline run that is created.
        """
        self.name = name
        self.properties = properties
        self.secure_properties = secure_properties
        self.headers_ = headers_
        self.body = body

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunTrigger':
        """Initialize a PipelineRunTrigger object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in PipelineRunTrigger JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = properties
        if (secure_properties := _dict.get('secure_properties')) is not None:
            args['secure_properties'] = secure_properties
        if (headers_ := _dict.get('headers')) is not None:
            args['headers_'] = headers_
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunTrigger object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'properties') and self.properties is not None:
            _dict['properties'] = self.properties
        if hasattr(self, 'secure_properties') and self.secure_properties is not None:
            _dict['secure_properties'] = self.secure_properties
        if hasattr(self, 'headers_') and self.headers_ is not None:
            _dict['headers'] = self.headers_
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PipelineRunTrigger object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PipelineRunTrigger') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PipelineRunTrigger') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class PipelineRunWorker:
    """
    Worker details used in this pipeline run.

    :param str name: (optional) Name of the worker. Computed based on the worker ID.
    :param str agent_id: (optional) The agent ID of the corresponding private worker
          integration used for this pipeline run.
    :param str service_id: (optional) The Service ID of the corresponding private
          worker integration used for this pipeline run.
    :param str id: Universally Unique Identifier.
    """

    def __init__(
        self,
        id: str,
        *,
        name: Optional[str] = None,
        agent_id: Optional[str] = None,
        service_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a PipelineRunWorker object.

        :param str id: Universally Unique Identifier.
        :param str name: (optional) Name of the worker. Computed based on the
               worker ID.
        :param str agent_id: (optional) The agent ID of the corresponding private
               worker integration used for this pipeline run.
        :param str service_id: (optional) The Service ID of the corresponding
               private worker integration used for this pipeline run.
        """
        self.name = name
        self.agent_id = agent_id
        self.service_id = service_id
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunWorker':
        """Initialize a PipelineRunWorker object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (agent_id := _dict.get('agent_id')) is not None:
            args['agent_id'] = agent_id
        if (service_id := _dict.get('service_id')) is not None:
            args['service_id'] = service_id
        if (id := _dict.get('id')) is not None:
            args['id'] = id
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
        if hasattr(self, 'agent_id') and self.agent_id is not None:
            _dict['agent_id'] = self.agent_id
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


class PipelineRunsCollection:
    """
    Tekton pipeline runs object.

    :param List[PipelineRun] pipeline_runs: Tekton pipeline runs list.
    :param int limit: The number of pipeline runs to return, sorted by creation
          time, most recent first.
    :param RunsFirstPage first: First page of pipeline runs.
    :param RunsNextPage next: (optional) Next page of pipeline runs relative to the
          `start` and `limit` params. Only included when there are more pages available.
    :param RunsLastPage last: (optional) Last page of pipeline runs relative to the
          `start` and `limit` params. Only included when the last page has been reached.
    """

    def __init__(
        self,
        pipeline_runs: List['PipelineRun'],
        limit: int,
        first: 'RunsFirstPage',
        *,
        next: Optional['RunsNextPage'] = None,
        last: Optional['RunsLastPage'] = None,
    ) -> None:
        """
        Initialize a PipelineRunsCollection object.

        :param List[PipelineRun] pipeline_runs: Tekton pipeline runs list.
        :param int limit: The number of pipeline runs to return, sorted by creation
               time, most recent first.
        :param RunsFirstPage first: First page of pipeline runs.
        :param RunsNextPage next: (optional) Next page of pipeline runs relative to
               the `start` and `limit` params. Only included when there are more pages
               available.
        :param RunsLastPage last: (optional) Last page of pipeline runs relative to
               the `start` and `limit` params. Only included when the last page has been
               reached.
        """
        self.pipeline_runs = pipeline_runs
        self.limit = limit
        self.first = first
        self.next = next
        self.last = last

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PipelineRunsCollection':
        """Initialize a PipelineRunsCollection object from a json dictionary."""
        args = {}
        if (pipeline_runs := _dict.get('pipeline_runs')) is not None:
            args['pipeline_runs'] = [PipelineRun.from_dict(v) for v in pipeline_runs]
        else:
            raise ValueError('Required property \'pipeline_runs\' not present in PipelineRunsCollection JSON')
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        else:
            raise ValueError('Required property \'limit\' not present in PipelineRunsCollection JSON')
        if (first := _dict.get('first')) is not None:
            args['first'] = RunsFirstPage.from_dict(first)
        else:
            raise ValueError('Required property \'first\' not present in PipelineRunsCollection JSON')
        if (next := _dict.get('next')) is not None:
            args['next'] = RunsNextPage.from_dict(next)
        if (last := _dict.get('last')) is not None:
            args['last'] = RunsLastPage.from_dict(last)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PipelineRunsCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pipeline_runs') and self.pipeline_runs is not None:
            pipeline_runs_list = []
            for v in self.pipeline_runs:
                if isinstance(v, dict):
                    pipeline_runs_list.append(v)
                else:
                    pipeline_runs_list.append(v.to_dict())
            _dict['pipeline_runs'] = pipeline_runs_list
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'first') and self.first is not None:
            if isinstance(self.first, dict):
                _dict['first'] = self.first
            else:
                _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            if isinstance(self.next, dict):
                _dict['next'] = self.next
            else:
                _dict['next'] = self.next.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            if isinstance(self.last, dict):
                _dict['last'] = self.last
            else:
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


class PropertiesCollection:
    """
    Pipeline properties object.

    :param List[Property] properties: Pipeline properties list.
    """

    def __init__(
        self,
        properties: List['Property'],
    ) -> None:
        """
        Initialize a PropertiesCollection object.

        :param List[Property] properties: Pipeline properties list.
        """
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PropertiesCollection':
        """Initialize a PropertiesCollection object from a json dictionary."""
        args = {}
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [Property.from_dict(v) for v in properties]
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
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
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


class Property:
    """
    Property object.

    :param str name: Property name.
    :param str value: (optional) Property value. Any string value is valid.
    :param str href: (optional) API URL for interacting with the property.
    :param List[str] enum: (optional) Options for `single_select` property type.
          Only needed when using `single_select` property type.
    :param str type: Property type.
    :param bool locked: (optional) When true, this property cannot be overridden by
          a trigger property or at runtime. Attempting to override it will result in run
          requests being rejected. The default is false.
    :param str path: (optional) A dot notation path for `integration` type
          properties only, that selects a value from the tool integration. If left blank
          the full tool integration data will be used.
    """

    def __init__(
        self,
        name: str,
        type: str,
        *,
        value: Optional[str] = None,
        href: Optional[str] = None,
        enum: Optional[List[str]] = None,
        locked: Optional[bool] = None,
        path: Optional[str] = None,
    ) -> None:
        """
        Initialize a Property object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Any string value is valid.
        :param str href: (optional) API URL for interacting with the property.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed when using `single_select` property type.
        :param bool locked: (optional) When true, this property cannot be
               overridden by a trigger property or at runtime. Attempting to override it
               will result in run requests being rejected. The default is false.
        :param str path: (optional) A dot notation path for `integration` type
               properties only, that selects a value from the tool integration. If left
               blank the full tool integration data will be used.
        """
        self.name = name
        self.value = value
        self.href = href
        self.enum = enum
        self.type = type
        self.locked = locked
        self.path = path

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Property':
        """Initialize a Property object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in Property JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (enum := _dict.get('enum')) is not None:
            args['enum'] = enum
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in Property JSON')
        if (locked := _dict.get('locked')) is not None:
            args['locked'] = locked
        if (path := _dict.get('path')) is not None:
            args['path'] = path
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
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'locked') and self.locked is not None:
            _dict['locked'] = self.locked
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


class ResourceGroupReference:
    """
    The resource group in which the pipeline was created.

    :param str id: (optional) ID.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ResourceGroupReference object.

        :param str id: (optional) ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceGroupReference':
        """Initialize a ResourceGroupReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceGroupReference object from a json dictionary."""
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
        """Return a `str` version of this ResourceGroupReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceGroupReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceGroupReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RunDefinition:
    """
    Reference to the pipeline definition of a pipeline run.

    :param str id: (optional) The ID of the definition used for a pipeline run.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a RunDefinition object.

        :param str id: (optional) The ID of the definition used for a pipeline run.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RunDefinition':
        """Initialize a RunDefinition object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RunDefinition object from a json dictionary."""
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
        """Return a `str` version of this RunDefinition object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RunDefinition') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RunDefinition') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RunPipeline:
    """
    Reference to the pipeline to which a pipeline run belongs.

    :param str id: (optional) The ID of the pipeline to which a pipeline run
          belongs.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a RunPipeline object.

        :param str id: (optional) The ID of the pipeline to which a pipeline run
               belongs.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RunPipeline':
        """Initialize a RunPipeline object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RunPipeline object from a json dictionary."""
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
        """Return a `str` version of this RunPipeline object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RunPipeline') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RunPipeline') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RunsFirstPage:
    """
    First page of pipeline runs.

    :param str href: General href URL.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a RunsFirstPage object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RunsFirstPage':
        """Initialize a RunsFirstPage object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in RunsFirstPage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RunsFirstPage object from a json dictionary."""
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
        """Return a `str` version of this RunsFirstPage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RunsFirstPage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RunsFirstPage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RunsLastPage:
    """
    Last page of pipeline runs relative to the `start` and `limit` params. Only included
    when the last page has been reached.

    :param str href: General href URL.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a RunsLastPage object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RunsLastPage':
        """Initialize a RunsLastPage object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in RunsLastPage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RunsLastPage object from a json dictionary."""
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
        """Return a `str` version of this RunsLastPage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RunsLastPage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RunsLastPage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RunsNextPage:
    """
    Next page of pipeline runs relative to the `start` and `limit` params. Only included
    when there are more pages available.

    :param str href: General href URL.
    """

    def __init__(
        self,
        href: str,
    ) -> None:
        """
        Initialize a RunsNextPage object.

        :param str href: General href URL.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RunsNextPage':
        """Initialize a RunsNextPage object from a json dictionary."""
        args = {}
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        else:
            raise ValueError('Required property \'href\' not present in RunsNextPage JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RunsNextPage object from a json dictionary."""
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
        """Return a `str` version of this RunsNextPage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RunsNextPage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RunsNextPage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StepLog:
    """
    Logs for a Tekton pipeline run step.

    :param str data: The raw log content of the step. Only included when fetching an
          individual log object.
    :param str id: Step log ID.
    """

    def __init__(
        self,
        data: str,
        id: str,
    ) -> None:
        """
        Initialize a StepLog object.

        :param str data: The raw log content of the step. Only included when
               fetching an individual log object.
        :param str id: Step log ID.
        """
        self.data = data
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StepLog':
        """Initialize a StepLog object from a json dictionary."""
        args = {}
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        else:
            raise ValueError('Required property \'data\' not present in StepLog JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in StepLog JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StepLog object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
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


class TektonPipeline:
    """
    Tekton pipeline object.

    :param str name: String.
    :param str status: Pipeline status.
    :param ResourceGroupReference resource_group: The resource group in which the
          pipeline was created.
    :param ToolchainReference toolchain: Toolchain object containing references to
          the parent toolchain.
    :param str id: Universally Unique Identifier.
    :param List[Definition] definitions: Definition list.
    :param List[Property] properties: Tekton pipeline's environment properties.
    :param datetime updated_at: Standard RFC 3339 Date Time String.
    :param datetime created_at: Standard RFC 3339 Date Time String.
    :param List[Trigger] triggers: Tekton pipeline triggers list.
    :param Worker worker: Details of the worker used to run the pipeline.
    :param str runs_url: URL for this pipeline showing the list of pipeline runs.
    :param str href: (optional) API URL for interacting with the pipeline.
    :param int build_number: The latest pipeline run build number. If this property
          is absent, the pipeline hasn't had any pipeline runs.
    :param int next_build_number: (optional) The build number that will be used for
          the next pipeline run.
    :param bool enable_notifications: Flag to enable notifications for this
          pipeline. If enabled, the Tekton pipeline run events will be published to all
          the destinations specified by the Slack and Event Notifications integrations in
          the parent toolchain. If omitted, this feature is disabled by default.
    :param bool enable_partial_cloning: Flag to enable partial cloning for this
          pipeline. When partial clone is enabled, only the files contained within the
          paths specified in definition repositories are read and cloned, this means that
          symbolic links might not work. If omitted, this feature is disabled by default.
    :param bool enabled: Flag to check if the trigger is enabled.
    """

    def __init__(
        self,
        name: str,
        status: str,
        resource_group: 'ResourceGroupReference',
        toolchain: 'ToolchainReference',
        id: str,
        definitions: List['Definition'],
        properties: List['Property'],
        updated_at: datetime,
        created_at: datetime,
        triggers: List['Trigger'],
        worker: 'Worker',
        runs_url: str,
        build_number: int,
        enable_notifications: bool,
        enable_partial_cloning: bool,
        enabled: bool,
        *,
        href: Optional[str] = None,
        next_build_number: Optional[int] = None,
    ) -> None:
        """
        Initialize a TektonPipeline object.

        :param str name: String.
        :param str status: Pipeline status.
        :param ResourceGroupReference resource_group: The resource group in which
               the pipeline was created.
        :param ToolchainReference toolchain: Toolchain object containing references
               to the parent toolchain.
        :param str id: Universally Unique Identifier.
        :param List[Definition] definitions: Definition list.
        :param List[Property] properties: Tekton pipeline's environment properties.
        :param datetime updated_at: Standard RFC 3339 Date Time String.
        :param datetime created_at: Standard RFC 3339 Date Time String.
        :param List[Trigger] triggers: Tekton pipeline triggers list.
        :param Worker worker: Details of the worker used to run the pipeline.
        :param str runs_url: URL for this pipeline showing the list of pipeline
               runs.
        :param int build_number: The latest pipeline run build number. If this
               property is absent, the pipeline hasn't had any pipeline runs.
        :param bool enable_notifications: Flag to enable notifications for this
               pipeline. If enabled, the Tekton pipeline run events will be published to
               all the destinations specified by the Slack and Event Notifications
               integrations in the parent toolchain. If omitted, this feature is disabled
               by default.
        :param bool enable_partial_cloning: Flag to enable partial cloning for this
               pipeline. When partial clone is enabled, only the files contained within
               the paths specified in definition repositories are read and cloned, this
               means that symbolic links might not work. If omitted, this feature is
               disabled by default.
        :param bool enabled: Flag to check if the trigger is enabled.
        :param str href: (optional) API URL for interacting with the pipeline.
        :param int next_build_number: (optional) The build number that will be used
               for the next pipeline run.
        """
        self.name = name
        self.status = status
        self.resource_group = resource_group
        self.toolchain = toolchain
        self.id = id
        self.definitions = definitions
        self.properties = properties
        self.updated_at = updated_at
        self.created_at = created_at
        self.triggers = triggers
        self.worker = worker
        self.runs_url = runs_url
        self.href = href
        self.build_number = build_number
        self.next_build_number = next_build_number
        self.enable_notifications = enable_notifications
        self.enable_partial_cloning = enable_partial_cloning
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TektonPipeline':
        """Initialize a TektonPipeline object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in TektonPipeline JSON')
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError('Required property \'status\' not present in TektonPipeline JSON')
        if (resource_group := _dict.get('resource_group')) is not None:
            args['resource_group'] = ResourceGroupReference.from_dict(resource_group)
        else:
            raise ValueError('Required property \'resource_group\' not present in TektonPipeline JSON')
        if (toolchain := _dict.get('toolchain')) is not None:
            args['toolchain'] = ToolchainReference.from_dict(toolchain)
        else:
            raise ValueError('Required property \'toolchain\' not present in TektonPipeline JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in TektonPipeline JSON')
        if (definitions := _dict.get('definitions')) is not None:
            args['definitions'] = [Definition.from_dict(v) for v in definitions]
        else:
            raise ValueError('Required property \'definitions\' not present in TektonPipeline JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [Property.from_dict(v) for v in properties]
        else:
            raise ValueError('Required property \'properties\' not present in TektonPipeline JSON')
        if (updated_at := _dict.get('updated_at')) is not None:
            args['updated_at'] = string_to_datetime(updated_at)
        else:
            raise ValueError('Required property \'updated_at\' not present in TektonPipeline JSON')
        if (created_at := _dict.get('created_at')) is not None:
            args['created_at'] = string_to_datetime(created_at)
        else:
            raise ValueError('Required property \'created_at\' not present in TektonPipeline JSON')
        if (triggers := _dict.get('triggers')) is not None:
            args['triggers'] = triggers
        else:
            raise ValueError('Required property \'triggers\' not present in TektonPipeline JSON')
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = Worker.from_dict(worker)
        else:
            raise ValueError('Required property \'worker\' not present in TektonPipeline JSON')
        if (runs_url := _dict.get('runs_url')) is not None:
            args['runs_url'] = runs_url
        else:
            raise ValueError('Required property \'runs_url\' not present in TektonPipeline JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (build_number := _dict.get('build_number')) is not None:
            args['build_number'] = build_number
        else:
            raise ValueError('Required property \'build_number\' not present in TektonPipeline JSON')
        if (next_build_number := _dict.get('next_build_number')) is not None:
            args['next_build_number'] = next_build_number
        if (enable_notifications := _dict.get('enable_notifications')) is not None:
            args['enable_notifications'] = enable_notifications
        else:
            raise ValueError('Required property \'enable_notifications\' not present in TektonPipeline JSON')
        if (enable_partial_cloning := _dict.get('enable_partial_cloning')) is not None:
            args['enable_partial_cloning'] = enable_partial_cloning
        else:
            raise ValueError('Required property \'enable_partial_cloning\' not present in TektonPipeline JSON')
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
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
        if hasattr(self, 'resource_group') and self.resource_group is not None:
            if isinstance(self.resource_group, dict):
                _dict['resource_group'] = self.resource_group
            else:
                _dict['resource_group'] = self.resource_group.to_dict()
        if hasattr(self, 'toolchain') and self.toolchain is not None:
            if isinstance(self.toolchain, dict):
                _dict['toolchain'] = self.toolchain
            else:
                _dict['toolchain'] = self.toolchain.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'definitions') and self.definitions is not None:
            definitions_list = []
            for v in self.definitions:
                if isinstance(v, dict):
                    definitions_list.append(v)
                else:
                    definitions_list.append(v.to_dict())
            _dict['definitions'] = definitions_list
        if hasattr(self, 'properties') and self.properties is not None:
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'triggers') and self.triggers is not None:
            triggers_list = []
            for v in self.triggers:
                if isinstance(v, dict):
                    triggers_list.append(v)
                else:
                    triggers_list.append(v.to_dict())
            _dict['triggers'] = triggers_list
        if hasattr(self, 'worker') and self.worker is not None:
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
                _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'runs_url') and self.runs_url is not None:
            _dict['runs_url'] = self.runs_url
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'build_number') and self.build_number is not None:
            _dict['build_number'] = self.build_number
        if hasattr(self, 'next_build_number') and self.next_build_number is not None:
            _dict['next_build_number'] = self.next_build_number
        if hasattr(self, 'enable_notifications') and self.enable_notifications is not None:
            _dict['enable_notifications'] = self.enable_notifications
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


class TektonPipelinePatch:
    """
    Request body used to update this pipeline.

    :param int next_build_number: (optional) Specify the build number that will be
          used for the next pipeline run. Build numbers can be any positive whole number
          between 0 and 100000000000000.
    :param bool enable_notifications: (optional) Flag to enable notifications for
          this pipeline. If enabled, the Tekton pipeline run events will be published to
          all the destinations specified by the Slack and Event Notifications integrations
          in the parent toolchain.
    :param bool enable_partial_cloning: (optional) Flag to enable partial cloning
          for this pipeline. When partial clone is enabled, only the files contained
          within the paths specified in definition repositories are read and cloned, this
          means that symbolic links might not work.
    :param WorkerIdentity worker: (optional) Specify the worker that is to be used
          to run the trigger, indicated by a worker object with only the worker ID. If not
          specified or set as `worker: { id: 'public' }`, the IBM Managed shared workers
          are used.
    """

    def __init__(
        self,
        *,
        next_build_number: Optional[int] = None,
        enable_notifications: Optional[bool] = None,
        enable_partial_cloning: Optional[bool] = None,
        worker: Optional['WorkerIdentity'] = None,
    ) -> None:
        """
        Initialize a TektonPipelinePatch object.

        :param int next_build_number: (optional) Specify the build number that will
               be used for the next pipeline run. Build numbers can be any positive whole
               number between 0 and 100000000000000.
        :param bool enable_notifications: (optional) Flag to enable notifications
               for this pipeline. If enabled, the Tekton pipeline run events will be
               published to all the destinations specified by the Slack and Event
               Notifications integrations in the parent toolchain.
        :param bool enable_partial_cloning: (optional) Flag to enable partial
               cloning for this pipeline. When partial clone is enabled, only the files
               contained within the paths specified in definition repositories are read
               and cloned, this means that symbolic links might not work.
        :param WorkerIdentity worker: (optional) Specify the worker that is to be
               used to run the trigger, indicated by a worker object with only the worker
               ID. If not specified or set as `worker: { id: 'public' }`, the IBM Managed
               shared workers are used.
        """
        self.next_build_number = next_build_number
        self.enable_notifications = enable_notifications
        self.enable_partial_cloning = enable_partial_cloning
        self.worker = worker

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TektonPipelinePatch':
        """Initialize a TektonPipelinePatch object from a json dictionary."""
        args = {}
        if (next_build_number := _dict.get('next_build_number')) is not None:
            args['next_build_number'] = next_build_number
        if (enable_notifications := _dict.get('enable_notifications')) is not None:
            args['enable_notifications'] = enable_notifications
        if (enable_partial_cloning := _dict.get('enable_partial_cloning')) is not None:
            args['enable_partial_cloning'] = enable_partial_cloning
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = WorkerIdentity.from_dict(worker)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TektonPipelinePatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_build_number') and self.next_build_number is not None:
            _dict['next_build_number'] = self.next_build_number
        if hasattr(self, 'enable_notifications') and self.enable_notifications is not None:
            _dict['enable_notifications'] = self.enable_notifications
        if hasattr(self, 'enable_partial_cloning') and self.enable_partial_cloning is not None:
            _dict['enable_partial_cloning'] = self.enable_partial_cloning
        if hasattr(self, 'worker') and self.worker is not None:
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
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


class Tool:
    """
    Reference to the repository tool in the parent toolchain.

    :param str id: ID of the repository tool instance in the parent toolchain.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a Tool object.

        :param str id: ID of the repository tool instance in the parent toolchain.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tool':
        """Initialize a Tool object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in Tool JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tool object from a json dictionary."""
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
        """Return a `str` version of this Tool object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tool') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tool') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ToolchainReference:
    """
    Toolchain object containing references to the parent toolchain.

    :param str id: Universally Unique Identifier.
    :param str crn: The CRN for the toolchain that contains the Tekton pipeline.
    """

    def __init__(
        self,
        id: str,
        crn: str,
    ) -> None:
        """
        Initialize a ToolchainReference object.

        :param str id: Universally Unique Identifier.
        :param str crn: The CRN for the toolchain that contains the Tekton
               pipeline.
        """
        self.id = id
        self.crn = crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ToolchainReference':
        """Initialize a ToolchainReference object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ToolchainReference JSON')
        if (crn := _dict.get('crn')) is not None:
            args['crn'] = crn
        else:
            raise ValueError('Required property \'crn\' not present in ToolchainReference JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ToolchainReference object from a json dictionary."""
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
        """Return a `str` version of this ToolchainReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ToolchainReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ToolchainReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Trigger:
    """
    Tekton pipeline trigger.

    """

    def __init__(
        self,
    ) -> None:
        """
        Initialize a Trigger object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join(['TriggerManualTrigger', 'TriggerScmTrigger', 'TriggerTimerTrigger', 'TriggerGenericTrigger'])
        )
        raise Exception(msg)


class TriggerPatch:
    """
    Tekton pipeline trigger object used for updating the trigger.

    :param str type: (optional) Trigger type.
    :param str name: (optional) Trigger name.
    :param str event_listener: (optional) Event listener name. The name of the event
          listener to which the trigger is associated. The event listeners are defined in
          the definition repositories of the Tekton pipeline.
    :param List[str] tags: (optional) Trigger tags array. Optional tags for the
          trigger.
    :param WorkerIdentity worker: (optional) Specify the worker used to run the
          trigger. Use `worker: { id: 'public' }` to use the IBM Managed workers. Use
          `worker: { id: 'inherit' }` to inherit the worker used by the pipeline.
    :param int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. If set to 0 then the custom concurrency limit
          is disabled for this trigger.
    :param bool limit_waiting_runs: (optional) Only used for SCM triggers. Flag that
          will limit the trigger to a maximum of one waiting run. A newly triggered run
          will cause waiting run(s) to be automatically cancelled.
    :param bool enabled: (optional) Defines if this trigger is enabled.
    :param GenericSecret secret: (optional) Only needed for Generic Webhook trigger
          type. The secret is used to start the Generic Webhook trigger.
    :param str cron: (optional) Only needed for timer triggers. CRON expression that
          indicates when this trigger will activate. Maximum frequency is every 5 minutes.
          The string is based on UNIX crontab syntax: minute, hour, day of month, month,
          day of week. Example: The CRON expression 0 */2 * * * - translates to - every 2
          hours.
    :param str timezone: (optional) Only used for timer triggers. Specify the
          timezone used for this timer trigger, which will ensure the CRON activates this
          trigger relative to the specified timezone. If no timezone is specified, the
          default timezone used is UTC. Valid timezones are those listed in the IANA
          timezone database, https://www.iana.org/time-zones.
    :param TriggerSourcePrototype source: (optional) Source repository for a Git
          trigger. Only required for Git triggers. The referenced repository URL must
          match the URL of a repository tool integration in the parent toolchain. Obtain
          the list of integrations from the toolchain API
          https://cloud.ibm.com/apidocs/toolchain#list-tools.
    :param List[str] events: (optional) Either 'events' or 'filter' is required
          specifically for Git triggers. Stores a list of events that a Git trigger
          listens to. Choose one or more from 'push', 'pull_request', and
          'pull_request_closed'. If SCM repositories use the 'merge request' term, they
          correspond to the generic term i.e. 'pull request'.
    :param str filter: (optional) Either 'events' or 'filter' can be used. Stores
          the CEL (Common Expression Language) expression value which is used for event
          filtering against the Git webhook payloads.
    :param bool favorite: (optional) Mark the trigger as a favorite.
    :param bool enable_events_from_forks: (optional) Only used for SCM triggers.
          When enabled, pull request events from forks of the selected repository will
          trigger a pipeline run.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        event_listener: Optional[str] = None,
        tags: Optional[List[str]] = None,
        worker: Optional['WorkerIdentity'] = None,
        max_concurrent_runs: Optional[int] = None,
        limit_waiting_runs: Optional[bool] = None,
        enabled: Optional[bool] = None,
        secret: Optional['GenericSecret'] = None,
        cron: Optional[str] = None,
        timezone: Optional[str] = None,
        source: Optional['TriggerSourcePrototype'] = None,
        events: Optional[List[str]] = None,
        filter: Optional[str] = None,
        favorite: Optional[bool] = None,
        enable_events_from_forks: Optional[bool] = None,
    ) -> None:
        """
        Initialize a TriggerPatch object.

        :param str type: (optional) Trigger type.
        :param str name: (optional) Trigger name.
        :param str event_listener: (optional) Event listener name. The name of the
               event listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param List[str] tags: (optional) Trigger tags array. Optional tags for the
               trigger.
        :param WorkerIdentity worker: (optional) Specify the worker used to run the
               trigger. Use `worker: { id: 'public' }` to use the IBM Managed workers. Use
               `worker: { id: 'inherit' }` to inherit the worker used by the pipeline.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. If set to 0 then the custom concurrency
               limit is disabled for this trigger.
        :param bool limit_waiting_runs: (optional) Only used for SCM triggers. Flag
               that will limit the trigger to a maximum of one waiting run. A newly
               triggered run will cause waiting run(s) to be automatically cancelled.
        :param bool enabled: (optional) Defines if this trigger is enabled.
        :param GenericSecret secret: (optional) Only needed for Generic Webhook
               trigger type. The secret is used to start the Generic Webhook trigger.
        :param str cron: (optional) Only needed for timer triggers. CRON expression
               that indicates when this trigger will activate. Maximum frequency is every
               5 minutes. The string is based on UNIX crontab syntax: minute, hour, day of
               month, month, day of week. Example: The CRON expression 0 */2 * * * -
               translates to - every 2 hours.
        :param str timezone: (optional) Only used for timer triggers. Specify the
               timezone used for this timer trigger, which will ensure the CRON activates
               this trigger relative to the specified timezone. If no timezone is
               specified, the default timezone used is UTC. Valid timezones are those
               listed in the IANA timezone database, https://www.iana.org/time-zones.
        :param TriggerSourcePrototype source: (optional) Source repository for a
               Git trigger. Only required for Git triggers. The referenced repository URL
               must match the URL of a repository tool integration in the parent
               toolchain. Obtain the list of integrations from the toolchain API
               https://cloud.ibm.com/apidocs/toolchain#list-tools.
        :param List[str] events: (optional) Either 'events' or 'filter' is required
               specifically for Git triggers. Stores a list of events that a Git trigger
               listens to. Choose one or more from 'push', 'pull_request', and
               'pull_request_closed'. If SCM repositories use the 'merge request' term,
               they correspond to the generic term i.e. 'pull request'.
        :param str filter: (optional) Either 'events' or 'filter' can be used.
               Stores the CEL (Common Expression Language) expression value which is used
               for event filtering against the Git webhook payloads.
        :param bool favorite: (optional) Mark the trigger as a favorite.
        :param bool enable_events_from_forks: (optional) Only used for SCM
               triggers. When enabled, pull request events from forks of the selected
               repository will trigger a pipeline run.
        """
        self.type = type
        self.name = name
        self.event_listener = event_listener
        self.tags = tags
        self.worker = worker
        self.max_concurrent_runs = max_concurrent_runs
        self.limit_waiting_runs = limit_waiting_runs
        self.enabled = enabled
        self.secret = secret
        self.cron = cron
        self.timezone = timezone
        self.source = source
        self.events = events
        self.filter = filter
        self.favorite = favorite
        self.enable_events_from_forks = enable_events_from_forks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerPatch':
        """Initialize a TriggerPatch object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (event_listener := _dict.get('event_listener')) is not None:
            args['event_listener'] = event_listener
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = WorkerIdentity.from_dict(worker)
        if (max_concurrent_runs := _dict.get('max_concurrent_runs')) is not None:
            args['max_concurrent_runs'] = max_concurrent_runs
        if (limit_waiting_runs := _dict.get('limit_waiting_runs')) is not None:
            args['limit_waiting_runs'] = limit_waiting_runs
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (secret := _dict.get('secret')) is not None:
            args['secret'] = GenericSecret.from_dict(secret)
        if (cron := _dict.get('cron')) is not None:
            args['cron'] = cron
        if (timezone := _dict.get('timezone')) is not None:
            args['timezone'] = timezone
        if (source := _dict.get('source')) is not None:
            args['source'] = TriggerSourcePrototype.from_dict(source)
        if (events := _dict.get('events')) is not None:
            args['events'] = events
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
        if (favorite := _dict.get('favorite')) is not None:
            args['favorite'] = favorite
        if (enable_events_from_forks := _dict.get('enable_events_from_forks')) is not None:
            args['enable_events_from_forks'] = enable_events_from_forks
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
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
                _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'limit_waiting_runs') and self.limit_waiting_runs is not None:
            _dict['limit_waiting_runs'] = self.limit_waiting_runs
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'secret') and self.secret is not None:
            if isinstance(self.secret, dict):
                _dict['secret'] = self.secret
            else:
                _dict['secret'] = self.secret.to_dict()
        if hasattr(self, 'cron') and self.cron is not None:
            _dict['cron'] = self.cron
        if hasattr(self, 'timezone') and self.timezone is not None:
            _dict['timezone'] = self.timezone
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'events') and self.events is not None:
            _dict['events'] = self.events
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'favorite') and self.favorite is not None:
            _dict['favorite'] = self.favorite
        if hasattr(self, 'enable_events_from_forks') and self.enable_events_from_forks is not None:
            _dict['enable_events_from_forks'] = self.enable_events_from_forks
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

    class EventsEnum(str, Enum):
        """
        List of events. Supported options are 'push' Git webhook events,
        'pull_request_closed' Git webhook events and 'pull_request' for 'open pull
        request' or 'update pull request' Git webhook events.
        """

        PUSH = 'push'
        PULL_REQUEST = 'pull_request'
        PULL_REQUEST_CLOSED = 'pull_request_closed'


class TriggerPropertiesCollection:
    """
    Trigger properties object.

    :param List[TriggerProperty] properties: Trigger properties list.
    """

    def __init__(
        self,
        properties: List['TriggerProperty'],
    ) -> None:
        """
        Initialize a TriggerPropertiesCollection object.

        :param List[TriggerProperty] properties: Trigger properties list.
        """
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerPropertiesCollection':
        """Initialize a TriggerPropertiesCollection object from a json dictionary."""
        args = {}
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [TriggerProperty.from_dict(v) for v in properties]
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
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
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


class TriggerProperty:
    """
    Trigger property object.

    :param str name: Property name.
    :param str value: (optional) Property value. Any string value is valid.
    :param str href: (optional) API URL for interacting with the trigger property.
    :param List[str] enum: (optional) Options for `single_select` property type.
          Only needed for `single_select` property type.
    :param str type: Property type.
    :param str path: (optional) A dot notation path for `integration` type
          properties only, that selects a value from the tool integration. If left blank
          the full tool integration data will be used.
    :param bool locked: (optional) When true, this property cannot be overridden at
          runtime. Attempting to override it will result in run requests being rejected.
          The default is false.
    """

    def __init__(
        self,
        name: str,
        type: str,
        *,
        value: Optional[str] = None,
        href: Optional[str] = None,
        enum: Optional[List[str]] = None,
        path: Optional[str] = None,
        locked: Optional[bool] = None,
    ) -> None:
        """
        Initialize a TriggerProperty object.

        :param str name: Property name.
        :param str type: Property type.
        :param str value: (optional) Property value. Any string value is valid.
        :param str href: (optional) API URL for interacting with the trigger
               property.
        :param List[str] enum: (optional) Options for `single_select` property
               type. Only needed for `single_select` property type.
        :param str path: (optional) A dot notation path for `integration` type
               properties only, that selects a value from the tool integration. If left
               blank the full tool integration data will be used.
        :param bool locked: (optional) When true, this property cannot be
               overridden at runtime. Attempting to override it will result in run
               requests being rejected. The default is false.
        """
        self.name = name
        self.value = value
        self.href = href
        self.enum = enum
        self.type = type
        self.path = path
        self.locked = locked

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerProperty':
        """Initialize a TriggerProperty object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in TriggerProperty JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (enum := _dict.get('enum')) is not None:
            args['enum'] = enum
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in TriggerProperty JSON')
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        if (locked := _dict.get('locked')) is not None:
            args['locked'] = locked
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
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'enum') and self.enum is not None:
            _dict['enum'] = self.enum
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'locked') and self.locked is not None:
            _dict['locked'] = self.locked
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


class TriggerSource:
    """
    Source repository for a Git trigger. Only required for Git triggers. The referenced
    repository URL must match the URL of a repository tool integration in the parent
    toolchain. Obtain the list of integrations from the toolchain API
    https://cloud.ibm.com/apidocs/toolchain#list-tools.

    :param str type: The only supported source type is "git", indicating that the
          source is a git repository.
    :param TriggerSourceProperties properties: Properties of the source, which
          define the URL of the repository and a branch or pattern.
    """

    def __init__(
        self,
        type: str,
        properties: 'TriggerSourceProperties',
    ) -> None:
        """
        Initialize a TriggerSource object.

        :param str type: The only supported source type is "git", indicating that
               the source is a git repository.
        :param TriggerSourceProperties properties: Properties of the source, which
               define the URL of the repository and a branch or pattern.
        """
        self.type = type
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerSource':
        """Initialize a TriggerSource object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in TriggerSource JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = TriggerSourceProperties.from_dict(properties)
        else:
            raise ValueError('Required property \'properties\' not present in TriggerSource JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'properties') and self.properties is not None:
            if isinstance(self.properties, dict):
                _dict['properties'] = self.properties
            else:
                _dict['properties'] = self.properties.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TriggerSourceProperties:
    """
    Properties of the source, which define the URL of the repository and a branch or
    pattern.

    :param str url: URL of the repository to which the trigger is listening.
    :param str branch: (optional) Name of a branch from the repo. Only one of
          branch, pattern, or filter should be specified.
    :param str pattern: (optional) The pattern of Git branch or tag. You can specify
          a glob pattern such as '!test' or '*master' to match against multiple tags or
          branches in the repository.The glob pattern used must conform to Bash 4.3
          specifications, see bash documentation for more info:
          https://www.gnu.org/software/bash/manual/bash.html#Pattern-Matching. Only one of
          branch, pattern, or filter should be specified.
    :param bool blind_connection: True if the repository server is not addressable
          on the public internet. IBM Cloud will not be able to validate the connection
          details you provide.
    :param str hook_id: (optional) Repository webhook ID. It is generated upon
          trigger creation.
    :param Tool tool: Reference to the repository tool in the parent toolchain.
    """

    def __init__(
        self,
        url: str,
        blind_connection: bool,
        tool: 'Tool',
        *,
        branch: Optional[str] = None,
        pattern: Optional[str] = None,
        hook_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a TriggerSourceProperties object.

        :param str url: URL of the repository to which the trigger is listening.
        :param bool blind_connection: True if the repository server is not
               addressable on the public internet. IBM Cloud will not be able to validate
               the connection details you provide.
        :param Tool tool: Reference to the repository tool in the parent toolchain.
        :param str branch: (optional) Name of a branch from the repo. Only one of
               branch, pattern, or filter should be specified.
        :param str pattern: (optional) The pattern of Git branch or tag. You can
               specify a glob pattern such as '!test' or '*master' to match against
               multiple tags or branches in the repository.The glob pattern used must
               conform to Bash 4.3 specifications, see bash documentation for more info:
               https://www.gnu.org/software/bash/manual/bash.html#Pattern-Matching. Only
               one of branch, pattern, or filter should be specified.
        :param str hook_id: (optional) Repository webhook ID. It is generated upon
               trigger creation.
        """
        self.url = url
        self.branch = branch
        self.pattern = pattern
        self.blind_connection = blind_connection
        self.hook_id = hook_id
        self.tool = tool

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerSourceProperties':
        """Initialize a TriggerSourceProperties object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in TriggerSourceProperties JSON')
        if (branch := _dict.get('branch')) is not None:
            args['branch'] = branch
        if (pattern := _dict.get('pattern')) is not None:
            args['pattern'] = pattern
        if (blind_connection := _dict.get('blind_connection')) is not None:
            args['blind_connection'] = blind_connection
        else:
            raise ValueError('Required property \'blind_connection\' not present in TriggerSourceProperties JSON')
        if (hook_id := _dict.get('hook_id')) is not None:
            args['hook_id'] = hook_id
        if (tool := _dict.get('tool')) is not None:
            args['tool'] = Tool.from_dict(tool)
        else:
            raise ValueError('Required property \'tool\' not present in TriggerSourceProperties JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerSourceProperties object from a json dictionary."""
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
        if hasattr(self, 'tool') and self.tool is not None:
            if isinstance(self.tool, dict):
                _dict['tool'] = self.tool
            else:
                _dict['tool'] = self.tool.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerSourceProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerSourceProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerSourceProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TriggerSourcePropertiesPrototype:
    """
    Properties of the source, which define the URL of the repository and a branch or
    pattern.

    :param str url: URL of the repository to which the trigger is listening.
    :param str branch: (optional) Name of a branch from the repo. Only one of
          branch, pattern, or filter should be specified.
    :param str pattern: (optional) The pattern of Git branch or tag. You can specify
          a glob pattern such as '!test' or '*master' to match against multiple tags or
          branches in the repository.The glob pattern used must conform to Bash 4.3
          specifications, see bash documentation for more info:
          https://www.gnu.org/software/bash/manual/bash.html#Pattern-Matching. Only one of
          branch, pattern, or filter should be specified.
    """

    def __init__(
        self,
        url: str,
        *,
        branch: Optional[str] = None,
        pattern: Optional[str] = None,
    ) -> None:
        """
        Initialize a TriggerSourcePropertiesPrototype object.

        :param str url: URL of the repository to which the trigger is listening.
        :param str branch: (optional) Name of a branch from the repo. Only one of
               branch, pattern, or filter should be specified.
        :param str pattern: (optional) The pattern of Git branch or tag. You can
               specify a glob pattern such as '!test' or '*master' to match against
               multiple tags or branches in the repository.The glob pattern used must
               conform to Bash 4.3 specifications, see bash documentation for more info:
               https://www.gnu.org/software/bash/manual/bash.html#Pattern-Matching. Only
               one of branch, pattern, or filter should be specified.
        """
        self.url = url
        self.branch = branch
        self.pattern = pattern

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerSourcePropertiesPrototype':
        """Initialize a TriggerSourcePropertiesPrototype object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError('Required property \'url\' not present in TriggerSourcePropertiesPrototype JSON')
        if (branch := _dict.get('branch')) is not None:
            args['branch'] = branch
        if (pattern := _dict.get('pattern')) is not None:
            args['pattern'] = pattern
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerSourcePropertiesPrototype object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerSourcePropertiesPrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerSourcePropertiesPrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerSourcePropertiesPrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TriggerSourcePrototype:
    """
    Source repository for a Git trigger. Only required for Git triggers. The referenced
    repository URL must match the URL of a repository tool integration in the parent
    toolchain. Obtain the list of integrations from the toolchain API
    https://cloud.ibm.com/apidocs/toolchain#list-tools.

    :param str type: The only supported source type is "git", indicating that the
          source is a git repository.
    :param TriggerSourcePropertiesPrototype properties: Properties of the source,
          which define the URL of the repository and a branch or pattern.
    """

    def __init__(
        self,
        type: str,
        properties: 'TriggerSourcePropertiesPrototype',
    ) -> None:
        """
        Initialize a TriggerSourcePrototype object.

        :param str type: The only supported source type is "git", indicating that
               the source is a git repository.
        :param TriggerSourcePropertiesPrototype properties: Properties of the
               source, which define the URL of the repository and a branch or pattern.
        """
        self.type = type
        self.properties = properties

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerSourcePrototype':
        """Initialize a TriggerSourcePrototype object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in TriggerSourcePrototype JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = TriggerSourcePropertiesPrototype.from_dict(properties)
        else:
            raise ValueError('Required property \'properties\' not present in TriggerSourcePrototype JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TriggerSourcePrototype object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'properties') and self.properties is not None:
            if isinstance(self.properties, dict):
                _dict['properties'] = self.properties
            else:
                _dict['properties'] = self.properties.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TriggerSourcePrototype object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TriggerSourcePrototype') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TriggerSourcePrototype') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TriggersCollection:
    """
    Tekton pipeline triggers object.

    :param List[Trigger] triggers: Tekton pipeline triggers list.
    """

    def __init__(
        self,
        triggers: List['Trigger'],
    ) -> None:
        """
        Initialize a TriggersCollection object.

        :param List[Trigger] triggers: Tekton pipeline triggers list.
        """
        self.triggers = triggers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggersCollection':
        """Initialize a TriggersCollection object from a json dictionary."""
        args = {}
        if (triggers := _dict.get('triggers')) is not None:
            args['triggers'] = triggers
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
            for v in self.triggers:
                if isinstance(v, dict):
                    triggers_list.append(v)
                else:
                    triggers_list.append(v.to_dict())
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


class UserInfo:
    """
    Information about the user that triggered a pipeline run. Only included for pipeline
    runs that were manually triggered.

    :param str iam_id: IBM Cloud IAM ID.
    :param str sub: User email address.
    """

    def __init__(
        self,
        iam_id: str,
        sub: str,
    ) -> None:
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
        if (iam_id := _dict.get('iam_id')) is not None:
            args['iam_id'] = iam_id
        else:
            raise ValueError('Required property \'iam_id\' not present in UserInfo JSON')
        if (sub := _dict.get('sub')) is not None:
            args['sub'] = sub
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


class Worker:
    """
    Details of the worker used to run the pipeline.

    :param str name: (optional) Name of the worker. Computed based on the worker ID.
    :param str type: (optional) Type of the worker. Computed based on the worker ID.
    :param str id: ID of the worker.
    """

    def __init__(
        self,
        id: str,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
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
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (id := _dict.get('id')) is not None:
            args['id'] = id
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


class WorkerIdentity:
    """
    Specify the worker that is to be used to run the trigger, indicated by a worker object
    with only the worker ID. If not specified or set as `worker: { id: 'public' }`, the
    IBM Managed shared workers are used.

    :param str id: ID of the worker.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a WorkerIdentity object.

        :param str id: ID of the worker.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkerIdentity':
        """Initialize a WorkerIdentity object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in WorkerIdentity JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkerIdentity object from a json dictionary."""
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
        """Return a `str` version of this WorkerIdentity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkerIdentity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkerIdentity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TriggerGenericTrigger(Trigger):
    """
    Generic webhook trigger, which triggers a pipeline run when the Tekton Pipeline
    Service receives a POST event with secrets.

    :param str type: Trigger type.
    :param str name: Trigger name.
    :param str href: (optional) API URL for interacting with the trigger. Only
          included when fetching the list of pipeline triggers.
    :param str event_listener: Event listener name. The name of the event listener
          to which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :param str id: The Trigger ID.
    :param List[TriggerProperty] properties: (optional) Optional trigger properties
          are used to override or supplement the pipeline properties when triggering a
          pipeline run.
    :param List[str] tags: (optional) Optional trigger tags array.
    :param Worker worker: (optional) Details of the worker used to run the trigger.
    :param int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. If omitted then the concurrency limit is
          disabled for this trigger.
    :param bool enabled: Flag to check if the trigger is enabled.
    :param bool favorite: (optional) Mark the trigger as a favorite.
    :param GenericSecret secret: (optional) Only needed for Generic Webhook trigger
          type. The secret is used to start the Generic Webhook trigger.
    :param str webhook_url: (optional) Webhook URL that can be used to trigger
          pipeline runs.
    :param str filter: (optional) Stores the CEL (Common Expression Language)
          expression value which is used for event filtering against the webhook payloads.
    """

    def __init__(
        self,
        type: str,
        name: str,
        event_listener: str,
        id: str,
        enabled: bool,
        *,
        href: Optional[str] = None,
        properties: Optional[List['TriggerProperty']] = None,
        tags: Optional[List[str]] = None,
        worker: Optional['Worker'] = None,
        max_concurrent_runs: Optional[int] = None,
        favorite: Optional[bool] = None,
        secret: Optional['GenericSecret'] = None,
        webhook_url: Optional[str] = None,
        filter: Optional[str] = None,
    ) -> None:
        """
        Initialize a TriggerGenericTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param str id: The Trigger ID.
        :param bool enabled: Flag to check if the trigger is enabled.
        :param str href: (optional) API URL for interacting with the trigger. Only
               included when fetching the list of pipeline triggers.
        :param List[TriggerProperty] properties: (optional) Optional trigger
               properties are used to override or supplement the pipeline properties when
               triggering a pipeline run.
        :param List[str] tags: (optional) Optional trigger tags array.
        :param Worker worker: (optional) Details of the worker used to run the
               trigger.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. If omitted then the concurrency limit is
               disabled for this trigger.
        :param bool favorite: (optional) Mark the trigger as a favorite.
        :param GenericSecret secret: (optional) Only needed for Generic Webhook
               trigger type. The secret is used to start the Generic Webhook trigger.
        :param str webhook_url: (optional) Webhook URL that can be used to trigger
               pipeline runs.
        :param str filter: (optional) Stores the CEL (Common Expression Language)
               expression value which is used for event filtering against the webhook
               payloads.
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
        self.enabled = enabled
        self.favorite = favorite
        self.secret = secret
        self.webhook_url = webhook_url
        self.filter = filter

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerGenericTrigger':
        """Initialize a TriggerGenericTrigger object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in TriggerGenericTrigger JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in TriggerGenericTrigger JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (event_listener := _dict.get('event_listener')) is not None:
            args['event_listener'] = event_listener
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerGenericTrigger JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in TriggerGenericTrigger JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [TriggerProperty.from_dict(v) for v in properties]
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = Worker.from_dict(worker)
        if (max_concurrent_runs := _dict.get('max_concurrent_runs')) is not None:
            args['max_concurrent_runs'] = max_concurrent_runs
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        else:
            raise ValueError('Required property \'enabled\' not present in TriggerGenericTrigger JSON')
        if (favorite := _dict.get('favorite')) is not None:
            args['favorite'] = favorite
        if (secret := _dict.get('secret')) is not None:
            args['secret'] = GenericSecret.from_dict(secret)
        if (webhook_url := _dict.get('webhook_url')) is not None:
            args['webhook_url'] = webhook_url
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
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
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
                _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'favorite') and self.favorite is not None:
            _dict['favorite'] = self.favorite
        if hasattr(self, 'secret') and self.secret is not None:
            if isinstance(self.secret, dict):
                _dict['secret'] = self.secret
            else:
                _dict['secret'] = self.secret.to_dict()
        if hasattr(self, 'webhook_url') and self.webhook_url is not None:
            _dict['webhook_url'] = self.webhook_url
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
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

    :param str type: Trigger type.
    :param str name: Trigger name.
    :param str href: (optional) API URL for interacting with the trigger. Only
          included when fetching the list of pipeline triggers.
    :param str event_listener: Event listener name. The name of the event listener
          to which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :param str id: The Trigger ID.
    :param List[TriggerProperty] properties: (optional) Optional trigger properties
          are used to override or supplement the pipeline properties when triggering a
          pipeline run.
    :param List[str] tags: (optional) Optional trigger tags array.
    :param Worker worker: (optional) Details of the worker used to run the trigger.
    :param int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. If omitted then the concurrency limit is
          disabled for this trigger.
    :param bool enabled: Flag to check if the trigger is enabled.
    :param bool favorite: (optional) Mark the trigger as a favorite.
    """

    def __init__(
        self,
        type: str,
        name: str,
        event_listener: str,
        id: str,
        enabled: bool,
        *,
        href: Optional[str] = None,
        properties: Optional[List['TriggerProperty']] = None,
        tags: Optional[List[str]] = None,
        worker: Optional['Worker'] = None,
        max_concurrent_runs: Optional[int] = None,
        favorite: Optional[bool] = None,
    ) -> None:
        """
        Initialize a TriggerManualTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param str id: The Trigger ID.
        :param bool enabled: Flag to check if the trigger is enabled.
        :param str href: (optional) API URL for interacting with the trigger. Only
               included when fetching the list of pipeline triggers.
        :param List[TriggerProperty] properties: (optional) Optional trigger
               properties are used to override or supplement the pipeline properties when
               triggering a pipeline run.
        :param List[str] tags: (optional) Optional trigger tags array.
        :param Worker worker: (optional) Details of the worker used to run the
               trigger.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. If omitted then the concurrency limit is
               disabled for this trigger.
        :param bool favorite: (optional) Mark the trigger as a favorite.
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
        self.enabled = enabled
        self.favorite = favorite

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerManualTrigger':
        """Initialize a TriggerManualTrigger object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in TriggerManualTrigger JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in TriggerManualTrigger JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (event_listener := _dict.get('event_listener')) is not None:
            args['event_listener'] = event_listener
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerManualTrigger JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in TriggerManualTrigger JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [TriggerProperty.from_dict(v) for v in properties]
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = Worker.from_dict(worker)
        if (max_concurrent_runs := _dict.get('max_concurrent_runs')) is not None:
            args['max_concurrent_runs'] = max_concurrent_runs
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        else:
            raise ValueError('Required property \'enabled\' not present in TriggerManualTrigger JSON')
        if (favorite := _dict.get('favorite')) is not None:
            args['favorite'] = favorite
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
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
                _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'favorite') and self.favorite is not None:
            _dict['favorite'] = self.favorite
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
    Git trigger type. It automatically triggers a pipeline run when the Tekton Pipeline
    Service receives a corresponding Git webhook event.

    :param str type: Trigger type.
    :param str name: Trigger name.
    :param str href: (optional) API URL for interacting with the trigger. Only
          included when fetching the list of pipeline triggers.
    :param str event_listener: Event listener name. The name of the event listener
          to which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :param str id: The Trigger ID.
    :param List[TriggerProperty] properties: (optional) Optional trigger properties
          are used to override or supplement the pipeline properties when triggering a
          pipeline run.
    :param List[str] tags: (optional) Optional trigger tags array.
    :param Worker worker: (optional) Details of the worker used to run the trigger.
    :param int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. If omitted then the concurrency limit is
          disabled for this trigger.
    :param bool enabled: Flag to check if the trigger is enabled.
    :param bool favorite: (optional) Mark the trigger as a favorite.
    :param bool enable_events_from_forks: (optional) When enabled, pull request
          events from forks of the selected repository will trigger a pipeline run.
    :param TriggerSource source: (optional) Source repository for a Git trigger.
          Only required for Git triggers. The referenced repository URL must match the URL
          of a repository tool integration in the parent toolchain. Obtain the list of
          integrations from the toolchain API
          https://cloud.ibm.com/apidocs/toolchain#list-tools.
    :param List[str] events: (optional) Either 'events' or 'filter' is required
          specifically for Git triggers. Stores a list of events that a Git trigger
          listens to. Choose one or more from 'push', 'pull_request', and
          'pull_request_closed'. If SCM repositories use the 'merge request' term, they
          correspond to the generic term i.e. 'pull request'.
    :param str filter: (optional) Either 'events' or 'filter' can be used. Stores
          the CEL (Common Expression Language) expression value which is used for event
          filtering against the Git webhook payloads.
    :param bool limit_waiting_runs: (optional) Flag that will limit the trigger to a
          maximum of one waiting run. A newly triggered run will cause waiting run(s) to
          be automatically cancelled.
    """

    def __init__(
        self,
        type: str,
        name: str,
        event_listener: str,
        id: str,
        enabled: bool,
        *,
        href: Optional[str] = None,
        properties: Optional[List['TriggerProperty']] = None,
        tags: Optional[List[str]] = None,
        worker: Optional['Worker'] = None,
        max_concurrent_runs: Optional[int] = None,
        favorite: Optional[bool] = None,
        enable_events_from_forks: Optional[bool] = None,
        source: Optional['TriggerSource'] = None,
        events: Optional[List[str]] = None,
        filter: Optional[str] = None,
        limit_waiting_runs: Optional[bool] = None,
    ) -> None:
        """
        Initialize a TriggerScmTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param str id: The Trigger ID.
        :param bool enabled: Flag to check if the trigger is enabled.
        :param str href: (optional) API URL for interacting with the trigger. Only
               included when fetching the list of pipeline triggers.
        :param List[TriggerProperty] properties: (optional) Optional trigger
               properties are used to override or supplement the pipeline properties when
               triggering a pipeline run.
        :param List[str] tags: (optional) Optional trigger tags array.
        :param Worker worker: (optional) Details of the worker used to run the
               trigger.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. If omitted then the concurrency limit is
               disabled for this trigger.
        :param bool favorite: (optional) Mark the trigger as a favorite.
        :param bool enable_events_from_forks: (optional) When enabled, pull request
               events from forks of the selected repository will trigger a pipeline run.
        :param TriggerSource source: (optional) Source repository for a Git
               trigger. Only required for Git triggers. The referenced repository URL must
               match the URL of a repository tool integration in the parent toolchain.
               Obtain the list of integrations from the toolchain API
               https://cloud.ibm.com/apidocs/toolchain#list-tools.
        :param List[str] events: (optional) Either 'events' or 'filter' is required
               specifically for Git triggers. Stores a list of events that a Git trigger
               listens to. Choose one or more from 'push', 'pull_request', and
               'pull_request_closed'. If SCM repositories use the 'merge request' term,
               they correspond to the generic term i.e. 'pull request'.
        :param str filter: (optional) Either 'events' or 'filter' can be used.
               Stores the CEL (Common Expression Language) expression value which is used
               for event filtering against the Git webhook payloads.
        :param bool limit_waiting_runs: (optional) Flag that will limit the trigger
               to a maximum of one waiting run. A newly triggered run will cause waiting
               run(s) to be automatically cancelled.
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
        self.enabled = enabled
        self.favorite = favorite
        self.enable_events_from_forks = enable_events_from_forks
        self.source = source
        self.events = events
        self.filter = filter
        self.limit_waiting_runs = limit_waiting_runs

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerScmTrigger':
        """Initialize a TriggerScmTrigger object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in TriggerScmTrigger JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in TriggerScmTrigger JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (event_listener := _dict.get('event_listener')) is not None:
            args['event_listener'] = event_listener
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerScmTrigger JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in TriggerScmTrigger JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [TriggerProperty.from_dict(v) for v in properties]
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = Worker.from_dict(worker)
        if (max_concurrent_runs := _dict.get('max_concurrent_runs')) is not None:
            args['max_concurrent_runs'] = max_concurrent_runs
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        else:
            raise ValueError('Required property \'enabled\' not present in TriggerScmTrigger JSON')
        if (favorite := _dict.get('favorite')) is not None:
            args['favorite'] = favorite
        if (enable_events_from_forks := _dict.get('enable_events_from_forks')) is not None:
            args['enable_events_from_forks'] = enable_events_from_forks
        if (source := _dict.get('source')) is not None:
            args['source'] = TriggerSource.from_dict(source)
        if (events := _dict.get('events')) is not None:
            args['events'] = events
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
        if (limit_waiting_runs := _dict.get('limit_waiting_runs')) is not None:
            args['limit_waiting_runs'] = limit_waiting_runs
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
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
                _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'favorite') and self.favorite is not None:
            _dict['favorite'] = self.favorite
        if hasattr(self, 'enable_events_from_forks') and self.enable_events_from_forks is not None:
            _dict['enable_events_from_forks'] = self.enable_events_from_forks
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'events') and self.events is not None:
            _dict['events'] = self.events
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'limit_waiting_runs') and self.limit_waiting_runs is not None:
            _dict['limit_waiting_runs'] = self.limit_waiting_runs
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

    class EventsEnum(str, Enum):
        """
        List of events. Supported options are 'push' Git webhook events,
        'pull_request_closed' Git webhook events and 'pull_request' for 'open pull
        request' or 'update pull request' Git webhook events.
        """

        PUSH = 'push'
        PULL_REQUEST = 'pull_request'
        PULL_REQUEST_CLOSED = 'pull_request_closed'


class TriggerTimerTrigger(Trigger):
    """
    Timer trigger, which triggers pipeline runs according to the provided CRON value and
    timezone.

    :param str type: Trigger type.
    :param str name: Trigger name.
    :param str href: (optional) API URL for interacting with the trigger. Only
          included when fetching the list of pipeline triggers.
    :param str event_listener: Event listener name. The name of the event listener
          to which the trigger is associated. The event listeners are defined in the
          definition repositories of the Tekton pipeline.
    :param str id: The Trigger ID.
    :param List[TriggerProperty] properties: (optional) Optional trigger properties
          are used to override or supplement the pipeline properties when triggering a
          pipeline run.
    :param List[str] tags: (optional) Optional trigger tags array.
    :param Worker worker: (optional) Details of the worker used to run the trigger.
    :param int max_concurrent_runs: (optional) Defines the maximum number of
          concurrent runs for this trigger. If omitted then the concurrency limit is
          disabled for this trigger.
    :param bool enabled: Flag to check if the trigger is enabled.
    :param bool favorite: (optional) Mark the trigger as a favorite.
    :param str cron: (optional) Only needed for timer triggers. CRON expression that
          indicates when this trigger will activate. Maximum frequency is every 5 minutes.
          The string is based on UNIX crontab syntax: minute, hour, day of month, month,
          day of week. Example: The CRON expression 0 */2 * * * - translates to - every 2
          hours.
    :param str timezone: (optional) Only used for timer triggers. Specify the
          timezone used for this timer trigger, which will ensure the CRON activates this
          trigger relative to the specified timezone. If no timezone is specified, the
          default timezone used is UTC. Valid timezones are those listed in the IANA
          timezone database, https://www.iana.org/time-zones.
    """

    def __init__(
        self,
        type: str,
        name: str,
        event_listener: str,
        id: str,
        enabled: bool,
        *,
        href: Optional[str] = None,
        properties: Optional[List['TriggerProperty']] = None,
        tags: Optional[List[str]] = None,
        worker: Optional['Worker'] = None,
        max_concurrent_runs: Optional[int] = None,
        favorite: Optional[bool] = None,
        cron: Optional[str] = None,
        timezone: Optional[str] = None,
    ) -> None:
        """
        Initialize a TriggerTimerTrigger object.

        :param str type: Trigger type.
        :param str name: Trigger name.
        :param str event_listener: Event listener name. The name of the event
               listener to which the trigger is associated. The event listeners are
               defined in the definition repositories of the Tekton pipeline.
        :param str id: The Trigger ID.
        :param bool enabled: Flag to check if the trigger is enabled.
        :param str href: (optional) API URL for interacting with the trigger. Only
               included when fetching the list of pipeline triggers.
        :param List[TriggerProperty] properties: (optional) Optional trigger
               properties are used to override or supplement the pipeline properties when
               triggering a pipeline run.
        :param List[str] tags: (optional) Optional trigger tags array.
        :param Worker worker: (optional) Details of the worker used to run the
               trigger.
        :param int max_concurrent_runs: (optional) Defines the maximum number of
               concurrent runs for this trigger. If omitted then the concurrency limit is
               disabled for this trigger.
        :param bool favorite: (optional) Mark the trigger as a favorite.
        :param str cron: (optional) Only needed for timer triggers. CRON expression
               that indicates when this trigger will activate. Maximum frequency is every
               5 minutes. The string is based on UNIX crontab syntax: minute, hour, day of
               month, month, day of week. Example: The CRON expression 0 */2 * * * -
               translates to - every 2 hours.
        :param str timezone: (optional) Only used for timer triggers. Specify the
               timezone used for this timer trigger, which will ensure the CRON activates
               this trigger relative to the specified timezone. If no timezone is
               specified, the default timezone used is UTC. Valid timezones are those
               listed in the IANA timezone database, https://www.iana.org/time-zones.
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
        self.enabled = enabled
        self.favorite = favorite
        self.cron = cron
        self.timezone = timezone

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TriggerTimerTrigger':
        """Initialize a TriggerTimerTrigger object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in TriggerTimerTrigger JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in TriggerTimerTrigger JSON')
        if (href := _dict.get('href')) is not None:
            args['href'] = href
        if (event_listener := _dict.get('event_listener')) is not None:
            args['event_listener'] = event_listener
        else:
            raise ValueError('Required property \'event_listener\' not present in TriggerTimerTrigger JSON')
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in TriggerTimerTrigger JSON')
        if (properties := _dict.get('properties')) is not None:
            args['properties'] = [TriggerProperty.from_dict(v) for v in properties]
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        if (worker := _dict.get('worker')) is not None:
            args['worker'] = Worker.from_dict(worker)
        if (max_concurrent_runs := _dict.get('max_concurrent_runs')) is not None:
            args['max_concurrent_runs'] = max_concurrent_runs
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        else:
            raise ValueError('Required property \'enabled\' not present in TriggerTimerTrigger JSON')
        if (favorite := _dict.get('favorite')) is not None:
            args['favorite'] = favorite
        if (cron := _dict.get('cron')) is not None:
            args['cron'] = cron
        if (timezone := _dict.get('timezone')) is not None:
            args['timezone'] = timezone
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
            properties_list = []
            for v in self.properties:
                if isinstance(v, dict):
                    properties_list.append(v)
                else:
                    properties_list.append(v.to_dict())
            _dict['properties'] = properties_list
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'worker') and self.worker is not None:
            if isinstance(self.worker, dict):
                _dict['worker'] = self.worker
            else:
                _dict['worker'] = self.worker.to_dict()
        if hasattr(self, 'max_concurrent_runs') and self.max_concurrent_runs is not None:
            _dict['max_concurrent_runs'] = self.max_concurrent_runs
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'favorite') and self.favorite is not None:
            _dict['favorite'] = self.favorite
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


class TektonPipelineRunsPager:
    """
    TektonPipelineRunsPager can be used to simplify the use of the "list_tekton_pipeline_runs" method.
    """

    def __init__(
        self,
        *,
        client: CdTektonPipelineV2,
        pipeline_id: str,
        limit: int = None,
        status: str = None,
        trigger_name: str = None,
    ) -> None:
        """
        Initialize a TektonPipelineRunsPager object.
        :param str pipeline_id: The Tekton pipeline ID.
        :param int limit: (optional) The number of pipeline runs to return, sorted
               by creation time, most recent first.
        :param str status: (optional) Filters the collection to resources with the
               specified status.
        :param str trigger_name: (optional) Filters the collection to resources
               with the specified trigger name.
        """
        self._has_next = True
        self._client = client
        self._page_context = {'next': None}
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
        :return: A List[dict], where each element is a dict that represents an instance of PipelineRun.
        :rtype: List[dict]
        """
        if not self.has_next():
            raise StopIteration(message='No more results available')

        result = self._client.list_tekton_pipeline_runs(
            pipeline_id=self._pipeline_id,
            limit=self._limit,
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
        :return: A List[dict], where each element is a dict that represents an instance of PipelineRun.
        :rtype: List[dict]
        """
        results = []
        while self.has_next():
            next_page = self.get_next()
            results.extend(next_page)
        return results
