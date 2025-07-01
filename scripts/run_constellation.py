#!/usr/bin/env python3
"""
Tool Constellation Runner

This script automates the process of generating constellation data and 
optionally serving the visualization locally for development/demo purposes.
"""

import subprocess
import sys
import webbrowser
import time
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import argparse


class ConstellationRunner:
    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.constellation_data_path = repo_root / 'constellation-data.json'
        self.html_path = repo_root / 'tool-constellation.html'
        
    def generate_constellation_data(self) -> bool:
        """Generate constellation data from tools.yaml"""
        print("🌌 Generating Tool Constellation Data...")
        
        try:
            script_path = self.repo_root / 'scripts' / 'constellation_processor.py'
            result = subprocess.run([
                sys.executable, str(script_path)
            ], cwd=self.repo_root, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Constellation data generated successfully!")
                print(result.stdout)
                return True
            else:
                print("❌ Failed to generate constellation data:")
                print(result.stderr)
                return False
                
        except Exception as e:
            print(f"❌ Error running constellation processor: {e}")
            return False
    
    def verify_files(self) -> bool:
        """Verify that required files exist"""
        required_files = [
            self.constellation_data_path,
            self.html_path
        ]
        
        missing_files = []
        for file_path in required_files:
            if not file_path.exists():
                missing_files.append(str(file_path))
        
        if missing_files:
            print("❌ Missing required files:")
            for file_path in missing_files:
                print(f"   - {file_path}")
            return False
        
        print("✅ All required files present")
        return True
    
    def serve_locally(self, port: int = 8000, open_browser: bool = True):
        """Serve the constellation locally using Python's built-in server"""
        if not self.verify_files():
            return False
        
        print(f"🚀 Starting local server on port {port}...")
        print(f"📂 Serving from: {self.repo_root}")
        
        # Change to repo directory for serving
        import os
        original_cwd = os.getcwd()
        os.chdir(self.repo_root)
        
        try:
            class CustomHandler(SimpleHTTPRequestHandler):
                def log_message(self, format, *args):
                    # Suppress default request logging
                    pass
                
                def end_headers(self):
                    # Add CORS headers for local development
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
                    self.send_header('Access-Control-Allow-Headers', 'Content-Type')
                    super().end_headers()
            
            server = HTTPServer(('localhost', port), CustomHandler)
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.daemon = True
            server_thread.start()
            
            constellation_url = f"http://localhost:{port}/tool-constellation.html"
            print(f"🌟 Tool Constellation available at: {constellation_url}")
            
            if open_browser:
                print("🌐 Opening in default browser...")
                time.sleep(1)  # Give server time to start
                webbrowser.open(constellation_url)
            
            print("\n" + "="*60)
            print("🌌 TOOL CONSTELLATION IS RUNNING!")
            print("="*60)
            print(f"URL: {constellation_url}")
            print("Press Ctrl+C to stop the server")
            print("="*60)
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n🛑 Shutting down server...")
                server.shutdown()
                server.server_close()
                
        except OSError as e:
            if "Address already in use" in str(e):
                print(f"❌ Port {port} is already in use. Try a different port with --port")
                return False
            else:
                print(f"❌ Server error: {e}")
                return False
        finally:
            os.chdir(original_cwd)
        
        return True
    
    def print_status(self):
        """Print current status of constellation files"""
        print("📊 Tool Constellation Status")
        print("="*40)
        
        # Check constellation data
        if self.constellation_data_path.exists():
            try:
                import json
                with open(self.constellation_data_path, 'r') as f:
                    data = json.load(f)
                
                print(f"✅ Constellation Data: {self.constellation_data_path}")
                print(f"   📊 Tools: {data['metadata']['tool_count']}")
                print(f"   📂 Categories: {data['metadata']['category_count']}")
                print(f"   🛤️  Skill Paths: {len(data.get('skill_paths', []))}")
                
            except Exception as e:
                print(f"⚠️  Constellation Data: Exists but corrupted ({e})")
        else:
            print(f"❌ Constellation Data: Not found")
        
        # Check HTML file
        if self.html_path.exists():
            print(f"✅ Visualization: {self.html_path}")
        else:
            print(f"❌ Visualization: Not found")
        
        # Check source data
        tools_yaml = self.repo_root / 'data' / 'tools.yaml'
        if tools_yaml.exists():
            print(f"✅ Source Data: {tools_yaml}")
        else:
            print(f"❌ Source Data: Not found")


def main():
    parser = argparse.ArgumentParser(
        description='Tool Constellation Runner',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/run_constellation.py --generate     # Generate data only
  python scripts/run_constellation.py --serve       # Serve with existing data  
  python scripts/run_constellation.py --full        # Generate data and serve
  python scripts/run_constellation.py --status      # Show current status
        """
    )
    
    parser.add_argument('--generate', action='store_true',
                       help='Generate constellation data from tools.yaml')
    parser.add_argument('--serve', action='store_true',
                       help='Serve the constellation locally')
    parser.add_argument('--full', action='store_true',
                       help='Generate data and serve (default)')
    parser.add_argument('--status', action='store_true',
                       help='Show current status of constellation files')
    parser.add_argument('--port', type=int, default=8000,
                       help='Port for local server (default: 8000)')
    parser.add_argument('--no-browser', action='store_true',
                       help='Don\'t open browser automatically')
    
    args = parser.parse_args()
    
    # Determine repo root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    
    runner = ConstellationRunner(repo_root)
    
    # If no specific action is chosen, default to full
    if not any([args.generate, args.serve, args.status]):
        args.full = True
    
    success = True
    
    if args.status:
        runner.print_status()
        return 0
    
    if args.generate or args.full:
        success = runner.generate_constellation_data()
    
    if success and (args.serve or args.full):
        success = runner.serve_locally(
            port=args.port, 
            open_browser=not args.no_browser
        )
    
    return 0 if success else 1


if __name__ == '__main__':
    exit(main())