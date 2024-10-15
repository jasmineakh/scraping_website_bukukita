import scrapy


class BukuSpider(scrapy.Spider):
    name = "buku"
    allowed_domains = ["bukukita.com"]
    start_urls = ['https://bukukita.com/katalogbuku.php?page='+str(i) for i in range(1,51)]

    def parse(self, response):
        #temukan seluruh link buku
        urls= response.css('div.products-listing div.ellipsis a::attr(href)').getall()
        for url in urls:
            if "bukukita.com" not in url:
                url = response.urljoin(url)
            yield scrapy.Request(url, callback=self.find_details)
            

    def find_details(self, response):
        rows = response.css('div.product-info div.row')
        buku = {
            'Source': response.url,
            'Harga lama': response.css('span.price-box__old::text').get(),
            'Harga baru': response.css('span.price-box__new::text').get()
        }
        for row in rows:
            cols = row.css('div[class*=col] ::text')
            if len(cols) == 2:
                key = cols[0].get()
                value = cols[1].get()
                buku.update({key: value})
        yield buku  
                