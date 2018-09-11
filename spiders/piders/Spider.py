from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Items import PeItem, PeItemLoader


class PeSpider(CrawlSpider):
    name = 'PensionSpider'
    allowed_domains = ["www.pfrf.ru"]
    start_urls = ["http://www.pfrf.ru/opendata"]
    rules = [Rule(LinkExtractor(
        restrict_xpaths=('//table[@id="opendata-list"]//tr'),
        allow=("http://www.pfrf.ru/opendata")),
        callback="parse_item"
    ),
        Rule(LinkExtractor(
            restrict_xpaths=['//url[contains(class, "pagination")]']),
            follow=True
        )
    ]

    def parse_item(self, response):
        print('\n\nProcessing..' + response.url)
        selector = Selector(response)
        item = PeItemLoader(PeItem(), selector, response)
        item.add_value('url', response.url)
        item.add_value('title', response.xpath('//*[@id="topArea"]//*[@class="layout content"]//h1//text()').extract())
        item.add_value('link', response.xpath('//*[@id="opendata-list"]//tr[8]//td[3]//a//@href').extract())
        return item.load_item()