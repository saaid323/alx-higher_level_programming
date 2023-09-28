#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.

# Send a GET request to the target URL and save the HTML content to a file
curl -s -o webpage.html http://0.0.0.0:5000/catch_me

# Use grep and sed to extract the URL from the HTML content
redirect_url=$(grep -o '<a href="/[^"]*' webpage.html | sed 's/<a href="//')

# Print the extracted URL
echo "$redirect_url"

# Clean up: Delete the temporary HTML file
rm -f webpage.html
