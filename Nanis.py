from random import randint
from aiogram import Bot, Dispatcher, executor, types


bot = Bot("6180157080:AAGOhpj9Buimk_lbRqq6P3EJSYQw_fhywMU")
dp = Dispatcher(bot)

@dp.message_handler(commands=["startik"])
async def all(message: types.Message):
    n = (open("words.txt", "r"))
    f = n.read()
    d = f.split(",")
    c = d[randint(0, len(d) - 1)]
    s = list(c)
    for i in range(0, len(c), 2):
        rand = randint(0, len(c)-1)
        s[rand] = "_"
        print(i)
    await message.answer("".join(s))



executor.start_polling(dp, skip_updates=True)