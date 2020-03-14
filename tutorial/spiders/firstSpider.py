from pathlib import Path
import scrapy
from scrapy.crawler import CrawlerProcess

# import os.path
# from os import path
from tutorial.Nlp_Preprocessing import Preprocessing


class GNewsSpider(scrapy.Spider):
    name = 'gnews'
    keyword = 'boeing'
    timeperiod = '1d'
    titles = []
    start_urls = ['https://news.google.com/search?q=' + keyword + ' when:' + timeperiod]

    def parse(self, response):
        global titles_ext
        titles = response.xpath('//a[@class="DY5T1d"]/text()')
        links = response.xpath('//a[@class="DY5T1d"]/@href')
        datetimes = response.xpath('//time[@class="WW6dff uQIVzc Sksgp"]/@datetime')

        length = len(titles)

        if length == len(links) & len(datetimes) == length:
            for p in range(len(titles)):
                yield {'title': titles[p].extract(), 'datetime': datetimes[p].extract(), 'link': links[p].extract()}
        else:
            print('not same length!!!')
        titles_ext = titles.extract()
        # print(titles_ext)


file = Path("C:\\Users\\Trika\\Desktop\\ScrapyProjectExample\\tutorial\\tutorial\\spiders\\gnews.json")
if not file.is_file():
    process = CrawlerProcess(settings={'FEED_FORMAT': 'json', 'FEED_URI': 'gnews.json'})
    process.crawl(GNewsSpider)
    process.start()  # the script will block here until the crawling is finished

runPreprocessing = Preprocessing()
runPreprocessing.get_data(file)
