# Web_scraping
<li>IMDB provides user based reviews(star based review)</li>
<li>Scraping text based review</li>
<li>This Scraping can be used for google review or any other websites that you want to scrape!</li>
<br><br>

## library uses
1. import urlib 
2. impirt urlib.request
3. from bs4 import Beaurifulsoup

<br><br>

## Step 1:
*this project will scraping movie 'parasite'*
- open IMDB user review area
https://www.imdb.com/title/tt6751668/reviews?ref_=tt_sa_3  //*this is for 'parasite' movie review*

## Step 2:
- put cursor on the review and click right. 
- click inspection
![alt text](image/readme-img.jpg?raw=true)
- check html code
- for example
    - >("div",{"class":"text show-more__control"})

## Step 3:
*IMDB doesn't show all text-based review unless you click 'load more' button which bring you to another url*
- check 'load more' button in the source code; you can see that they have 'data-key'
![alt text](image/readme-img2.jpg?raw=true)
- scrape until there are no 'data-key'
<br><br>
## Explanation:
- Create funtion to open the url and read data.
```Python
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage,"html.parser")
    return soupdata
```

- put the url which you want to scrape 
 ```Python
 soup = make_soup("https://www.imdb.com/title/tt6751668/reviews?ref_=tt_sa_3")
```
- keep check if key is available. If there are no key for 'load more' it means that page is the last page.
- pReview; collect all review data and add up together to create a output .txt file
```Python
isKeyAvailable = True 
pReview=""
```
- while key is True, it will collect data.
- After collect all data, check if there are key for 'load more'
- if key is available, change url with new load more url key
```Python
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

```

- After collect all data, save it as .txt file
```Python
file =open(os.path.expanduser("Parasite.txt"),"wb")
file.write(bytes(pReview, encoding="ascii",errors='ignore'))
```