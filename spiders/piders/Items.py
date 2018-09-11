import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join, Compose

clean_text = Compose(MapCompose(lambda v: v.strip()), Join())


class PeItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()


class PeItemLoader(ItemLoader):
    default_item_class = PeItem
    url = TakeFirst()
    title = clean_text
    link = clean_text