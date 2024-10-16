import requests

# Configuration
GITLAB_URL = 'https://gitlab.com'  # Change to your GitLab instance URL if self-hosted
ACCESS_TOKEN = ''  # Replace with your GitLab Personal Access Token

# API endpoint to get namespaces
url = f'{GITLAB_URL}/api/v4/namespaces'

# Headers for authentication
headers = {
    'Private-Token': ACCESS_TOKEN,
    'Content-Type': 'application/json',
}

# Fetch namespaces
response = requests.get(url, headers=headers)
if response.status_code == 200:
    namespaces = response.json()
    for namespace in namespaces:
        print(f"ID: {namespace['id']}, Name: {namespace['name']}")
else:
    print('Failed to fetch namespaces.')
    print('Status code:', response.status_code)
    print('Response:', response.json())
