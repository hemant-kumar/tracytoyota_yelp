# -*- coding: utf-8 -*-
import scrapy


class TracyToyotaYelpSpider(scrapy.Spider):
    name = "tracytoyota_yelp"
    allowed_domains = ["www.yelp.com"]
    start_urls = [
        'https://www.yelp.com/biz/tracy-toyota-tracy',
    ]

    def parse(self, response):
        for book_url in response.css("head > meta:nth-child(93) ::attr(content)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_page)
        next_page = response.css("#super-container > div > div > div.column.column-alpha.main-section > div:nth-child(4) > div.feed > div.review-pager > div > div > div.pagination-links.arrange_unit > div > div:nth-child(10) > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_page(self, response):
        item = {}
        item["html"] = response
        yield item
