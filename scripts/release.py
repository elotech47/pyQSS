#!/usr/bin/env python3
"""
Release script for QSS Integrator.

This script helps create proper releases with version bumping and changelog generation.
"""

import argparse
import subprocess
import sys
from pathlib import Path
import re

def get_current_version():
    """Get current version from pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        raise FileNotFoundError("pyproject.toml not found")
    
    content = pyproject_path.read_text()
    match = re.search(r'version = "([^"]+)"', content)
    if not match:
        raise ValueError("Version not found in pyproject.toml")
    
    return match.group(1)

def bump_version(version, bump_type):
    """Bump version number"""
    parts = version.split('.')
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    
    if bump_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif bump_type == 'minor':
        minor += 1
        patch = 0
    elif bump_type == 'patch':
        patch += 1
    else:
        raise ValueError(f"Invalid bump type: {bump_type}")
    
    return f"{major}.{minor}.{patch}"

def update_version(new_version):
    """Update version in pyproject.toml"""
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    
    # Update version
    content = re.sub(
        r'version = "[^"]+"',
        f'version = "{new_version}"',
        content
    )
    
    pyproject_path.write_text(content)
    print(f"Updated version to {new_version}")

def run_command(cmd, check=True):
    """Run a shell command"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
    return result

def main():
    parser = argparse.ArgumentParser(description="Release QSS Integrator")
    parser.add_argument("bump_type", choices=["major", "minor", "patch"], 
                       help="Type of version bump")
    parser.add_argument("--dry-run", action="store_true", 
                       help="Show what would be done without executing")
    
    args = parser.parse_args()
    
    try:
        current_version = get_current_version()
        new_version = bump_version(current_version, args.bump_type)
        
        print(f"Current version: {current_version}")
        print(f"New version: {new_version}")
        
        if args.dry_run:
            print("Dry run - no changes made")
            return
        
        # Update version
        update_version(new_version)
        
        # Commit changes
        run_command("git add pyproject.toml")
        run_command(f"git commit -m 'Bump version to {new_version}'")
        
        # Create tag
        tag_name = f"v{new_version}"
        run_command(f"git tag {tag_name}")
        
        # Push changes
        run_command("git push origin main")
        run_command(f"git push origin {tag_name}")
        
        print(f"\n✅ Release {new_version} created successfully!")
        print(f"Tag: {tag_name}")
        print("GitHub Actions will now build and publish the package.")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
