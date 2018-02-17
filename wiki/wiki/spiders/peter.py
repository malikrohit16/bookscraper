# -*- coding: utf-8 -*-
import scrapy


class PeterSpider(scrapy.Spider):
    name = 'peter'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population']

    def parse(self, response):
        ls=response.xpath('//table[@class="wikitable sortable"]')
        for l in ls:
            cities=ls.xpath('.//tr/td[2]')
            city=cities.xpath('.//a/@title').extract()
            pop_2011=ls.xpath('.//tr/td[3]//text()').extract()
            pop_2001=ls.xpath('.//tr/td[4]//text()').extract()
            state=ls.xpath('.//tr/td[5]//text()').extract()
            for a,b,c,d in zip(city,pop_2011,pop_2001,state):
                  yield{"city":a,"pop_2011":b,"pop_2001":c,"state":d}


