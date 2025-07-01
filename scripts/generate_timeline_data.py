#!/usr/bin/env python3
"""
Timeline Data Generator for Developer Tools

This script analyzes the tools in the YAML data and generates enriched timeline data
including historical information, trend analysis, and evolution chains.
"""

import json
import yaml
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import requests
from urllib.parse import urlparse

# Historical data for major tools (year of first release)
TOOL_BIRTH_YEARS = {
    # Editors & IDEs
    "vim": 1991,
    "neovim": 2014,
    "visual studio code": 2015,
    "vscode": 2015,
    "vs code": 2015,
    "intellij idea": 2001,
    "pycharm": 2010,
    "webstorm": 2010,
    "android studio": 2013,
    "sublime text": 2008,
    "atom": 2014,
    "eclipse": 2001,
    "emacs": 1976,
    "nano": 1999,
    "helix": 2021,
    "zed": 2022,
    
    # Version Control
    "git": 2005,
    "github": 2008,
    "gitlab": 2011,
    "bitbucket": 2008,
    "subversion": 2000,
    "svn": 2000,
    "mercurial": 2005,
    "cvs": 1990,
    
    # Build Tools
    "webpack": 2012,
    "vite": 2020,
    "rollup": 2015,
    "parcel": 2017,
    "esbuild": 2020,
    "gulp": 2013,
    "grunt": 2012,
    "make": 1976,
    "cmake": 2000,
    "ninja": 2012,
    "bazel": 2015,
    
    # JavaScript Frameworks
    "react": 2013,
    "vue": 2014,
    "angular": 2010,
    "angularjs": 2010,
    "svelte": 2016,
    "jquery": 2006,
    "backbone.js": 2010,
    "ember.js": 2011,
    "knockout.js": 2010,
    
    # Package Managers
    "npm": 2010,
    "yarn": 2016,
    "pnpm": 2017,
    "pip": 2008,
    "conda": 2012,
    "homebrew": 2009,
    "chocolatey": 2011,
    "cargo": 2014,
    
    # Languages
    "typescript": 2012,
    "rust": 2015,
    "go": 2009,
    "kotlin": 2016,
    "swift": 2014,
    "dart": 2011,
    "python": 1991,
    "javascript": 1995,
    "java": 1995,
    "c++": 1985,
    "c": 1972,
    
    # Testing
    "jest": 2014,
    "mocha": 2011,
    "jasmine": 2010,
    "cypress": 2017,
    "selenium": 2004,
    "playwright": 2020,
    "vitest": 2021,
    "pytest": 1998,
    "junit": 1997,
    
    # DevOps & Infrastructure
    "docker": 2013,
    "kubernetes": 2014,
    "ansible": 2012,
    "terraform": 2014,
    "vagrant": 2010,
    "jenkins": 2011,
    "travis ci": 2011,
    "circle ci": 2011,
    "github actions": 2018,
    
    # Databases
    "mysql": 1995,
    "postgresql": 1996,
    "mongodb": 2009,
    "redis": 2009,
    "elasticsearch": 2010,
    "sqlite": 2000,
    "cassandra": 2008,
    
    # Terminal Tools
    "tmux": 2007,
    "screen": 1987,
    "zsh": 1990,
    "bash": 1989,
    "fish": 2005,
    "oh my zsh": 2009,
    "starship": 2019,
    "alacritty": 2017,
    "iterm2": 2013,
    "hyper": 2016,
    
    # Modern CLI Tools
    "ripgrep": 2016,
    "fd": 2017,
    "bat": 2018,
    "exa": 2014,
    "lsd": 2018,
    "fzf": 2013,
    "jq": 2012,
    "fx": 2017,
    "yq": 2015,
    "htop": 2004,
    "bottom": 2019,
    "procs": 2019,
    "dust": 2018,
    "duf": 2020,
    "tokei": 2015,
    "hyperfine": 2017,
    "watchexec": 2016,
    "lazygit": 2018,
    "lazydocker": 2019,
    "delta": 2019,
    "zoxide": 2020,
    "starship": 2019,
    "direnv": 2010,
    "tldr": 2013,
    "lnav": 2009,
    "broot": 2018,
    "ranger": 2009,
    "nnn": 2016,
    "visidata": 2016,
    "bandwhich": 2019,
    "parquet-tools": 2013,
    
    # Package Managers & Version Managers
    "uv": 2023,
    "poetry": 2018,
    "pdm": 2021,
    "pipenv": 2017,
    "nvm": 2010,
    "fnm": 2019,
    "rbenv": 2011,
    "sdkman": 2012,
    "rustup": 2016,
    "mise": 2023,
    "asdf": 2014,
    
    # Development Environments
    "gitpod": 2019,
    "codespaces": 2020,
    "devpod": 2023,
    "coder": 2017,
    "vagrant": 2010,
    "lima": 2021,
    "multipass": 2018,
    "utm": 2019,
    "nix": 2003,
    "guix": 2012,
    "tilt": 2018,
    "devspace": 2019,
    "garden": 2018,
    "telepresence": 2017,
    "code-server": 2019,
    "theia": 2016,
    "cookiecutter": 2013,
    "yeoman": 2012,
    "degit": 2018,
    "plop": 2015,
    
    # Web Frameworks & Tools
    "fastapi": 2018,
    "django": 2005,
    "flask": 2010,
    "starlette": 2018,
    "jupyter": 2014,
    "pandas": 2008,
    "numpy": 1995,
    "scikit-learn": 2007,
    "polars": 2020,
    "pyarrow": 2016,
    "click": 2014,
    "typer": 2019,
    "rich": 2020,
    "textual": 2021,
    
    # Build Tools
    "just": 2016,
    "task": 2017,
    "turbo": 2021,
    "rspack": 2022,
    "swc": 2019,
    "rome": 2020,
    "biome": 2023,
    
    # Testing Tools
    "vitest": 2021,
    "playwright": 2020,
    "storybook": 2016,
    "faker.js": 2010,
    "testing library": 2018,
    
    # Code Quality
    "eslint": 2013,
    "prettier": 2017,
    "black": 2018,
    "ruff": 2022,
    "pylint": 2003,
    "flake8": 2010,
    "isort": 2013,
    "mypy": 2012,
    "rustfmt": 2016,
    "clippy": 2014,
    "semgrep": 2020,
    
    # API Tools
    "postman": 2012,
    "insomnia": 2016,
    "httpie": 2012,
    "curl": 1997,
    "swagger": 2011,
    "redoc": 2015,
    "json-server": 2013,
    "wiremock": 2011,
    "mockoon": 2017,
    
    # Database Tools
    "dbeaver": 2010,
    "tableplus": 2018,
    "pgadmin": 1998,
    "mongodb compass": 2015,
    "prisma": 2019,
    "drizzle": 2022,
    "flyway": 2010,
    "liquibase": 2006,
    "neo4j": 2007,
    "kuzudb": 2022,
    "duckdb": 2019,
    "clickhouse": 2016,
    
    # Monitoring & Security
    "datadog": 2010,
    "new relic": 2008,
    "sentry": 2008,
    "grafana": 2014,
    "prometheus": 2012,
    "elk stack": 2010,
    "fluentd": 2011,
    "loki": 2018,
    "snyk": 2015,
    "owasp zap": 2010,
    "bandit": 2014,
    "hashicorp vault": 2015,
    
    # Documentation
    "gitbook": 2014,
    "mkdocs": 2014,
    "docusaurus": 2017,
    "vitepress": 2020,
    "stoplight": 2016,
    
    # Design & Asset Tools
    "figma": 2016,
    "sketch": 2010,
    "adobe xd": 2016,
    "imageoptim": 2007,
    "tinypng": 2014,
    "svgo": 2012,
    
    # Productivity
    "linear": 2019,
    "notion": 2016,
    "jira": 2002,
    "rescuetime": 2008,
    "toggl": 2006,
    "obsidian": 2020,
    "roam research": 2019,
    "logseq": 2020,
    
    # Cloud Platforms
    "aws cli": 2013,
    "gcloud": 2013,
    "azure cli": 2017,
    "crossplane": 2018,
    
    # Mobile Development
    "flutter": 2017,
    "react native": 2015,
    "expo": 2016,
    "xcode": 2003,
    
    # AI Era Tools
    "github copilot": 2021,
    "cursor": 2023,
    "tauri": 2019,
    "claude": 2022,
    "chatgpt": 2022,
}

# Development eras and their characteristics
DEVELOPMENT_ERAS = {
    "unix": {
        "title": "Unix Era",
        "period": "1970s - 1980s",
        "years": (1970, 1989),
        "description": "The foundation of modern development tools. Unix philosophy of small, composable tools laid the groundwork for everything that followed.",
        "characteristics": ["Command-line focused", "Composable tools", "Text processing", "Shell scripting"],
        "key_innovations": ["vi/vim", "grep", "sed", "awk", "make", "cc"]
    },
    "internet": {
        "title": "Internet Era", 
        "period": "1990s",
        "years": (1990, 1999),
        "description": "The web revolutionized software distribution and collaboration. Version control and the first web development tools emerged.",
        "characteristics": ["Web emergence", "Email collaboration", "FTP distribution", "Early IDEs"],
        "key_innovations": ["HTML", "HTTP", "CVS", "Eclipse precursors", "Perl", "TCL/Tk"]
    },
    "web": {
        "title": "Web 2.0 Era",
        "period": "2000s", 
        "years": (2000, 2009),
        "description": "Dynamic web applications emerged. JavaScript frameworks, AJAX, and modern web development practices were born.",
        "characteristics": ["Dynamic web apps", "AJAX", "Early frameworks", "IDE maturation"],
        "key_innovations": ["jQuery", "Eclipse", "IntelliJ IDEA", "Subversion", "Firefox DevTools"]
    },
    "mobile": {
        "title": "Mobile Era",
        "period": "2010s",
        "years": (2010, 2019), 
        "description": "Mobile development transformed software. Modern JavaScript frameworks, cloud services, and agile development practices emerged.",
        "characteristics": ["Mobile-first", "Cloud services", "Modern frameworks", "DevOps emergence"],
        "key_innovations": ["React", "Angular", "Node.js", "Docker", "Git", "GitHub", "AWS"]
    },
    "cloud": {
        "title": "Cloud-Native Era",
        "period": "2015 - Present",
        "years": (2015, 2023),
        "description": "Cloud-first development with microservices, serverless, and DevOps. Tools became faster, more specialized, and cloud-integrated.",
        "characteristics": ["Microservices", "Containerization", "CI/CD", "Infrastructure as Code"],
        "key_innovations": ["VS Code", "Kubernetes", "Terraform", "Rust tools", "Vite", "TypeScript"]
    },
    "ai": {
        "title": "AI Era", 
        "period": "2020 - Future",
        "years": (2020, 2030),
        "description": "AI-powered development tools, automated code generation, and intelligent assistance are transforming how we write software.",
        "characteristics": ["AI assistance", "Code generation", "Intelligent tooling", "Natural language interfaces"],
        "key_innovations": ["GitHub Copilot", "ChatGPT", "Cursor", "AI-powered IDEs", "Code analysis"]
    }
}

# Tool evolution chains
EVOLUTION_CHAINS = {
    "text_editors": {
        "category": "Text Editors",
        "description": "Evolution from simple text editors to AI-powered development environments",
        "chain": ["ed", "vi", "vim", "neovim", "helix"]
    },
    "ides": {
        "category": "Integrated Development Environments", 
        "description": "From heavyweight IDEs to lightweight, extensible editors",
        "chain": ["turbo pascal", "visual studio", "eclipse", "intellij idea", "vs code", "cursor"]
    },
    "version_control": {
        "category": "Version Control",
        "description": "Evolution of collaborative development and code management", 
        "chain": ["rcs", "cvs", "subversion", "git", "github"]
    },
    "build_tools": {
        "category": "Build Tools",
        "description": "From simple makefiles to modern ultra-fast bundlers",
        "chain": ["make", "ant", "maven", "grunt", "gulp", "webpack", "vite"]
    },
    "js_frameworks": {
        "category": "JavaScript Frameworks",
        "description": "From jQuery simplicity to modern reactive frameworks",
        "chain": ["prototype.js", "jquery", "backbone.js", "angular", "react", "vue", "svelte"]
    },
    "package_managers": {
        "category": "Package Managers",
        "description": "Evolution of dependency management",
        "chain": ["tar.gz", "rpm", "deb", "npm", "yarn", "pnpm"]
    },
    "testing": {
        "category": "Testing Frameworks",
        "description": "From simple assertions to comprehensive testing ecosystems",
        "chain": ["unittest", "junit", "jasmine", "mocha", "jest", "vitest"]
    },
    "containerization": {
        "category": "Containerization",
        "description": "From virtual machines to lightweight containers",
        "chain": ["chroot", "lxc", "docker", "podman", "kubernetes"]
    }
}

def load_tools_data() -> Dict[str, Any]:
    """Load tools data from YAML file."""
    yaml_path = Path(__file__).parent.parent / "data" / "tools.yaml"
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)

def extract_github_info(url: str) -> Optional[Dict[str, Any]]:
    """Extract GitHub repository information from URL."""
    if "github.com" not in url:
        return None
    
    # Parse GitHub URL
    path_parts = urlparse(url).path.strip('/').split('/')
    if len(path_parts) >= 2:
        owner, repo = path_parts[0], path_parts[1]
        return {"owner": owner, "repo": repo}
    return None

def estimate_tool_birth_year(tool_name: str, tool_url: str = "") -> int:
    """Estimate the birth year of a tool based on name and URL."""
    name_lower = tool_name.lower()
    
    # Check exact matches first
    if name_lower in TOOL_BIRTH_YEARS:
        return TOOL_BIRTH_YEARS[name_lower]
    
    # Check partial matches (more specific matching)
    for known_tool, year in TOOL_BIRTH_YEARS.items():
        # More precise matching
        if (len(known_tool) > 3 and known_tool in name_lower) or \
           (len(name_lower) > 3 and name_lower in known_tool and len(name_lower) >= len(known_tool) * 0.8):
            return year
    
    # Special cases for common patterns
    if "vs code" in name_lower or "visual studio code" in name_lower:
        return 2015
    if "github" in name_lower:
        return 2008
    if "docker" in name_lower:
        return 2013
    if "kubernetes" in name_lower or "k8s" in name_lower:
        return 2014
    if "react" in name_lower:
        return 2013
    if "vue" in name_lower:
        return 2014
    if "angular" in name_lower:
        return 2010
    
    # Category-based estimation
    github_info = extract_github_info(tool_url)
    if github_info:
        # GitHub was founded in 2008, most projects are newer
        return 2015  # Conservative estimate for GitHub projects
    
    # Default based on URL patterns
    if any(domain in tool_url for domain in [".io", ".dev", ".app"]):
        return 2018  # Modern domains tend to be newer
    elif ".com" in tool_url:
        return 2010  # .com domains could be older
    elif ".org" in tool_url:
        return 2005  # .org often used by older projects
    
    # Final fallback
    return 2015

def categorize_by_era(birth_year: int) -> str:
    """Categorize a tool by its development era."""
    for era_id, era_info in DEVELOPMENT_ERAS.items():
        start_year, end_year = era_info["years"]
        if start_year <= birth_year <= end_year:
            return era_id
    
    # Default to AI era for very recent tools
    return "ai"

def estimate_trend(tool_name: str, birth_year: int) -> str:
    """Estimate the current trend of a tool."""
    current_year = datetime.now().year
    age = current_year - birth_year
    name_lower = tool_name.lower()
    
    # Rising tools (recent, modern, or actively growing)
    rising_indicators = [
        "rust", "vite", "deno", "bun", "tauri", "cursor", "zed", "helix",
        "github copilot", "copilot", "claude", "chatgpt", "ai", "ml",
        "nextjs", "next.js", "vercel", "netlify", "supabase", "prisma",
        "tailwind", "svelte", "solid", "qwik", "fresh"
    ]
    
    # Declining tools (legacy or being replaced)
    declining_indicators = [
        "jquery", "bower", "grunt", "gulp", "angular.js", "angularjs",
        "internet explorer", "ie", "flash", "silverlight", "coffeescript",
        "sass", "less", "backbone", "ember", "knockout", "prototype"
    ]
    
    # Check for explicit indicators
    for indicator in rising_indicators:
        if indicator in name_lower:
            return "rising"
    
    for indicator in declining_indicators:
        if indicator in name_lower:
            return "declining"
    
    # Age-based heuristics
    if age < 3:
        return "rising"
    elif age > 15:
        return "declining" 
    else:
        return "stable"

def estimate_adoption_score(tool_name: str, era: str, trend: str) -> int:
    """Estimate adoption score based on various factors."""
    name_lower = tool_name.lower()
    
    # High adoption tools
    high_adoption = [
        "git", "npm", "node", "react", "vue", "angular", "vs code", "vscode",
        "docker", "kubernetes", "python", "javascript", "typescript", "java"
    ]
    
    # Medium adoption tools  
    medium_adoption = [
        "webpack", "babel", "eslint", "prettier", "jest", "cypress", "selenium",
        "jenkins", "travis", "circle ci", "gitlab", "bitbucket"
    ]
    
    # Check for explicit matches
    for tool in high_adoption:
        if tool in name_lower:
            return min(95, 85 + (5 if trend == "rising" else 0))
    
    for tool in medium_adoption:
        if tool in name_lower:
            return min(85, 70 + (10 if trend == "rising" else 0))
    
    # Era-based scoring
    era_base_scores = {
        "ai": 40,
        "cloud": 70, 
        "mobile": 65,
        "web": 45,
        "internet": 30,
        "unix": 80  # Unix tools are still widely used
    }
    
    base_score = era_base_scores.get(era, 50)
    
    # Trend adjustments
    if trend == "rising":
        return min(95, base_score + 20)
    elif trend == "declining":
        return max(10, base_score - 25)
    else:
        return base_score

def estimate_community_size(adoption_score: int, trend: str) -> str:
    """Estimate community size based on adoption and trend."""
    if adoption_score >= 90:
        return "Huge"
    elif adoption_score >= 70:
        return "Large" 
    elif adoption_score >= 50:
        return "Medium"
    elif adoption_score >= 30:
        return "Small"
    else:
        return "Niche"

def estimate_learning_curve(tool_name: str, category: str) -> str:
    """Estimate learning curve difficulty."""
    name_lower = tool_name.lower()
    
    # Easy tools
    easy_tools = [
        "vs code", "vscode", "github", "npm", "yarn", "prettier", "jest",
        "react", "vue", "express", "flask", "git", "docker"
    ]
    
    # Steep learning curve tools
    steep_tools = [
        "vim", "neovim", "emacs", "kubernetes", "ansible", "terraform",
        "webpack", "babel", "jenkins", "spring", "angular"
    ]
    
    for tool in easy_tools:
        if tool in name_lower:
            return "Easy"
    
    for tool in steep_tools:
        if tool in name_lower:
            return "Steep"
    
    # Category-based defaults
    if "editor" in category.lower() or "ide" in category.lower():
        return "Moderate"
    elif "testing" in category.lower():
        return "Easy"
    elif "devops" in category.lower() or "infrastructure" in category.lower():
        return "Steep"
    else:
        return "Moderate"

def build_evolution_chains(tools_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Build evolution chains for tool categories."""
    chains = []
    
    for chain_id, chain_info in EVOLUTION_CHAINS.items():
        chain_tools = []
        
        for tool_name in chain_info["chain"]:
            # Try to find the tool in our data
            found_tool = None
            for tool in tools_data:
                if tool_name.lower() in tool["name"].lower() or tool["name"].lower() in tool_name.lower():
                    found_tool = tool
                    break
            
            if found_tool:
                chain_tools.append({
                    "name": found_tool["name"],
                    "year": found_tool["birth_year"],
                    "url": found_tool.get("url", "")
                })
            else:
                # Add with estimated data
                chain_tools.append({
                    "name": tool_name.title(),
                    "year": TOOL_BIRTH_YEARS.get(tool_name, 2000),
                    "url": ""
                })
        
        # Sort by year
        chain_tools.sort(key=lambda x: x["year"])
        
        chains.append({
            "id": chain_id,
            "category": chain_info["category"],
            "description": chain_info["description"],
            "tools": chain_tools
        })
    
    return chains

def generate_predictions() -> List[Dict[str, Any]]:
    """Generate predictions about future tool trends."""
    return [
        {
            "title": "AI-Native Development Environments",
            "description": "IDEs will become AI-first, with natural language interfaces, automated refactoring, and predictive code generation becoming standard. Tools like Cursor and GitHub Copilot are just the beginning.",
            "confidence": 85,
            "timeframe": "2025-2027",
            "impact_areas": ["Productivity", "Code Quality", "Learning Curve"]
        },
        {
            "title": "WebAssembly Revolution",
            "description": "WASM will enable any language to run in browsers efficiently, leading to diverse frontend development ecosystems beyond JavaScript dominance.",
            "confidence": 78, 
            "timeframe": "2024-2026",
            "impact_areas": ["Performance", "Language Diversity", "Browser Capabilities"]
        },
        {
            "title": "Rust-Based Tool Ecosystem",
            "description": "Memory-safe, high-performance tools written in Rust will continue replacing traditional C/C++ and interpreted language tools for better performance and safety.",
            "confidence": 90,
            "timeframe": "2024-2028",
            "impact_areas": ["Performance", "Safety", "Developer Experience"]
        },
        {
            "title": "Edge-First Development",
            "description": "Development tools will optimize for edge computing, with built-in CDN integration, edge functions, and distributed development workflows.",
            "confidence": 70,
            "timeframe": "2025-2028", 
            "impact_areas": ["Performance", "Global Distribution", "Serverless"]
        },
        {
            "title": "Quantum Development Tools",
            "description": "Specialized IDEs and frameworks for quantum computing will emerge as quantum computers become more accessible to developers.",
            "confidence": 45,
            "timeframe": "2028-2035",
            "impact_areas": ["Quantum Computing", "New Programming Paradigms"]
        },
        {
            "title": "No-Code/Low-Code Enterprise",
            "description": "Visual programming environments will handle increasingly complex enterprise applications, reducing the need for traditional coding in many scenarios.",
            "confidence": 65,
            "timeframe": "2025-2030",
            "impact_areas": ["Accessibility", "Development Speed", "Business Logic"]
        },
        {
            "title": "Unified Development Platforms",
            "description": "All-in-one platforms combining coding, testing, deployment, and monitoring will replace tool chains, offering integrated development experiences.",
            "confidence": 55,
            "timeframe": "2026-2030",
            "impact_areas": ["Developer Experience", "Tool Integration", "Productivity"]
        },
        {
            "title": "AI-Powered Code Review and Analysis",
            "description": "Advanced AI will automatically review code, suggest optimizations, detect security vulnerabilities, and enforce coding standards in real-time.",
            "confidence": 88,
            "timeframe": "2024-2026",
            "impact_areas": ["Code Quality", "Security", "Best Practices"]
        }
    ]

def enrich_tool_data(tools_data: Dict[str, Any]) -> Dict[str, Any]:
    """Enrich the tools data with timeline and trend information."""
    enriched_data = {
        "metadata": tools_data["metadata"],
        "eras": {},
        "evolution_chains": [],
        "predictions": generate_predictions(),
        "statistics": {
            "total_tools": 0,
            "tools_by_era": {},
            "tools_by_trend": {"rising": 0, "stable": 0, "declining": 0},
            "average_age": 0,
            "newest_tool_year": 0,
            "oldest_tool_year": 9999
        }
    }
    
    # Initialize eras
    for era_id, era_info in DEVELOPMENT_ERAS.items():
        enriched_data["eras"][era_id] = {
            "id": era_id,
            "title": era_info["title"],
            "period": era_info["period"], 
            "description": era_info["description"],
            "characteristics": era_info["characteristics"],
            "key_innovations": era_info["key_innovations"],
            "tools": []
        }
    
    # Process all tools
    all_tools = []
    birth_years = []
    
    for category in tools_data["categories"]:
        for subcategory in category.get("subcategories", []):
            for tool in subcategory.get("tools", []):
                # Enrich tool data
                birth_year = estimate_tool_birth_year(tool["name"], tool.get("url", ""))
                era = categorize_by_era(birth_year)
                trend = estimate_trend(tool["name"], birth_year)
                adoption_score = estimate_adoption_score(tool["name"], era, trend)
                community_size = estimate_community_size(adoption_score, trend)
                learning_curve = estimate_learning_curve(tool["name"], category["name"])
                
                enriched_tool = {
                    "name": tool["name"],
                    "url": tool.get("url", ""),
                    "description": tool.get("description", ""),
                    "birth_year": birth_year,
                    "era": era,
                    "trend": trend,
                    "category": category["name"],
                    "subcategory": subcategory["name"],
                    "metrics": {
                        "adoption_score": adoption_score,
                        "community_size": community_size,
                        "learning_curve": learning_curve
                    },
                    "github_info": extract_github_info(tool.get("url", ""))
                }
                
                # Add to era
                enriched_data["eras"][era]["tools"].append(enriched_tool)
                all_tools.append(enriched_tool)
                birth_years.append(birth_year)
                
                # Update statistics
                enriched_data["statistics"]["total_tools"] += 1
                enriched_data["statistics"]["tools_by_trend"][trend] += 1
                enriched_data["statistics"]["newest_tool_year"] = max(
                    enriched_data["statistics"]["newest_tool_year"], birth_year
                )
                enriched_data["statistics"]["oldest_tool_year"] = min(
                    enriched_data["statistics"]["oldest_tool_year"], birth_year
                )
    
    # Calculate era statistics
    for era_id, era_data in enriched_data["eras"].items():
        enriched_data["statistics"]["tools_by_era"][era_id] = len(era_data["tools"])
    
    # Calculate average age
    if birth_years:
        enriched_data["statistics"]["average_age"] = round(
            sum(birth_years) / len(birth_years)
        )
    
    # Generate evolution chains
    enriched_data["evolution_chains"] = build_evolution_chains(all_tools)
    
    return enriched_data

def main():
    """Main function to generate timeline data."""
    print("Loading tools data...")
    tools_data = load_tools_data()
    
    print("Enriching with timeline and trend data...")
    enriched_data = enrich_tool_data(tools_data)
    
    # Save enriched data
    output_path = Path(__file__).parent.parent / "tool-timeline-data.json"
    with open(output_path, 'w') as f:
        json.dump(enriched_data, f, indent=2)
    
    print(f"Timeline data generated and saved to {output_path}")
    print(f"Total tools processed: {enriched_data['statistics']['total_tools']}")
    print(f"Tools by era: {enriched_data['statistics']['tools_by_era']}")
    print(f"Tools by trend: {enriched_data['statistics']['tools_by_trend']}")

if __name__ == "__main__":
    main()