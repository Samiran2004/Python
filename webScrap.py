import requests
from bs4 import BeautifulSoup

url = "https://www.netflix.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = [link['href'] for link in soup.find_all('a')]

print(links)