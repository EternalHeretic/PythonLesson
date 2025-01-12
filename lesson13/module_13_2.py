from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

API_TOKEN = "API"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")  # Ответ пользователю
    print("Привет! Я бот, помогающий твоему здоровью.")

@dp.message(Command(commands=['menu']))
async def start(message: types.Message):
    await message.answer("Я меню которое ты не увидишь!")  # Ответ пользователю
    print("Я меню которое ты не увидишь!")

@dp.message()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, чтобы начать общение.")  # Ответ пользователю
    print('Введите команду /start, чтобы начать общение.')

async def main():
    try:
        print("Бот запущен. Ожидание сообщений...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())