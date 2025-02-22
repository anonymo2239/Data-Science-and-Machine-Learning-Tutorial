import scrapy

# iki turlu link var:
# 1) Absolute link = Tam URL’yi içerir. Örneğin: https://www.worldometers.info/world-population/india-population/
# 2) Relative link = Sadece yol bilgisini içerir. Örneğin:/world-population/india-population/


class A2worldometersSpider(scrapy.Spider):
    name = "2worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        # title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # absolute_url = f'https://www.worldometers.info/{link}'
            # absolute_url = response.urljoin(link)  # ikinci yol

            # yield scrapy.Request(url=absolute_url)

            # ucuncu yol
            yield response.follow(url=link, callback=self.parse_country, meta={'country': country_name})

    def parse_country(self, response):  # parse_country fonksiyonunu ayırmanın nedeni, her ülkenin sayfasını ayrı bir fonksiyonla işlemenizi sağlamaktır.
        # response.xpath('(//table[@class="table table-striped table-bordered table-'
        #               'hover table-condensed table-list"])[1]/tbody/tr')
        # aynı gösterim
        country = response.request.meta['country']
        rows = response.xpath('(//table[contains(@class, "table")])[1]/tbody/tr')

        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {
                'country': country,
                'year': year,
                'population': population,
            }

            # to store data as json file:
            # scrapy crawl 2worldometers -o population.json

            # Burada meta={'country': country_name} ile "ülke adını" taşıyoruz.
            # Sonra response.request.meta['country'] ile geri alıyoruz.
            #
            # Amaç: Ülke sayfasında, hangi ülkeye ait verileri işlediğimizi bilmek.

