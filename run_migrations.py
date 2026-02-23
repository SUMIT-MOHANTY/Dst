import subprocess
import sys

print('Running Alembic migrations...')

try:
    subprocess.run([sys.executable, '-m', 'alembic', 'revision', '--autogenerate', '-m', 'Initial migration'], check=True)
    print('Migration generated successfully!')
except subprocess.CalledProcessError as e:
    print(f'Error generating migration: {e}')

try:
    subprocess.run([sys.executable, '-m', 'alembic', 'upgrade', 'head'], check=True)
    print('Migrations applied successfully!')
except subprocess.CalledProcessError as e:
    print(f'Error applying migration: {e}')
