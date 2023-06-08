
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
    def get_or_create(cls, chat_id,USER_LIST):
        for i in USER_LIST:
            if i.id_chat == chat_id:
                return i
        user = User(chat_id)
        return user



