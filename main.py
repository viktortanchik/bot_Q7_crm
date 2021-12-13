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
import re

#row = rows.clear()
rows = (get_all(con))


def all_users():
    rows = (get_all(con))
    print("all_users>>",rows)
    return rows



#rows.append(get_all(con))



@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.delete()
    # rows.clear()
    # for i in get_all(con):
    #     rows.append(i)
    # print(rows)

    data =[str(message.chat.title),'user_id',str(message['from'].username),'real_name','name_of_agency','payid','strikes','hyperlink','tag','comments','deposit']
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

global newrows
newrows=['test_3']
@dp.message_handler(Text(equals="ALL USER"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["на главную"]
    keyboard.add(*buttons)
    rows= get_all(con)
    print('rows>>',rows)
    mes=''
    for row in range (len(rows)):
        mes += ' /'
        print(rows[row])
        mes+=str(rows[row][3])
        newrows.append(rows[row][3])
        print('newrows >> ', newrows)
        #mes+=' /'cxvbcvxxb
    dp.message_handler(commands=[newrows[row] for row in range(len(newrows))])
    await message.answer(mes, reply_markup=keyboard)


@dp.message_handler(commands=[newrows[row] for row in range (len(newrows))])
#@dp.message_handler(commands=[all_users()[row][3] for row in range (len(all_users()))])
async def process_start_command(message: types.Message):
    print("message.text >> ",message.text)
    s1 = re.sub("[/]", "", message.text)
    print(message['from'].id)
    print('s1 >> ',s1)
    file = open(str(message['from'].id)+"user.txt", "w")
    file.write(s1)
    file.close()
    card = sql_select_id(con,s1)
    buttons =[]
    name_buttons=['chat','user_id','username','real_name','name_of_agency','payid','strikes','hyperlink','tag','comments','deposit']
    lennames=0
    for i in card[1:]:
        print(i)
        buttons.append(types.InlineKeyboardButton(text=name_buttons[lennames]+' '+i, callback_data=name_buttons[lennames]))
        lennames+=1

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("card "+s1, reply_markup=keyboard) # test_pots_pip  -1001600149738   # test_chat -1001392919876

    #await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

name_buttons=['chat','user_id','username','real_name','name_of_agency','payid','strikes','hyperlink','tag','comments','deposit']
@dp.callback_query_handler(text=[button for button in name_buttons])
async def send_random_value(call: types.CallbackQuery):
    print(call)
    users = open(str(call['from'].id)+"user.txt", "r")
    user = users.read()
    users.close()

    print(call.data)
    temps = open(str(call['from'].id) + "temp.txt", "r")
    UPDATE = temps.read()
    users.close()

    set = (str(call.data))
    set_name = (str(UPDATE))
    where = ('username')
    where_name =(str(user))
    sql_update(con,set,set_name,where,where_name)
    await call.message.answer("You are in the user card "+user+' and trying to change '+call.data)

    #await message.answer(mes, reply_markup=keyboard)



@dp.message_handler(Text(equals="Найти пользователя"))
async def with_puree(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["изменить", "на главную"]
    keyboard.add(*buttons)

    await message.answer("Что бы изменить настройки пользователя введите его никнейм ", reply_markup=keyboard)




@dp.message_handler()
async def echo_message(msg: types.Message):
    print(msg)
    print(msg.chat.title)
    print(msg.text)
    file = open(str(msg['from'].id) + "temp.txt", "w")
    file.write(str(msg.text))
    file.close()
    #mess = 'Пользователь '+msg['from'].username+' в чате '+msg.chat.title+' написал такой текст '+msg.text
    #await bot.send_message(msg.from_user.id, mess)


if __name__ == '__main__':
    executor.start_polling(dp)