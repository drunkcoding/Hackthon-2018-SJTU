import logging
import scrapy
from scrapy.shell import inspect_response


class NutritionSpider(scrapy.Spider):
    name = "nutrition_spider"

    def __init__(self, food="", *args, **kwargs):
        self.start_urls = ["https://ndb.nal.usda.gov/ndb/search/list"]
        self.domain = "https://ndb.nal.usda.gov"
        self.food = food
        super().__init__(*args, **kwargs)

    def parse(self, response):
        return scrapy.FormRequest.from_response(response, formdata={"qlookup": self.food, "ds": "SR"},
                                                callback=self.select_food)

    def select_food(self, response):
        results = response.xpath("//table/tbody/tr")
        name_link_dict = {}
        for line in results:
            name = line.xpath("./td[2]/a//text()").extract_first().strip("\n\t ").split(" ", 1)[-1]
            link = line.xpath("./td[2]/a/@href").extract_first()
            name_link_dict.update({name: link})
        # todo: select one of the results
        if name_link_dict:
            return scrapy.Request(self.domain + name_link_dict[list(name_link_dict.keys())[0]],
                                  callback=self.parse_nutrition)
        else:
            return {"message": "No result found!"}

    def parse_nutrition(self, response):
        nutrition_table = {}
        proximates = response.xpath("//table/tbody//td[./text()='Proximates']")
        for line in proximates:
            item = line.xpath("./following-sibling::td[1]/text()").extract_first().strip("\n\t ").split(",", 1)[0]
            quantity = line.xpath("./following-sibling::td[3]/text()").extract_first().strip("\n\t ") \
                       + line.xpath("./following-sibling::td[2]/text()").extract_first().strip("\n\t ")
            nutrition_table.update({item: quantity})
        return nutrition_table


