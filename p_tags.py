import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.tdi.texas.gov/tips/what-to-do-after-a-wreck.html'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

visible_text = ' '.join(filter(None, (p.get_text() for p in soup.find_all('p'))))

with open('website_content.json', 'w') as json_file:
    json.dump(visible_text, json_file)

print("Data saved to website_content.json")
