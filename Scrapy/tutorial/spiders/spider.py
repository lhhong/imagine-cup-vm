import scrapy
import re
from scrapy_splash import SplashRequest
import urllib
import json

#### TO DO AFTER FINALISING CATEGORIES OF SHOES

class QuotesSpider(scrapy.Spider):
    name = "spider"

    def start_requests(self):
        urls = [
            #'http://www.asos.com/men/shoes-boots-trainers/cat/?cid=4209&refine=attribute_989:4908&currentpricerange=10-635&pgesize=204',
            #'http://www.asos.com/men/shoes-boots-trainers/cat/?cid=4209&refine=attribute_989:4922&currentpricerange=10-635&pgesize=204',
            #'http://www.asos.com/men/shoes-boots-trainers/cat/?cid=4209&refine=attribute_989:6576&currentpricerange=10-635&pgesize=204',
            #'http://www.asos.com/men/shoes-boots-trainers/cat/?cid=4209&refine=attribute_989:4916&currentpricerange=10-635&pgesize=204',
            'http://www.asos.com/men/shirts/cat/?cid=3602&refine=attribute_961:4069&currentpricerange=25-475&pgesize=204',


        ]
        for url in urls:
            ### MAY NOT NEED SPLASH ###
            # yield SplashRequest(url, self.parse,
            #     endpoint='render.html',
            #     args={'wait': 0.5},
            # )

            yield scrapy.Request(url=url, callback=self.parse)

        
    def parse(self, response):
        for link in response.css('a.product.product-link::attr(href)').extract():
            link = urllib.urlopen(link).geturl()

            yield scrapy.Request(url=link, callback=self.getinfo)
            # yield SplashRequest(link, self.getinfo,
            #         endpoint='render.html',
            #         args={'wait': 0.5},
            #     )

        

    def getinfo(self, response):
    	yield {
            'url': response.url,
    		'image': response.css('div.window img::attr(src)').extract_first(),
            'price': json.loads(response.xpath('//script[contains(., "Pages/FullProduct")]/text()').re_first("view\('(\{.*\})',"))['price']['current'],
            'brand': response.css('div.brand-description span a strong::text').extract_first(),
            'title': response.css('title::text').extract_first(),
            'colour': json.loads(response.xpath('//script[contains(., "Pages/FullProduct")]/text()').re_first("view\('(\{.*\})',"))['images'][0]['colour'],
            'description': response.css('div.product-description span ul li::text').extract() #a list of descriptors
    	}

