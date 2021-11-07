
from bs4 import BeautifulSoup
with open("text.html") as f:
    soup = BeautifulSoup(f, 'html.parser')
for item in soup.select(".article-overview"):
    title = item.select('.heading-title a')[0].text

    print()
