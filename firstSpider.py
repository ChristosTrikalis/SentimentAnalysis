import scrapy
import pandas
class QuotesSpider(scrapy.Spider):
    name = 'example2'
    titles = []
    start_urls = [
        #'http://quotes.toscrape.com/page/1/', 'https://www.york.ac.uk/teaching/cws/wws/webpage1.html'
        'https://news.google.com/search?q=boeing'
        #'https://www.businessinsider.com/space-elevator-on-earth-moon-2019-9'
    ]

    def parse(self, response):
        titles = response.xpath('//a[@class="DY5T1d"]/text()')
        links = response.xpath('//a[@class="DY5T1d"]/@href')
        # df = pandas.DataFrame()
        # df['titles'] = titles
        # df['links'] = links
        #ldata = zip(titles, links)
        #for item in titles:
            #slist = {'titles': item[0], 'links': item[1]}
            #print(item[0]+" "+item[1])

        #h me8odos extract travaei to keimeno apo kapoia ontothta
        # for date, row in df.T.iteritems():
        #     yield{
        #         df[date][row].extract()
        #     }

        for p in range(len(titles)):  #'//p'
            yield{
                'title': titles[p].extract()
            }
        for p in range(len(titles)):  #'//p'
            yield{
                'link': links[p].extract()
            }

        # for l in links:
        #     yield {
        #         'links': l.extract()                        #kanei extract ta links se morfh link - An eixa valei text() 8a epsaxne mono gia ontothtes typou text
        #     }



