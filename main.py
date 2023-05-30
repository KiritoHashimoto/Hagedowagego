from random import randint
from aiogram import Bot, Dispatcher, executor, types
from Gaben.secret import Api
import pickle
import traceback

bot = Bot(Api)
dp = Dispatcher(bot)

class User:
    def __init__(self, id_chat):
        self.id_chat = id_chat
        self.word = None
        self.wins = 0



    def update_word(self, word):
        self.word = word

    def update_wins(self, wins):
        self.wins = wins


def load_file_pkl():
    with open("data.pkl", "r+b") as file_load:
        res = pickle.load(file_load)
        print(res)
        print("")

def dump_file_pkl(user):
    with open("data.pkl", "w+b") as file_dump:
        pickle.dump(user, file_dump)
# user1 = User(999571194)




async def get_user(id_chat):
    for i in user_list:
        if i.id_chat == id_chat:
            return i

async def create_user(id_chat):
    user = User(id_chat)
    user_list.append(user)
    return user


user_list = []






async def get_old_word(message: types.Message, user):
    chat_id = message.chat.id
    real_word = user.word
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        random = randint(0, len(real_word) - 1)
        fake_word[random] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)


async def give_new_word(message: types.Message, user):
    with open("words.txt", "r") as read_file_word:
        already_read_file_word = read_file_word.read()
    words = already_read_file_word.split(",")
    real_word = words[randint(0, len(words) - 1)]
    user.update_word(real_word)
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        random = randint(0, len(real_word) - 1)
        fake_word[random] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)





@dp.message_handler(commands=["startik"])
async def id_check(message: types.Message):
    chat_id = message.chat.id
    user = await get_user(chat_id)
    if user is None:                   #Создание User
        user = await create_user(chat_id)
        print("New People")
    last_word = user.word
    if last_word is None:
        await give_new_word(message, user)
        print("Give new word")  #Если слова нет
    else:
        await get_old_word(message, user)
        print("Give old word")    #Если слово есть




@dp.message_handler()
async def check(message: types.Message):
    chat_id = message.chat.id
    user = await get_user(chat_id)
    if message.text == user.word:
        wins = user.wins
        user.update_wins(wins + 1)
        user.update_word(None)
        await message.answer(f"Ты выиграл уже: {wins + 1} раз")
        dump_file_pkl(user_list)


executor.start_polling(dp, skip_updates=True)

