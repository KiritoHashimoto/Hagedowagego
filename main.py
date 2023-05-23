from random import randint
from aiogram import Bot, Dispatcher, executor, types
from Gaben.secret import Api
import pickle

bot = Bot(Api)
dp = Dispatcher(bot)


with open("Gaben/id_chat.pkl", "rb") as file:
    file_read = pickle.load(file)

async def give_word(message: types.Message):
    chat_id = message.chat.id
    real_word = file_read[f"{chat_id}"][0]
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        random = randint(0, len(real_word) - 1)
        fake_word[random] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)


async def give_new_word(message: types.Message):
    chat_id = message.chat.id
    read_file_word = open("words.txt", "r")
    already_read_file_word = read_file_word.read()
    words = already_read_file_word.split(",")
    real_word = words[randint(0, len(words) - 1)]
    file_read[f"{chat_id}"] = [f"{real_word}", file_read[f"{chat_id}"][1]]
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
        test_id = file_read[f"{chat_id}"]
        if test_id[0] != "-":
            print("Give word")  # выдавать слово
            await give_word(message)
        else:
            print("Create word") # обрашятся к функции которая выдает слово
            await give_new_word(message)
    except KeyError:  # Если у человека нет id в json
        file_read[f"{chat_id}"] = ["-", 0]
        print("New People") #Если человек зарегистрировался то надо заново писать /startik




@dp.message_handler()
async def check(message: types.Message):
    chat_id = message.chat.id

    if message.text == file_read[f"{chat_id}"][0]:
        await message.answer("GG")
        file_read[f"{chat_id}"][0] = "-"
        file_read[f"{chat_id}"][1] += 1
        with open("Gaben/id_chat.pkl", "wb") as files:
            pickle.dump(file_read, files)
        await message.answer(f"Ты выиграл уже: {file_read[f'{chat_id}'][1]} раз")
executor.start_polling(dp, skip_updates=True)
