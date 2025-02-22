import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]

    def parse(self, response):
        product_container = response.xpath("//div[@class='adbl-impression-container ']/div/span[2]/ul/li")

        for product in product_container:
            product.xpath(".//li[contains(@class, 'authorLabel')]/text()")
