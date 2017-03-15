import scrapy
import re
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "tshirts"

    def start_requests(self):
        urls = [
            #'https://www.zalora.sg/men/clothing/solid-t-shirts/?sort=popularity&dir=desc&category_id=2101',
            #'https://www.zalora.sg/men/clothing/solid-t-shirts/?sort=popularity&dir=desc&page=2&category_id=2101',
            #'https://www.zalora.sg/men/clothing/solid-t-shirts/?sort=popularity&dir=desc&page=3&category_id=2101',
            #'https://www.zalora.sg/men/clothing/solid-t-shirts/?sort=popularity&dir=desc&page=4&category_id=2101',
            #'https://www.zalora.sg/men/clothing/solid-t-shirts/?sort=popularity&dir=desc&page=5&category_id=2101',
            #'https://www.zalora.sg/men/clothing/solid-t-shirts/?sort=popularity&dir=desc&page=6&category_id=2101',
            'https://www.zalora.sg/men/clothing/solid-t-shirts/?sort=popularity&dir=desc&page=7&category_id=2101',


        ]
        for url in urls:
            #yield scrapy.Request(url=url, callback=self.parse, endpoint='render.html', args={'wait': 0.5},)
            # yield SplashRequest(url, self.parse, meta={
            #     'splash': {
            #         'endpoint': 'render.html',
            #         'args': {'wait': 0.5, 'proxy': 'default'}
            #     }
            # })
            yield SplashRequest(url, self.parse,
                endpoint='render.html',
                args={'wait': 0.5},
            )

        
    def parse(self, response):
        for item in response.css('li.b-catalogList__itm.js-catalogList__itm.unit.size1of3'):
            link = item.css('a::attr(href)').extract_first()
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.getinfo)

        

    def getinfo(self, response):
        if response.css('div.price-box__regular-price.js-detail_updateSku_skuPrice span::text').extract_first() is not None:
        	yield {
                'url': response.url,
        		'image': response.css('div.l-productImage.box div.productZoom::attr(data-zoom)').extract_first(),
                'colour': response.css('td[itemprop="color"]::text').extract_first(),
                'brand': response.css('div.js-prd-brand.product__brand a::text').extract_first(),
                'title': response.css('div.product__title.fsm::text').extract_first(),
                'price': response.css('div.price-box__regular-price.js-detail_updateSku_skuPrice span::text').extract_first(),
                'description': response.css('div#productDesc.box.mtl.fss.clearfix::text').extract(),
        	}
        else:
            yield {
                'url': response.url,
                'image': response.css('div.l-productImage.box div.productZoom::attr(data-zoom)').extract_first(),
                'colour': response.css('td[itemprop="color"]::text').extract_first(),
                'brand': response.css('div.js-prd-brand.product__brand a::text').extract_first(),
                'title': response.css('div.product__title.fsm::text').extract_first(),
                'price': response.css('span.js-detail_updateSku_specialPrice span.value::text').extract_first(),
                'description': response.css('div#productDesc.box.mtl.fss.clearfix::text').extract(),
            }