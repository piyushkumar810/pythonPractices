# use news api and request module to fetch the daily news related to different topics. 
# go to : https://newsapi.org/
# and explore the various options to build your application.

import requests
import json

query=input("what type of news you are intrested in ? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2024-11-29&sortBy=publishedAt&apiKey=f3a0cc6520e9402fab946feba5d39535"
r=requests.get(url)

news=json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------------------------------------")