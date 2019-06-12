# -*- coding: utf-8 -*-
import scrapy


class BarronsSpider(scrapy.Spider):
    name = 'Barrons'
    allowed_domains = ['member.rakuten-sec.co.jp']
    start_urls = ['http://member.rakuten-sec.co.jp/']

    def parse(self, response):
        pass
