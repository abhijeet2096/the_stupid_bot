#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import spacy
nlp = spacy.load('en')
import MySQLdb

db = MySQLdb.connect("localhost","root","Jigyasha#$","tt" )
cursor = db.cursor()
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)



Start_loc,End_loc = range(2)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    reply_keyboard = [['Mandi', 'South', 'North']]
    update.message.reply_text(
        'Hi! I am the stupid Bot.'
        'Send /cancel to stop talking to me.\n\n'
        'Where Do you wanna go?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True))
    delay(1000)
    Start = update.message.text
    update.message.reply_text(Start)
    return Start


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    doc = nlp(update.message.text)
    flag_mandi_to,flag_south_to,flag_north_to = 0,0,0
    flag_mandi_from,flag_south_from,flag_north_from = 0,0,0
    for chunk in doc.noun_chunks:
        if(chunk.root.text == "Mandi" and chunk.root.head.text == "to"):
            flag_mandi_to = 1;
        elif(chunk.root.text == "South" and chunk.root.head.text == "to"):
            flag_south_to = 1;
        elif(chunk.root.text == "North" and chunk.root.head.text == "to"):
            flag_north_to = 1;
        elif(chunk.root.text == "Mandi" and chunk.root.head.text == "from"):
            flag_mandi_from = 1;
        elif(chunk.root.text == "South" and chunk.root.head.text == "from"):
            flag_south_from = 1;
        elif(chunk.root.text == "North" and chunk.root.head.text == "from"):
            flag_north_from = 1;

    if(flag_north_from and flag_south_to):
        #update.message.reply_text("you want to go from north to south")
        cursor.execute("select t.Day, t.Vehicle, t.North_South  from main as t where t.North_South + 120000 - current_time() > 0 and  t.North_South + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("you want to go from north to south")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])
    elif(flag_north_from and flag_mandi_to):
        cursor.execute("select t.Day, t.Vehicle, t.North_South  from main as t where t.North_South + 120000 - current_time() > 0 and  t.North_South + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("you want to go from north to mandi , you should take north to south and south to mandi")
        update.message.reply_text("North to South in next 1 hr!")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])
        cursor.execute("select t.Day, t.Vehicle, t.South_Mandi  from main as t where t.South_Mandi + 120000 - current_time() > 0 and  t.South_Mandi + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("South to North in next 1 hr!")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])

    elif(flag_mandi_from and flag_south_to):
        cursor.execute("select t.Day, t.Vehicle, t.Mandi_South  from main as t where t.Mandi_South + 120000 - current_time() > 0 and  t.Mandi_South + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("you want to go from mandi to south")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])
    elif(flag_mandi_from and flag_north_to):
        cursor.execute("select t.Day, t.Vehicle, t.Mandi_South  from main as t where t.Mandi_South + 120000 - current_time() > 0 and  t.Mandi_South + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("you want to go from mandi to north, you should take mandi to south and then south to north")
        update.message.reply_text("Mandi to South in next 1 hr!")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])
        cursor.execute("select t.Day, t.Vehicle, t.South_North  from main as t where t.South_North + 120000 - current_time() > 0 and  t.South_North + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("South to North in next 1 hr!")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])

    elif(flag_south_from and flag_mandi_to):
        cursor.execute("select t.Day, t.Vehicle, t.South_Mandi  from main as t where t.South_Mandi + 120000 - current_time() > 0 and  t.South_Mandi + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("you want to go from south to mandi")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])
    elif(flag_south_from and flag_north_to):
        cursor.execute("select t.Day, t.Vehicle, t.South_North  from main as t where t.South_North + 120000 - current_time() > 0 and  t.South_North + 120000 - current_time()  < 010000 limit 1 ;")
        data = cursor.fetchone()
        update.message.reply_text("you want to go from south to north")
        update.message.reply_text(data[0])
        update.message.reply_text(data[1])

        #update.message.reply_text(chunk.root.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("Key - Here")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
