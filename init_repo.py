import os
import subprocess

def run_cmd(command):
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)

def main():
    os.chdir('/workspace')
    if not os.path.exists('.git'):
        print('Initializing Repository...')
        run_cmd('git init')
        run_cmd('git config user.email "security-bot@local.ai"')
        run_cmd('git config user.name "Security Bot"')
        run_cmd('git checkout -b main')
        run_cmd('git add .')
        run_cmd('git commit -m "Initial commit: Security compliance setup"')
    else:
        print('Repository already initialized.')

if __name__ == '__main__':
    try:
        main()
        print('SUCCESS: Git structure initialized.')
    except Exception as e:
        print(f'ERROR: {e}')
        sys.exit(1)
