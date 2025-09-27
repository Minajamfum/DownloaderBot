import telebot
from telebot import types
from yt_dlp import YoutubeDL
import os
from dotenv import load_dotenv
import requests

Token = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(Token)

def find_pinterest_links(url):
    try:
        r = requests.get(url,allow_redirects=True)
        return r.url
    except:
        return url

@bot.message_handler(commands = ['start'])
def start_bot(message):
    mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/start")
    btn2 = types.KeyboardButton("/help")
    mark.add(btn1,btn2)


    bot.send_message(
        message.chat.id,
        "سلام به دانلودر خوش آمدید.\nبرای دانلود ویدیو مورد نظر تنها ارسال لینک کافی است. \n\n\nپلتفرم های پشتیبانی شده: \nاینستاگرام\nپینترست \n\nتنها ویدیو پشتیبانی میشود.",
        reply_markup=mark
    )

@bot.message_handler(commands = ['help'])
def help_message(message):
    bot.send_message(
        message.chat.id,
    "لینک مربوط به ویديو را ارسال کنید.\nتنها ویديو هایی قابل دریافت است که حجم آنها کمتر از 50 مگابایت باشند.",
    )

@bot.message_handler(func = lambda m: True)
def insta_link(message):
    url = message.text
    if "pin.it" in url:
        url = find_pinterest_links(url)

    if "instagram.com" not in url and "pin" not in url:
        bot.reply_to(message, "فقط لینک های اینستاگرام و پینترست!")
        return

    bot.reply_to(message,"لطفا صبر کنید.در حال دانلود...")

    ydl_opts = {
        "outtmpl" : "video.mp4",
        "ffmpeg_location": r"C:\ffmpeg\bin"
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    if os.path.getsize("video.mp4") > 50 * 1024 * 1024:
        bot.send_message(message.chat.id, "ویدیو بزرگتر از 50MB هست و نمیشه ارسالش کرد.")
        os.remove("video.mp4")
        return

    with open("video.mp4", "rb") as video:
        bot.send_video(message.chat.id, video)

    os.remove("video.mp4")


bot.infinity_polling()