# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from bokiman.items import BokimanItem

class PeterSpider(scrapy.Spider):
    name = 'peter'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        urls=response.xpath('//h3/a/@href').extract()
        for url in urls:
            yield scrapy.Request(response.urljoin(url),callback=self.parse_details)
    def parse_details(self,response):
        l=ItemLoader(item=BokimanItem(),response=response)
        image_urls=response.xpath('//div[@class="item active"]/img/@src').extract_first()
        image_urls=image_urls.replace("../../","http://books.toscrape.com/") 
        l.add_value('image_urls',image_urls)
        return l.load_item()
        #yield {'i':img_url}
         
      
