# Задача "Продуктовая база":
# Подготовка:
# Для решения этой задачи вам понадобится код из предыдущей задачи.
# Дополните его, следуя пунктам задачи ниже.
#
# Дополните ранее написанный код для Telegram-бота:
# Создайте файл crud_functions.py и напишите там следующие функции:
# initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса.
# Эта таблица должна содержать следующие поля:
# id - целое число, первичный ключ
# title(название продукта) - текст (не пустой)
# description(описание) - текст
# price(цена) - целое число (не пустой)
# get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.
#
# Изменения в Telegram-бот:
# В самом начале запускайте ранее написанную функцию get_all_products.
# Измените функцию get_buying_list в модуле с Telegram-ботом,
# используя вместо обычной нумерации продуктов функцию get_all_products.
# Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
# Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.
#
# Пример результата выполнения программы:
# Добавленные записи в таблицу Product и их отображение в Telegram-bot:
#
# Примечания:
# Название продуктов и картинок к ним можете выбрать самостоятельно. (Минимум 4)

import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.bot import DefaultBotProperties
from crud_functions import initiate_db, get_all_products, add_test_data

API_TOKEN = 'API'

logging.basicConfig(level=logging.INFO)

default_bot_properties = DefaultBotProperties(parse_mode="HTML")

bot = Bot(token=API_TOKEN, default=default_bot_properties)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

initiate_db()
add_test_data()

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

    products = get_all_products()

    for product in products:
        product_id, title, description, price, image_url = product
        try:
            await message.answer_photo(
                photo=image_url,
                caption=f"Название: {title} | Описание: {description} | Цена: {price} руб."
            )
        except Exception as e:
            logging.error(f"Ошибка при отправке изображения: {e}")
            await message.answer(
                f"Название: {title} | Описание: {description} | Цена: {price} руб.\n"
                f"Изображение недоступно."
            )

    inline_keyboard_buying = types.InlineKeyboardMarkup(inline_keyboard=[])
    for product in products:
        product_id, title, _, _, _ = product
        inline_keyboard_buying.inline_keyboard.append(
            [types.InlineKeyboardButton(text=title, callback_data=f"product_buying_{product_id}")]
        )

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_keyboard_buying)

@dp.callback_query(F.data.startswith("product_buying_"))
async def send_confirm_message(call: types.CallbackQuery):
    product_id = int(call.data.split("_")[-1])
    products = get_all_products()
    product = next((p for p in products if p[0] == product_id), None)
    if product:
        _, title, description, price, _ = product
        await call.message.answer(
            f"Вы успешно приобрели продукт: {title}\n"
            f"Описание: {description}\n"
            f"Цена: {price} руб."
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