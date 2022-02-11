from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="titlelink")
texts = []
links = []
for article_tag in articles:
    article_text = article_tag.getText()
    texts.append(article_text)
    article_link = article_tag.get("href")
    links.append(article_link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

index_max_voted = article_upvotes.index(max(article_upvotes))
text_max_voted = texts[index_max_voted]
link_max_voted = links[index_max_voted]

print(text_max_voted)