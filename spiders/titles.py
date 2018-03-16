import scrapy

class JobsSpider(scrapy.Spider):
    name = "titles"
    allowed_domains = ["craigslist.ca"]
    start_urls = ["https://montreal.craigslist.ca/search/apa"]

    def parse(self, response):
        titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        
        for title in titles:
            yield {'Title': title}