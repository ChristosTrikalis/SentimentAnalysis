# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'X'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
