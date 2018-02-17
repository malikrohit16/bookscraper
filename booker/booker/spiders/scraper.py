# -*- coding: utf-8 -*-
import scrapy


class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
       urls=response.xpath('//h3/a/@href').extract()  
       for url in urls:
           absolute_url=response.urljoin(url)
           yield scrapy.Request(absolute_url,callback=self.parse_details)
       next=response.xpath('//li[@class="next"]/a/@href').extract_first()
       absolute_next=response.urljoin(next)  
       yield scrapy.Request(absolute_next,callback=self.parse) 
    def parse_details(self,response):
        title=response.xpath('//h1//text()').extract_first()
        detail=response.xpath('//div[@id="content_inner"]/article/p//text()').extract_first()
        price=response.xpath('//p[@class="price_color"]//text()').extract_first()
        rating=response.xpath('//p[contains(@class,"star-rating")]//@class').extract_first()
        rating=rating.replace('star-rating',' ')
        yield {'title':title,'detail':detail,'price':price,'rating':rating}
  
