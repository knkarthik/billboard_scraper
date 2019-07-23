from _datetime import datetime

import scrapy
from scrapy.log import logger


class BillboardSpider(scrapy.Spider):
    name = "billboard_scraper"

    def __init__(self, date=None, *args, **kwargs):
        super(BillboardSpider, self).__init__(*args, **kwargs)
        if date:
            try:
                date = datetime.strptime(date, '%Y-%m-%d').date()
                self.start_urls = ['https://www.billboard.com/charts/hot-100/%s' % date]
            except ValueError as e:
                logger.warn(f"*** Invalid Date. Expecting YYYY-MM-DD. Using {datetime.now().strftime('%Y-%m-%d')} ***")
                self.start_urls = ['https://www.billboard.com/charts/hot-100']
        else:
            self.start_urls = ['https://www.billboard.com/charts/hot-100']

    def parse(self, response):
        rank = []
        song = []
        artist = []
        last_week = []
        peak_position = []
        weeks_on_chart = []
        chart_list_item = response.css(".chart-list-item")
        # new = response.css(".chart-list-item__trend-icon").xpath("./img[contains(@src, 'arrow-new.svg')]")
        for item in chart_list_item:
            rank.append(item.attrib['data-rank'])
            song.append(item.attrib['data-title'])
            artist.append(item.attrib['data-artist'])
            new = item.css(".chart-list-item__trend-icon > img[src*='arrow-new.svg']")
            if new:
                last_week.append("-")
                peak_position.append("-")
                weeks_on_chart.append("-")

            else:
                last_week.append(item.css(".chart-list-item__last-week::text").get())
                peak_position.append(item.css(".chart-list-item__weeks-at-one::text").get())
                weeks_on_chart.append(item.css(".chart-list-item__weeks-on-chart::text").get())
        for r, s, a, l, p, w in zip(rank, song, artist, last_week, peak_position, weeks_on_chart):
            yield {
                'rank': r,
                'song': s,
                'artist': a,
                'last-week': l,
                'peak-position': p,
                'weeks-on-chart': w
            }
