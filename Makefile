.PHONY: help install generate readme json csv list clean check constellation constellation-data constellation-serve constellation-full constellation-status matchmaker matchmaker-data timeline timeline-data

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

install:  ## Install Python dependencies
	pip install -r requirements.txt

generate:  ## Generate all formats from YAML data
	python scripts/generate.py
	python scripts/generate_timeline_data.py

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

constellation:  ## Generate constellation data and serve visualization
	python scripts/run_constellation.py --full

constellation-data:  ## Generate constellation data only
	python scripts/run_constellation.py --generate

constellation-serve:  ## Serve constellation with existing data
	python scripts/run_constellation.py --serve

constellation-full:  ## Generate data and serve constellation (same as constellation)
	python scripts/run_constellation.py --full

constellation-status:  ## Show constellation system status
	python scripts/run_constellation.py --status

matchmaker:  ## Generate AI matchmaker system with data
	python scripts/generate_matchmaker_data.py

matchmaker-data:  ## Generate only matchmaker data
	python scripts/generate_matchmaker_data.py

timeline:  ## Generate timeline visualization with data
	python scripts/generate_timeline_data.py

timeline-data:  ## Generate only timeline data
	python scripts/generate_timeline_data.py

clean:  ## Remove generated files
	rm -f README.md tools.json tools.csv TOOLS_LIST.txt constellation-data.json tool-matchmaker-data.json tool-timeline-data.json