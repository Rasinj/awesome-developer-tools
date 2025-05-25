# Development Guide

This repository uses a structured approach to maintain tool listings across multiple formats. Instead of manually editing the README.md, you should edit the YAML data source and regenerate all files.

## Architecture

```
├── data/
│   └── tools.yaml          # Single source of truth for all tool data
├── templates/
│   └── README.md.j2        # Jinja2 template for README generation
├── scripts/
│   └── generate.py         # Generation script
├── requirements.txt        # Python dependencies
└── Generated files:
    ├── README.md           # Main documentation (auto-generated)
    ├── tools.json          # JSON export for APIs
    ├── tools.csv           # CSV export for spreadsheets
    └── TOOLS_LIST.txt      # Simple text list
```

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Make the generation script executable:
   ```bash
   chmod +x scripts/generate.py
   ```

## Making Changes

### Adding a New Tool

1. Edit `data/tools.yaml`
2. Find the appropriate category and subcategory
3. Add your tool following this format:
   ```yaml
   - name: "Tool Name"
     url: "https://example.com"
     description: "Brief description of what the tool does"
   ```
4. Regenerate all files: `python scripts/generate.py`

### Adding a New Category

1. Edit `data/tools.yaml`
2. Add a new category to the `categories` list:
   ```yaml
   - name: "New Category"
     id: "new-category"  # Used for anchor links, lowercase with hyphens
     description: "Optional category description"
     subcategories:
       - name: "Subcategory Name"
         tools:
           - name: "Tool Name"
             url: "https://example.com"
             description: "Tool description"
   ```
3. Regenerate all files: `python scripts/generate.py`

### Modifying Templates

1. Edit the Jinja2 template in `templates/README.md.j2`
2. Use standard Jinja2 syntax to access data from the YAML file
3. Regenerate: `python scripts/generate.py --format readme`

## Generation Commands

```bash
# Generate all formats
python scripts/generate.py

# Generate only README
python scripts/generate.py --format readme

# Generate only JSON export
python scripts/generate.py --format json

# Generate only CSV export
python scripts/generate.py --format csv

# Generate only simple text list
python scripts/generate.py --format list

# Use custom paths
python scripts/generate.py --data custom/data.yaml --output-dir output/
```

## Benefits of This Approach

1. **Single Source of Truth**: All tool data lives in one YAML file
2. **Multiple Formats**: Generate README, JSON, CSV, and text formats from the same data
3. **Consistency**: Templates ensure consistent formatting across all generated files
4. **Easy Maintenance**: Add/remove tools in one place, regenerate everywhere
5. **API-Friendly**: JSON export can be consumed by websites, apps, or scripts
6. **Spreadsheet-Friendly**: CSV export for analysis or bulk operations
7. **Version Control**: YAML changes are easy to review in pull requests

## Pre-commit Hook (Recommended)

To ensure generated files stay in sync, add this to `.git/hooks/pre-commit`:

```bash
#!/bin/bash
python scripts/generate.py
git add README.md tools.json tools.csv TOOLS_LIST.txt
```

Then make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

This automatically regenerates files before each commit.