import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

#Star Review = 8.6

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser")
    return soupdata

soup = make_soup("https://www.imdb.com/title/tt6751668/reviews?ref_=tt_sa_3")
isKeyAvailable = True
pReview=""

while(isKeyAvailable):
    for review in soup.findAll("div",{"class":"text show-more__control"}):
        print(review.text+"\n")
        pReview = pReview + review.text + "\n"

    if (soup.find("div", {"class": "load-more-data"}) is None):
        isKeyAvailable = False
    else:
        key = soup.find("div", {"class": "load-more-data"})["data-key"]
        soup = make_soup("https://www.imdb.com/title/tt8579674/reviews/_ajax?paginationKey="+key)
        print("https://www.imdb.com/title/tt8579674/reviews/_ajax?paginationKey="+key)

file =open(os.path.expanduser("Parasite.txt"),"wb")
file.write(bytes(pReview, encoding="ascii",errors='ignore'))
