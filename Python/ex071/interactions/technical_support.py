from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import re
from lib import read_file, write_to_file

class Support:

    FILE_NAME = 'support_requests.csv'
    SUPPORT_ANSWERS = 'support_answers.csv'
    STANDARD_MESSANGE = 'неизвестен'
    
    def __init__(self) -> None:
        pass

    async def request(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        req = update.message.text.split(' ',1)
        text = ''
        if len(req) > 1:
            text += "Спасибо за обращение! Ваше сообщение записано! \n Текст сообщения: {}".format(req[1])
            text_to_file = '{},{},"{}"\n'.format(update.effective_user.id, update.effective_user.first_name, req[1].replace('"', ' '))
            write_to_file(text_to_file, self.FILE_NAME, 'a')
        else:
            text += 'Введите сообщение вместе с коммандой\n Пример: /support текст сообщения'
        
        await update.message.reply_text('Ответ поддержки: {}'.format(text))

    async def question(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        req = update.message.text.split(' ',1)
        text = ''
        if len(req) > 1:
            text += "Ваш вопрос: {} \n".format(req[1])
            all_questions = {}
            for question in read_file(self.SUPPORT_ANSWERS).split('\n'):
                splited= question.split(',')
                all_questions[splited[0]] = splited[1]
            text += "Ответ: "
            if req[1] in all_questions:
                text += all_questions[req[1]]
            else:
                text += all_questions[self.STANDARD_MESSANGE]

            
            
        else:
            text += 'Введите ваш вопрос вместе с коммандой\n Пример: /q текст сообщения'
        
        await update.message.reply_text('Ответ поддержки: {}'.format(text))