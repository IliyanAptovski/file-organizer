# 📄 Changelog

All notable changes to this project will be documented in this file.  
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]
### Planned
- Prepare for Streamlit web interface
- Optional AI-based file categorization
- Packaging as an installable Python package

---

## [0.3.0] - 2025-10-07
### Added
- Robust error handling for invalid paths and empty folders
- Graceful handling of permission errors
- Friendly CLI messages with warnings and success emojis
- Skip non-file items (already organized folders or subdirectories)

### Changed
- Updated CLI output logic to respect --summary and --dry-run flags
- Minor internal refactoring for better readability

---

## [0.2.0] - 2025-10-05
### Added
- `--dry-run` option for safe previews
- `--summary` option for concise output
- `requirements.txt` for dependency tracking
- **Contributing** section in README.md
- Updated testing setup with `pytest`

### Changed
- Improved folder structure and documentation layout

---

## [0.1.0] - 2025-10-02
### Added
- Initial release: CLI tool to organize files by **type** or **date**
- Base project setup with:
  - `README.md`, `.gitignore`, and `LICENSE`
  - `organizer.py` and `utils.py`
  - Initial file organization logic
