import requests

# Configuration
GITLAB_URL = 'https://gitlab.com'
ACCESS_TOKEN = ''  # Replace with your GitLab Personal Access Token

# API endpoint to get groups
url = f'{GITLAB_URL}/api/v4/groups'

# Headers for authentication
headers = {
    'Private-Token': ACCESS_TOKEN,
    'Content-Type': 'application/json',
}

# Fetch groups
response = requests.get(url, headers=headers)
if response.status_code == 200:
    groups = response.json()
    for group in groups:
        print(f"ID: {group['id']}, Name: {group['name']}, Path: {group['path']}")
else:
    print('Failed to fetch groups.')
    print('Status code:', response.status_code)
    print('Response:', response.json())
