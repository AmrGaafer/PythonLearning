import requests

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = 'b1cfe81b892f6e6b77e3912ebf4913e5'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Define the city you want to retrieve weather data for
city_name = 'Munich'

# Construct the API request URL with the city name and API key
url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"

# Send a GET request to retrieve weather data
response = requests.get(url)

# Check if the request was successful (status code 200 indicates success)
if response.status_code == 200:
    # Access the response data in JSON format
    data = response.json()

    # Extract relevant information from the response
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']

    # Print the weather information
    print(f"Weather in {city_name}:")
    print(f"Temperature: {temperature} K")
    print(f"Description: {weather_description}")
else:
    # If the request was not successful, print the error message
    print(f"Error: {response.status_code} - {response.text}")