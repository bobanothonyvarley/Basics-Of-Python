from bs4 import BeautifulSoup
import requests

#look up on youtube for tutorial


page_to_scrape = requests.get('https://quotes.toscrape.com')
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

quotes = soup.findAll('span', attrs={'class':'text'})
authors = soup.findAll('small', attrs={'class':'author'})

for q, a in zip(quotes, authors):
    print(q.text, ' - ', a.text, '\n')