📥 Telegram Video Downloader Bot




یک ربات تلگرام برای دانلود ویدیو از اینستاگرام و پینترست.
کاربران تنها با ارسال لینک ویدیو، می‌توانند آن را مستقیماً دریافت کنند.

📑 Table of Contents

ویژگی‌ها

پیش‌نیازها

نصب و اجرا

Docker

نکات مهم

منابع

⚡ ویژگی‌ها

✅ پشتیبانی از لینک‌های اینستاگرام و پینترست

✅ محدودیت حجم ویدیو: 50MB

✅ دانلود و ارسال مستقیم ویدیو در چت تلگرام

✅ اجرا آسان روی VPS / Render / Fly.io / Oracle Cloud

📦 پیش‌نیازها

Python 3.10+

ffmpeg نصب شده و در PATH موجود باشد

کتابخانه‌های Python موجود در requirements.txt:

pyTelegramBotAPI
yt_dlp
requests
python-dotenv

⚙️ نصب و اجرا

کلون کردن پروژه:

git clone https://github.com/YOUR_USERNAME/mybot.git
cd mybot


ساخت virtual environment و نصب وابستگی‌ها:

python3 -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
pip install -r requirements.txt


ساخت فایل .env و قرار دادن Token ربات:

TELEGRAM_TOKEN=توکن_ربات_تو


اجرای ربات:

python3 bot.py


برای اجرای ۲۴/۷، توصیه می‌شود از tmux یا systemd service استفاده شود.

🐳 Docker (اختیاری)
FROM python:3.11-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

💡 نکات مهم

مسیر دانلود ویدیو بهتر است /tmp/video.mp4 باشد تا روی سرورهای لینوکس مشکلی ایجاد نشود.

استفاده از Environment Variable برای Token توصیه می‌شود.

این ربات با Cloudflare Workers سازگار نیست، چون نیاز به اتصال دائمی به Telegram API دارد.

🔗 منابع

pyTelegramBotAPI Documentation

yt-dlp Documentation
