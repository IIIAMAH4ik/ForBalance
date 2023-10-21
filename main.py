import telebot
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import ParseMode, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram.types.web_app_info import WebAppInfo

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


# Создаем клавиатуру с кнопками
menu_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
buttons = [
    KeyboardButton("Теория зерна"),
    KeyboardButton("Оборудование"),
    KeyboardButton("Спешиалти кофе"),
    KeyboardButton("Введение эспрессо"),
    KeyboardButton("Service Book"),
    KeyboardButton("Сроки годности"),
]
menu_keyboard.add(*buttons)

# Клавиатура для подменю "Теории зерна"
sub_menu_theory = InlineKeyboardMarkup(row_width=2)
sub_menu_theory_buttons = [
    InlineKeyboardButton("История возникновения кофе", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/history/')),
    InlineKeyboardButton("Распространение кофе", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/rasprost/')),
    InlineKeyboardButton("Ареал произрастания кофе", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/areal/')),
    InlineKeyboardButton("Арабика и робуста", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/arabica/')),
    InlineKeyboardButton("Теруар", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/tereuar/')),
    InlineKeyboardButton("Строение кофейной ягоды", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/sead/')),
    InlineKeyboardButton("Методы сбора урожая", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/zbor/')),
    InlineKeyboardButton("Методы обработки урожая", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/obrabotka/')),
    InlineKeyboardButton("Ферментация", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/fermentasiya/')),
    InlineKeyboardButton("Обжарка", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/obzarka/')),
]
sub_menu_theory.add(*sub_menu_theory_buttons)

# Клавиатура для подменю "Оборудования"
sub_menu_equipment = InlineKeyboardMarkup(row_width=2)
sub_menu_equipment_buttons = [
    InlineKeyboardButton("Кофемашины", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/kofemashini/')),
    InlineKeyboardButton("Кофемолки", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/kofemolki/')),
    InlineKeyboardButton("Фильтр кофеварки", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/filter/')),
]
sub_menu_equipment.add(*sub_menu_equipment_buttons)

# Клавиатура для подменю "Спешиалти кофе"
sub_menu_specialty_coffee = InlineKeyboardMarkup(row_width=2)
sub_menu_specialty_coffee_buttons = [
    InlineKeyboardButton("Что такое спешиалти кофе", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/spetialty/')),
    InlineKeyboardButton("Направления обучения", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/associac/')),
    InlineKeyboardButton("Ассоциация", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/asociac/')),
    InlineKeyboardButton("Дескрипторы", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/discript/')),
    InlineKeyboardButton("Альтернатива", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/alternative/')),
    InlineKeyboardButton("Три волны культуры", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/threewayvs/')),
    InlineKeyboardButton("Молоко и его влияние", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/milk/')),
]
sub_menu_specialty_coffee.add(*sub_menu_specialty_coffee_buttons)

# Клавиатура для подменю "Введение эспрессо"
sub_menu_espresso = InlineKeyboardMarkup(row_width=2)
sub_menu_espresso_buttons = [
    InlineKeyboardButton("История эспрессо", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/vvedenie/')),
    InlineKeyboardButton("Экстракция", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/Whatisesprecco/')),
    InlineKeyboardButton("Зерно", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/Zerno/')),
    InlineKeyboardButton("Стандарты", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/standarts/')),
    InlineKeyboardButton("Дегустация", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/digustation/')),
    InlineKeyboardButton("Оборудование", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/oborud/')),
]
sub_menu_espresso.add(*sub_menu_espresso_buttons)

# Клавиатура для подменю "Service Book"
sub_menu_service_book = InlineKeyboardMarkup(row_width=2)
sub_menu_service_book_buttons = [
    InlineKeyboardButton("Service Book", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/service/')),
    InlineKeyboardButton("Контакт", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/contact/')),
    InlineKeyboardButton("Потребности", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/potreb/')),
    InlineKeyboardButton("Презентация товара", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/prezent/')),
    InlineKeyboardButton("Возражения", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/vozraj/')),
    InlineKeyboardButton("Завершение продажи", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/prodaj/')),
    InlineKeyboardButton("Обратная связь", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/sbor/')),
]
sub_menu_service_book.add(*sub_menu_service_book_buttons)

# Клавиатура для подменю "Сроки годности"
sub_menu_expiry_dates = InlineKeyboardMarkup(row_width=2)
sub_menu_expiry_dates_buttons = [
    InlineKeyboardButton("Сроки годности", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/dezerts/')),
    InlineKeyboardButton("Описание вкуса", web_app=WebAppInfo(url='https://iiiamah4ik.github.io/vkus/')),
]
sub_menu_expiry_dates.add(*sub_menu_expiry_dates_buttons)

# Состояния для отслеживания выбора разделов
class MenuState:
    Theory = "theory"
    Equipment = "equipment"
    SpecialtyCoffee = "specialty_coffee"
    Espresso = "espresso"
    ServiceBook = "service_book"
    ExpiryDates = "expiry_dates"

# Функция для удаления предыдущего сообщения
async def delete_last_message(message: types.Message):
    last_message = message.message_id - 2
    await bot.delete_message(message.chat.id, last_message)
async def delete_last_message2(message: types.Message):
    last_message = message.message_id - 1
    await bot.delete_message(message.chat.id, last_message)

# Функция для обработки команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):  # Удаляем предыдущие сообщения
    await message.answer("Приступим к изучению", reply_markup=menu_keyboard)

@dp.message_handler(commands=['menu'])
async def show_menu(message: types.Message):
    await delete_last_message(message)
    await delete_last_message2(message)
    await bot.send_message(message.chat.id, "Приступим к изучению", reply_markup=menu_keyboard)
# Обработчик для раздела "Теория зерна"
@dp.message_handler(lambda message: message.text == "Теория зерна")
async def theory_menu(message: types.Message):
    await delete_last_message(message)
    await delete_last_message2(message)
    await message.answer("Выберите подраздел:", reply_markup=sub_menu_theory)
    await MenuState.Theory.set()

# Обработчик для раздела "Оборудование"
@dp.message_handler(lambda message: message.text == "Оборудование")
async def equipment_menu(message: types.Message):
    await delete_last_message(message)
    await delete_last_message2(message) # Удаляем предыдущие сообщения
    await message.answer("Выберите подраздел:", reply_markup=sub_menu_equipment)
    await MenuState.Equipment.set()

# Обработчик для раздела "Спешиалти кофе"
@dp.message_handler(lambda message: message.text == "Спешиалти кофе")
async def specialty_coffee_menu(message: types.Message):
    await delete_last_message(message)
    await delete_last_message2(message) # Удаляем предыдущие сообщения
    await message.answer("Выберите подраздел:", reply_markup=sub_menu_specialty_coffee)
    await MenuState.SpecialtyCoffee.set()

# Обработчик для раздела "Введение эспрессо"
@dp.message_handler(lambda message: message.text == "Введение эспрессо")
async def espresso_menu(message: types.Message):
    await delete_last_message(message)
    await delete_last_message2(message) # Удаляем предыдущие сообщения
    await message.answer("Выберите подраздел:", reply_markup=sub_menu_espresso)
    await MenuState.Espresso.set()

# Обработчик для раздела "Service Book"
@dp.message_handler(lambda message: message.text == "Service Book")
async def service_book_menu(message: types.Message):
    await delete_last_message(message)
    await delete_last_message2(message) # Удаляем предыдущие сообщения
    await message.answer("Выберите подраздел:", reply_markup=sub_menu_service_book)
    await MenuState.ServiceBook.set()

# Обработчик для раздела "Сроки годности"
@dp.message_handler(lambda message: message.text == "Сроки годности")
async def expiry_dates_menu(message: types.Message):
    await delete_last_message(message)
    await delete_last_message2(message)
    await message.answer("Выберите подраздел:", reply_markup=sub_menu_expiry_dates)
    await MenuState.ExpiryDates.set()

# Обработчик для подразделов "Теории зерна"
@dp.callback_query_handler(Text(equals=["history", "distribution", "habitat", "arabica_robusta", "taste", "terroir", "roasters", "berry_structure", "harvest_methods", "processing_methods", "fermentation", "roasting"]))
async def theory_sub_menu(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        selected_theory = callback_query.data
        data["selected_theory"] = selected_theory
        await delete_last_message(callback_query.message)
        await delete_last_message2(callback_query.message)# Удаляем предыдущие сообщения
        await callback_query.message.edit_text(f"Вы выбрали: {selected_theory}. Приступим к изучению {selected_theory}.")

# Обработчик для подразделов "Оборудования"
@dp.callback_query_handler(Text(equals=["coffee_machines", "coffee_grinders", "coffee_maker_filter"]))
async def equipment_sub_menu(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        selected_equipment = callback_query.data
        data["selected_equipment"] = selected_equipment
        await delete_last_message(callback_query.message)
        await delete_last_message2(callback_query.message) # Удаляем предыдущее сообщение
        await callback_query.message.edit_text(f"Вы выбрали: {selected_equipment}. Приступим к изучению {selected_equipment}.")

# Обработчик для подразделов "Спешиалти кофе"
@dp.callback_query_handler(Text(equals=["what_is_specialty_coffee", "training_directions", "association", "descriptors", "alternative", "coffee_culture", "milk_impact"]))
async def specialty_coffee_sub_menu(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        selected_specialty_coffee = callback_query.data
        data["selected_specialty_coffee"] = selected_specialty_coffee
        await delete_last_message(callback_query.message)
        await delete_last_message2(callback_query.message)
        await callback_query.message.edit_text(f"Вы выбрали: {selected_specialty_coffee}. Приступим к изучению {selected_specialty_coffee}.")

# Обработчик для подразделов "Введение эспрессо"
@dp.callback_query_handler(Text(equals=["espresso_history", "what_is_espresso", "espresso_standards", "tasting_time"]))
async def espresso_sub_menu(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        selected_espresso = callback_query.data
        data["selected_espresso"] = selected_espresso
        await delete_last_message(callback_query.message)
        await delete_last_message2(callback_query.message)
        await callback_query.message.edit_text(f"Вы выбрали: {selected_espresso}. Приступим к изучению {selected_espresso}.")

# Обработчик для подразделов "Service Book"
@dp.callback_query_handler(Text(equals=["service_book", "contact", "needs", "product_presentation", "objections", "sales_completion", "feedback"]))
async def service_book_sub_menu(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        selected_service_book = callback_query.data
        data["selected_service_book"] = selected_service_book
        await delete_last_message(callback_query.message)
        await delete_last_message2(callback_query.message) # Удаляем предыдущее сообщение
        await callback_query.message.edit_text(f"Вы выбрали: {selected_service_book}. Приступим к изучению {selected_service_book}.")

# Обработчик для подразделов "Сроки годности"
@dp.callback_query_handler(Text(equals=["desserts", "lunches", "consumables"]))
async def expiry_dates_sub_menu(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        selected_expiry_date = callback_query.data
        data["selected_expiry_date"] = selected_expiry_date
        await delete_last_message(callback_query.message)
        await delete_last_message2(callback_query.message)# Удаляем предыдущее сообщение
        await callback_query.message.edit_text(f"Вы выбрали: {selected_expiry_date}. Приступим к изучению {selected_expiry_date}.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
