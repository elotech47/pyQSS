#!/usr/bin/env python3
"""
Local test script for cibuildwheel.
This script can be used to test the build process locally.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return success status."""
    print(f"\n🔄 {description}")
    print(f"Running: {cmd}")
    
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - SUCCESS")
        if result.stdout:
            print("STDOUT:", result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return False

def test_local_build():
    """Test local build process."""
    print("🚀 Testing local build process...")
    
    # Check if we're in the right directory
    if not os.path.exists("pyproject.toml"):
        print("❌ Not in the project root directory")
        return False
    
    # Test basic build
    success = True
    
    # Clean previous builds
    success &= run_command("rm -rf dist/ build/", "Cleaning previous builds")
    
    # Test build
    success &= run_command("python -m build", "Building package")
    
    # Test installation
    success &= run_command("pip install dist/*.whl --force-reinstall", "Installing package")
    
    # Test functionality
    success &= run_command("python test_cibuildwheel.py", "Testing functionality")
    
    return success

def test_cibuildwheel_local():
    """Test cibuildwheel locally (if available)."""
    print("\n🚀 Testing cibuildwheel locally...")
    
    # Check if cibuildwheel is available
    try:
        import cibuildwheel
        print("✅ cibuildwheel is available")
    except ImportError:
        print("❌ cibuildwheel not available. Install with: pip install cibuildwheel")
        return False
    
    # Test cibuildwheel
    success = run_command("cibuildwheel --platform linux", "Testing cibuildwheel (Linux)")
    
    return success

def main():
    """Main test function."""
    print("🧪 Local Build Testing")
    print("=" * 50)
    
    # Test basic build
    basic_success = test_local_build()
    
    # Test cibuildwheel if available
    cibuildwheel_success = test_cibuildwheel_local()
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    print(f"Basic Build: {'✅ PASS' if basic_success else '❌ FAIL'}")
    print(f"cibuildwheel: {'✅ PASS' if cibuildwheel_success else '❌ FAIL'}")
    
    if basic_success:
        print("\n🎉 Basic build process works!")
        print("Ready for cibuildwheel deployment!")
    else:
        print("\n❌ Basic build process failed!")
        print("Fix issues before deploying with cibuildwheel")
    
    return 0 if basic_success else 1

if __name__ == "__main__":
    sys.exit(main())
