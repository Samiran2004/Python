import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/10')

if response.status_code == 200:
    print(response.json())
    print(response.content)
    print(response.text)
else:
    print(f"Error: {response.status_code}")