import random
from aiogram import Bot, Dispatcher, executor, types
from Gaben.secret import Api
import pickle
import atexit

bot = Bot(Api)
dp = Dispatcher(bot)

def dump_file(USER_LIST):
    with open("filename.pickle", "wb") as file_dump:
        pickle.dump(USER_LIST, file_dump)

def load_file_pkl():
    try:
        with open("filename.pickle", "rb") as file_load:
            res = pickle.load(file_load)
            return res
    except FileNotFoundError:
        return []

read_file_word = open("words.txt", "r")
already_read_file_word = read_file_word.read()
words = already_read_file_word.split(",")
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

USER_LIST = load_file_pkl()

async def get_old_word(message: types.Message, user):
    real_word = user.word
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        randoms = random.randint(0, len(real_word) - 1)
        fake_word[randoms] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)

async def give_new_word(message: types.Message, user):
    real_word = random.choice(words)
    user.update_word(real_word)
    fake_word = list(real_word)
    for i in range(0, len(real_word), 2):
        randoms = random.randint(0, len(real_word) - 1)
        fake_word[randoms] = " _ "
    await message.answer("".join(fake_word))
    await message.answer(real_word)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет,\nв этом боте нужно отгадывать слова на английском\nчтобы начать нажми: /startik")


@dp.message_handler(commands=["startik"])
async def id_check(message: types.Message):
    chat_id = message.chat.id
    user = User.get_or_create(chat_id)
    last_word = user.word
    if last_word is None:
        await give_new_word(message, user)
    else:
        await get_old_word(message, user)

@dp.message_handler()
async def check(message: types.Message):
    chat_id = message.chat.id
    user = User.get_or_create(chat_id)
    if message.text == user.word:
        wins = user.wins
        user.update_wins(wins + 1)
        user.update_word(None)
        await message.answer(f"Ты выиграл уже: {user.wins} раз \n(/startik)")
    elif user.word is None:
        await message.answer(f"Чтобы получить слово нажми: /startik")
    else:
        await message.answer("Надо не так")

@atexit.register
def goodbye():
    dump_file(USER_LIST)
    read_file_word.close()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
