import requests

# Correct URL
url = "https://jsonplaceholder.typicode.com/posts"

# Data you waant to send to the server
payload = {
    "title": "Weather app project",
    "body": "This is a simple weather project.",
    "userId": 1
}

# POST request
response = requests.post(url, json=payload, timeout=10)

print(f"Status code: {response.status_code}")

# 201 = Created successfully
if response.status_code == 201:
    created_data = response.json()

    print(f"Server created post with ID: {created_data['id']}")
    print(f"Title: {created_data['title']}")
else:
    print("Error:", response.text)