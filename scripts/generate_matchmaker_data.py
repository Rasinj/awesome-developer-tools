#!/usr/bin/env python3
"""
Generate tool matchmaker data from the YAML tools database.
This script analyzes tool characteristics and generates compatibility scores
for different developer archetypes.
"""

import yaml
import json
import re
from pathlib import Path
from typing import Dict, List, Any

def load_tools_data() -> Dict[str, Any]:
    """Load tools data from YAML file."""
    yaml_path = Path(__file__).parent.parent / "data" / "tools.yaml"
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def analyze_tool_characteristics(tool: Dict[str, str]) -> Dict[str, Any]:
    """
    Analyze tool characteristics to determine archetype compatibility.
    
    Uses description text analysis and known patterns to determine:
    - Learning curve (gentle, moderate, steep)
    - Customization level (minimal, moderate, extensive)
    - Complexity level (low, medium, high)
    - Target audience (individual, team, enterprise)
    """
    name = tool.get('name', '').lower()
    description = tool.get('description', '').lower()
    
    # Learning curve analysis
    learning_curve = "moderate"
    if any(keyword in description for keyword in ['simple', 'easy', 'lightweight', 'minimal']):
        learning_curve = "gentle"
    elif any(keyword in description for keyword in ['advanced', 'powerful', 'comprehensive', 'complex']):
        learning_curve = "steep"
    
    # Customization analysis
    customization = "moderate"
    if any(keyword in description for keyword in ['configurable', 'extensible', 'customizable', 'plugins']):
        customization = "extensive"
    elif any(keyword in description for keyword in ['opinionated', 'zero-config', 'convention']):
        customization = "minimal"
    
    # Extract tags based on description content
    tags = []
    
    # Technology tags
    if 'javascript' in description or 'js' in description or 'node' in description:
        tags.append('javascript')
    if 'python' in description:
        tags.append('python')
    if 'rust' in description:
        tags.append('rust')
    if 'java' in description:
        tags.append('java')
    
    # Feature tags
    if any(keyword in description for keyword in ['terminal', 'command-line', 'cli']):
        tags.append('terminal')
    if any(keyword in description for keyword in ['gui', 'visual', 'interface']):
        tags.append('gui')
    if any(keyword in description for keyword in ['fast', 'performance', 'speed']):
        tags.append('fast')
    if any(keyword in description for keyword in ['collaboration', 'team', 'sharing']):
        tags.append('collaborative')
    if any(keyword in description for keyword in ['enterprise', 'professional', 'commercial']):
        tags.append('enterprise')
    if any(keyword in description for keyword in ['open source', 'community']):
        tags.append('open-source')
    if any(keyword in description for keyword in ['modern', 'next-generation', 'cutting-edge']):
        tags.append('modern')
    if any(keyword in description for keyword in ['cross-platform', 'multi-platform']):
        tags.append('cross-platform')
    
    return {
        'learning_curve': learning_curve,
        'customization': customization,
        'tags': tags
    }


def calculate_archetype_scores(tool_data: Dict[str, Any]) -> Dict[str, int]:
    """
    Calculate compatibility scores for each developer archetype.
    Scores range from 1-10 based on tool characteristics.
    """
    characteristics = tool_data['characteristics']
    learning_curve = characteristics['learning_curve']
    customization = characteristics['customization']
    tags = characteristics['tags']
    
    scores = {
        'minimalist': 5,      # Base score
        'tinkerer': 5,
        'enterprise': 5,
        'explorer': 5,
        'pragmatist': 5,
        'collaborator': 5
    }
    
    # Learning curve impact
    if learning_curve == 'gentle':
        scores['minimalist'] += 3
        scores['pragmatist'] += 2
        scores['tinkerer'] -= 1
    elif learning_curve == 'steep':
        scores['tinkerer'] += 3
        scores['explorer'] += 1
        scores['minimalist'] -= 2
        scores['pragmatist'] -= 1
    
    # Customization impact
    if customization == 'extensive':
        scores['tinkerer'] += 3
        scores['explorer'] += 1
        scores['minimalist'] -= 2
    elif customization == 'minimal':
        scores['minimalist'] += 2
        scores['pragmatist'] += 1
        scores['tinkerer'] -= 2
    
    # Tag-based scoring
    for tag in tags:
        if tag == 'terminal':
            scores['minimalist'] += 2
            scores['tinkerer'] += 2
            scores['enterprise'] -= 1
        elif tag == 'gui':
            scores['enterprise'] += 1
            scores['collaborator'] += 1
            scores['minimalist'] -= 1
        elif tag == 'fast':
            scores['minimalist'] += 2
            scores['pragmatist'] += 1
        elif tag == 'collaborative':
            scores['collaborator'] += 3
            scores['enterprise'] += 2
        elif tag == 'enterprise':
            scores['enterprise'] += 3
            scores['collaborator'] += 1
            scores['explorer'] -= 1
        elif tag == 'modern':
            scores['explorer'] += 3
            scores['tinkerer'] += 1
            scores['pragmatist'] -= 1
        elif tag == 'open-source':
            scores['tinkerer'] += 2
            scores['explorer'] += 1
        elif tag == 'javascript':
            scores['explorer'] += 1
            scores['collaborator'] += 1
        elif tag == 'python':
            scores['explorer'] += 1
            scores['pragmatist'] += 1
        elif tag == 'rust':
            scores['explorer'] += 2
            scores['tinkerer'] += 2
            scores['minimalist'] += 1
    
    # Ensure scores are within bounds
    for archetype in scores:
        scores[archetype] = max(1, min(10, scores[archetype]))
    
    return scores


def generate_matchmaker_data() -> Dict[str, Any]:
    """Generate the complete matchmaker data structure."""
    tools_yaml = load_tools_data()
    matchmaker_data = {
        'tools': {},
        'categories': {},
        'metadata': {
            'version': '1.0',
            'generated_at': None,
            'total_tools': 0
        }
    }
    
    # Process each category and its tools
    for category in tools_yaml.get('categories', []):
        category_name = category['name']
        matchmaker_data['categories'][category_name] = {
            'id': category['id'],
            'description': category.get('description', ''),
            'tools': []
        }
        
        # Process subcategories
        for subcategory in category.get('subcategories', []):
            for tool in subcategory.get('tools', []):
                tool_name = tool['name']
                
                # Analyze tool characteristics
                characteristics = analyze_tool_characteristics(tool)
                
                # Calculate archetype scores
                archetype_scores = calculate_archetype_scores({
                    'characteristics': characteristics
                })
                
                # Build tool data structure
                tool_data = {
                    'name': tool_name,
                    'url': tool['url'],
                    'description': tool['description'],
                    'category': category_name,
                    'subcategory': subcategory.get('name', ''),
                    'characteristics': characteristics,
                    'archetype_scores': archetype_scores
                }
                
                matchmaker_data['tools'][tool_name] = tool_data
                matchmaker_data['categories'][category_name]['tools'].append(tool_name)
    
    # Update metadata
    matchmaker_data['metadata']['total_tools'] = len(matchmaker_data['tools'])
    matchmaker_data['metadata']['generated_at'] = None  # Will be set by JavaScript
    
    return matchmaker_data


def main():
    """Main function to generate and save matchmaker data."""
    print("Generating AI Tool Matchmaker data...")
    
    # Generate data
    matchmaker_data = generate_matchmaker_data()
    
    # Save to JSON file
    output_path = Path(__file__).parent.parent / "tool-matchmaker-data.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(matchmaker_data, f, indent=2, ensure_ascii=False)
    
    print(f"Generated data for {matchmaker_data['metadata']['total_tools']} tools")
    print(f"Data saved to: {output_path}")
    
    # Print summary by category
    print("\nTools by category:")
    for category, data in matchmaker_data['categories'].items():
        print(f"  {category}: {len(data['tools'])} tools")


if __name__ == "__main__":
    main()