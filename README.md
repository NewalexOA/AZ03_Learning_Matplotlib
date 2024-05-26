
# Price Distribution Scraper

*Choose language: [English](#english) | [Русский](#русский)*

---

## English

### [main.py](https://github.com/NewalexOA/AZ03_Learning_Matplotlib/blob/main/main.py)
This project scrapes price data from a specified website, saves it into a CSV file, and generates a histogram of the price distribution.

### Requirements
- Python 3.x
- Scrapy
- pandas
- matplotlib

### Installation
1. Clone the repository or download the script.
2. Install the required libraries using pip:
   ```bash
   pip install scrapy pandas matplotlib
   ```

### Usage
1. Ensure that the `DivanSpider` is correctly configured to scrape the desired data.
2. Run the script:
   ```bash
   python main.py
   ```
3. The script will:
   - Run the Scrapy spider to scrape price data and save it to `divan_prices.csv`.
   - Calculate and print the average price.
   - Generate and save a histogram of the price distribution as `price_hist.png`.

### Additional Scripts

#### [HW01.py](https://github.com/NewalexOA/AZ03_Learning_Matplotlib/blob/main/HW01.py)
This script generates a histogram of 1000 samples drawn from a normal distribution with a mean of 0 and a standard deviation of 1.

#### [HW02.py](https://github.com/NewalexOA/AZ03_Learning_Matplotlib/blob/main/HW02.py)
This script generates a scatter plot of 150 random points.

---

## Русский

### [main.py](https://github.com/NewalexOA/AZ03_Learning_Matplotlib/blob/main/main.py)
Этот проект собирает данные о ценах с указанного веб-сайта, сохраняет их в файл CSV и генерирует гистограмму распределения цен.

### Требования
- Python 3.x
- Scrapy
- pandas
- matplotlib

### Установка
1. Клонируйте репозиторий или скачайте скрипт.
2. Установите необходимые библиотеки с помощью pip:
   ```bash
   pip install scrapy pandas matplotlib
   ```

### Использование
1. Убедитесь, что `DivanSpider` правильно настроен для сбора необходимых данных.
2. Запустите скрипт:
   ```bash
   python main.py
   ```
3. Скрипт выполнит следующие действия:
   - Запустит паука Scrapy для сбора данных о ценах и сохранит их в `divan_prices.csv`.
   - Вычислит и выведет среднюю цену.
   - Сгенерирует и сохранит гистограмму распределения цен как `price_hist.png`.

### Дополнительные скрипты

#### [HW01.py](https://github.com/NewalexOA/AZ03_Learning_Matplotlib/blob/main/HW01.py)
Этот скрипт генерирует гистограмму из 1000 выборок, взятых из нормального распределения с математическим ожиданием 0 и стандартным отклонением 1.

#### [HW02.py](https://github.com/NewalexOA/AZ03_Learning_Matplotlib/blob/main/HW02.py)
Этот скрипт генерирует диаграмму рассеяния из 150 случайных точек.
