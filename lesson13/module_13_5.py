# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.
# Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
# Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и 'Информация'.
# Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
# Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
# В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками.
# При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age,
# growth и weight.

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties

# Укажите ваш токен
API_TOKEN = 'API'

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание DefaultBotProperties с parse_mode="HTML"
default_bot_properties = DefaultBotProperties(parse_mode="HTML")

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN, default=default_bot_properties)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Определение состояний
class UserState(StatesGroup):
    age = State()    # Состояние для возраста
    growth = State()  # Состояние для роста
    weight = State()  # Состояние для веса

# Создание клавиатуры
keyboard = types.ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton(text="Рассчитать"), types.KeyboardButton(text="Информация")]],
    resize_keyboard=True
)

# Функция обработки команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Нажми 'Рассчитать', чтобы начать.", reply_markup=keyboard)

# Функция для ввода возраста
@dp.message(F.text == "Рассчитать")
async def set_age(message: types.Message, state: FSMContext):
    await message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(UserState.age)

# Функция для ввода роста
@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Обновляем состояние возраста
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)

# Функция для ввода веса
@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Обновляем состояние роста
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)

# Функция для вычисления норм калорий
@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Обновляем состояние веса
    data = await state.get_data()  # Получаем ранее введённые данные

    # Применение формулы Миффлина - Сан Жеора для женщин
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал", reply_markup=keyboard)
    await state.clear()  # Завершение машины состояний

# Обработчик для кнопки 'Информация'
@dp.message(F.text == "Информация")
async def send_info(message: types.Message):
    await message.answer("Информация которая должна вам помочь. Нажмите 'Расчитать' что бы начать.", reply_markup=keyboard)

# Обработчик неопознанных сообщений
@dp.message()
async def handle_unrecognized(message: types.Message):
    await message.answer("Извините, я не понял вас. Пожалуйста, нажмите 'Рассчитать' для начала.", reply_markup=keyboard)

async def main():
    # Запуск бота
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())