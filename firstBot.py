import logging, os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv('TOKEN_TESTES')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nomeDoUsuario = update.effective_user.name
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Olá, {nomeDoUsuario}, sou um Bot")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()