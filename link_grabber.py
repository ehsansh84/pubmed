from tools import get_page
from bs4 import BeautifulSoup
from publics import db
col_bulk = db()['bulk']
col_articles = db()['articles']
keywords = ['knee']
BASE_URL = 'https://pubmed.ncbi.nlm.nih.gov/?term=%s&filter=simsearch1.' \
           'fha&filter=years.%s-%s&format=abstract&size=%s&page=%s'
BASE_ARTICLE_URL = 'https://pubmed.ncbi.nlm.nih.gov'
keyword = keywords[0]

for bulk in col_bulk.find({'page': {'$lte': 50}}):
    page = get_page(bulk['url'])
    soup = BeautifulSoup(page, 'html.parser')
    for item in soup.select(".article-overview"):
        title = item.select('.heading-title a')[0].text.strip()
        link = BASE_ARTICLE_URL + item.select('.heading-title a')[0]['href']
        abstract = item.select('p')[0].text.strip()
        pmid = item.select('.current-id')[0].text.strip()
        try:
            doi = item.select('.id-link')[0].text.strip()
        except:
            doi = ""
        authors = item.select('.authors-list .authors-list-item a.full-name')
        authors_list = []
        for author in authors:
            authors_list.append({'name': author.text, 'author_id': author['href'].split('=')[2]})
        col_articles.insert_one({
            'bulk_id': str(bulk['_id']),
            'source_page_url': bulk['url'],
            'title': title,
            'link': link,
            'abstract': abstract,
            'pmid': pmid,
            'doi': doi,
            'authors': authors_list
        })
    col_bulk.update_one({'_id': bulk['_id']}, {'$set': {'status': 'crawled'}})
