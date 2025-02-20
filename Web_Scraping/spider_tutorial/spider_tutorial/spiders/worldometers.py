# scrapy bench çalışmaz ise notepad den bench kodundaki Response'u response olarak değiştir.
import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"  # bu isim unique'dir.
    allowed_domains = ["www.worldometers.info"]  # Burada sadece domain kısmı yazmalı
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]  # http yerine https

    def parse(self, response):  # we get the respone here
        # title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a').getall()

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            yield {  # yield veriyi döndürür ve devam eder.
                'country_names': country_name,
                'links': link
            }
            # Bu kodu çalıştırırken spider'ın olduğu dizinde olmalısın
            # scrapy crawl worldometers komutu ile bu spider çalıştırılır.

            # HATAYI ÇÖZZ
