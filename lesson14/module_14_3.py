# Задача "Витамины для всех!":
# Подготовка:
# Подготовьте Telegram-бота из последнего домашнего задания 13 модуля сохранив код с ним в файл module_14_3.py.
# Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.
#
# Дополните ранее написанный код для Telegram-бота:
# Создайте и дополните клавиатуры:
# В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
# Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4".
# У всех кнопок назначьте callback_data="product_buying"
# Создайте хэндлеры и функции к ним:
# Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
# Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза.
# После каждой надписи выводите картинки к продуктам.
# В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
# Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
# Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"
#
# Пример результата выполнения программы:
# Обновлённое главное меню:
#
# Список товаров и меню покупки:
#
# Примечания:
# Название продуктов и картинок к ним можете выбрать самостоятельно. (Минимум 4)

import asyncio
import logging
import sqlite3
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties

API_TOKEN = 'API'

logging.basicConfig(level=logging.INFO)

default_bot_properties = DefaultBotProperties(parse_mode="HTML")

bot = Bot(token=API_TOKEN, default=default_bot_properties)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

conn = sqlite3.connect('telegram_bot.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER NOT NULL,
    image_url TEXT NOT NULL
)
''')
conn.commit()

cursor.execute('SELECT COUNT(*) FROM products')
if cursor.fetchone()[0] == 0:
    products = [
        ("Биостимул", "Комплекс витаминов", 100, "https://naturalsupp.ru/upload/iblock/a47/10eq49g67pnwzx2mxj1nrr9ordk7uz71.jpg"),
        ("Экстракт Чаги", "Источник полифенолов", 200, "https://www.ametis.ru/files/ametis/styles/product_full/public/images/product/15/chaga.jpg?itok=ujkP-1Ly"),
        ("Ундевит", "Вкусная витаминка", 300, "https://cdn.eapteka.ru/upload/offer_photo/518/171/1_5e84a5d7529c372f28ff5aea128c7322.png?t=1688566933&_cvc=1737038322"),
        ("Bud", "Запрещенно вкусная витаминка", 400, "https://main-cdn.sbermegamarket.ru/big1/hlr-system/113/437/400/082/123/9/100027324179b0.jpg")
    ]
    cursor.executemany('INSERT INTO products (name, description, price, image_url) VALUES (?, ?, ?, ?)', products)
    conn.commit()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="Рассчитать"), types.KeyboardButton(text="Информация")],
        [types.KeyboardButton(text="Купить")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer("Привет! Нажми 'Рассчитать', чтобы начать.", reply_markup=keyboard)

@dp.message(F.text == "Рассчитать")
async def main_menu(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
            [types.InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
        ]
    )
    await message.answer("Выберите опцию:", reply_markup=inline_keyboard)

@dp.callback_query(F.data == "formulas")
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора для женщин: BMR = 10 * weight + 6.25 * height - 5 * age - 161")
    await call.answer()

@dp.callback_query(F.data == "calories")
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст:", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(UserState.age)
    await call.answer()

@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.growth)

@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.weight)

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

@dp.message(F.text == "Информация")
async def send_info(message: types.Message):
    await message.answer("Информация которая должна вам помочь. Нажмите 'Рассчитать' чтобы начать.", reply_markup=keyboard)

@dp.message(F.text == "Купить")
async def get_buying_list(message: types.Message):
    cursor.execute('SELECT id, name, description, price, image_url FROM products')
    products = cursor.fetchall()

    for product in products:
        product_id, name, description, price, image_url = product
        try:
            await message.answer_photo(
                photo=image_url,
                caption=f"<b>Название:</b> {name}\n<b>Описание:</b> {description}\n<b>Цена:</b> {price} руб."
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer(
                f"<b>Название:</b> {name}\n<b>Описание:</b> {description}\n<b>Цена:</b> {price} руб.\n"
                f"<i>Изображение недоступно.</i>"
            )

    inline_keyboard_buying = types.InlineKeyboardMarkup(inline_keyboard=[])
    for product in products:
        product_id, name, _, _, _ = product
        inline_keyboard_buying.inline_keyboard.append(
            [types.InlineKeyboardButton(text=name, callback_data=f"product_buying_{product_id}")]
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard_buying)

@dp.callback_query(F.data.startswith("product_buying_"))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = int(call.data.split("_")[-1])
    cursor.execute('SELECT name, description, price, image_url FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    if product:
        name, description, price, image_url = product
        try:
            await call.message.answer_photo(
                photo=image_url,
                caption=f"<b>Вы успешно приобрели продукт:</b> {name}\n"
                        f"<b>Описание:</b> {description}\n"
                        f"<b>Цена:</b> {price} руб."
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await call.message.answer(
                f"<b>Вы успешно приобрели продукт:</b> {name}\n"
                f"<b>Описание:</b> {description}\n"
                f"<b>Цена:</b> {price} руб.\n"
                f"<i>Изображение недоступно.</i>"
            )
    else:
        await call.message.answer("Продукт не найден.")
    await call.answer()

@dp.message()
async def handle_unrecognized(message: types.Message):
    await message.answer("Извините, я не понял вас. Пожалуйста, нажмите 'Рассчитать' для начала.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    asyncio.run(main())