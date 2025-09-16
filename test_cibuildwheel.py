#!/usr/bin/env python3
"""
Test script for cibuildwheel builds.
This script tests the basic functionality of the QSS integrator.
"""

import sys
import numpy as np

def test_basic_import():
    """Test basic import functionality."""
    try:
        import qss_integrator
        print("✅ qss_integrator imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import qss_integrator: {e}")
        return False

def test_class_import():
    """Test class import functionality."""
    try:
        from qss_integrator import QssIntegrator, QssOde, PyQssOde
        print("✅ QssIntegrator classes imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Failed to import QssIntegrator classes: {e}")
        return False

def test_basic_functionality():
    """Test basic functionality."""
    try:
        # Debug: Check where qss_integrator is being imported from
        import qss_integrator
        print(f"qss_integrator location: {qss_integrator.__file__}")
        
        # Try to import the classes
        from qss_integrator import QssIntegrator, PyQssOde
        
        # Create a simple test ODE
        def simple_ode(t, y, corrector=False):
            # Simple exponential decay: dy/dt = -y
            dydt = -y[0]
            return [dydt], [0.0]  # q, d as separate lists
        
        # Create integrator
        integrator = QssIntegrator()
        ode = PyQssOde(simple_ode)
        integrator.setOde(ode)
        
        # Set initial conditions
        y0 = [1.0]  # Initial value
        integrator.setState(y0, 0.0)
        
        # Just check if we can access the state
        print(f"✅ Integrator created successfully")
        print(f"   Current time: {integrator.tn}")
        print(f"   Current state: {integrator.y}")
        
        print("✅ Basic functionality test passed")
        return True
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("Running cibuildwheel tests...")
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    
    tests = [
        test_basic_import,
        test_class_import,
        test_basic_functionality
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())
