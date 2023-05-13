from random import randint
from aiogram import Bot, Dispatcher, executor, types
from secret import Api

bot = Bot(Api)
DP = Dispatcher(bot)

real_word = ""


@DP.message_handler(commands=["startik"])
async def create_word(message: types.Message):
    with open("words.txt", "r") as file_None:
        global real_word
        file_read = file_None.read()
        real_word = file_read.split(",")
        real_word = real_word[randint(0, len(real_word) - 1)]
        fake = list(real_word)
        for i in range(0, len(real_word), 2):
            random_number_index = randint(0, len(real_word) - 1)
            fake[random_number_index] = " _ "
    await message.answer("".join(fake))


@DP.message_handler(state='*')
async def gues(message: types.Message):
    if message.text == real_word:
        await message.answer("GG")


executor.start_polling(DP, skip_updates=True)
