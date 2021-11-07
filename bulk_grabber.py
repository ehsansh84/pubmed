from tools import get_page
from bs4 import BeautifulSoup
from publics import db
col_bulk = db()['bulk']
keywords = ['knee']
BASE_URL = 'https://pubmed.ncbi.nlm.nih.gov/?term=%s&filter=simsearch1.' \
           'fha&filter=years.%s-%s&format=abstract&size=%s&page=%s'
keyword = keywords[0]

for year in range(2010, 2022):
    print(year)
    page = get_page(BASE_URL % (keyword, year, year, 200, 1))
    soup = BeautifulSoup(page, 'html.parser')
    page_count = int(soup.select('.of-total-pages')[0].text.split()[1])
    for i in range(1, page_count + 1):
        url = BASE_URL % (keyword, year, year, 200, i)
        print(url)
        data = '' if i > 1 else page
        col_bulk.insert_one({
            'keyword': keyword,
            'year': year,
            'page': i,
            'url': url,
            'data': data
        })
