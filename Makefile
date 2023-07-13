.DEFAULT_GOAL := help

SHELL=/bin/bash

UNAME=$(shell uname -s)
KERNEL=$(shell poetry version | cut -d' ' -f1)

.PHONY: install
install:  ## Install a virtual environment
	python -m venv .venv
	# see https://stackoverflow.com/questions/44052093/makefile-with-source-get-error-no-such-file-or-directory
	. .venv/bin/activate
	which python
	which pip
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install jupyter-book


.PHONY: fmt
fmt: install ## Run autoformatting and linting
	. .venv/bin/activate
	pip install pre-commit
	pre-commit install
	pre-commit run --all-files

.PHONY: build
build: install ## Build the book
	. .venv/bin/activate
	jupyter-book clean book
	jupyter-book build book
	touch book/_build/html/.nojekyll


.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@rm -rf .venv
	@rm -rf .idea
	@rm -rf .ruff_cache

	@find . -type f -name '*.py[co]' -delete -or -type d -name __pycache__ -delete
	@find . -type d -name .ipynb_checkpoints -exec rm -rf {} +


.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort
