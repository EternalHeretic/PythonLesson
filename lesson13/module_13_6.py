# Задача "Ещё больше выбора":
# Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
# С текстом 'Рассчитать норму калорий' и callback_data='calories'
# С текстом 'Формулы расчёта' и callback_data='formulas'
# Создайте новую функцию main_menu(message), которая:
# Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
# Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
# Создайте новую функцию get_formulas(call), которая:
# Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
# Будет присылать сообщение с формулой Миффлина-Сан Жеора.
# Измените функцию set_age и декоратор для неё:
# Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
# Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
# По итогу получится следующий алгоритм:
# Вводится команда /start
# На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
# В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
# По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
# По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
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

# Создание обычной клавиатуры
keyboard = types.ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton(text="Рассчитать"), types.KeyboardButton(text="Информация")]],
    resize_keyboard=True
)

# Создание Inline клавиатуры
inline_keyboard = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [types.InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

# Функция обработки команды /start
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Нажми 'Рассчитать', чтобы начать.", reply_markup=keyboard)

# Функция для основного меню
@dp.message(F.text == "Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

# Функция для обработки callback 'formulas'
@dp.callback_query(F.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора для женщин: BMR = 10 * weight + 6.25 * height - 5 * age - 161")
    await call.answer()

# Функция для ввода возраста (начало FSM)
@dp.callback_query(F.data == "calories")
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(UserState.age)
    await call.answer()

# Функция для ввода роста
@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)

# Функция для ввода веса
@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)

# Функция для вычисления норм калорий
@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Ваша норма калорий: {calories:.2f} ккал", reply_markup=keyboard)
    await state.clear()

# Функция для кнопки 'Информация'
@dp.message(F.text == "Информация")
async def send_info(message: types.Message):
    await message.answer("Информация которая должна вам помочь. Нажмите 'Расчитать' что бы начать.", reply_markup=keyboard)

# Обработчик неопознанных сообщений
@dp.message()
async def handle_unrecognized(message: types.Message):
    await message.answer("Извините, я не понял вас. Пожалуйста, нажмите 'Рассчитать' для начала.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())