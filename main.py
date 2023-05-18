from random import randint
from aiogram import Bot, Dispatcher, executor, types
from Gaben.secret import Api
import json

bot = Bot(Api)
dp = Dispatcher(bot)



@dp.message_handler(commands=["sd"])
async def give_new_word(message: types.Message):
    chat_id = message.chat.id
    read_file = open("words.txt", "r")
    already_read_file = read_file.read()
    words = already_read_file.split(",")
    real_word = words[randint(0, len(words) - 1)]
    with open("id_chat.json", "r") as id_chat_value:
        dict_as_file = json.load(id_chat_value)
        dict_as_file[f"{chat_id}"] = [f"{real_word}", dict_as_file[f"{chat_id}"][1]]
    with open("id_chat.json", "w") as id_chat_value:
        json.dump(dict_as_file, id_chat_value)
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        random = randint(0, len(real_word) - 1)
        fake_word[random] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)


@dp.message_handler(commands=["sd"])
async def give_word(message: types.Message):
    chat_id = message.chat.id
    with open("id_chat.json", "r") as id_chat_value:
        dict_as_file = json.load(id_chat_value)
        real_word = dict_as_file[f"{chat_id}"][0]
        fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        random = randint(0, len(real_word) - 1)
        fake_word[random] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)

@dp.message_handler(commands=["startik"])
async def id_check(message: types.Message):
    chat_id = message.chat.id
    try:
        with open("id_chat.json", "r") as id_chat_value:  # есть ли человек в bd и есть у него слово
            dict_as_file = json.load(id_chat_value)
            test_id = dict_as_file[f"{chat_id}"]
            if test_id[0] != "-":
                print("asdghfjg")  # выдавать слово
                await give_word(message)
            else:
                print("gg321")
                await give_new_word(message)
                # обрашятся к функции которая выдает слово
    except KeyError:  # Если у человека нет id в bd
        with open("id_chat.json", "r") as id_chat_value:
            dict_as_file = json.load(id_chat_value)
            dict_as_file[f"{chat_id}"] = ["-", 0]
        with open("id_chat.json", "w") as id_chat_value:
            json.dump(dict_as_file, id_chat_value)
        print("New People")#Если человек зарегестрировался то надо заново писать /startik




@dp.message_handler()
async def check(message: types.Message):
    chat_id = message.chat.id
    with open("id_chat.json", "r") as id_chat_value:
        dict_as_file = json.load(id_chat_value)
    if message.text == dict_as_file[f"{chat_id}"][0]:
        await message.answer("GG")
        dict_as_file[f"{chat_id}"][0] = "-"
        dict_as_file[f"{chat_id}"][1] += 1
        with open("id_chat.json", "w") as id_chat_value:
            json.dump(dict_as_file, id_chat_value)

executor.start_polling(dp, skip_updates=True)
