[![Build Status](https://travis-ci.com/IBM/continuous-delivery-python-sdk.svg?branch=main)](https://travis.ibm.com/IBM/continuous-delivery-python-sdk)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ibm-continuous-delivery)](https://pypi.org/project/ibm-continuous-delivery/)
[![Latest Stable Version](https://img.shields.io/pypi/v/ibm-continuous-delivery.svg)](https://pypi.python.org/pypi/ibm-continuous-delivery)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)

# IBM Cloud Continuous Delivery Python SDK v1.3.0
 
The Python client library to interact with the [IBM Cloud Continuous Delivery Toolchain and Tekton Pipeline APIs](https://cloud.ibm.com/docs?tab=api-docs&category=devops).

# Python Version
The current minimum Python version supported is 3.7.

## Table of Contents

<!--
  The TOC below is generated using the `markdown-toc` node package.

      https://github.com/jonschlinkert/markdown-toc

  You should regenerate the TOC after making changes to this file.

      npx markdown-toc -i README.md
  -->

<!-- toc -->

- [IBM Cloud Continuous Delivery Python SDK v1.3.0](#ibm-cloud-continuous-delivery-python-sdk-v037)
- [Python Version](#python-version)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Using the SDK](#using-the-sdk)
  - [Questions](#questions)
  - [Issues](#issues)
  - [Open source @ IBM](#open-source--ibm)
  - [Contributing](#contributing)
  - [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Continuous Delivery Python SDK allows developers to programmatically interact with the following
IBM Cloud services:

Service Name | Module Name | Imported Class Name
--- | --- | ---
[Toolchain API](https://cloud.ibm.com/apidocs/toolchain?code=python) | cd_toolchain_v2| CdToolchainV2
[Tekton Pipeline API](https://cloud.ibm.com/apidocs/tekton-pipeline?code=python) | cd_tekton_pipeline_v2 | CdTektonPipelineV2

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.7 or above.

## Installation

To install, use `pip`:

```bash
pip install --upgrade ibm-continuous-delivery
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/main/README.md)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).
Alternatively, you can reach out to the IBM Cloud Continuous Delivery development team by joining us on [Slack](https://ic-devops-slack-invite.us-south.devops.cloud.ibm.com/).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/continuous-delivery-python-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](https://github.com/IBM/continuous-delivery-python-sdk/blob/main/CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](https://github.com/IBM/continuous-delivery-python-sdk/blob/main/LICENSE).
