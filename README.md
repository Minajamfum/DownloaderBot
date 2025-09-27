Telegram Video Downloader Bot

یک ربات تلگرام برای دانلود ویدیو از اینستاگرام و پینترست. کاربران تنها با ارسال لینک ویدیو، می‌توانند آن را مستقیماً دریافت کنند.

ویژگی‌ها

پشتیبانی از لینک‌های اینستاگرام و پینترست

محدودیت حجم ویدیو: 50MB

دانلود و ارسال مستقیم ویدیو در چت تلگرام

اجرا آسان روی VPS یا سرویس‌های cloud

پیش‌نیازها

Python 3.10+

ffmpeg نصب شده و در PATH موجود باشد

کتابخانه‌های Python: pyTelegramBotAPI, yt_dlp, requests, python-dotenv

نصب و اجرا

کلون کردن پروژه:

git clone https://github.com/YOUR_USERNAME/mybot.git
cd mybot


ساخت virtual environment و نصب وابستگی‌ها:

python3 -m venv venv
source venv/bin/activate  # در ویندوز: venv\Scripts\activate
pip install -r requirements.txt


ساخت فایل .env و قرار دادن Token تلگرام:

TELEGRAM_TOKEN=توکن_ربات_تو


اجرای ربات:

python3 bot.py


برای اجرای دائم روی سرور توصیه می‌شود از tmux یا systemd service استفاده شود.

نکات مهم

مسیر دانلود ویدیو بهتر است /tmp/video.mp4 باشد تا روی سرورهای لینوکس مشکلی ایجاد نشود.

استفاده از Environment Variable برای Token توصیه می‌شود.

ربات با Cloudflare Workers سازگار نیست، چون نیاز به اتصال دائمی به Telegram API دارد.

منابع

pyTelegramBotAPI Documentation: https://github.com/eternnoir/pyTelegramBotAPI

yt-dlp Documentation: https://github.com/yt-dlp/yt-dlp
