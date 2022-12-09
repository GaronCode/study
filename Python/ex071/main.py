
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import com


API_KEY = "9999999999:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

app = ApplicationBuilder().token().build()



print('start')

for item in com:
    for command in item['commands']:
        app.add_handler(CommandHandler(command, item['fx']))



app.run_polling()