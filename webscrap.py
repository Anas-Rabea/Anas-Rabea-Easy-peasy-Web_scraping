import requests
from bs4 import BeautifulSoup
import re



url = 'http://coreyms.com'
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('article')
# print(article.prettify())
table = []
for article in soup.find_all('article'):
    try:
        title = article.find('h2' , class_ = 'entry-title').a.text
        content = article.find('div' , class_ = 'entry-content').p.text
        date = article.find('p' , class_ = 'entry-meta').time.text
        youtubelink =article.find('span' , class_ = 'embed-youtube').iframe['src']
        id_ = re.findall('embed/([^\?]*)' , youtubelink)
        link = 'https://www.youtube.com/watch?v='+ id_[0]
        table.append({"Title":title,"Content":content,"Date":date,"YT_Link":link})
    except:
        pass
import pandas as pd
data = pd.DataFrame(table)
print(data.head())
