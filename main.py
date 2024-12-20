from dotenv import load_dotenv
import os
from telegram import Update, Bot
from telegram.ext import Application, CommandHandler, CallbackContext
import json

load_dotenv()

# Substitua 'YOUR_TOKEN' pelo token do seu bot
TOKEN = os.getenv("TELEGRAM_KEY")

# Lista global para armazenar usuários que aceitaram ser mencionadosgit
notified_users = set()

# Função que responde ao comando /start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Ola, Use /all para marcar todos os membros do grupo.')

#Função para colocar os participantes do grupo na lista



# Função para mencionar uma lista manual de usernames
async def mention_members(update: Update, context: CallbackContext) -> None:
    # Carregar dados do arquivo JSON
    with open('members.json', 'r') as file:
        data = json.load(file)
        members = data['Nome']
    
    mentions = [f'@{str(member)}' for member in members]

    if mentions:
        await update.message.reply_text(' '.join(mentions))
    else:
        await update.message.reply_text('Não consegui encontrar membros para mencionar.')



# Define a função principal
if __name__ == '__main__':
    # Cria a aplicação com o token do bot
    application = Application.builder().token(TOKEN).build()

    # Adiciona os manipuladores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("mention_members", mention_members))  # Comando para mencionar uma lista manual de usernames
 

    # Inicia a aplicação em modo de polling
    application.run_polling()