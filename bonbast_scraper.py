from selenium import webdriver
from bs4 import BeautifulSoup
import requests


class BonbastScraper:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.browser = None
        self.price = None

    def __enter__(self):
        self.browser = webdriver.Chrome(self.driver_path)
        self.browser.get('https://bonbast.com/')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.browser.quit()

    def get_price(self):
        soup = BeautifulSoup(self.browser.page_source, "html.parser")
        sell_usd = soup.find_all("td", {"id": "usd1"})
        buy_usd = soup.find_all("td", {"id": "usd2"})

        for item in sell_usd:
            if int(item.text) > 50000:
                self.price = item.text
                break

    def print_price(self):
        if self.price:
            print("قطار پیشرفت جمهوری اسلامی به سرعت در حال حرکت است! ")
            print("قیمت این لحظه دلار: ", self.price, "تومان")
        else:
            print("هیچ تغییری در قیمت دلار نیست.")


if __name__ == '__main__':
    with BonbastScraper('/usr/lib/chromium-browser/chromedriver') as scraper:
        scraper.get_price()
        scraper.print_price()
