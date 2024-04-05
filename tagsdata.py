import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.tdi.texas.gov/tips/what-to-do-after-a-wreck.html'

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    tags_to_extract = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'strong', 'a', 'span', 'li', 'label']
    extracted_text = []
    for tag_name in tags_to_extract:
        tags = soup.find_all(tag_name)
        for tag in tags:
            # Remove unwanted characters from the text
            text = tag.text.strip().replace('Back to Top','').replace('\u00a0', '').replace('\u00f1', '').replace('\u25ba', '').replace('\u2019', '').replace('\u00c2', '').replace('\u00c3','').replace('\u00b1','')
            extracted_text.append(text)

    # Remove empty strings
    extracted_text = [text for text in extracted_text if text]

    with open('webpage_text_tags.json', 'w') as json_file:
        json.dump(extracted_text, json_file, indent=4)
else:
    # Print an error message if the request failed
    print(f'Error: {response.status_code}')
