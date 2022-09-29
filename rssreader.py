from bs4 import BeautifulSoup
import requests

url = requests.get('https://timesofindia.indiatimes.com/rssfeedstopstories.cms')

soup = BeautifulSoup(url.content, 'xml')
entries = soup.find_all('item')

for entry in entries:
    title = entry.title.text
    description = entry.description.text
    link = entry.link.text
    pubDate = entry.pubDate.text
    print(f"Title: {title}\n\nSummary: {description}\n\nPublication Date: {pubDate}\n\nLink: {link}\n\n****************************************\n\n")
