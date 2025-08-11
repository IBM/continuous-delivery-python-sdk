## [2.0.4](https://github.com/IBM/continuous-delivery-python-sdk/compare/v2.0.3...v2.0.4) (2025-08-11)


### Bug Fixes

* add ca-mon support to toolchains ([#56](https://github.com/IBM/continuous-delivery-python-sdk/issues/56)) ([7198978](https://github.com/IBM/continuous-delivery-python-sdk/commit/719897865870dfdf1ca0287e50dad141dfec986b))

## [2.0.3](https://github.com/IBM/continuous-delivery-python-sdk/compare/v2.0.2...v2.0.3) (2025-08-01)


### Bug Fixes

* add ca-mon support to pipeline ([3cad3f0](https://github.com/IBM/continuous-delivery-python-sdk/commit/3cad3f0dffa4bfbfc709c0ceb9734a4b533b4b0a))

## [2.0.2](https://github.com/IBM/continuous-delivery-python-sdk/compare/v2.0.1...v2.0.2) (2025-08-01)


### Bug Fixes

* bump python and packages ([ed2e2e6](https://github.com/IBM/continuous-delivery-python-sdk/commit/ed2e2e6a006757a8a12ecc6d394decd3486e09ea))

## [2.0.1](https://github.com/IBM/continuous-delivery-python-sdk/compare/v2.0.0...v2.0.1) (2025-07-18)


### Bug Fixes

* **tekton:** add support for waiting runs limit ([26af24c](https://github.com/IBM/continuous-delivery-python-sdk/commit/26af24cf290b95f1a3398935a8e68c09804d4ea4))
* **tekton:** further limit_waiting_run updates ([43cf6c8](https://github.com/IBM/continuous-delivery-python-sdk/commit/43cf6c8fd9c157b9a4839095fbe011b4f2512fd5))

# [2.0.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.11.0...v2.0.0) (2024-10-16)


### Features

* **toolchain:** add text plain object property for create_toolchain_event function ([#50](https://github.com/IBM/continuous-delivery-python-sdk/issues/50)) ([4261f8d](https://github.com/IBM/continuous-delivery-python-sdk/commit/4261f8d614917f59681d079e6178e13c1fcaade6))


### BREAKING CHANGES

* **toolchain:** the text_plain string property is being replaced by a ToolchainEventPrototypeDataTextPlain object. String values must be provided using the ToolchainEventPrototypeDataTextPlain.content property

Signed-off-by: Omar Al Bastami <omar.albastami@ibm.com>

* update secrets baseline

Signed-off-by: Omar Al Bastami <omar.albastami@ibm.com>

# [1.11.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.10.0...v1.11.0) (2024-10-03)


### Features

* **tekton:** more fork property support ([dbe2210](https://github.com/IBM/continuous-delivery-python-sdk/commit/dbe2210300c02b56f38be8fdc00d2953f64b7ee9))

# [1.10.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.9.0...v1.10.0) (2024-09-30)


### Features

* **tekton:** Add fork events option ([b6e8a0c](https://github.com/IBM/continuous-delivery-python-sdk/commit/b6e8a0cb8af5bcb799d3707981dcf480d2ba1690))

# [1.9.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.8.0...v1.9.0) (2024-09-25)


### Features

* **tekton:** add run description for pipeline runs ([b40c2f6](https://github.com/IBM/continuous-delivery-python-sdk/commit/b40c2f686c7c83a66e3b0f414afe2ffe437c3d7a))

# [1.8.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.7.1...v1.8.0) (2024-09-04)


### Bug Fixes

* bump python core and update build files ([8a0b9cc](https://github.com/IBM/continuous-delivery-python-sdk/commit/8a0b9cc2f48fcdd275fa3959f8425d6d7295377a))
* lint ([2654fb0](https://github.com/IBM/continuous-delivery-python-sdk/commit/2654fb0235204b2a6791ce80620c3bbc27ac50d6))
* lint fixes ([7090a14](https://github.com/IBM/continuous-delivery-python-sdk/commit/7090a141632501c13f3622d98b136023292516ce))


### Features

* **toolchain:** add eu-es region ([a74d110](https://github.com/IBM/continuous-delivery-python-sdk/commit/a74d110594e0ab6962682f729abc74871778ca16))

## [1.7.1](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.7.0...v1.7.1) (2024-08-14)


### Bug Fixes

* bump python core and update build files ([#45](https://github.com/IBM/continuous-delivery-python-sdk/issues/45)) ([256b6d2](https://github.com/IBM/continuous-delivery-python-sdk/commit/256b6d2796127ea03976601b939397fb3ac8ed6d))

# [1.7.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.6.0...v1.7.0) (2024-07-29)


### Bug Fixes

* update sdk core and bump tooling ([9b7307d](https://github.com/IBM/continuous-delivery-python-sdk/commit/9b7307de197fbf76f6100a39bef2178005072a4c))


### Features

* **tekton:** Add support for CEL filtering ([d6a809a](https://github.com/IBM/continuous-delivery-python-sdk/commit/d6a809a41d7159c5cad3a761493eadd5bf28daad))

# [1.6.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.5.0...v1.6.0) (2024-05-22)


### Bug Fixes

* **build:** fix travis builds ([746e6af](https://github.com/IBM/continuous-delivery-python-sdk/commit/746e6afc2f4f7e8a3056a20cead4effd007ba1d0))
* **build:** fix version.py ([4f70202](https://github.com/IBM/continuous-delivery-python-sdk/commit/4f70202cd165c84813fc00c0c3c12f78bc88d830))


### Features

* **tekton:** locked property support ([5aefc0e](https://github.com/IBM/continuous-delivery-python-sdk/commit/5aefc0e946b1bb9266521359fde571a903c1d40c))

# [1.5.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.4.0...v1.5.0) (2023-12-15)


### Features

* **toolchain:** add function to create toolchain event ([#39](https://github.com/IBM/continuous-delivery-python-sdk/issues/39)) ([4ff7032](https://github.com/IBM/continuous-delivery-python-sdk/commit/4ff7032c71aa8235f12daa856b748b0dfcf6d5da))

# [1.4.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.3.1...v1.4.0) (2023-11-10)


### Bug Fixes

* dir fix to Makefile ([22f0f55](https://github.com/IBM/continuous-delivery-python-sdk/commit/22f0f55275f3b3f798f13d27431ee9c196e590c6))


### Features

* bump SDK version ([#38](https://github.com/IBM/continuous-delivery-python-sdk/issues/38)) ([347f6fb](https://github.com/IBM/continuous-delivery-python-sdk/commit/347f6fb983cca4f782a35608dc0121b65061e9e9))
* support eu-es region ([#37](https://github.com/IBM/continuous-delivery-python-sdk/issues/37)) ([b79698d](https://github.com/IBM/continuous-delivery-python-sdk/commit/b79698da2b98fac78f04800970be673c007b2cbb)), closes [#35](https://github.com/IBM/continuous-delivery-python-sdk/issues/35)

## [1.3.1](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.3.0...v1.3.1) (2023-10-27)


### Bug Fixes

* **tekton:** add error message to PipelineRun ([77c0ae9](https://github.com/IBM/continuous-delivery-python-sdk/commit/77c0ae91f64e3f24c0872f1113a6f2089cc7061f))

# [1.3.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.2.1...v1.3.0) (2023-09-19)


### Features

* **toolchain:** add name query param to list toolchains ([41beaa6](https://github.com/IBM/continuous-delivery-python-sdk/commit/41beaa6d57ce18f6a8fb16e314a3060fb048cc87))

## [1.2.1](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.2.0...v1.2.1) (2023-08-25)


### Bug Fixes

* **tekton:** pipeline run trigger properties ([e1c8083](https://github.com/IBM/continuous-delivery-python-sdk/commit/e1c808325b800b2f102fbdc1eabe99a9e7ea4eb5))

# [1.2.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.1.0...v1.2.0) (2023-08-09)


### Bug Fixes

* **tekton:** support favorite triggers ([35cd5d8](https://github.com/IBM/continuous-delivery-python-sdk/commit/35cd5d85931047263f75c7e8fde253d064e6d967))


### Features

* **tekton:** update for latest v2 tekton APIs ([#1](https://github.com/IBM/continuous-delivery-python-sdk/issues/1)) ([0cf77f4](https://github.com/IBM/continuous-delivery-python-sdk/commit/0cf77f4a2b935fa16296e9025d9077d039968d74))

# [1.1.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.0.1...v1.1.0) (2023-04-27)


### Features

* **tekton:** add next build number support ([282171e](https://github.com/IBM/continuous-delivery-python-sdk/commit/282171ed1e7402d00871857e0265edc6ab37ed18))

## [1.0.1](https://github.com/IBM/continuous-delivery-python-sdk/compare/v1.0.0...v1.0.1) (2023-04-26)


### Bug Fixes

* sync with template repo ([baf894b](https://github.com/IBM/continuous-delivery-python-sdk/commit/baf894baced182de65392b634f67b7f44b464009))

# [1.0.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.7...v1.0.0) (2023-02-21)


### Features

* **build:** trigger major version build ([e9f2e84](https://github.com/IBM/continuous-delivery-python-sdk/commit/e9f2e845edacbdc23957003f541eb7d0d3c3ed3c))


### BREAKING CHANGES

* **build:** release v1.0.0

Signed-off-by: Omar Al Bastami <omar.albastami@ibm.com>

## [0.3.7](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.6...v0.3.7) (2023-02-16)


### Bug Fixes

* **doc:** fix up readme issues ([332bfa0](https://github.com/IBM/continuous-delivery-python-sdk/commit/332bfa0914a798fc61cc85248a79887ccc0800a5))

## [0.3.6](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.5...v0.3.6) (2023-01-18)


### Bug Fixes

* **tekton:** WorkerIdentity and hrefs updated ([dc70e35](https://github.com/IBM/continuous-delivery-python-sdk/commit/dc70e35761405c95af0a908eab7ce0d8d8b7ab66))

## [0.3.5](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.4...v0.3.5) (2023-01-12)


### Bug Fixes

* **build:** fix sem-ver release issue ([e469482](https://github.com/IBM/continuous-delivery-python-sdk/commit/e4694826095f3b12c488f569ef405357f73f56b1))
* **tekton:** post GA updates ([9b1148c](https://github.com/IBM/continuous-delivery-python-sdk/commit/9b1148cf9cf9abc5879a17a51416cb76ba4ecf5f))
* **tekton:** update to match latest API ([c283f3a](https://github.com/IBM/continuous-delivery-python-sdk/commit/c283f3a4c2da54b813613abb09dbffeff8cd225c))

## [0.3.4](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.3...v0.3.4) (2022-12-07)


### Bug Fixes

* remove unused SDK files ([c1910d4](https://github.com/IBM/continuous-delivery-python-sdk/commit/c1910d4e9ba04754681dea0d2bef4fc2dd4c8916))

## [0.3.3](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.2...v0.3.3) (2022-12-05)


### Bug Fixes

* **toolchain:** add missing toolchain import ([2a29268](https://github.com/IBM/continuous-delivery-python-sdk/commit/2a292683fb1f64fbcca18249e6e03b75855c88d4))

## [0.3.2](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.1...v0.3.2) (2022-12-02)


### Bug Fixes

* **toolchain:** add missing toolchain import ([cfad41d](https://github.com/IBM/continuous-delivery-python-sdk/commit/cfad41dda34cf838ce8aad93c984fb1af496c0dd))

## [0.3.1](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.3.0...v0.3.1) (2022-11-30)


### Bug Fixes

* **tekton:** remove offset and patch defaults ([d14b33b](https://github.com/IBM/continuous-delivery-python-sdk/commit/d14b33b1b4e81d4b043b7635b9472e90aaf3b2b5))

# [0.3.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.2.0...v0.3.0) (2022-11-23)


### Bug Fixes

* **toolchain:** remove unnecessary comments ([6b2304c](https://github.com/IBM/continuous-delivery-python-sdk/commit/6b2304ca1b40da839b10e4670153ea690b92d9d6))


### Features

* **toolchain:** add toolchain python SDK ([44c2332](https://github.com/IBM/continuous-delivery-python-sdk/commit/44c2332a16fba33c8db6eb54ae7f489c7842d5c4))

# [0.2.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.1.0...v0.2.0) (2022-11-18)


### Features

* **tekton:** update to match V2 API GA ([40f14cb](https://github.com/IBM/continuous-delivery-python-sdk/commit/40f14cb0a5c3bc6f4a62a20a5c4be1a8f67be91d))

# [0.1.0](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.0.2...v0.1.0) (2022-09-30)


### Features

* **tekton:** update for latest v2 tekton APIs ([#7](https://github.com/IBM/continuous-delivery-python-sdk/issues/7)) ([ae4700a](https://github.com/IBM/continuous-delivery-python-sdk/commit/ae4700a2f6c3f1fdeec0bd1d8563a14558f31b3d))

## [0.0.2](https://github.com/IBM/continuous-delivery-python-sdk/compare/v0.0.1...v0.0.2) (2022-08-02)


### Bug Fixes

* **semver:** small change to test auto sem ver process ([#5](https://github.com/IBM/continuous-delivery-python-sdk/issues/5)) ([ad0db07](https://github.com/IBM/continuous-delivery-python-sdk/commit/ad0db07693e23fa242a4d393421a715a7a4d40dc))
