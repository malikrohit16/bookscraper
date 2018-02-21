# -*- coding: utf-8 -*-
import scrapy


class qouteSpider(scrapy.Spider):
    name = 'kiraspider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    def parse(self,response):
         qs=response.xpath("//span[@class='text']//text()").extract()
         for q in qs:
             yield {"quote":q}         

  
         next=response.xpath('//li[@class="next"]/a/@href').extract_first()
         abs_url=response.urljoin(next[0])
         if next is not None:
             yield response.follow(next,self.parse)

            
