# Contributing to QSS Integrator

We welcome contributions to the QSS Integrator project! This document provides guidelines for contributing.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/yourusername/qss-integrator.git
   cd qss-integrator
   ```
3. Install the package in development mode:
   ```bash
   pip install -e .[dev]
   ```

## Development Setup

### Prerequisites

- Python 3.7 or higher
- C++ compiler with C++17 support
- CMake (for building from source)

### Building from Source

```bash
# Install build dependencies
pip install pybind11 numpy

# Build the package
python setup.py build_ext --inplace
```

## Code Style

We use the following tools for code formatting and linting:

- **Black**: Code formatting
- **Flake8**: Linting
- **MyPy**: Type checking

Run the formatting tools before submitting:

```bash
black qss_integrator/ tests/ examples/
flake8 qss_integrator/ tests/ examples/
mypy qss_integrator/
```

## Testing

We use pytest for testing. Run the test suite:

```bash
pytest tests/
```

### Writing Tests

- Place tests in the `tests/` directory
- Use descriptive test names
- Test both success and failure cases
- Include docstrings for test functions

Example:
```python
def test_integrator_creation():
    """Test that integrator can be created."""
    integrator = QssIntegrator()
    assert integrator is not None
```

## Documentation

- Update docstrings for any new functions or classes
- Add examples to the `examples/` directory
- Update the README.md if adding new features

## Submitting Changes

1. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and commit them:
   ```bash
   git add .
   git commit -m "Add your feature"
   ```

3. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request on GitHub

## Pull Request Guidelines

- Provide a clear description of the changes
- Include tests for new functionality
- Ensure all tests pass
- Update documentation as needed
- Keep PRs focused on a single feature or bugfix

## Reporting Issues

When reporting issues, please include:

- Python version
- Operating system
- Steps to reproduce the issue
- Expected vs. actual behavior
- Any error messages or stack traces

## Questions?

Feel free to open an issue or start a discussion on GitHub if you have questions about contributing.
