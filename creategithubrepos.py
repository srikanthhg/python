# before run this
# pip install requests
# python -c "import requests; print(requests.__version__)"  #verify installation
# Use 'import gitlab' when you want a straightforward way to interact with Gitlab and leverage its built-in features
# Use 'import requests' if you need more control over your http requests or if you are working with multiple APIs
# Both approaches are valid; the choice depends on your specific needs and preferences!

import requests

# Configuration
GITLAB_URL = 'https://gitlab.com'  # Change to your GitLab instance URL if self-hosted
ACCESS_TOKEN = ''  # Replace with your GitLab Personal Access Token
NAMESPACE_ID = 92684201
# List of projects to create
projects = [
    {
        'name': 'frontend',
        'description': 'This is project one.',
        'visibility': 'private'  # Options: 'private', 'internal', 'public'
    },
    {
        'name': 'productcatalogservice',
        'description': 'This is project two.',
        'visibility': 'private'
    },
    {
        'name': 'checkoutservice',
        'description': 'This is project three.',
        'visibility': 'private'
    },
    {
        'name': 'shippingservice',
        'description': 'This is project three.',
        'visibility': 'private'
    },
    {
        'name': 'adservice',
        'description': 'This is project three.',
        'visibility': 'private'
    },
    {
        'name': 'cartservice',
        'description': 'This is project three.',
        'visibility': 'private'
    },
    {
        'name': 'currencyservice',
        'description': 'This is project three.',
        'visibility': 'private'
    },
    {
        'name': 'emailservice',
        'description': 'This is project three.',
        'visibility': 'private'
    },
    {
        'name': 'paymentservice',
        'description': 'This is project three.',
        'visibility': 'private'
    },
    {
        'name': 'recommendationservice',
        'description': 'This is project three.',
        'visibility': 'private'
    }

]

# API endpoint
url = f'{GITLAB_URL}/api/v4/projects'
#url = f'{GITLAB_URL}/api/v4/groups'

# Headers for authentication
headers = {
    'Private-Token': ACCESS_TOKEN,
    'Content-Type': 'application/json',
}

def create_project(project_data):
    project_data['namespace_id'] = NAMESPACE_ID
    response = requests.post(url, headers=headers, json=project_data)
    return response

def main():
    for project in projects:
        print(f"Creating project: {project['name']}")
        response = create_project(project)
        if response.status_code == 201:
            print('Project created successfully!')
            print('Project URL:', response.json().get('web_url'))
        else:
            print('Failed to create project.')
            print('Status code:', response.status_code)
            print('Response:', response.json())
        print()

if __name__ == "__main__":
    main()
