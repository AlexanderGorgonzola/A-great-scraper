#ugh, camelCase
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = "crawlThing"
    allowed_domains = ["dictionary.com"]
    start_urls = ["https://www.dictionary.com/list/a"]

    rules = (
        Rule(LinkExtractor(allow="list")),
        Rule(LinkExtractor(allow="browse"), callback="parse_item"),
    )
    
    def parse_item(self, response):
        yield {
            "word": response.css(".bZjAAKVoBi7vttR0xUts h1::text").get(),

        }