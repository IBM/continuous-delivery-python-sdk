PYTHON=python3
LINT=black
LINT_DIRS=ibm_continuous_delivery test/unit test/integration examples

setup: deps dev-deps install-project

all: upgrade-pip setup test-unit lint

ci: all

publish-release: build-dist publish-dist

upgrade-pip:
	${PYTHON} -m pip install --upgrade pip

deps:
	${PYTHON} -m pip install .

dev-deps:
	${PYTHON} -m pip install .[dev]
	${PYTHON} -m pip install environs

publish-deps:
	${PYTHON} -m pip install .[publish]

install-project:
	${PYTHON} -m pip install -e .

test: test-unit test-int

test-unit:
	${PYTHON} -m pytest test/unit

test-int:
	${PYTHON} -m pytest test/integration

test-examples:
	${PYTHON} -m pytest examples

lint:
	${PYTHON} -m pylint ${LINT_DIRS} --exit-zero
	${LINT} --check ${LINT_DIRS}

lint-fix:
	${LINT} ${LINT_DIRS}

build-dist:
	rm -fr dist
	${PYTHON} -m build

# This target requires the TWINE_PASSWORD env variable to be set to the user's pypi.org API token.
publish-dist:
	TWINE_USERNAME=__token__ ${PYTHON} -m twine upload --non-interactive --verbose dist/*
