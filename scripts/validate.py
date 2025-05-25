#!/usr/bin/env python3
"""
Validation script for tools.yaml data structure.

This script validates:
- YAML structure and syntax
- Required fields presence
- URL accessibility (optional)
- Duplicate tool names
- Proper category and subcategory structure
"""

import yaml
import requests
import sys
from pathlib import Path
from typing import Dict, List, Set
import argparse
from urllib.parse import urlparse


def load_yaml(file_path: Path) -> Dict:
    """Load and parse YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ YAML syntax error: {e}")
        return None
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None


def validate_structure(data: Dict) -> List[str]:
    """Validate the basic structure of the YAML data."""
    errors = []
    
    # Check top-level structure
    if 'metadata' not in data:
        errors.append("Missing 'metadata' section")
    elif not isinstance(data['metadata'], dict):
        errors.append("'metadata' must be a dictionary")
    else:
        # Check metadata fields
        required_metadata = ['title', 'description', 'badge_url', 'badge_alt']
        for field in required_metadata:
            if field not in data['metadata']:
                errors.append(f"Missing metadata field: {field}")
    
    if 'categories' not in data:
        errors.append("Missing 'categories' section")
        return errors
    
    if not isinstance(data['categories'], list):
        errors.append("'categories' must be a list")
        return errors
    
    # Check each category
    for i, category in enumerate(data['categories']):
        if not isinstance(category, dict):
            errors.append(f"Category {i} must be a dictionary")
            continue
        
        # Check required category fields
        required_cat_fields = ['name', 'id', 'subcategories']
        for field in required_cat_fields:
            if field not in category:
                errors.append(f"Category '{category.get('name', i)}' missing field: {field}")
        
        # Check subcategories
        if 'subcategories' in category:
            if not isinstance(category['subcategories'], list):
                errors.append(f"Category '{category['name']}' subcategories must be a list")
                continue
            
            for j, subcategory in enumerate(category['subcategories']):
                if not isinstance(subcategory, dict):
                    errors.append(f"Subcategory {j} in '{category['name']}' must be a dictionary")
                    continue
                
                # Check required subcategory fields
                if 'name' not in subcategory:
                    errors.append(f"Subcategory {j} in '{category['name']}' missing 'name'")
                if 'tools' not in subcategory:
                    errors.append(f"Subcategory '{subcategory.get('name', j)}' in '{category['name']}' missing 'tools'")
                    continue
                
                if not isinstance(subcategory['tools'], list):
                    errors.append(f"Tools in '{subcategory['name']}' must be a list")
                    continue
                
                # Check each tool
                for k, tool in enumerate(subcategory['tools']):
                    if not isinstance(tool, dict):
                        errors.append(f"Tool {k} in '{subcategory['name']}' must be a dictionary")
                        continue
                    
                    # Check required tool fields
                    required_tool_fields = ['name', 'url', 'description']
                    for field in required_tool_fields:
                        if field not in tool:
                            errors.append(f"Tool {k} in '{subcategory['name']}' missing field: {field}")
    
    return errors


def validate_duplicates(data: Dict) -> List[str]:
    """Check for duplicate tool names across all categories."""
    errors = []
    tool_names: Set[str] = set()
    tool_urls: Set[str] = set()
    
    for category in data.get('categories', []):
        for subcategory in category.get('subcategories', []):
            for tool in subcategory.get('tools', []):
                name = tool.get('name', '').strip()
                url = tool.get('url', '').strip()
                
                if name:
                    if name in tool_names:
                        errors.append(f"Duplicate tool name: '{name}'")
                    else:
                        tool_names.add(name)
                
                if url:
                    if url in tool_urls:
                        errors.append(f"Duplicate tool URL: '{url}'")
                    else:
                        tool_urls.add(url)
    
    return errors


def validate_urls(data: Dict, check_accessibility: bool = False) -> List[str]:
    """Validate URL formats and optionally check accessibility."""
    errors = []
    
    # Check metadata URLs
    metadata = data.get('metadata', {})
    badge_url = metadata.get('badge_url', '')
    if badge_url:
        if not is_valid_url(badge_url):
            errors.append(f"Invalid badge URL: {badge_url}")
        elif check_accessibility and not is_url_accessible(badge_url):
            errors.append(f"Badge URL not accessible: {badge_url}")
    
    # Check tool URLs
    for category in data.get('categories', []):
        for subcategory in category.get('subcategories', []):
            for tool in subcategory.get('tools', []):
                url = tool.get('url', '').strip()
                name = tool.get('name', 'Unknown')
                
                if url:
                    if not is_valid_url(url):
                        errors.append(f"Invalid URL for '{name}': {url}")
                    elif check_accessibility and not is_url_accessible(url):
                        errors.append(f"URL not accessible for '{name}': {url}")
    
    return errors


def is_valid_url(url: str) -> bool:
    """Check if URL has valid format."""
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except Exception:
        return False


def is_url_accessible(url: str, timeout: int = 10) -> bool:
    """Check if URL is accessible (returns 200-399 status code)."""
    try:
        response = requests.head(url, timeout=timeout, allow_redirects=True)
        return 200 <= response.status_code < 400
    except Exception:
        return False


def validate_ids(data: Dict) -> List[str]:
    """Validate category IDs follow proper format."""
    errors = []
    
    for category in data.get('categories', []):
        cat_id = category.get('id', '')
        name = category.get('name', '')
        
        if not cat_id:
            continue
        
        # Check ID format (lowercase, hyphens only)
        if not cat_id.replace('-', '').replace('&', '').islower():
            errors.append(f"Category ID '{cat_id}' should be lowercase with hyphens")
        
        # Check if ID roughly matches name
        expected_id = name.lower().replace(' ', '-').replace('&', '')
        if cat_id != expected_id and not cat_id.startswith(expected_id.split('-')[0]):
            errors.append(f"Category ID '{cat_id}' doesn't match name '{name}' (expected something like '{expected_id}')")
    
    return errors


def count_tools(data: Dict) -> Dict[str, int]:
    """Count tools by category for statistics."""
    stats = {}
    total_tools = 0
    
    for category in data.get('categories', []):
        cat_name = category.get('name', 'Unknown')
        cat_count = 0
        
        for subcategory in category.get('subcategories', []):
            subcat_count = len(subcategory.get('tools', []))
            cat_count += subcat_count
        
        stats[cat_name] = cat_count
        total_tools += cat_count
    
    stats['_total'] = total_tools
    return stats


def main():
    parser = argparse.ArgumentParser(description='Validate tools.yaml structure and content')
    parser.add_argument('--file', type=Path, default='data/tools.yaml',
                       help='Path to YAML file to validate')
    parser.add_argument('--check-urls', action='store_true',
                       help='Check URL accessibility (slow)')
    parser.add_argument('--stats', action='store_true',
                       help='Show tool count statistics')
    
    args = parser.parse_args()
    
    # Ensure we're in the right directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    yaml_file = repo_root / args.file
    
    print(f"🔍 Validating {yaml_file}")
    
    # Load YAML
    data = load_yaml(yaml_file)
    if data is None:
        return 1
    
    # Run validations
    all_errors = []
    
    print("📋 Checking structure...")
    all_errors.extend(validate_structure(data))
    
    print("🔍 Checking for duplicates...")
    all_errors.extend(validate_duplicates(data))
    
    print("🔗 Validating URLs...")
    all_errors.extend(validate_urls(data, check_accessibility=args.check_urls))
    
    print("🏷️  Checking category IDs...")
    all_errors.extend(validate_ids(data))
    
    # Show results
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} validation errors:")
        for error in all_errors:
            print(f"  • {error}")
        return 1
    else:
        print("\n✅ All validations passed!")
    
    # Show statistics if requested
    if args.stats:
        print("\n📊 Tool Statistics:")
        stats = count_tools(data)
        total = stats.pop('_total')
        
        for category, count in sorted(stats.items()):
            print(f"  {category}: {count} tools")
        print(f"  \nTotal: {total} tools across {len(stats)} categories")
    
    return 0


if __name__ == '__main__':
    exit(main())