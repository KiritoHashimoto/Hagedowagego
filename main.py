from random import randint
from aiogram import Bot, Dispatcher, executor, types
from secret import Api
import sqlite3


bot = Bot(Api)
DP = Dispatcher(bot)

real_world = ""


@DP.message_handler()
async def stage1(message: types.Message):
    chat_id = message.chat.id
    read_file = (open("words.txt", "r"))
    already_read_file = read_file.read()
    chat_id = message.chat.id
    with sqlite3.connect("id_chat.db") as connect:
        cursor = connect.cursor()
        word = already_read_file.split(",")
        global real_world
        real_world = word[randint(0, len(word) - 1)]
        cursor.execute(f"UPDATE memori SET word = {real_world} WHERE id_chat = {chat_id}")
        # fake_word = list(real_world)
        # for i in range(0, len(real_world), 2):
        #     random = randint(0, len(real_world) - 1)
        #     fake_word[random] = " _ "
        # await message.answer("".join(fake_word))

@DP.message_handler()
def none_id(message: types.Message):
    with sqlite3.connect("id_chat.db") as connect:
        cursor = connect.cursor()
    cursor.execute("INSERT INTO memori VALUES( , -, 0),")



@DP.message_handler(commands=["startik"])
async def id_check(message: types.Message):
    chat_id = message.chat.id
    with sqlite3.connect("id_chat.db") as connect:
        cursor = connect.cursor()
    if cursor.execute(f"SELECT * FROM memori WHERE id_chat = {chat_id}") != None:
        stage1
    else:
        none_id



@DP.message_handler(state='*')
async def check(message: types.Message):
    if message.text == real_world:
        await message.answer("GG")


executor.start_polling(DP, skip_updates=True)
