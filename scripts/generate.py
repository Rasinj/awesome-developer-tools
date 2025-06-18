#!/usr/bin/env python3
"""
Generate README and other formats from YAML data source.

This script reads tool data from data/tools.yaml and generates:
- README.md (from Jinja2 template)
- JSON export for APIs
- CSV export for spreadsheets
- Simple text list for quick reference
"""

import json
import csv
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import argparse


def load_data(data_path: Path) -> dict:
    """Load YAML data from file."""
    with open(data_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_readme(data: dict, template_path: Path, output_path: Path):
    """Generate README.md from Jinja2 template."""
    env = Environment(loader=FileSystemLoader(template_path.parent))
    template = env.get_template(template_path.name)
    
    content = template.render(**data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Generated README.md at {output_path}")


def generate_json(data: dict, output_path: Path):
    """Generate JSON export of tools data."""
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated JSON export at {output_path}")


def generate_csv(data: dict, output_path: Path):
    """Generate CSV export of all tools."""
    tools = []
    
    for category in data['categories']:
        for subcategory in category['subcategories']:
            for tool in subcategory['tools']:
                tools.append({
                    'category': category['name'],
                    'subcategory': subcategory['name'],
                    'name': tool['name'],
                    'url': tool['url'],
                    'description': tool['description']
                })
    
    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['category', 'subcategory', 'name', 'url', 'description'])
        writer.writeheader()
        writer.writerows(tools)
    
    print(f"✅ Generated CSV export at {output_path}")


def generate_simple_list(data: dict, output_path: Path):
    """Generate simple text list of tools."""
    lines = [f"# {data['metadata']['title']}\n"]
    
    for category in data['categories']:
        lines.append(f"\n## {category['name']}\n")
        for subcategory in category['subcategories']:
            lines.append(f"\n### {subcategory['name']}\n")
            for tool in subcategory['tools']:
                lines.append(f"- {tool['name']}: {tool['url']}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    
    print(f"✅ Generated simple list at {output_path}")


def main():
    parser = argparse.ArgumentParser(description='Generate documentation from YAML data')
    parser.add_argument('--format', choices=['all', 'readme', 'json', 'csv', 'list'], 
                       default='all', help='Format to generate')
    parser.add_argument('--data', type=Path, default='data/tools.yaml',
                       help='Path to YAML data file')
    parser.add_argument('--output-dir', type=Path, default='.',
                       help='Output directory')
    
    args = parser.parse_args()
    
    # Ensure we're in the right directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    data_path = repo_root / args.data
    output_dir = repo_root / args.output_dir
    template_path = repo_root / 'templates' / 'README.md.j2'
    
    # Load data
    try:
        data = load_data(data_path)
    except FileNotFoundError:
        print(f"❌ Data file not found: {data_path}")
        return 1
    except yaml.YAMLError as e:
        print(f"❌ Error parsing YAML: {e}")
        return 1
    
    # Generate formats
    if args.format in ['all', 'readme']:
        generate_readme(data, template_path, output_dir / 'README.md')
    
    if args.format in ['all', 'json']:
        generate_json(data, output_dir / 'tools.json')
    
    if args.format in ['all', 'csv']:
        generate_csv(data, output_dir / 'tools.csv')
    
    if args.format in ['all', 'list']:
        generate_simple_list(data, output_dir / 'TOOLS_LIST.txt')
    
    print("🎉 Generation complete!")
    return 0


if __name__ == '__main__':
    exit(main())