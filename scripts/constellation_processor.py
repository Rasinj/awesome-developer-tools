#!/usr/bin/env python3
"""
Tool Constellation Data Processor

This script processes the tools.yaml data to create constellation mappings
for the visual tool discovery system. It analyzes tool relationships,
creates skill progression paths, and generates ecosystem mappings.
"""

import json
import yaml
import math
import random
from pathlib import Path
from typing import Dict, List, Any, Tuple
from collections import defaultdict
import argparse


class ConstellationProcessor:
    def __init__(self, data: Dict[str, Any]):
        self.data = data
        self.tools_map = {}
        self.categories_map = {}
        self.tool_relationships = defaultdict(list)
        self.skill_paths = []
        
    def process_tools(self):
        """Process all tools and create mappings."""
        tool_id = 0
        
        for category in self.data['categories']:
            self.categories_map[category['id']] = {
                'name': category['name'],
                'id': category['id'],
                'description': category.get('description', ''),
                'subcategories': []
            }
            
            for subcategory in category['subcategories']:
                subcat_info = {
                    'name': subcategory['name'],
                    'tools': []
                }
                
                for tool in subcategory['tools']:
                    tool_data = {
                        'id': tool_id,
                        'name': tool['name'],
                        'url': tool['url'],
                        'description': tool['description'],
                        'category': category['name'],
                        'category_id': category['id'],
                        'subcategory': subcategory['name'],
                        'position': self._generate_position(tool_id, category['id']),
                        'connections': [],
                        'popularity': self._calculate_popularity(tool),
                        'difficulty': self._estimate_difficulty(tool, category),
                        'tags': self._extract_tags(tool, category, subcategory)
                    }
                    
                    self.tools_map[tool_id] = tool_data
                    subcat_info['tools'].append(tool_id)
                    tool_id += 1
                
                self.categories_map[category['id']]['subcategories'].append(subcat_info)
    
    def _generate_position(self, tool_id: int, category_id: str) -> Dict[str, float]:
        """Generate position coordinates for tools in different view modes."""
        # Galaxy view - spiral positioning
        angle = (tool_id * 2.4) % (2 * math.pi)
        radius = 50 + (tool_id % 10) * 30
        galaxy_x = radius * math.cos(angle)
        galaxy_y = radius * math.sin(angle)
        
        # Solar system view - circular orbits per category
        category_index = hash(category_id) % 12
        orbit_radius = 100 + category_index * 50
        tool_angle = (tool_id * 0.8) % (2 * math.pi)
        solar_x = orbit_radius * math.cos(tool_angle)
        solar_y = orbit_radius * math.sin(tool_angle)
        
        # Skill tree view - hierarchical positioning
        tree_x = (tool_id % 8) * 150 - 600
        tree_y = (tool_id // 8) * 100 - 400
        
        return {
            'galaxy': {'x': galaxy_x, 'y': galaxy_y},
            'solar': {'x': solar_x, 'y': solar_y},
            'tree': {'x': tree_x, 'y': tree_y}
        }
    
    def _calculate_popularity(self, tool: Dict[str, str]) -> float:
        """Estimate tool popularity based on name recognition and type."""
        popular_tools = {
            'Visual Studio Code': 0.95,
            'Git': 0.98,
            'Docker': 0.90,
            'React': 0.88,
            'Node.js': 0.85,
            'Python': 0.92,
            'JavaScript': 0.90,
            'GitHub': 0.88,
            'Stack Overflow': 0.85,
            'AWS': 0.80,
            'Google': 0.85,
            'Microsoft': 0.80,
            'Neovim': 0.75,
            'Vim': 0.70,
            'tmux': 0.65,
            'zsh': 0.60,
            'PostgreSQL': 0.75,
            'MySQL': 0.70,
            'MongoDB': 0.65,
            'Redis': 0.60,
            'Kubernetes': 0.70,
            'Terraform': 0.65,
            'Jenkins': 0.60,
            'Jest': 0.70,
            'Webpack': 0.65,
            'npm': 0.80,
            'yarn': 0.65,
            'pip': 0.75
        }
        
        name = tool['name']
        for popular_name, score in popular_tools.items():
            if popular_name.lower() in name.lower():
                return score
        
        # Default scoring based on description keywords
        desc = tool['description'].lower()
        if any(word in desc for word in ['popular', 'widely used', 'standard', 'industry']):
            return random.uniform(0.6, 0.8)
        elif any(word in desc for word in ['modern', 'fast', 'efficient', 'powerful']):
            return random.uniform(0.5, 0.7)
        else:
            return random.uniform(0.3, 0.6)
    
    def _estimate_difficulty(self, tool: Dict[str, str], category: Dict[str, str]) -> str:
        """Estimate learning difficulty for skill progression."""
        name = tool['name'].lower()
        desc = tool['description'].lower()
        cat_name = category['name'].lower()
        
        # Easy tools
        if any(word in desc for word in ['simple', 'easy', 'beginner', 'quick', 'lightweight']):
            return 'beginner'
        elif any(word in name for word in ['vs code', 'visual studio code', 'github']):
            return 'beginner'
        
        # Advanced tools
        elif any(word in desc for word in ['advanced', 'enterprise', 'professional', 'complex']):
            return 'advanced'
        elif any(word in cat_name for word in ['devops', 'infrastructure', 'security']):
            return 'advanced'
        elif any(word in name for word in ['kubernetes', 'terraform', 'ansible']):
            return 'advanced'
        
        # Intermediate by default
        return 'intermediate'
    
    def _extract_tags(self, tool: Dict[str, str], category: Dict[str, str], subcategory: Dict[str, str]) -> List[str]:
        """Extract relevant tags for filtering and connections."""
        tags = []
        
        # Add category and subcategory as tags
        tags.extend([category['name'].lower().replace(' ', '-'), 
                    subcategory['name'].lower().replace(' ', '-')])
        
        # Extract technology tags from descriptions
        tech_keywords = {
            'javascript': ['javascript', 'js', 'node', 'npm', 'react', 'vue', 'angular'],
            'python': ['python', 'django', 'flask', 'jupyter', 'pandas'],
            'rust': ['rust', 'cargo'],
            'go': ['go', 'golang'],
            'java': ['java', 'jvm', 'scala', 'kotlin'],
            'web': ['web', 'html', 'css', 'browser', 'http'],
            'cli': ['command-line', 'terminal', 'cli', 'shell'],
            'git': ['git', 'version control', 'github', 'gitlab'],
            'database': ['database', 'sql', 'nosql', 'postgres', 'mysql', 'mongo'],
            'docker': ['docker', 'container', 'kubernetes'],
            'cloud': ['cloud', 'aws', 'azure', 'gcp', 'google cloud'],
            'testing': ['test', 'testing', 'unit test', 'integration'],
            'monitoring': ['monitor', 'logging', 'observability', 'analytics'],
            'security': ['security', 'vulnerability', 'authentication']
        }
        
        desc_lower = tool['description'].lower()
        name_lower = tool['name'].lower()
        
        for tag, keywords in tech_keywords.items():
            if any(keyword in desc_lower or keyword in name_lower for keyword in keywords):
                tags.append(tag)
        
        return list(set(tags))  # Remove duplicates
    
    def generate_connections(self):
        """Generate connections between related tools."""
        for tool_id, tool in self.tools_map.items():
            connections = []
            
            # Connect tools with shared tags
            for other_id, other_tool in self.tools_map.items():
                if tool_id == other_id:
                    continue
                
                shared_tags = set(tool['tags']).intersection(set(other_tool['tags']))
                if len(shared_tags) >= 2:  # Strong connection
                    connections.append({
                        'target': other_id,
                        'strength': min(len(shared_tags) * 0.3, 1.0),
                        'type': 'technology'
                    })
                elif len(shared_tags) == 1:  # Weak connection
                    connections.append({
                        'target': other_id,
                        'strength': 0.1,
                        'type': 'category'
                    })
            
            # Limit connections to avoid clutter
            connections.sort(key=lambda x: x['strength'], reverse=True)
            tool['connections'] = connections[:8]
    
    def generate_skill_paths(self):
        """Generate learning progression paths through tools."""
        # Define common skill progression patterns
        path_templates = [
            {
                'name': 'Web Development Journey',
                'description': 'From basic web development to full-stack mastery',
                'stages': [
                    {'level': 'beginner', 'tags': ['web', 'html', 'css']},
                    {'level': 'intermediate', 'tags': ['javascript', 'web']},
                    {'level': 'intermediate', 'tags': ['javascript', 'testing']},
                    {'level': 'advanced', 'tags': ['web', 'devops']}
                ]
            },
            {
                'name': 'DevOps Pipeline',
                'description': 'Master the DevOps toolchain',
                'stages': [
                    {'level': 'beginner', 'tags': ['git', 'version-control']},
                    {'level': 'intermediate', 'tags': ['docker', 'containerization']},
                    {'level': 'intermediate', 'tags': ['testing', 'ci/cd']},
                    {'level': 'advanced', 'tags': ['kubernetes', 'cloud']}
                ]
            },
            {
                'name': 'Data Science Path',
                'description': 'Journey into data science and machine learning',
                'stages': [
                    {'level': 'beginner', 'tags': ['python', 'data-science']},
                    {'level': 'intermediate', 'tags': ['python', 'jupyter']},
                    {'level': 'intermediate', 'tags': ['database', 'analytics']},
                    {'level': 'advanced', 'tags': ['machine-learning', 'ai']}
                ]
            }
        ]
        
        for template in path_templates:
            path = {
                'name': template['name'],
                'description': template['description'],
                'stages': []
            }
            
            for stage in template['stages']:
                matching_tools = []
                for tool_id, tool in self.tools_map.items():
                    if (tool['difficulty'] == stage['level'] and
                        any(tag in tool['tags'] for tag in stage['tags'])):
                        matching_tools.append(tool_id)
                
                if matching_tools:
                    # Select up to 3 tools per stage
                    path['stages'].append({
                        'level': stage['level'],
                        'tools': matching_tools[:3]
                    })
            
            if path['stages']:  # Only add paths with actual tools
                self.skill_paths.append(path)
    
    def create_ecosystem_views(self) -> Dict[str, Any]:
        """Create different ecosystem view configurations."""
        return {
            'galaxy': {
                'name': 'Tool Galaxy',
                'description': 'Explore tools as stars in a vast constellation',
                'center': {'x': 0, 'y': 0},
                'zoom_range': [0.1, 3.0],
                'force_strength': 0.3,
                'collision_radius': 25
            },
            'solar': {
                'name': 'Tech Solar Systems',
                'description': 'Each category forms its own solar system',
                'center': {'x': 0, 'y': 0},
                'zoom_range': [0.1, 2.0],
                'force_strength': 0.5,
                'collision_radius': 20
            },
            'tree': {
                'name': 'Skill Constellation',
                'description': 'Follow learning paths through the tool universe',
                'center': {'x': 0, 'y': -200},
                'zoom_range': [0.2, 1.5],
                'force_strength': 0.4,
                'collision_radius': 30
            }
        }
    
    def export_constellation_data(self, output_path: Path):
        """Export processed constellation data to JSON."""
        constellation_data = {
            'metadata': {
                'title': 'Developer Tools Constellation',
                'description': 'Interactive visual discovery system for developer tools',
                'generated_from': self.data['metadata']['title'],
                'tool_count': len(self.tools_map),
                'category_count': len(self.categories_map)
            },
            'tools': list(self.tools_map.values()),
            'categories': self.categories_map,
            'skill_paths': self.skill_paths,
            'ecosystem_views': self.create_ecosystem_views(),
            'search_index': self._create_search_index()
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(constellation_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Generated constellation data at {output_path}")
        print(f"📊 Processed {len(self.tools_map)} tools across {len(self.categories_map)} categories")
        print(f"🛤️  Created {len(self.skill_paths)} skill progression paths")
    
    def _create_search_index(self) -> Dict[str, List[int]]:
        """Create search index for fast tool discovery."""
        index = defaultdict(list)
        
        for tool_id, tool in self.tools_map.items():
            # Index tool name
            words = tool['name'].lower().split()
            for word in words:
                index[word].append(tool_id)
            
            # Index description keywords
            desc_words = tool['description'].lower().split()
            for word in desc_words:
                if len(word) > 3:  # Skip short words
                    index[word].append(tool_id)
            
            # Index tags
            for tag in tool['tags']:
                index[tag].append(tool_id)
        
        # Remove duplicates and convert to regular dict
        return {word: list(set(tool_ids)) for word, tool_ids in index.items()}


def load_data(data_path: Path) -> dict:
    """Load YAML data from file."""
    with open(data_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def main():
    parser = argparse.ArgumentParser(description='Generate constellation data from YAML tools')
    parser.add_argument('--data', type=Path, default='data/tools.yaml',
                       help='Path to YAML data file')
    parser.add_argument('--output', type=Path, default='constellation-data.json',
                       help='Output JSON file')
    
    args = parser.parse_args()
    
    # Ensure we're in the right directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    data_path = repo_root / args.data
    output_path = repo_root / args.output
    
    # Load and process data
    try:
        data = load_data(data_path)
        processor = ConstellationProcessor(data)
        
        print("🔄 Processing tools and generating constellation mappings...")
        processor.process_tools()
        
        print("🔗 Generating tool connections...")
        processor.generate_connections()
        
        print("🛤️  Creating skill progression paths...")
        processor.generate_skill_paths()
        
        print("💾 Exporting constellation data...")
        processor.export_constellation_data(output_path)
        
        print("✨ Constellation processing complete!")
        return 0
        
    except FileNotFoundError:
        print(f"❌ Data file not found: {data_path}")
        return 1
    except yaml.YAMLError as e:
        print(f"❌ Error parsing YAML: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error processing constellation data: {e}")
        return 1


if __name__ == '__main__':
    exit(main())