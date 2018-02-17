# -*- coding: utf-8 -*-
import scrapy


class PeterSpider(scrapy.Spider):
    name = 'peter'
    allowed_domains = ['newyork.craigslist.org']
    start_urls = ['http://newyork.craigslist.org/search/zip/']

    def parse(self, response):
        urls=response.xpath('//a[@class="result-title hdrlnk"]/@href').extract() 
        for url in urls:
              yield scrapy.Request(url,callback=self.parse_detail)
        next=response.xpath('//a[@class="button next"]/@href').extract_first()
        yield scrapy.Request(response.urljoin(next),self.parse)    
    def parse_detail(self,response):
        item=response.xpath('//span[@id="titletextonly"]//text()').extract_first()
        yield {"item":item}
