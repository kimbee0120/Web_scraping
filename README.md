# Web_scraping
<li>IMDB provides user based reviews(star based review)</li>
<li>Scraping text based review</li>
<li>This Scraping can be used for google review or any other websites that you want to scrape!</li>

## library uses
1. import urlib 
2. impirt urlib.request
3. from bs4 import Beaurifulsoup

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