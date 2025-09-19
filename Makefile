# ! Make version must be ≥3.82 to use ONESHELL!
.ONESHELL:

# Terminate on error.
.SHELLFLAGS = -ec

# Set default target for `make`.
.DEFAULT_GOAL := .venv/

.venv/: pyproject.toml
	pyenv install -s
	pyenv local
	poetry config virtualenvs.in-project true
	poetry env use $$(pyenv which python)
	poetry install
	poetry update
	touch .venv/
