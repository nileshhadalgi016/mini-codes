# This is a basic google search engine using python

import requests
import webbrowser

# Get the query string from the user
query_string = input("Enter your search query: ")

# Create the request URL
url = "https://www.google.com/search?q=" + query_string

# Make the request
response = requests.get(url)

# Parse the response and open the first search result
if response.status_code == 200:
    webbrowser.open_new_tab(response.url)
else:
    print("Error: Unable to access the search engine.")