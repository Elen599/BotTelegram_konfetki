from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from control import *
import model

bot_token = "5671173769:AAFE8QhdtD3-xf6Gx0BZcnLk6OG3HpKNACs"
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, f"Привет, друг!\nОзнакомься с условиями игры с ботом:\n"
                                                       f"На столе лежат 50 конфет\nКаждый игрок может взять от 1 до 10 конфет\n"
                                                       f"Выигрывает тот, кто возьмет конфеты последним.\n\n /begin - начать игру\n /stop - остановить игру")


def begin_game(update, context):
    context.bot.send_message(update.effective_chat.id, 'Возьми конфеты')
    return 1


def game_proces(update, context):
    if model.balance > 0:
        update.message.reply_text(result_massage(update.message.text))
        return 1
    else:
        return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
begin_game_handler = ConversationHandler(
        entry_points=[CommandHandler('begin', begin_game)],
        states={1: [MessageHandler(Filters.text & ~Filters.command, game_proces)]},
        fallbacks=[CommandHandler('stop', stop)])


dispatcher.add_handler(begin_game_handler)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()

# print (result_massage("4"))