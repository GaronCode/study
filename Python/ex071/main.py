
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from commands import com




app = ApplicationBuilder().token("5786494992:AAEGcPJ2USficrtLKMsRP179Hhk7nkGOEBQ").build()



print('start')

for item in com:
    for command in item['commands']:
        app.add_handler(CommandHandler(command, item['fx']))



app.run_polling()