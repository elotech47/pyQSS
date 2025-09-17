#!/usr/bin/env python3
"""
Improved release script for QSS Integrator.
This script creates a GitHub release which will trigger the build-wheels workflow.
"""

import argparse
import subprocess
import sys
from pathlib import Path
import re
import json

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

def update_version_files(new_version):
    """Update version in all relevant files"""
    # Update pyproject.toml
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    content = re.sub(r'version = "[^"]+"', f'version = "{new_version}"', content)
    pyproject_path.write_text(content)
    
    # Update __init__.py
    init_path = Path("qss_integrator/__init__.py")
    if init_path.exists():
        content = init_path.read_text()
        content = re.sub(r'__version__ = "[^"]+"', f'__version__ = "{new_version}"', content)
        init_path.write_text(content)
    
    print(f"Updated version to {new_version}")

def run_command(cmd, check=True, capture_output=False):
    """Run a shell command"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=capture_output, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr if capture_output else 'Command failed'}")
        sys.exit(1)
    return result

def create_github_release(version, dry_run=False):
    """Create a GitHub release using gh CLI"""
    tag_name = f"v{version}"
    
    # Check if gh CLI is available
    result = run_command("gh --version", check=False, capture_output=True)
    if result.returncode != 0:
        print("GitHub CLI (gh) not found. Please install it or create the release manually.")
        print(f"Manual steps:")
        print(f"1. Go to https://github.com/elotech47/pyQSS/releases/new")
        print(f"2. Create tag: {tag_name}")
        print(f"3. Set title: Release {version}")
        print(f"4. Add release notes")
        print(f"5. Publish release")
        return False
    
    if dry_run:
        print(f"Would create GitHub release: {tag_name}")
        return True
    
    # Create release
    release_notes = f"""# Release {version}

## Changes
- Version bump to {version}
- See CHANGELOG.md for detailed changes

## Installation
```bash
pip install qss-integrator=={version}
```

## Wheels
This release includes pre-built wheels for:
- Python 3.8-3.12
- Linux (x86_64)
- macOS (x86_64, arm64)  
- Windows (x86_64)
"""
    
    # Write release notes to temp file
    notes_file = Path("release_notes.md")
    notes_file.write_text(release_notes)
    
    try:
        run_command(f'gh release create {tag_name} --title "Release {version}" --notes-file release_notes.md')
        print(f"✅ GitHub release {tag_name} created successfully!")
        return True
    finally:
        if notes_file.exists():
            notes_file.unlink()

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
            create_github_release(new_version, dry_run=True)
            return
        
        # Update version files
        update_version_files(new_version)
        
        # Commit changes
        run_command("git add .")
        run_command(f"git commit -m 'Bump version to {new_version}'")
        run_command("git push origin main")
        
        # Create GitHub release (this will trigger the workflow)
        if create_github_release(new_version):
            print(f"\n✅ Release process completed successfully!")
            print(f"Release: v{new_version}")
            print("GitHub Actions will now build and publish the package.")
            print("Check: https://github.com/elotech47/pyQSS/actions")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()#!/usr/bin/env python3
"""
Improved release script for QSS Integrator.
This script creates a GitHub release which will trigger the build-wheels workflow.
"""

import argparse
import subprocess
import sys
from pathlib import Path
import re
import json

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

def update_version_files(new_version):
    """Update version in all relevant files"""
    # Update pyproject.toml
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    content = re.sub(r'version = "[^"]+"', f'version = "{new_version}"', content)
    pyproject_path.write_text(content)
    
    # Update __init__.py
    init_path = Path("qss_integrator/__init__.py")
    if init_path.exists():
        content = init_path.read_text()
        content = re.sub(r'__version__ = "[^"]+"', f'__version__ = "{new_version}"', content)
        init_path.write_text(content)
    
    print(f"Updated version to {new_version}")

def run_command(cmd, check=True, capture_output=False):
    """Run a shell command"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=capture_output, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr if capture_output else 'Command failed'}")
        sys.exit(1)
    return result

def create_github_release(version, dry_run=False):
    """Create a GitHub release using gh CLI"""
    tag_name = f"v{version}"
    
    # Check if gh CLI is available
    result = run_command("gh --version", check=False, capture_output=True)
    if result.returncode != 0:
        print("GitHub CLI (gh) not found. Please install it or create the release manually.")
        print(f"Manual steps:")
        print(f"1. Go to https://github.com/elotech47/pyQSS/releases/new")
        print(f"2. Create tag: {tag_name}")
        print(f"3. Set title: Release {version}")
        print(f"4. Add release notes")
        print(f"5. Publish release")
        return False
    
    if dry_run:
        print(f"Would create GitHub release: {tag_name}")
        return True
    
    # Create release
    release_notes = f"""# Release {version}

## Changes
- Version bump to {version}
- See CHANGELOG.md for detailed changes

## Installation
```bash
pip install qss-integrator=={version}
```

## Wheels
This release includes pre-built wheels for:
- Python 3.8-3.12
- Linux (x86_64)
- macOS (x86_64, arm64)  
- Windows (x86_64)
"""
    
    # Write release notes to temp file
    notes_file = Path("release_notes.md")
    notes_file.write_text(release_notes)
    
    try:
        run_command(f'gh release create {tag_name} --title "Release {version}" --notes-file release_notes.md')
        print(f"✅ GitHub release {tag_name} created successfully!")
        return True
    finally:
        if notes_file.exists():
            notes_file.unlink()

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
            create_github_release(new_version, dry_run=True)
            return
        
        # Update version files
        update_version_files(new_version)
        
        # Commit changes
        run_command("git add .")
        run_command(f"git commit -m 'Bump version to {new_version}'")
        run_command("git push origin main")
        
        # Create GitHub release (this will trigger the workflow)
        if create_github_release(new_version):
            print(f"\n✅ Release process completed successfully!")
            print(f"Release: v{new_version}")
            print("GitHub Actions will now build and publish the package.")
            print("Check: https://github.com/elotech47/pyQSS/actions")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()