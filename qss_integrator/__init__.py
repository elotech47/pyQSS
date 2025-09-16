"""
QSS Integrator: Quasi-Steady State method for stiff ODE systems.

This package provides efficient numerical integration for stiff ordinary
differential equations using the Quasi-Steady State method, with particular
focus on combustion chemistry applications.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# Import the compiled extension
try:
    from .qss_py import QssIntegrator, QssOde, PyQssOde

    __all__ = ["QssIntegrator", "QssOde", "PyQssOde"]
except ImportError:
    # Handle case where C++ extension is not built
    import warnings

    warnings.warn(
        "QSS C++ extension not found. Please build the package first.", ImportWarning
    )
    __all__ = []
