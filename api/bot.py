from telegram import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Bot, Update,ReplyKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, Updater
# import db
import json

TOKEN = "5777160491:AAGZYNh3NjYcen93fdkDbTCkAz7cRW7HLcc"
bot = Bot(token=TOKEN)
class Personal_bot:
    def __init__(self) -> None:
        # self.db = db.DB("Personal.json")
        self.index_list = 0
    def start(update:Update, context:CallbackContext):
        chat_id = update.message.chat_id
        text = "Abdullatif haqidagi barcha rasm va videolar!!"
        key1 = InlineKeyboardButton(text="Rasmlar🌄", callback_data='rasm' )
        key2 = InlineKeyboardButton(text="Videolar📹", callback_data='videolar')
        keyboard = InlineKeyboardMarkup([[key1, key2]])
        bot = context.bot
        bot.send_message(chat_id,text, reply_markup = keyboard)
        
    def pictures(self, update:Update, context:CallbackContext):
        chat_id = update.message.chat_id
        text = "Marhamat rasmlarni tanlang"
        # query = update.callback_query
        # picture = query.data[1:]
        # data = self.db.imeges(picture)
        # img_url = data[0]['url']
        # company = data[-1]
        # mobil = data[1]
        # x = data[2]

        # self.index_list = self.index_list -1
        # index = self.index_list
        
        # inline_list = []
        # inline_str = 'Qidirgan madilingizni tanlang\n\n'
        # n = 1
        # all_index = self.db.company_name(mobil, self.index_list)[1]

        # if all_index-1 > index:
        #     index = index
        # elif all_index-1 <= index:
        #     self.index_list = 0
        #     index = self.index_list

        # for i in self.db.company_name(mobil, index)[0]:
        #     if n <= 10:
        #         inline_str += f'{n}.{i},\n'
        #         inline_list.append([InlineKeyboardButton(f'{n}', callback_data=f'📲{i}')])
        #     n += 1
        # inline_str += f'                                    ⏪{all_index-1}/{abs(index+1)}⏩'
        # inline_list.append([
        #     InlineKeyboardButton(f'ortga⏪', callback_data=f'⏪_{mobil}_{x}_{company}'),
        #     InlineKeyboardButton(f'yopish❌', callback_data=f'❌'), 
        #     InlineKeyboardButton(f'oldinga⏩', callback_data=f'⏩_{mobil}_{x}_{company}')])
        # reply_markup = InlineKeyboardMarkup(inline_list)

        # query.edit_message_text(inline_str)
        # query.edit_message_reply_markup(reply_markup = reply_markup)
        
        

    def query(update:Update, context: CallbackContext):
        query= update.callback_query
        chat_id = query.message.chat_id
        data = query.data
        bot = context.bot
        
        with open('Personal.json', 'r') as rasmlar:
            rasmlar = json.load(rasmlar)
        
        if data == 'rasm':
            bot.sendMessage(chat_id, "Marhamat rasmlar!!")
            for i in rasmlar['Rasmlar']: 
                x = rasmlar["Rasmlar"][i]["url"]              
            bot.send_message(chat_id, x)
        if data == 'videolar':
            bot.sendMessage(chat_id, "Videolar hali joylanmagan!")