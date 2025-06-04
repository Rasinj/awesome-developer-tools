# Contributing to Awesome Developer Tools

Thank you for your interest in contributing to this curated list of developer tools! This guide will help you understand how to contribute effectively.

## How to Contribute

### Adding a New Tool

1. **Edit the YAML file**: All changes must be made to `data/tools.yaml` - this is our single source of truth
2. **Follow the structure**: Add tools in the appropriate category/subcategory using this format:
   ```yaml
   - name: "Tool Name"
     url: "https://example.com"
     description: "Brief description of what the tool does"
   ```
3. **Generate output files**: Run `make generate` to update all generated files
4. **Submit a pull request**: Include a clear description of the tool and why it should be included

### Adding a New Category

To add a new category, edit `data/tools.yaml` and add to the `categories` list:
```yaml
- name: "New Category"
  id: "new-category"  # lowercase with hyphens for anchor links
  description: "Optional category description"
  subcategories:
    - name: "Subcategory Name"
      tools: [...]
```

## Guidelines

### Tool Selection Criteria

- **Quality**: Tools should be well-maintained and actively developed
- **Usefulness**: Tools should provide real value to developers
- **Uniqueness**: Avoid duplicating functionality of existing listed tools
- **Documentation**: Tools should have clear documentation or README files

### Description Guidelines

- Keep descriptions concise (under 100 characters when possible)
- Focus on what the tool does, not implementation details
- Use consistent tone and style with existing entries
- Avoid marketing language or superlatives

## Development Workflow

1. **Never edit generated files directly** (README.md, tools.json, tools.csv, TOOLS_LIST.txt)
2. **Always edit `data/tools.yaml`** to make changes
3. **Run `make generate`** after any changes
4. **Use `make check`** to verify files are in sync before committing

## Setup for Development

```bash
# Install dependencies
make install

# Generate all formats
make generate

# Check if files are up to date
make check
```

## Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes to `data/tools.yaml`
4. Run `make generate` to update all output formats
5. Commit your changes with a clear message
6. Submit a pull request with:
   - Clear title describing the change
   - Description of what tool(s) you're adding/modifying
   - Why the tool deserves inclusion

## Questions?

If you have questions about contributing, please open an issue for discussion before submitting a pull request.