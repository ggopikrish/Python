import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.hackerrank.com')
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify())
n=soup.find_all("div",class_='span-sm-16 span-md-16 span-lg-8 border-right')
print(n[0].text)
