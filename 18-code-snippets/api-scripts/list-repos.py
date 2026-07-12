import requests
token = 'your_github_token'
headers = {'Authorization': f'token {token}'}
response = requests.get('https://api.github.com/user/repos', headers=headers)
for repo in response.json():
    print(repo['full_name'])