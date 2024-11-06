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
        if (len((response.css(".bZjAAKVoBi7vttR0xUts h1::text").get()).split()) == 1) and ("." not in (response.css(".bZjAAKVoBi7vttR0xUts h1::text").get()).split()):
            yield {
                response.css(".bZjAAKVoBi7vttR0xUts h1::text").get(): [response.css(".S3nX0leWTGgcyInfTEbW h2::text").get()],

            }