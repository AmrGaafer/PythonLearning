# resource: https://www.nylas.com/blog/use-python-requests-module-rest-apis/
import requests

# Define the GitHub user you want to retrieve data data for
BASE_URL = 'https://api.github.com/users/'
user_name = 'AmrGaafer'

# Construct the API request URL with the city name and API key
url = f"{BASE_URL}?q={user_name}"

# Send a GET request to retrieve weather data
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Access the response data in JSON format
    data = response.json()
    
else:
    # If the request was not successful, print the error message
    print(f"Error: {response.status_code} - {response.text}")