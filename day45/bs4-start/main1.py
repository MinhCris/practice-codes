from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/newest")
print(response.text)