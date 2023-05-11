from random import randint
from aiogram import Bot, Dispatcher, executor, types


bot = Bot("6180157080:AAGOhpj9Buimk_lbRqq6P3EJSYQw_fhywMU")
dp = Dispatcher(bot)


c = ""
@dp.message_handler(commands=["startik"])
async def all(message: types.Message):
    n = (open("words.txt", "r"))
    f = n.read()
    word = f.split(",")
    global c
    c = word[randint(0, len(word) - 1)]
    fake = list(c)
    for i in range(0, len(c), 2):
        rand = randint(0, len(c)-1)
        fake[rand] = " _ "
        print(i)
    await message.answer("".join(fake))

@dp.message_handler(state='*')
async def palino(message: types.Message):
    if message.text == c:
        await message.answer("GG")




        # answer =  await message.reply('Второй!', reply=False)
        # if answer == word:
        #     await message.answer("lol")




executor.start_polling(dp, skip_updates=True)