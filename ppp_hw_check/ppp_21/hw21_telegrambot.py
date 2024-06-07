import telegram
import random
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token = "7332705777:AAGhBzs9Jo42rejhe_VBRQSFIlvzDfEns80"
id = "7264988366"

bot = telegram.Bot(token)
info_message = ('''헤어스타일 추천해줄까?
                머리스타일 추천 받고 싶으면 "짧은머리" or "ㅉ" or "긴머리" or "ㄱ" 입력 ''')
bot.sendMessage(chat_id=id, text=info_message)

updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if (user_text == "짧은머리") or (user_text == "ㅉ"):
        context.user_data['current_style'] = 'short'
        short_hair_images = ["짧은머리1.jpg", "짧은머리2.jpg", "짧은머리3.jpg", "짧은머리4.jpg", "짧은머리5.jpg", "짧은머리6.jpg"]
        selected_image = random.choice(short_hair_images)
        bot.send_photo(chat_id=id, photo=open(selected_image, 'rb'))
        bot.send_message(chat_id=id, text="요건 어때?")

    elif (user_text == "긴머리") or (user_text == "ㄱ"):
        context.user_data['current_style'] = 'long'
        long_hair_images = ["긴머리1.jpg", "긴머리2.jpg", "긴머리3.jpg", "긴머리4.jpg", "긴머리5.jpg"]
        selected_image = random.choice(long_hair_images)
        bot.send_photo(chat_id=id, photo=open(selected_image, 'rb'))
        bot.send_message(chat_id=id, text="이건 어떤데?")

    elif (user_text == "다른거") or (user_text == "별로"):
        current_style = context.user_data.get('current_style')
        if current_style == 'short':
            short_hair_images = ["짧은머리1.jpg", "짧은머리2.jpg", "짧은머리3.jpg", "짧은머리4.jpg", "짧은머리5.jpg", "짧은머리6.jpg"]
            selected_image = random.choice(short_hair_images)
            bot.send_photo(chat_id=id, photo=open(selected_image, 'rb'))
            bot.send_message(chat_id=id, text="요건 어때?")
        elif current_style == 'long':
            long_hair_images = ["긴머리1.jpg", "긴머리2.jpg", "긴머리3.jpg", "긴머리4.jpg", "긴머리5.jpg"]
            selected_image = random.choice(long_hair_images)
            bot.send_photo(chat_id=id, photo=open(selected_image, 'rb'))
            bot.send_message(chat_id=id, text="이건 어떤데?")

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)
