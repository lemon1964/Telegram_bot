from telethon.sync import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon import events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.sessions import StringSession
import re
import redis
import hashlib
# import Bot

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


api_id = 23....37
api_hash = "0f3......12d"
phone = "+79....346"

user_id = 27....845


conn = redis.Redis(host='localhost', port=6379, db=2, charset="utf-8", decode_responses=True)
# TRIGGER = ['создать бота', 'нужен бот', 'сделать бота', 'сделать чат-бот', 'нужен кодер','нужен программист','нужен прогер','написать бот','кто делает бот','кто сделает бот','пишет бот','создаст бота']
TRIGGER = ['цена', 'привет', 'кто', 'курс', 'сайт', 'продам', 'канал', 'эфир', 'дождь', 'на', 'ак', 'се', 'ла', 'а']
hash_object = []
string_session = '' # тут должен быть ключ стринг сессии, если вы используете ее
id = 27.....45 # ваше id, куда бот будет скидывать вам ссылки на найденные сообщения
#client = TelegramClient(StringSession(string_session), 2496 , "8da85b0d5bfe62527e5b244c209159c3", flood_sleep_threshold = 0) #способ авторизации с помощью ключа типа строка
# client = TelegramClient('my_account_session', 2496 , "8da85b0d5bfe62527e5b244c209159c3", flood_sleep_threshold = 0) #способ авторизации с помощью файлы сессии
client = TelegramClient(phone, api_id, api_hash, flood_sleep_threshold = 0)
client.start()
#print('String Session = ', client.session.save()) # получение ключа типа string_session, который надо вставить в переменную string_session



@client.on(events.NewMessage) #апдейт на новые сообщения только из групп
async def hahdler_group(event):
    bot = Bot(token='584...............CqEtk', parse_mode=types.ParseMode.HTML)
    if event.is_group == True:
        r = re.compile("|".join(TRIGGER), flags=re.I)
        list_count = r.findall(event.raw_text)
        if len(list_count) >= 1:
            # if conn.get(event.from_id.user_id) == None: #чтобы не было повторов от одного id в разных группых в течении 200 сек
                if not hashlib.md5(str(str(event.from_id.user_id)+event.raw_text).encode()).hexdigest() in hash_object: #проверяем дубилрование сообщений от одного юзера
                    out = ''.join(list_count)
                    # await Bot.bot.send_message(id, "Триггер сработал на <b>"+str(list_count)+"</b>\nТекст сообщения: "+str(event.raw_text.replace(out,"<b>"+out+"</b>"))+"\nСсылка на сообщение: <i>t.me/c/"+str(event.peer_id.channel_id)+"/"+str(event.message.id)+"</i>", disable_web_page_preview=True)
                    # await bot.send_message(id, "Триггер сработал на <b>"+str(list_count)+"</b>\nТекст сообщения: "+str(event.raw_text.replace(out,"<b>"+out+"</b>"))+"\nСсылка на сообщение: <i>t.me/c/"+str(event.peer_id.channel_id)+"/"+str(event.message.id)+"</i>", disable_web_page_preview=True)
                    await bot.send_message(id, "Триггер сработал на <b>"+str(list_count)+"</b>\nТекст сообщения: "+str(event.raw_text.replace(out,"<b>"+out+"</b>"))+"\nСсылка на сообщение: <i>t.me/c/"+str(event.message.chat.id)+"/"+str(event.message.id)+"</i>", disable_web_page_preview=True)
                    # await bot.send_message(id, "Триггер сработал", disable_web_page_preview=True)
                    conn.set(event.from_id.user_id, 1, ex=200)
                    hash_object.append(hashlib.md5(str(str(event.from_id.user_id)+event.raw_text).encode()).hexdigest())




@client.on(events.NewMessage) #апдейт на новые сообщения только из каналов
async def hahdler_chanell(event):
    bot = Bot(token='584..............CqEtk', parse_mode=types.ParseMode.HTML)
    if not event.is_group and not event.is_private:
            r = re.compile("|".join(TRIGGER), flags=re.I)
            list_count = r.findall(event.raw_text)
            if len(list_count) >= 1:
                    channel_title = await client.get_entity(event.message.chat.id)
                    out = ''.join(list_count)
                    # await Bot.bot.send_message(id, "Триггер сработал на <b>"+str(list_count)+"</b>\nТекст сообщения: "+str(event.raw_text.replace(out,"<b>"+out+"</b>"))+"\nСсылка на сообщение: <i>t.me/c/"+str(event.peer_id.channel_id)+"/"+str(event.message.id)+"</i>", disable_web_page_preview=True)
                    # await bot.send_message(id, "Триггер сработал на <b>"+str(list_count)+"</b>\nТекст сообщения: "+str(event.raw_text.replace(out,"<b>"+out+"</b>"))+"\nСсылка на сообщение: <i>t.me/c/"+"/"+str(event.message.id)+"</i>", disable_web_page_preview=True)
                    await bot.send_message(id, "Триггер сработал на <b>"+str(list_count)+"</b>\nТекст сообщения: "+str(event.raw_text.replace(out,"<b>"+out+"</b>"))+"\nСсылка на сообщение: <i>t.me/c/"+str(event.message.chat.id)+"/"+str(event.message.id)+"</i>", disable_web_page_preview=True)



client.run_until_disconnected()





bot = Bot(token='584917................2CqEtk', parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp)