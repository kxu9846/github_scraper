from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://github.com/trending"
content = urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")

articles = soup.find_all('article')

count = 1
for article in articles:
    title = article.h1.a['href'][1:]
    print(str(count) + ":" + title)
    count += 1
