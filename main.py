from telegram.ext import Application, CommandHandler, CallbackContext
from telegram import Update
import requests
import re
import asyncio

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['https://telegram.me/IbmecJrBot']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def bop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello!')

async def main():
    application = Application.builder().token('7267610597:AAFv-mOthdzcqTglYV54QHM4w9UHtAzkw7U').build()
    application.add_handler(CommandHandler('start', start))
    await application.initialize()
    await application.start()
    async with application:
        await application.updater.start_polling()


if __name__ == '__main__':
    try:
        # Verifica se o loop já está rodando
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # Se não houver loop rodando, cria um
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    # Executa a função main no loop existente
    loop.run_until_complete(main())