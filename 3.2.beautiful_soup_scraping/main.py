from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
articles = soup.find_all(name="span",class_="titleline")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a")["href"]
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]

#print(article_texts)
#print(article_links)
#print(article_upvotes)

for index in range(0,len(article_upvotes)):
    if article_upvotes[index] == max(article_upvotes):
        print(f"Highest number of upvotes : {article_upvotes[index]} , title of article : {article_texts[index]}. ")


    
