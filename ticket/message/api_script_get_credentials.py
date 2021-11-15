import requests
import json
import pprint


url = 'http://127.0.0.1:8000/api/credentials/'
response = requests.get(url)
response_on_python = response.json()

with open(r'C:\Users\Denis\Desktop\credentials.txt', 'w') as file:
    for credential in response_on_python:
        file.write(
            f"author: {credential['name']} "
            f"description: {credential['description']}, "
            f"email: {credential['email']}\n"
        )
pprint.pprint(response_on_python, width=1)