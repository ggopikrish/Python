import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.dataquest.io/blog/web-scraping-tutorial-python/')
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
n=soup.find_all('nav',class_="site-footer-nav")
print(n[0].text)
