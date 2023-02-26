#load necessary libraries
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
browser.get('https://bonbast.com/')

soup = BeautifulSoup(browser.page_source, "html.parser")
sellUsd = soup.find_all("td", {"id": "usd1"})
buyUSD = soup.find_all("td", {"id": "usd2"})

for item in sellUsd:
    print("قطار پیشرفت آیت الله رئیسی دلار را امروز به ",item.text,"ریال ، رسانده است !")

browser.quit()