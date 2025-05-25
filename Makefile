.PHONY: help install generate readme json csv list clean check

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install Python dependencies
	pip install -r requirements.txt

generate:  ## Generate all formats from YAML data
	python scripts/generate.py

readme:  ## Generate only README.md
	python scripts/generate.py --format readme

json:  ## Generate only JSON export
	python scripts/generate.py --format json

csv:  ## Generate only CSV export
	python scripts/generate.py --format csv

list:  ## Generate only simple text list
	python scripts/generate.py --format list

check:  ## Check if generated files are up to date
	@python scripts/generate.py --format readme && \
	if ! git diff --quiet README.md; then \
		echo "❌ README.md is out of date. Run 'make generate' to update."; \
		exit 1; \
	else \
		echo "✅ Generated files are up to date."; \
	fi

clean:  ## Remove generated files
	rm -f README.md tools.json tools.csv TOOLS_LIST.txt