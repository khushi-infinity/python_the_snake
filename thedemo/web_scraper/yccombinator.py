from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/jobs")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

articles = [full.find("a") for full in soup.find_all("span",class_="titleline")]

article_texts =[]
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_time = [time.getText() for time in soup.find_all(name="span",class_="age")]

print(articles)
print(article_texts)
print(article_links)
print(article_time)

with open("ycombinator.txt","w") as file:
    for job in range(len(article_texts)):
        file.write(f"{article_texts[job]}      {article_links[job]}          {article_time[job]}\n\n")
