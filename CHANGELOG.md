# Changelog

All notable changes to GuardRail AI will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial public release
- Support for OpenAI and Hugging Face adapters
- 40+ jailbreak and EU AI Act compliance prompts
- HTML and JSON reporting capabilities
- CI/CD integration with threshold-based gating
- Docker support
- Comprehensive documentation

### Security
- OpenAI moderation API integration
- Secure API key handling
- No sensitive data logging

## [0.1.0] - 2024-01-XX

### Added
- Initial release of GuardRail AI
- Core evaluation engine
- CLI interface with Typer
- Multi-provider LLM support
- Configurable prompt sets and policies
- Threshold-based pass/fail logic
- HTML report generation with Jinja2
- GitHub Actions CI/CD workflow
- Comprehensive test suite

### Features
- **CLI Commands**:
  - `test` - Single prompt testing
  - `evaluate` - Full evaluation suite
  - `version` - Version information
- **Supported Providers**:
  - OpenAI (GPT-3.5, GPT-4)
  - Hugging Face (Inference API)
- **Report Formats**:
  - JSON (machine-readable)
  - HTML (human-readable dashboard)
- **Configuration**:
  - YAML-based prompt sets
  - Policy definitions
  - Configurable thresholds

### Documentation
- Comprehensive README.md
- Contributing guidelines
- Docker setup instructions
- CI/CD integration examples

---

## Release Types

- **Major**: Breaking changes, new major features
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes, documentation updates

## Support

For questions about releases or to report issues:
- [GitHub Issues](https://github.com/taifbuilds/GuardRailAI/issues)
- [GitHub Discussions](https://github.com/taifbuilds/GuardRailAI/discussions)
