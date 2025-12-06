# Contributing to SE Asia Tectonic Animation

First off, thank you for considering contributing to this project! 🎉

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Describe the behavior you observed and what you expected**
- **Include screenshots or GIFs if applicable**
- **Include your environment details:**
  - OS (Windows, macOS, Linux)
  - Python version
  - GPlately version
  - Cartopy version

### Suggesting Enhancements

Enhancement suggestions are welcome! Please provide:

- **A clear and descriptive title**
- **A detailed description of the proposed enhancement**
- **Explain why this enhancement would be useful**
- **List any alternative solutions you've considered**

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Install development dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Make your changes** and ensure they work correctly
4. **Test your changes** with different time ranges and extents
5. **Update documentation** if needed
6. **Submit your pull request**

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Include docstrings for functions

## Adding New Features

### New Plate Models

To add support for a new plate model:

1. Check if the model is available in GPlately's DataServer
2. Test the model with your desired time range
3. Update the documentation with the new model option

### New Visualization Options

When adding new visualization features:

1. Use GPlately's built-in plotting methods when possible
2. Ensure the feature works across different time ranges
3. Add appropriate legend entries
4. Document the new feature in the README

## Questions?

Feel free to open an issue with your question or contact the maintainer directly.

Thank you for contributing! 🌏
