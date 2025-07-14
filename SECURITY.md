# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |
| < 0.1   | :x:                |

## Reporting a Vulnerability

The GuardRail AI team takes security bugs seriously. We appreciate your efforts to responsibly disclose your findings, and will make every effort to acknowledge your contributions.

### Where to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to: **security@taifbuilds.com**

### What to Include

Please include the following information in your report:

1. **Description** - A brief description of the vulnerability
2. **Steps to Reproduce** - Detailed steps to reproduce the issue
3. **Impact** - Your assessment of the potential impact
4. **Affected Versions** - Which versions of GuardRail AI are affected
5. **Proof of Concept** - If applicable, include a proof of concept
6. **Suggested Fix** - If you have ideas for how to fix the issue

### Response Timeline

- **Initial Response**: Within 48 hours
- **Status Updates**: Every 5 business days until resolution
- **Resolution**: Target within 90 days for critical issues

### Security Update Process

1. **Confirmation** - We'll confirm the vulnerability and determine severity
2. **Development** - We'll develop and test a fix
3. **Release** - We'll release a security update
4. **Disclosure** - We'll publicly disclose the vulnerability (with credit to reporter if desired)

## Security Best Practices

When using GuardRail AI:

### API Key Security
- Never commit API keys to version control
- Use environment variables or secure secret management
- Rotate API keys regularly
- Use least-privilege access for API keys

### Data Privacy
- Be aware that prompts are sent to LLM providers
- Don't include sensitive data in test prompts
- Review your organization's data handling policies
- Consider using anonymized or synthetic test data

### Infrastructure
- Keep dependencies updated
- Use virtual environments
- Run in isolated environments for CI/CD
- Monitor for unusual API usage patterns

### Responsible Use
- Only test systems you have permission to test
- Don't use actual harmful prompts for testing
- Follow your organization's security policies
- Respect rate limits and terms of service

## Known Security Considerations

1. **API Key Exposure**: Ensure API keys are properly secured
2. **Data Transmission**: Prompts are sent to external LLM APIs
3. **Log Files**: Check that logs don't contain sensitive information
4. **Dependencies**: Keep all dependencies updated

## Security Features

- No storage of API responses containing sensitive data
- Configurable redaction of sensitive information in logs
- Support for proxy configurations
- Rate limiting awareness

## Bug Bounty

We currently do not offer a paid bug bounty program, but we will acknowledge security researchers who report valid vulnerabilities.

## Contact

For security-related questions or concerns:
- Email: security@taifbuilds.com
- For general issues: [GitHub Issues](https://github.com/taifbuilds/GuardRailAI/issues)
