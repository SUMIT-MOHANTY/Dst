# Setup Instructions

## Prerequisites
- Python 3.9+
- PostgreSQL 13+

## Installation
1. Clone the repository.
2. Install dependencies: \`pip install -r requirements.txt\`
3. Configure environment variables in \`.env\`.
4. Run migrations: \`python manage.py migrate\`
5. Start server: \`python manage.py runserver\`

## Troubleshooting
Ensure ports 5432 (DB) and 8000 (App) are available.
