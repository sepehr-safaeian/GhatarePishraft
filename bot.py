import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = telebot.TeleBot("6279327605:AAFMDbo2twMTgQLsAk2YI3Qa-C3k0wMtL-U")

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "به ربات تلگرام قطار پیشرفت خوش آمدید !\n"
                      f"من قطار پیشرفت جمهوری اسلامی هستم ؟ چطور می توانم به شما کمک کنم ؟")

# USD > Rial
@bot.message_handler(commands=['USD'])
def send_usd(message):
    with webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install())) as driver:
        driver.get("https://bonbast.com/")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        sell_usd = soup.find_all("td", {"id": "usd1"})

        if sell_usd:
            current_price = sell_usd[0].text
            reply_message = "تبریک میگم قطار پیشرفت جمهوری اسلامی با شتاب در حال حرکت است !\n" + f"قیمت هر یک دلار برابر با {current_price} تومان است.🚀"
            markup = InlineKeyboardMarkup()
            markup.add(InlineKeyboardButton("چرا؟", url="t.me/tasvireazadi"))
            bot.reply_to(message, reply_message, reply_markup=markup)



# This function will handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.polling()
