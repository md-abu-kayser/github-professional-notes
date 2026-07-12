import requests

# Provide my GitHub token and repository details
token = 'py_github_token'
owner = 'py_github_project'  # my GitHub username
repo = 'my-new-awesome-repo'     # The repository where i want to create the issue

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github+json'
}

# The data for the new issue
issue_data = {
    'title': 'Found a bug in the authentication code', # Title of the issue
    'body': 'The app crashes whenever a user tries to log in. This needs to be fixed ASAP.', # Description
    'labels': ['bug', 'critical'] # GitHub labels
}

# Send the POST request to the GitHub API
url = f'https://api.github.com/repos/{owner}/{repo}/issues'
response = requests.post(url, headers=headers, json=issue_data)

# Check the response status
if response.status_code == 201:
    print(f"Issue created successfully! URL: {response.json()['html_url']}")
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.json())