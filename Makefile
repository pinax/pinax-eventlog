all: init test

# Install package in development mode and required tools
init:
	uv pip install -e .
	uv tool install tox
	uv tool install coverage

# Run basic tests (linting + Python 3.9 + Django 4.2)
test:
	uvx coverage erase
	uvx -p 3.9 tox -e checkqa,py39-dj42
	uvx coverage html

# Run all tests across all Python/Django combinations  
test-all:
	uvx coverage erase
	uvx -p 3.9 tox
	uvx coverage html

# Run only code quality checks (flake8 + isort)
lint:
	uvx -p 3.9 tox -e checkqa

# Test with specific Python/Django version (e.g., make test-env ENV=py312-dj52)
test-env:
	uvx -p 3.12 tox -e $(ENV)

# Create Django migrations
makemigrations:
	uv run -p 3.10 --with=Django==5.2 python makemigrations.py

# Clean up build artifacts and caches
clean:
	rm -rf .tox/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf *.egg-info/
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

# Show available targets
help:
	@echo "Available targets:"
	@echo "  init      - Install package and tools"
	@echo "  test      - Run basic tests (lint + py39-dj42)"
	@echo "  test-all  - Run all tests across all environments"
	@echo "  lint      - Run code quality checks only"
	@echo "  test-env  - Test specific environment (ENV=py312-dj52)"
	@echo "  makemigrations - Create Django migrations"
	@echo "  clean     - Remove build artifacts and caches"
	@echo "  help      - Show this help message"

.PHONY: all init test test-all lint test-env makemigrations clean help
