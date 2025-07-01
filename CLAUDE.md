# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Structure

This is an "awesome list" repository that maintains a curated collection of developer tools. The project uses a data-driven approach where a YAML file serves as the single source of truth, and multiple output formats are generated from it.

Key architecture:
- `data/tools.yaml` - Single source of truth for all tool data
- `templates/README.md.j2` - Jinja2 template for README generation  
- `scripts/generate.py` - Python script that generates all output formats
- `scripts/generate_matchmaker_data.py` - AI matchmaker data generation
- Generated files: `README.md`, `tools.json`, `tools.csv`, `TOOLS_LIST.txt`
- AI Matchmaker: `tool-matchmaker.html`, `tool-matchmaker-data.json`

## Essential Commands

```bash
# Install dependencies
make install
# or: pip install -r requirements.txt

# Generate all formats from YAML data
make generate
# or: python scripts/generate.py

# Generate specific formats
make readme     # README.md only
make json       # tools.json only  
make csv        # tools.csv only
make list       # TOOLS_LIST.txt only

# Check if generated files are up to date
make check

# Clean generated files
make clean

# AI Matchmaker system
make matchmaker       # Generate AI matchmaker data
make matchmaker-data  # Generate only matchmaker data
```

## Development Workflow

1. **Never edit generated files directly** (README.md, tools.json, tools.csv, TOOLS_LIST.txt)
2. **Always edit `data/tools.yaml`** to make changes to tool listings
3. **Run `make generate`** after any YAML changes to update all output formats
4. **Use `make check`** to verify files are in sync before committing

## Adding Tools

Edit `data/tools.yaml` and add tools in this structure:
```yaml
- name: "Tool Name"
  url: "https://example.com"
  description: "Brief description of what the tool does"
```

Then regenerate: `make generate`

## Adding Categories

Add new categories to the `categories` list in `data/tools.yaml`:
```yaml
- name: "New Category"
  id: "new-category"  # lowercase with hyphens for anchor links
  description: "Optional category description"
  subcategories:
    - name: "Subcategory Name"
      tools: [...]
```

## AI Matchmaker System

The repository includes an advanced AI-powered tool matchmaking system:

- `tool-matchmaker.html` - Interactive personality-driven tool recommendation engine
- `scripts/generate_matchmaker_data.py` - Analyzes tools and generates compatibility scores
- Developer archetype profiling with 6 distinct personality types
- Machine learning algorithm that improves recommendations based on user feedback
- Tool compatibility matrix showing synergistic tool combinations

See `AI_MATCHMAKER.md` for detailed technical documentation.

## Critical Rules

- The YAML file is the authoritative source - all changes must be made there
- Generated files should never be manually edited
- Always run `make generate` after YAML changes
- Run `make matchmaker` to update AI recommendation data after tool changes
- The `make check` command can verify if generated files are current