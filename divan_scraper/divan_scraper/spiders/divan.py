import scrapy
import logging

class DivanSpider(scrapy.Spider):
    name = 'divan'
    allowed_domains = ['divan.ru']
    start_urls = ['https://www.divan.ru/category/divany-i-kresla?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54']

    handle_httpstatus_list = [404]  # Обрабатываем статус 404

    def parse(self, response):
        if response.status == 404:
            self.log('No more pages to load, stopping the spider.', level=scrapy.log.INFO)
            return

        self.log(f'Processing page: {response.url}')

        price_containers = response.css('div.q5Uds.T7z9Z.fxA6s')
        for container in price_containers:
            price = container.css('span[data-testid="price"]::text').get()
            if price:
                price = price.strip().replace(' ', '')
                self.log(f'Found price: {price}')
                yield {'Цена': price}

        # Переход на следующую страницу без проверки ссылки
        current_page_number = int(response.url.split('page-')[-1].split('?')[0]) if 'page-' in response.url else 1
        next_page_number = current_page_number + 1
        next_page_url = f'https://www.divan.ru/category/divany-i-kresla/page-{next_page_number}?types%5B%5D=1&types%5B%5D=4&types%5B%5D=54'
        yield scrapy.Request(next_page_url, callback=self.parse)