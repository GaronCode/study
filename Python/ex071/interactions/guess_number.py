from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


class guess_number:
    
    players = {}
    
    def __init__(self) -> None:
        self.players = {}
    async def command(self,update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        text = ''
        if self.new_player(update.effective_user.id,update.effective_user.first_name):
            text = 'Бот загадал число от 1 до 1000. Попробуйте его отгадать! '
        req = update.message.text.split()
        if len(req) > 1:
            attempt = int(req[1])
            if attempt > 0 and attempt < 1001:
                player = self.players[update.effective_user.id]
                player['attempts'] += 1
                if player['guess_number'] == attempt:
                    text += '{}, вы угадали! Поздравляем! Попыток: {}'.format(player['name'], player['attempts'])
                    del self.players[update.effective_user.id]
                else:  
                    text += 'Не отгадали :( Попробуйте снова!'

        else:
            text += 'Чтобы отгадать число, введите его через пробел.'
        await update.message.reply_text(text)
    
    def new_player(self,player_id,player_name) -> bool:
        import random as r
        if player_id in self.players:
            return False
        
        self.players[player_id] = {
            'name': player_name,
            'guess_number': r.randint(1,1000),
            'attempts': 0
        }
        print(self.players[player_id])
        return True