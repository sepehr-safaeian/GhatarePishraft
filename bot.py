import telebot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# Create the bot
bot = telebot.TeleBot("6279327605:AAFMDbo2twMTgQLsAk2YI3Qa-C3k0wMtL-U")

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Create inline keyboard
    markup = InlineKeyboardMarkup(row_width=2)
    # Create buttons and assign callback data to each
    button_usd = InlineKeyboardButton("قیمت دلار📈 ", callback_data='USD')
    button_Crypto = InlineKeyboardButton("وضعیت کریپتوکارنسی ₿ ", callback_data='Crypto')

    # Add buttons to the inline keyboard
    markup.add(button_usd, button_Crypto,)
    
    # Send welcome message with inline keyboard
    bot.reply_to(message, "به ربات تلگرام قطار پیشرفت خوش آمدید !\n"
        f"من قطار پیشرفت جمهوری اسلامی هستم. چطور می توانم به شما کمک کنم؟", reply_markup=markup)


# USD > Rial
@bot.callback_query_handler(func=lambda call: call.data == 'USD')
def send_usd(call):
    with webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install())) as driver:
        driver.get("https://bonbast.com/")
        soup = BeautifulSoup(driver.page_source, "html.parser")
        sell_usd = soup.find_all("td", {"id": "usd1"})

        if sell_usd:
            current_price = sell_usd[0].text
            reply_message = "تبریک می‌گم! قطار پیشرفت جمهوری اسلامی با شتاب در حال حرکت است!\n" + f"قیمت هر یک دلار برابر با {current_price} تومان است.🚀"
            markup = InlineKeyboardMarkup()
            bot.send_message(call.message.chat.id, reply_message, reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, "هیچ تغییری در قیمت دلار نیست.")



# CryptoCurrency
@bot.callback_query_handler(func=lambda call: call.data == 'Crypto')

# This function will handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.polling()
