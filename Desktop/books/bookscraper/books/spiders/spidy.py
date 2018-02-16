# -*- coding: utf-8 -*-
import scrapy


class SpidySpider(scrapy.Spider):
    name = 'spidy'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        books=response.xpath('//h3/a/@title').extract()
        prices=response.xpath('//p[@class="price_color"]//text()').extract()
        rating=response.xpath('//p[contains(@class,"star-rating ")]//@class').extract()
        i=0 
        for book,price in zip(books,prices):
             yield {"book":book,'price':price,'rating':rating[i].replace('star-rating',' ')}
             i=i+6
        url=response.xpath('//li[@class="next"]/a/@href').extract_first()
        yield response.follow(url,self.parse)
