import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.tdi.texas.gov/tips/what-to-do-after-a-wreck.html'

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

visible_text = soup.get_text()

unwanted_strings = [
    '\n', '\t',  
    'Skip to Top Main Navigation', 
    'Skip to Content Area',
    'Skip to Footer','\u00a0', '\u00f1', '\u25ba', '\u2019',''
]

# Remove unwanted substrings from the text content
for string in unwanted_strings:
    visible_text = visible_text.replace(string, '')

# Strip any leading or trailing whitespace
visible_text = visible_text.strip()

# Create a dictionary to store the extracted data
data = {
    'content': visible_text
}

final=list(data.values())

# Split each string into another list based on two white spaces
split_lines = [line.split('  ') for line in final]

# Display the result
# for line in split_lines:
#     print(line)

# Remove empty strings from the nested list
filtered_list = [[item for item in inner_list if item != ""] for inner_list in split_lines]


with open('website_content.json', 'w') as json_file:
    json.dump(filtered_list, json_file)

print("Data saved to website_content.json")
