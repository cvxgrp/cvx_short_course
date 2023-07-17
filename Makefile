.DEFAULT_GOAL := help

VENV :=.venv

.PHONY: install
install:  ## Install a virtual environment
	python -m venv ${VENV}
	${VENV}/bin/pip install --upgrade pip
	${VENV}/bin/pip install -r requirements.txt

.PHONY: fmt
fmt: install ## Run autoformatting and linting
	${VENV}/bin/pip install pre-commit
	${VENV}/bin/pre-commit install
	${VENV}/bin/pre-commit run --all-files

.PHONY: build
build: install ## Build the book
	${VENV}/bin/pip install jupyter-book
	${VENV}/bin/jupyter-book clean book
	${VENV}/bin/jupyter-book build book
	touch book/_build/html/.nojekyll

.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@rm -rf .idea
	@rm -rf .ruff_cache
	@find . -type f -name '*.py[co]' -delete -or -type d -name __pycache__ -delete
	@find . -type d -name .ipynb_checkpoints -exec rm -rf {} +

.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort
