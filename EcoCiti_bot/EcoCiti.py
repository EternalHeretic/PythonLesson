Token = '7922839201:AAHCwwd1ouZDVkvtI2gQA0MpR9zOpNy2bHg'
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define conversation states
NAME, PHONE, ADDRESS, TIME, AREA, ADDITIONAL_CORNERS, LIGHT_FIXTURES, PIPE_OUTLINES, CHANDELUIERS, CURTAIN_RODS = range(10)

# Predefined prices
PRICES = {
    'area': 1000,  # 1000 rubles per square meter
    'additional_corners': 500,  # 500 rubles per additional corner
    'light_fixtures': 50,
    'pipe_outlines': 30,
    'chandeliers': 100,
    'curtain_rods': 20,
}

# Handler functions defined as async
async def start(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text(
        'Привет! Этот бот принимает заявки на замер натяжных потолков.\n'
        'Введите ваше имя:'
    )
    return NAME

async def receive_name(update: Update, context: CallbackContext) -> int:
    name = update.message.text
    if name.isalpha():
        context.user_data['name'] = name
        await update.message.reply_text('Введите ваш номер телефона (формат +7XXXXXXXXXX):')
        return PHONE
    else:
        await update.message.reply_text('Имя должно содержать только буквы. Пожалуйста, введите имя еще раз:')
        return NAME

async def receive_phone(update: Update, context: CallbackContext) -> int:
    phone = update.message.text
    if phone.startswith('+7') and len(phone) == 12 and phone[2:].isdigit():
        context.user_data['phone'] = phone
        await update.message.reply_text('Введите ваш адрес:')
        return ADDRESS
    else:
        await update.message.reply_text('Номер телефона должен быть в формате +7XXXXXXXXXX. Пожалуйста, введите номер еще раз:')
        return PHONE

async def receive_address(update: Update, context: CallbackContext) -> int:
    context.user_data['address'] = update.message.text
    await update.message.reply_text('Введите удобное время для замера (например, "10:00 25.05.2023"):')
    return TIME

# Define other handler functions similarly...

async def cancel(update: Update, context: CallbackContext) -> int:
    await update.message.reply_text('Операция отменена.')
    return ConversationHandler.END

def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    application = ApplicationBuilder().token(Token).build()

    # Set up the ConversationHandler with the states NAME, PHONE, etc.
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_phone)],
            ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_address)],
            # Add other states here...
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    application.add_handler(conv_handler)

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()