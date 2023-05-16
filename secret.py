Api = "5874536365:AAGF2G2qWU73dXtVAJSlhDxwqiPHbFHO3jM"





from random import randint
from aiogram import Bot, Dispatcher, executor, types
from secret import Api

bot = Bot(Api)
dp = Dispatcher(bot)


real_world = ""
# @dp.message_handler(commands=["startik"])
# async def stage1(message: types.Message):
#     cursor = connect.cursor()
#     read_file = (open("words.txt", "r"))
#     already_read_file = read_file.read()
#     word = already_read_file.split(",")
#     global real_world
#     real_world = word[randint(0, len(word) - 1)]
#     fake_word = list(real_world)
#     for i in range(0, len(real_world), 2):
#         random = randint(0, len(real_world)-1)
#         fake_word[random] = " _ "
#     await message.answer("".join(fake_word))
#
# @dp.message_handler(state='*')
# async def check(message: types.Message):
#     if message.text == real_world:
#         await message.answer("GG")







# executor.start_polling(dp, skip_updates=True)