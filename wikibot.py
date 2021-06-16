from bs4 import BeautifulSoup
import requests
import string


search_word = string.capwords(input('Search: '))
word_spacing = search_word.split()
word = '_'.join(word_spacing)

url = "https://en.wikipedia.org/wiki/"+word
def wikibot(url):
    url_open =requests.get(url)
    soup = BeautifulSoup(url_open.content, 'html.parser')
    details =soup('table', {'class':'infobox'})
    for i in details:
        h =i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            if heading is not None and detail is not None:
                for x,y in zip(heading, detail):
                    print("{} :: {}".format(x.text,y.text))
                    print("---------------------")

    for i in range(0,3):
        print(soup('p')[i].text)


wikibot(url)
