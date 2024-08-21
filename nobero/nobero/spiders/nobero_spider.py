import scrapy
import json

class NoberoSpider(scrapy.Spider):
    name = "nobero"
    start_urls = ['https://nobero.com/pages/men']

    def parse(self, response):
        # Extract category links
        categories = response.css('a.category-link::attr(href)').getall()
        for category in categories:
            yield response.follow(category, self.parse_category)

    def parse_category(self, response):
        # Extract product links from the category page
        products = response.css('a.product-link::attr(href)').getall()
        for product in products:
            yield response.follow(product, self.parse_product)

    def parse_product(self, response):
        # Extract product details
        product = {
            "category": response.css('h1.product-title::text').get(),
            "url": response.url,
            "title": response.css('h1.product-title::text').get(),
            "price": response.css('span.price::text').get().replace('₹', '').strip(),
            "MRP": response.css('span.mrp::text').get().replace('₹', '').strip(),
            "last_7_day_sale": response.css('span.sale-price::text').get().replace('₹', '').strip(),
            "available_skus": self.parse_skus(response),
            "fit": response.css('span.fit::text').get(),
            "fabric": response.css('span.fabric::text').get(),
            "neck": response.css('span.neck::text').get(),
            "sleeve": response.css('span.sleeve::text').get(),
            "pattern": response.css('span.pattern::text').get(),
            "length": response.css('span.length::text').get(),
            "description": response.css('div.product-description::text').get().strip()
        }
        yield product

    def parse_skus(self, response):
        skus = []
        colors = response.css('div.color-options span::text').getall()
        sizes = response.css('div.size-options span::text').getall()
        for color in colors:
            skus.append({
                "color": color,
                "size": sizes
            })
        return skus
