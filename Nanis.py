
from aiogram import Bot, Dispatcher, executor, types

aa = "5841270627:AAHL9sXIz-iSYhSEoduaG12TAB37pCnT1zA"
# bot = Bot("5874536365:AAGF2G2qWU73dXtVAJSlhDxwqiPHbFHO3jM")
bot = Bot(aa)
dp = Dispatcher(bot)

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
#     print("start1")
#     """
#     This handler will be called when user sends `/start` or `/help` command
#     """
#     await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# @dp.message_handler(state='*')
# async def stage1(message: types.Message):
#     print("start")
#     print(message)


@dp.message_handler(commands=['start'])
async def none(message: types.Message):
    print("ger")
    chat_id = message.chat.id
    await message.answer(chat_id)


executor.start_polling(dp)


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)