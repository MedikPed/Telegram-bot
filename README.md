Быстрый старт
Предварительные требования
Python 3.8 или выше

Токен бота от @BotFather

Базовое понимание Python

Установка и запуск
1. Клонирование репозитория
bash
git clone https://github.com/MedikPed/telegram-bots-collection.git
cd telegram-bots-collection
2. Создание виртуального окружения
bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Установка зависимостей
Для Aiogram:

bash
pip install -r requirements-aiogram.txt
Установит: aiogram, aiohttp, python-dotenv

Для Python-Telegram-Bot:

bash
pip install -r requirements-ptb.txt
Установит: python-telegram-bot, python-dotenv

4. Настройка токена
Скопируйте файл .env.example в .env:

bash
cp .env.example .env
Отредактируйте .env, добавив свой токен:

env
BOT_TOKEN=ваш_токен_здесь
5. Запуск примера
Aiogram:

bash
cd aiogram_examples/01_basics
python 01_echo_bot.py
Python-Telegram-Bot:

bash
cd ptb_examples/01_basics
python 01_echo_bot.py
