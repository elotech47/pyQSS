# GitHub Actions Setup Guide

This guide explains how to set up the CI/CD pipeline for automatic testing and publishing.

## Required GitHub Secrets

To enable automatic publishing, you need to add the following secrets to your GitHub repository:

### 1. Go to Repository Settings
- Navigate to your GitHub repository
- Click on "Settings" tab
- Click on "Secrets and variables" → "Actions"

### 2. Add Required Secrets

#### `TESTPYPI_API_TOKEN`
- Go to https://test.pypi.org/manage/account/token/
- Create a new API token with scope "Entire account"
- Copy the token (starts with `pypi-`)
- Add it as a secret named `TESTPYPI_API_TOKEN`

#### `PYPI_API_TOKEN`
- Go to https://pypi.org/manage/account/token/
- Create a new API token with scope "Entire account"
- Copy the token (starts with `pypi-`)
- Add it as a secret named `PYPI_API_TOKEN`

## Workflow Triggers

### Automatic Testing
- **Push to main/develop**: Runs tests on all Python versions
- **Pull requests**: Runs tests and code quality checks

### TestPyPI Publishing
- **Push to main branch**: Automatically publishes to TestPyPI

### PyPI Publishing
- **Create GitHub Release**: Automatically publishes to PyPI

## Creating Releases

### Method 1: GitHub Web Interface
1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Choose a tag (e.g., `v0.1.0`)
4. Write release notes
5. Click "Publish release"

### Method 2: Command Line
```bash
# Create and push a tag
git tag v0.1.0
git push origin v0.1.0

# This will trigger the release workflow
```

## Workflow Features

- **Multi-platform testing**: Ubuntu, Windows, macOS
- **Multi-version testing**: Python 3.7-3.12
- **Code quality checks**: Black, Flake8, MyPy
- **Security scanning**: Bandit, Safety
- **Coverage reporting**: Codecov integration
- **Automatic publishing**: TestPyPI and PyPI

## Troubleshooting

### Common Issues

1. **Build failures**: Check that all dependencies are properly specified
2. **Test failures**: Ensure tests pass locally before pushing
3. **Publishing failures**: Verify API tokens are correct and have proper permissions

### Getting Help

- Check the Actions tab in your GitHub repository for detailed logs
- Review the workflow files in `.github/workflows/`
- Open an issue if you encounter problems
