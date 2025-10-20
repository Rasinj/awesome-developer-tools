#!/usr/bin/env python3
"""
Generate an interactive tool finder from the tools.yaml data.
This creates an intent-driven discovery interface that helps users find tools
based on what they're trying to accomplish rather than browsing categories.
"""

import yaml
import json
from pathlib import Path

def load_tools_data():
    """Load tools from the YAML file."""
    yaml_path = Path(__file__).parent.parent / "data" / "tools.yaml"
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def create_intent_mappings(tools_data):
    """Create intent-based mappings from the tools data."""

    # Define intent keywords and their associated tool categories/subcategories
    intent_mappings = {
        'set up new project': {
            'keywords': ['project', 'setup', 'new', 'start', 'scaffold', 'template'],
            'categories': ['Development Environments', 'Package Managers'],
            'subcategories': ['Project Scaffolding', 'Containerized Environments', 'Version Managers']
        },
        'debug performance issues': {
            'keywords': ['debug', 'performance', 'slow', 'profile', 'monitor', 'analyze'],
            'categories': ['Debugging & Profiling', 'Monitoring & Logging'],
            'subcategories': ['Debuggers', 'Performance Profiling', 'Application Monitoring']
        },
        'deploy to production': {
            'keywords': ['deploy', 'production', 'release', 'publish', 'ship', 'ci', 'cd'],
            'categories': ['DevOps & Infrastructure', 'Build Tools & Task Runners'],
            'subcategories': ['CI/CD', 'Containerization', 'Infrastructure as Code']
        },
        'manage dependencies': {
            'keywords': ['dependencies', 'package', 'install', 'manage', 'version'],
            'categories': ['Package Managers', 'Development Environments'],
            'subcategories': ['Language-Specific', 'Version Managers', 'Reproducible Systems']
        },
        'code collaboration': {
            'keywords': ['collaboration', 'team', 'share', 'review', 'merge', 'branch'],
            'categories': ['Version Control', 'Productivity'],
            'subcategories': ['Git Tools', 'Project Management']
        },
        'automate testing': {
            'keywords': ['test', 'testing', 'automate', 'ci', 'quality', 'check'],
            'categories': ['Testing', 'DevOps & Infrastructure'],
            'subcategories': ['Testing Frameworks', 'CI/CD', 'Code Analysis']
        },
        'write better code': {
            'keywords': ['code quality', 'lint', 'format', 'clean', 'style', 'best practices'],
            'categories': ['Code Quality & Linting', 'Code Editors & IDEs'],
            'subcategories': ['Linters & Formatters', 'Code Analysis', 'Modern Editors']
        },
        'work with databases': {
            'keywords': ['database', 'data', 'sql', 'query', 'store', 'persist'],
            'categories': ['Database Tools', 'Data Science & Machine Learning'],
            'subcategories': ['Database Clients', 'Database Development', 'Data Processing']
        }
    }

    # Extract tools for each intent
    tool_recommendations = {}
    
    for intent, mapping in intent_mappings.items():
        tools = []
        
        for category in tools_data['categories']:
            if category['name'] in mapping['categories']:
                for subcategory in category.get('subcategories', []):
                    if subcategory['name'] in mapping['subcategories']:
                        for tool in subcategory.get('tools', []):
                            tools.append({
                                'name': tool['name'],
                                'url': tool['url'],
                                'description': tool['description'],
                                'category': category['name'],
                                'subcategory': subcategory['name']
                            })
        
        # Limit to top 6 tools per intent for better UX
        tool_recommendations[intent] = tools[:6]
    
    return tool_recommendations

def generate_tool_finder_data():
    """Generate the tool finder data as JSON."""
    tools_data = load_tools_data()
    intent_mappings = create_intent_mappings(tools_data)
    
    # Add "why" explanations for each tool based on context
    why_explanations = {
        'Cookiecutter': 'Perfect for quickly scaffolding new projects with best practices built-in',
        'Dev Containers': 'Ensures everyone on your team has the exact same development environment',
        'Gitpod': 'Zero setup time - just click and start coding in a full environment',
        'GitHub Actions': 'Seamless integration with your GitHub workflow for automated deployments',
        'Docker': 'Ensures your app runs the same in development and production',
        'Terraform': 'Manage your infrastructure with code for reproducible deployments',
        'Chrome DevTools': 'Industry standard for debugging web performance with detailed profiling',
        'Lighthouse': 'Automated performance analysis with actionable improvement suggestions',
        'Sentry': 'Real-time error tracking and performance monitoring in production',
        'Poetry': 'Modern Python dependency management with lock files and virtual environments',
        'pnpm': 'Faster and more disk-efficient than npm with better dependency resolution',
        'Nix': 'Complete reproducibility - never worry about "it works on my machine" again',
        'Linear': 'Streamlined issue tracking designed specifically for engineering teams',
        'Notion': 'Centralize documentation, planning, and knowledge sharing for your team',
        'pytest': 'Simple yet powerful testing framework with great plugin ecosystem',
        'Playwright': 'Reliable browser automation for testing user workflows',
        'ESLint': 'Catches bugs and enforces coding standards automatically',
        'Prettier': 'Automatically formats code to maintain consistent style',
        'VS Code': 'Most popular editor with excellent extension ecosystem and debugging support',
        'Neovim': 'Highly customizable modal editor for efficient text editing',
        'DBeaver': 'Universal database client that works with all major databases',
        'PostgreSQL': 'Robust, feature-rich open-source relational database',
        'DuckDB': 'Lightning-fast analytical database perfect for data analysis'
    }
    
    # Add why explanations to tools
    for intent, tools in intent_mappings.items():
        for tool in tools:
            tool['why'] = why_explanations.get(tool['name'], f"Excellent tool for {intent.replace('_', ' ')}")
    
    return intent_mappings

def save_tool_finder_data():
    """Save the tool finder data as JSON for the frontend."""
    data = generate_tool_finder_data()
    
    output_path = Path(__file__).parent.parent / "tool-finder-data.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Generated tool finder data at {output_path}")
    return data

if __name__ == "__main__":
    data = save_tool_finder_data()
    
    # Print some stats
    total_tools = sum(len(tools) for tools in data.values())
    print(f"📊 Generated {len(data)} intent categories with {total_tools} total tool recommendations")
    
    for intent, tools in data.items():
        print(f"  • {intent}: {len(tools)} tools")