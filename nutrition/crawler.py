import logging
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class GetResultCrawler(object):
    def __init__(self):
        self.crawled_items = []
        settings = get_project_settings()
        settings["LOG_LEVEL"] = logging.WARNING
        self.process = CrawlerProcess(settings)

    def crawl(self, spider_dict):
        def _add_crawled_item(item):
            if item:
                self.crawled_items.append(item)
        for spider_name, spider_kwargs in spider_dict.items():
            crawler = self.process.create_crawler(spider_name)
            crawler.signals.connect(_add_crawled_item, signals.item_scraped)
            self.process.crawl(crawler, **spider_kwargs)

        self.process.start(stop_after_crawl=True)
        return self.crawled_items
