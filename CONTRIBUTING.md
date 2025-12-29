# Contributing to UET Harness

Thank you for your interest in contributing! 🎉

## Ways to Contribute

### 🐛 Report Bugs
- Open an issue with:
  - Description of the bug
  - Steps to reproduce
  - Expected vs actual behavior
  - Python version and OS

### 📝 Documentation
- Improve README, docstrings, or tutorials
- Add examples for new use cases
- Fix typos or clarify explanations

### 🔬 Add Physics Tests
- Propose new validation tests
- Add real data comparisons
- Extend to new physics domains

### 🚀 Code Improvements
- Performance optimizations
- Bug fixes
- New features (discuss first in an issue)

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/uet-harness.git
cd uet-harness

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install in development mode
pip install -e ".[dev]"

# Run tests
python research/run_unified_tests.py
```

## Pull Request Process

1. **Fork** the repository
2. **Create a branch** (`git checkout -b feature/amazing-feature`)
3. **Make changes** and add tests
4. **Run tests** (`python research/run_unified_tests.py`)
5. **Commit** (`git commit -m 'Add amazing feature'`)
6. **Push** (`git push origin feature/amazing-feature`)
7. **Open a Pull Request**

## Code Style

- Follow PEP 8
- Add type hints
- Write docstrings (Google style)
- Keep functions focused and small

## Questions?

Open an issue or start a discussion!

---

*Thank you for helping make UET better!*
