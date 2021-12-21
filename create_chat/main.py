import sqlite3
import time

from telethon import sync, events

from telethon.sync import TelegramClient
from telethon import functions, types

from telethon.tl.types import PeerUser, PeerChat, PeerChannel

# для корректного переноса времени сообщений в json
from datetime import date, datetime
# x = 1
#
# db = sqlite3.connect('Account.db')
# cur = db.cursor()
# cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
# time.sleep(0.4)
# Phone = str(cur.fetchone()[0])
# print("Входим в аккаунт: " + Phone, ' Номер ',x)
# cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
# time.sleep(0.4)
# api_id = str(cur.fetchone()[0])
# cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
# time.sleep(0.4)
# api_hash = str(cur.fetchone()[0])
# session = str("anon" + str(x))
#
# client = TelegramClient(session, api_id, api_hash)
# client.start()
# x+= 1
 # Выбор номера бота
#print(client.get_me().stringify())
# user_id=674868256
#channel_id=1622152087


#client.send_message('username', 'Hello! Talking to you from Telethon')
#client.send_file('username', '/home/myself/Pictures/holidays.jpg')

#client.download_profile_photo('me')
#messages = client.get_messages('username')
#messages[0].download_media()
#client.send_message('My awesome title_02', 'Hello! Talking to you from Telethon')


#['@Ihortihor',674868256]

chat_name='test_Q7_create_chat_02'
admin_id=[674868256]#['@Ihortihor',674868256]
account=1
x = account


db = sqlite3.connect('Account.db')
cur = db.cursor()
cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
Phone = str(cur.fetchone()[0])
print("Входим в аккаунт: " + Phone, ' Номер ',x)
cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
api_id = str(cur.fetchone()[0])
cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
time.sleep(0.4)
api_hash = str(cur.fetchone()[0])
session = str("anon" + str(x))

client = TelegramClient(session, api_id, api_hash)
client.start()
x+= 1


@client.on(events.NewMessage())
async def handler(event):
    print(event)
    #await event.respond('Hey!')

# client.run_until_disconnected()
#
# # chat_name='My awesome title_05'
# results = client(functions.messages.CreateChatRequest(
#     users=admin_id,
#     title=chat_name
# ))
# # print(results)
# # print(results.chats[0].id)
# # time.sleep(1)
# # client.send_message(results.chats[0].id, 'Hello! Talking to you from Telethon')
# chat_id= int(results.chats[0].id)
# #557620350
# result = client(functions.messages.EditChatAdminRequest(
#     chat_id=chat_id,
#     user_id=admin_id,  # '@Ihortihor',
#     is_admin=True
# ))
# print(result)
# print(result.stringify())
client.run_until_disconnected()

def create_chat(chat_name,admin_id,account):
    x = account

    db = sqlite3.connect('Account.db')
    cur = db.cursor()
    cur.execute(f"SELECT PHONE FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    Phone = str(cur.fetchone()[0])
    print("Входим в аккаунт: " + Phone, ' Номер ', x)
    cur.execute(f"SELECT API_ID FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_id = str(cur.fetchone()[0])
    cur.execute(f"SELECT API_HASH FROM Account WHERE ID = '{x}'")
    time.sleep(0.4)
    api_hash = str(cur.fetchone()[0])
    session = str("anon" + str(x))

    client = TelegramClient(session, api_id, api_hash)
    client.start()
    x += 1

    #chat_name='My awesome title_05'
    results = client(functions.messages.CreateChatRequest(
        users=admin_id,
        title=chat_name
    ))
    time.sleep(1)
    #username =  client.get_peer_id(chat_name)
    #username = client.get_entity(PeerChat(chat_name))
    print(">>>",type(chat_name))
    username = client.get_entity(chat_name)
    print(username)
    result = client(functions.messages.EditChatAdminRequest(
        chat_id=username.id,
        user_id=admin_id, #'@Ihortihor',
        is_admin=True
        ))
    print(result)
    #print(result.stringify())
    client.run_until_disconnected()

#create_chat(chat_name,admin_id,account)