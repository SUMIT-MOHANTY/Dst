# Analytics Configuration
ANALYTICS_CONFIG = {
    'enabled': True,
    'consent_required': True,
    'data_retention_days': 90,
    'anonymize_ip': True,
    'respect_dnt': True,
    'sample_rate': 1.0,
    'batch_size': 50,
    'flush_interval_seconds': 30,
    'allowed_events': ['pageview', 'click', 'scroll', 'form_submit'],
    'blocked_paths': ['/login', '/admin', '/account'],
    'sensitive_params': ['password', 'ssn', 'credit_card', 'token']
}
