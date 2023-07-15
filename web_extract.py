import requests
from bs4 import BeautifulSoup
import re


def extract_data_from_webpage(url):
    # Send a GET request to the webpage
    response = requests.get(url)

    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <p> and <head> tags and extract their text
    paragraphs = soup.find_all(['p', 'head'])
    text = ' '.join([p.get_text() for p in paragraphs])

    # Remove unnecessary spaces
    text = re.sub('\s+', ' ', text).strip()

    # Remove unrecognized symbols
    text = re.sub(r'[^\x00-\x7F]+', '', text)

    # Return the cleaned up data
    return text
