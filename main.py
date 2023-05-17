import requests

# Replace with your own GitHub personal access token
TOKEN = '<GITHUB_TOKEN>'

# Set the API endpoint URL for webhook events on a specific repository
repo_name = '<GITHUB_ORG>/<REPO_NAME>'
url = f'https://api.github.com/repos/{repo_name}/events'

# Set the headers to include your personal access token
headers = {'Authorization': f'token {TOKEN}'}

# Set the query parameters to filter events related to pull request merges
params = {'event_type': 'pull_request', 'action': 'closed', 'pull_request': {'merged': True}}

# Send the API request to retrieve relevant webhook events
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON data
    events = response.json()

    # Loop through the events and extract the username of the user who merged the pull request
    for event in events:
        
        if event['type'] == 'PullRequestEvent' and event['payload']['action'] == 'closed' and event['payload']['pull_request']['merged'] and event['payload']['pull_request']['merged_by']['login']:
            print(event['repo']['name'])
            print(event['payload']['number'])
            print(event['payload']['pull_request']['html_url'])
            print(event['payload']['pull_request']['head']['ref'])
            print(event['payload']['pull_request']['base']['ref'])
            print(event['payload']['action'])
            print(event['payload']['pull_request']['user']['login'])
            print(event['payload']['pull_request']['merged_by']['login'])
            print('=======')
            # print(f"Username of user who merged pull request: {username}")
else:
    print(f"Error retrieving webhook events: {response.status_code}")