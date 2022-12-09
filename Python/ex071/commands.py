from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

from interactions.guess_number import guess_number
from interactions.technical_support import Support
async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    string = ''
    for item in com:
        string+='\n'
        for c in item['commands']:
            string+='/{} '.format(c)
        string+='-> {}'.format(item['help_text'])
        
    await update.message.reply_text(string)

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Server Time: {datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    print(msg)
    items = msg.split()
    await update.message.reply_text('{} + {} = {}'.format(items[1],items[2],float(items[1]) + float(items[2])))

## Задание 
async def expression_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('1 + 4 * 2 = {}'.format(1 + 4 * 2))





com = [
    {
        'commands': ['hi','hello'],
        'fx': hi_command,
        'help_text': 'Ответит своим приветствием на ваше'
    },
    {
        'commands': ['time'],
        'fx': time_command,
        'help_text': 'Выдаст время сервера'
    },
    {
        'commands': ['help'],
        'fx': help_command,
        'help_text': 'Список всех доступных команд'
    },
    {
        'commands': ['sum'],
        'fx': sum_command,
        'help_text': 'Суммирует два числа, переданных через запятую ("/sum 1 2" выдаст 3)'
    },
    {
        'commands': ['expression'],
        'fx': expression_command,
        'help_text': 'Выводит результат выполнения выражения 1 + 4 * 2'
    },
    {
        'commands': ['guess_number', 'gn'],
        'fx': guess_number().command,
        'help_text': 'Игра "Угадай число!"'
    },
    {
        'commands': ['support'],
        'fx': Support().request,
        'help_text': 'Написать в поддержку.Пример:  /support текст обращения'
    },
    {
        'commands': ['question','q'],
        'fx': Support().question,
        'help_text': 'Написать в поддержку.Пример:  /support текст обращения'
    },
]

