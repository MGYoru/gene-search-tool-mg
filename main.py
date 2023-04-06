import requests
import json

# Define the API endpoint and parameters
endpoint = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "prop": "extracts",
    "titles": "Python (programming language)",
    "exsectionformat": "wiki",
    "explaintext": True,
    "redirects": True
}

# Make the API request and parse the JSON response
response = requests.get(endpoint, params=params)
data = json.loads(response.text)

# Extract the article content from the response
page = next(iter(data['query']['pages'].values()))
content = page['extract']

# Print the content
print(content)
#In this example, the script retrieves the content of the Wikipedia page for the Python programming language and prints it to the console. You can modify the titles parameter to retrieve content for a different Wikipedia page. Additionally, you can modify the prop parameter to retrieve different types of data from the API, such as images or categories.