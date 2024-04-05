# Web-Scraping
WEB SCRAPING USING BeautifulSoup

Install requests and beautifulsoup4 libraries using the commands
-pip install requests 
-pip install beautifulsoup4

Change the URL accordingly


Python scripts extracts visible text content from a webpage and saves it to a JSON file

1) one.py 
Using BeautifulSoup, it parses the HTML content and extracts visible text using the get_text() method.
It removes unwanted substrings such as newline characters, tabs, and specific strings like "Skip to Top Main Navigation" from the extracted text content.

2) p_tags.py 
Using BeautifulSoup, it parses the HTML content.
It finds all p (paragraph) elements in the parsed HTML and extracts their text content using a generator expression within the join() function. This concatenates the text of all paragraphs into a single string.

3) tagsdata.py 
Using BeautifulSoup, it parses the HTML content.
It defines a list of HTML tags from which text will be extracted. These include paragraph tags (p), heading tags (h1 to h6), strong tags (strong), anchor tags (a), etc. 
Extracting Text: It iterates over each specified tag, extracts the text content, removes unwanted characters, and appends the cleaned text to the extracted_text list.
It removes any empty strings from the extracted_text list.
