import scrapy


class BookSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = ['https://books.toscrape.com/']

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            yield {
                'title': book.css('h3 a::attr(title)').get(),
                'price': book.css('.price_color::text').get(),
                'rating': book.css('p.star-rating::attr(class)').get().replace("star-rating", "").strip(),
                'link': response.urljoin(book.css('h3 a::attr(href)').get())
            }
