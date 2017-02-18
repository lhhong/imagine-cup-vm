import scrapy
import re
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = "tshirts"

    def start_requests(self):
        urls = [
            'https://www.zalora.sg/men/clothing/pants/?sort=popularity&dir=desc&category_id=30',
            'https://www.zalora.sg/men/clothing/pants/?sort=popularity&dir=desc&page=2&category_id=30',
            'https://www.zalora.sg/men/clothing/pants/?sort=popularity&dir=desc&page=3&category_id=30',
            'https://www.zalora.sg/men/clothing/pants/?sort=popularity&dir=desc&page=4&category_id=30',
            'https://www.zalora.sg/men/clothing/pants/?sort=popularity&dir=desc&page=5&category_id=30',
            'https://www.zalora.sg/men/clothing/pants/?sort=popularity&dir=desc&page=6&category_id=30',
            

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
  #   	yield {
  #   		'test': response.xpath("//script[contains(., 'app.settings = {')]/text()").re('(?<="facet_prices":).+(?=")'),
		# }

        # yield {
        #     # 'html':response.css('div.b-catalogList__itm.js-catalogList__itm.unit.size1of3'),
        #     # 'img': response.css('img.b-catalogList__itm-img.js-itm-img.js-itm-hover-img-front'),
        #     #'image': response.css('span.b-catalogList__itmImageWrapper.js-catalogImage.js-itm-hover img::attr(src)').extract()
        #     'links': response.css('li.b-catalogList__itm.js-catalogList__itm.unit.size1of3')
        # }

        for item in response.css('li.b-catalogList__itm.js-catalogList__itm.unit.size1of3'):
            link = item.css('a::attr(href)').extract_first()
            link = response.urljoin(link)
            yield scrapy.Request(link, callback=self.getinfo)

        # for x in response.css('ul.ui-listHorizontal.pgn')

        # for page in response.css('li.ui-listItem'):
        #     print 'hi'
        #     page = page.css('a::attr(href)').extract()
        #     if page is not None:
        #         print page
                # page = response.urljoin(page)
                # yield scrapy.Request(page, callback=self.parsepage)

    def getinfo(self, response):
    	yield {
            'url': response.url,
    		'image': response.css('div.l-productImage.box div.productZoom::attr(data-zoom)').extract_first(),
            'colour': response.css('td[itemprop="color"]::text').extract_first(), #but can't extract just the text
            'description': response.css('div.product__title.fsm::text').extract_first(),
    	}

    	#do saving of picture and description here 