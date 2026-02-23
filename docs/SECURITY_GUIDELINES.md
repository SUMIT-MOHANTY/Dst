# AI Security Guidelines

1. **Input Validation**: All user inputs must pass `sanitize_input`.
2. **Output Sanitization**: Enable `sanitize_output` for PII redaction.
3. **Testing**: Run `pytest` before every deployment.
4. **Monitoring**: Log all blocked injection attempts.
