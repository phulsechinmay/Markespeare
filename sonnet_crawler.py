from requests import get
from bs4 import BeautifulSoup
import sys
import re

sonnets = []
sonnetUrls = []

mainUrl = 'http://shakespeare.mit.edu/Poetry/sonnets.html'
baseUrl = 'http://shakespeare.mit.edu/Poetry/'

def getSonnetUrls():
    mainSonnetPage = get(mainUrl)
    mainSonnetPageText = mainSonnetPage.text

    mainSonnetHtml = BeautifulSoup(mainSonnetPageText, 'html.parser')
    sonnetListHtml = mainSonnetHtml.find_all('dt')

    for sonnetListingHtml in sonnetListHtml:
        sonnetUrls.append(baseUrl + str(sonnetListingHtml.a['href']))


def getSonnets():
    for sonnetUrl in sonnetUrls:
        sonnetPage = get(sonnetUrl)
        sonnetPageText = sonnetPage.text
        
        sonnetPageHtml = BeautifulSoup(sonnetPageText, 'html.parser')
        sonnetBody = sonnetPageHtml.body.blockquote
        sonnetText = sonnetBody.text

        sonnetText = sonnetText.replace('  ', ' ')
        sonnetText = sonnetText.replace('\n', ' ')

        sonnets.append(sonnetText)

def writeSonnetsToFile():
    with open('sonnets.txt', 'w+') as f:
        for sonnet in sonnets:
            f.write(sonnet)
            f.write('\n\n')

def main():
    getSonnetUrls()
    getSonnets()
    writeSonnetsToFile()

if __name__ == '__main__':
    main()