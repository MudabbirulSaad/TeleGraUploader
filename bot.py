import logging
import os
from telegram import Update, parsemode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegraph import upload_file
from config import Config, Text

TOKEN = Config.BOT_TOKEN
WELCOME_TEXT = Text.WELCOME_TEXT
HELP_TEXT = Text.HELP_TEXT
MAINTAINER = Text.MAINTAINER

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"{WELCOME_TEXT}\n\n*Made with ❤ by @MudabbirulSaad*\n*Bot maintained by {MAINTAINER}*", parse_mode="Markdown")


def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(HELP_TEXT, parse_mode="Markdown")


def image_upload(update: Update, context: CallbackContext) -> None:
    file_id = update.message.photo[-1].file_id
    fileName = file_id + ".jpg"
    newFile = context.bot.get_file(file_id)
    newFile.download(fileName)
    response = upload_file(fileName)
    update.message.reply_text(f"*Here is your telegraph link* 👇\n\n`https://telegra.ph{response[0]}`\n\n*Tnx for using me!*\n*Made with ❤ by @MudabbirulSaad*\n*Bot maintained by {MAINTAINER}*", parse_mode="Markdown")
    os.remove(fileName)

def ot(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("*I can upload image only!*", parse_mode="Markdown")
    

def main():
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.photo & ~Filters.command, image_upload))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, ot))
    dispatcher.add_handler(MessageHandler(Filters.video & ~Filters.command, ot ))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()