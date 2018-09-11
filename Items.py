import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class PeItem(scrapy.Item):
    url             = scrapy.Field()
    title           = scrapy.Field()
    link            = scrapy.Field()
    #subtitle       = scrapy.Field()
    #description    = scrapy.Field()
    #logo           = scrapy.Field()
    #tables         = scrapy.Field()

class PeItemLoader(ItemLoader):
    url = TakeFirst()
    title = TakeFirst()
    link = TakeFirst()
    # subtitle      = TakeFirst()
    # description   = TakeFirst()
    # logo          = TakeFirst()
    # tables        = TakeFirst()
    url_put        = MapCompose(lambda x: x.lower())