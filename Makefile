SHELL := /bin/bash

POETRY_RUN := poetry run

.PHONY: clean
clean:
	rm -f .make.*
	rm -rf .venv

### REQUIREMENTS:

poetry.lock: pyproject.toml
	poetry lock
	touch $@

requirements.txt: poetry.lock
	poetry export --without-hashes -f requirements.txt -o $@

.make.venv: requirements.txt
	poetry install
	touch $@

### SERVER:

.PHONY: server
server: .make.venv
	${POETRY_RUN} flask --app app run --debug
