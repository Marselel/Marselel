import requests
from bs4 import BeautifulSoup as bs
from collections.abc import Mapping
link = 'https://kakoysegodnyaprazdnik.ru/'
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}

response = requests.get(url=link, headers=HEADERS)
soup = bs(response.content, 'html.parser')
block = soup.find('div', class_='listing_wr')
cards = block.findAll('div', itemprop='suggestedAnswer')
    # for item in cards:
    #     name=item.find('span',itemprop='text').text
    #     print(name)
    # break
nazvaniya = [item.find('span', itemprop='text').text for item in cards][0:10]
print ('\n'.join( nazvaniya))