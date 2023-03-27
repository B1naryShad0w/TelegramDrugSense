#libraries and stuff
import logging
import openai
import os
from telegram import Update, ForceReply
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters


#api keys
openai.api_key = "<API KEY>"
telegram_api_key = "<API KEY>"


#system message to openai
openai_system = "You are a telegram bot named DrugSense who's goal is to advise students on safe drug usage. Don't try to discourage taking drugs, rather tell them how to do so safely. Try to insert emojis when appropriate but don't repeat emojis much. Cursing and NSFW humor is encouraged. Try to stay under 150 tokens."


#setup debugging
logging.basicConfig(
    filename="log",
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


#start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    request = [
        {"role": "system", "content": openai_system + "greet " + update.effective_user.first_name},
        {"role": "user", "content": "who are you and what can you help me with?"}
    ]
    logging.info("Request: ")
    logging.info(request)

    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = request
    )
    logging.info("Reply: ")
    logging.info(response['usage'])
    logging.info(response['choices'][0]['message'])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response['choices'][0]['message']['content'], reply_markup=ForceReply())


#response from openai
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        request = [
                {"role": "system", "content": openai_system + "no greetings"},
                {"role": "assistant", "content": update.message.reply_to_message.text},
                {"role": "user", "content": update.message.text}
            ]
    except AttributeError:
        request = [
                {"role": "system", "content": openai_system + "no greetings"},
                {"role": "user", "content": update.message.text}
            ]
    logging.info("Request: ")
    logging.info(request)

    response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages= request
    )
    logging.info("Reply: ")
    logging.info(response['usage'])
    logging.info(response['choices'][0]['message'])

    await context.bot.send_message(chat_id=update.effective_chat.id, text=response['choices'][0]['message']['content'], reply_markup=ForceReply())


if __name__ == '__main__':
    application = ApplicationBuilder().token(telegram_api_key).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()