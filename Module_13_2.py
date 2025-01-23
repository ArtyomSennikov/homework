# Задача "Бот поддержки (начало)".

# К коду из подготовительного видео напишите две асинхронные функции:
# 1. start(message) - печатает строку в консоли 'Привет! Я бот помогающий твоему здоровью.'
# Запускается только когда написана команда '/start' в чате с ботом (используйте соответствующий декоратор).
# 2. all_massages(message) - печатает строку в консоли 'Введите команду /start, чтобы начать общение.'
# Запускается при любом обращении не описанном ранее (используйте соответствующий декоратор).
# Запустите ваш Telegram-бот и проверьте его на работоспособность.

# Пример результата выполнения программы:
# Ввод в чат Telegram:
# Хэй!
# /start

# Вывод в консоль:
# Updates were skipped successfully.
# Введите команду /start, чтобы начать общение.
# Привет! Я бот помогающий твоему здоровью.

# Примечания:
# 1. Для ответа на сообщение используйте декоратор message_handler.
# 2. При отправке вашего кода на GitHub не забудьте убрать ключ для подключения к вашему боту!

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

token = ''
bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_message(message):
    print('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)