import feedparser
import requests

parser = feedparser.parse('https://audioboom.com/channels/4981334.rss')


items = parser.entries


i=0
for item in items:
        for content in parser.entries[i].media_content:
            title = parser.entries[i].title
            if title.find(":")!=-1:
	               title = title.replace(":"," ")
            if title.find("?")!=-1:
	               title = title.replace("?"," ")
            url = content['url']
            print(title)
            print(content['url'])
            i=i+1
            doc = requests.get(url)
            with open(title +".mp3", 'wb') as f:
                f.write(doc.content)
