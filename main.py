import matplotlib.pyplot as plt
import pandas as pd
from scrapy.crawler import CrawlerProcess
from divan_scraper.divan_scraper.spiders.divan import DivanSpider

def run_spider():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "divan_prices.csv": {
                "format": "csv",
                "overwrite": True
            },
        },
        "USER_AGENT": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        "LOG_ENABLED": False
    })

    process.crawl(DivanSpider)
    process.start()

if __name__ == "__main__":
    run_spider()

    df = pd.read_csv('divan_prices.csv')
    print(f'Средняя цена: {int(df.mean().item())} рублей.')

    plt.figure(figsize=(10, 5))
    plt.title('Распределение цен')
    plt.xlabel('Цена')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.hist(df['Цена'], bins=20)
    plt.savefig('price_hist.png')
    plt.show()
