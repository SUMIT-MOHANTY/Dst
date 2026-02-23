import json

def validate_portfolio(portfolio_data, requirements):
    errors = []
    # Check role
    if portfolio_data.get('role') != requirements['role']:
        errors.append(f"Role mismatch: {portfolio_data.get('role')} != {requirements['role']}")
    # Check sections
    for section in requirements['required_sections']:
        if section not in portfolio_data.get('sections', []):
            errors.append(f"Missing section: {section}")
    return errors

if __name__ == '__main__':
    with open('portfolio_data.json') as f, open('../content/requirements_manifest.json') as r:
        p_data = json.load(f)
        reqs = json.load(r)
    issues = validate_portfolio(p_data, reqs)
    print(f"Validation Complete. Issues found: {len(issues)}")
    for issue in issues:
        print(issue)
