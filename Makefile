# This Makefile provides commands for setting up the development environment,
# running formatting tools, and cleaning the repository.

# Set the default target to 'help' when running make without arguments
.DEFAULT_GOAL := help

# Create a Python virtual environment using uv (faster alternative to venv)
venv:
	@if ! command -v uv >/dev/null 2>&1; then \  # Check if uv is installed
		echo "uv not found. Installing..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	fi
	@uv venv  # Create a virtual environment in the current directory

# Mark 'install' as a phony target (not associated with a file)
.PHONY: install
install: venv ## Install a virtual environment
	@uv pip install --upgrade pip                       # Ensure pip is up to date
	@uv pip install --no-cache-dir -r requirements.txt  # Install project dependencies from requirements.txt

# Code Quality
.PHONY: fmt
fmt: install ## Run autoformatting and linting
	@uv pip install pre-commit  # Install pre-commit hooks
	@uv run pre-commit install  # Set up pre-commit hooks
	@uv run pre-commit run --all-files  # Run pre-commit hooks on all files

# Book Building
.PHONY: build
build: install ## Build the book
	@uv pip install jupyter-book  # Install jupyter-book
	@uv run jupyter-book clean book  # Clean previous builds
	@uv run jupyter-book build book  # Build the book
	touch book/_build/html/.nojekyll  # Add .nojekyll file for GitHub Pages

# Cleanup
.PHONY: clean
clean:  ## Clean up caches and build artifacts
	@git clean -X -d -f  # Remove files ignored by git

# Help
.PHONY: help
help:  ## Display this help screen
	@echo -e "\033[1mAvailable commands:\033[0m"  # Print header in bold
	@grep -E '^[a-z.A-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}' | sort  # Extract and format targets with comments

# Jupyter Setup
.PHONY: jupyter
jupyter: install ## Start jupyterlab
	@uv pip install jupyterlab  # Install JupyterLab
	@uv run jupyter lab  # Start JupyterLab server
