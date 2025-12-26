.PHONY: help doctor format lint test

help:
	@echo "Targets:"
	@echo "  doctor  - environment checks"
	@echo "  format  - run black"
	@echo "  lint    - run ruff"
	@echo "  test    - run pytest"

doctor:
	python -m clinical_risk.cli doctor

format:
	black src tests

lint:
	ruff check src tests

test:
	pytest -q