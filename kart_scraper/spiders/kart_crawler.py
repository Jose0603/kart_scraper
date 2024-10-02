import scrapy

class KartSpider(scrapy.Spider):
    name = "kart"
    start_urls = [
  "https://www.j3competition.com/shop/?v=cfcdc267f6a0"
]

    def parse(self, response):
        if response.css('header.woocommerce-products-header h1::text').get() is None:
            yield {
                "title" : response.css("h1::text").get(default='').strip(),
                "category" : response.css("div.product_meta span.posted_in a::text").get(default=''),
                "price" : response.css("span.woocommerce-Price-amount bdi::text").get(default='').strip(),
                "part_number": response.css("span.sku::text").get(default='').strip(),
                "description": response.css('div.panel-body p::text').get(default='').strip(),
                "url": response.url,
                "img": response.css('div.kleo-images-wrapper a::attr(href)').get(default='')
            }
        else: #if there's no h1 header that means we're on the item list
            next_pages = response.css("div.product-details h3 a::attr(href)").getall()

            for page in next_pages:
                yield response.follow(page, callback = self.parse)

        # get numbered pages in case the next page exists and isn't disabled
        if response.css('a.next.page-numbers').get() is not None:
            url_parts = response.url.split('/')
            page_number_part = url_parts[-2] if len(url_parts) >= 2 else None
            if page_number_part and page_number_part.isnumeric(): #check if last digit is a number, if it is a number that means we're on page 2 at least
                page_num = int(page_number_part)
                next_page_num = page_num + 1
                new_url = response.url.replace(f"/page/{page_num}/", f"/page/{next_page_num}/")
                yield response.follow(new_url, callback=self.parse)
            else:
                yield response.follow(response.url.replace("/shop/?", "/shop/page/2/?"))
