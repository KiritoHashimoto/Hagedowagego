import random
from aiogram import Bot, Dispatcher, executor, types
from Gaben.secret import Api
import pickle

bot = Bot(Api)
dp = Dispatcher(bot)

def load_file_pkl():
    try:
        with open("data.pkl", "rb") as file_load:
            res = pickle.load(file_load)
            return res
    except FileNotFoundError:
        return []

USER_LIST = []

class User:
    def __init__(self, id_chat):
        self.id_chat = id_chat
        self.word = None
        self.wins = 0

    def update_word(self, word):
        self.word = word

    def update_wins(self, wins):
        self.wins = wins

    @classmethod
    def get_or_create(cls, chat_id):
        for i in USER_LIST:
            if i.id_chat == chat_id:
                return i
        user = User(chat_id)
        USER_LIST.append(user)
        return user
                #todo: предвинуть две функции чтобы была как одна.






# async def get_user(id_chat):
#     for i in USER_LIST:
#         if i.id_chat == id_chat:
#             return i
#
#
# async def create_user(id_chat):
#     user = User(id_chat)
#     USER_LIST.append(user)
#     return user





async def get_old_word(message: types.Message, user):
    global random
    real_word = user.word
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        randoms = random.randint(0, len(real_word) - 1)
        fake_word[randoms] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)


async def give_new_word(message: types.Message, user):
    with open("words.txt", "r") as read_file_word:
        already_read_file_word = read_file_word.read()
    words = already_read_file_word.split(",")
    real_word = random.choice(words)
    user.update_word(real_word)
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        randoms = random.randint(0, len(real_word) - 1)
        fake_word[randoms] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)


@dp.message_handler(commands=["startik"])
async def id_check(message: types.Message):
    chat_id = message.chat.id
    user = User.get_or_create(chat_id)
    last_word = user.word
    if last_word is None:
        await give_new_word(message, user)
        print("Give new word")  # Если слова нет
    else:
        await get_old_word(message, user)
        print("Give old word")  # Если слово есть


@dp.message_handler()
async def check(message: types.Message):
    chat_id = message.chat.id
    user = await get_user(chat_id)
    if message.text == user.word:
        wins = user.wins
        user.update_wins(wins + 1)
        user.update_word(None)
        await message.answer(f"Ты выиграл уже: {user.wins} раз")


try:
    print("lolm")
    executor.start_polling(dp, skip_updates=True)
finally:
    print("fan")


    with open("data.pkl", "w+b") as file_dump:
        print(USER_LIST)
        print("")
        my_pickled_object = pickle.dump(USER_LIST, file_dump)
