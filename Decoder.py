#Gives the headlines from the specified url.
import requests
from bs4 import BeautifulSoup
url='http://warthunder.com/en/news/'
r=requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
for heading in soup.find_all(class_="news-item__anons"):
    if heading.a:
        print(heading.a.text.replace("\n"," ").strip())
    else:
        print(heading.contents[0].strip())


