

Python web-scraper for *[Billboard's Hot 100 Chart](https://www.billboard.com/charts/hot-100)* using **Scrapy**. 
#### How to use:
1. Install [scrapy](https://scrapy.org/](https://scrapy.org/))
2. Clone the repo
3. From the root of the repo run:

    `scrapy crawl -a date=2019-01-01 billboard_scraper -o result.csv`

#### csv Headers:
* Song name
* Artist name
* Last week position
* Peak position
* Weeks on chart