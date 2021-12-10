from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
#5049839636:AAGU4R4Ibn-qwonYWMBfFWHfU0xM6LubqFA
import sqlite3
from db import *
bot = Bot(token="5049839636:AAGU4R4Ibn-qwonYWMBfFWHfU0xM6LubqFA")
dp = Dispatcher(bot)
con = sqlite3.connect('bot.sqlite')

rows=(get_all(con))
#row = rows.clear()



#rows.append(get_all(con))



@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.delete()
    rows.clear()
    for i in get_all(con):
        rows.append(i)
    print(rows)

    data =[str(message.chat.title),'user_id',str(message['from'].username),'real_name','name_of_agency','payid','strikes','hyperlink','tag','comments']
    sql_insert_all(con,data)
    await bot.send_message(674868256, "Привет!\n добавлен новый пользователь ")
    #rowsget_all(con)

    #await message.reply("Привет!\n добавлен новый пользователь ")

@dp.message_handler(commands='start')
async def process_start_command(message: types.Message):
    print(message['from'].username)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Найти пользователя","ALL USER"]
    keyboard.add(*buttons)
    await message.answer("готов к работе", reply_markup=keyboard)



@dp.message_handler(Text(equals="ALL USER"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["на главную"]
    keyboard.add(*buttons)
    rows= get_all(con)
    print(rows)
    mes=''
    for row in range (len(rows)):
        mes += ' /'
        print(rows[row])
        mes+=str(rows[row][3])
        #mes+=' /'
    await message.answer(mes, reply_markup=keyboard)


@dp.message_handler(commands=[rows[row][3] for row in range (len(rows))])
async def process_start_command(message: types.Message):
    print("ALL OK")
        #mes+='\n'


    #await message.answer(mes, reply_markup=keyboard)



@dp.message_handler(Text(equals="Найти пользователя"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["изменить", "на главную"]
    keyboard.add(*buttons)

    await message.answer("Что бы изменить настройки пользователя введите его никнейм ", reply_markup=keyboard)




    await message.reply("Отличный выбор!")



@dp.message_handler()
async def echo_message(msg: types.Message):
    print(msg)
    print(msg.chat.title)
    print(msg.text)
    #mess = 'Пользователь '+msg['from'].username+' в чате '+msg.chat.title+' написал такой текст '+msg.text
    #await bot.send_message(msg.from_user.id, mess)


if __name__ == '__main__':
    executor.start_polling(dp)