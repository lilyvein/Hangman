import glob
import sqlite3


class Model:
    def __init__(self):
        self.database_name = 'databases/hangman_words_ee.db'
        self.image_files = glob.glob('images/*.png')   # all hangman imagaes
        # new game
        self.new_word = None  # luuakse uus sõna ja pole teada ühtegi tähte
        self.user_word = []  # tühi list
        self.all_user_chars = []  # tähed mis on leitud
        self.counter = 0  # Error counter (wrong letters)
        # edetabel
        self.player_name = 'UNKNOWN'
        self.leaderboard_file = 'leaderboard.txt'
        self.score_data = []  # leaderboard file contents

    def start_new_game(self):
        self.get_random_word()  # set new word (self.new_word)
        # print(self.new_word)  # for testing
        self.user_word = []
        self.all_user_chars = []
        self.counter = 0
        # all letters replace with _
        for x in range(len(self.new_word)):
            self.user_word.append('_')

        print(self.new_word)  # Test Autojuht
        print(self.user_word)  # test ['_', '_', '_', '_', '_', '_', '_', '_']

    def get_random_word(self):
        connection = sqlite3.connect(self.database_name)  # luuakse ühendus andmebaasiga
        cursor = connection.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1')
        self.new_word = cursor.fetchone()[1]  # 0 on id ja 1 on sõna
        connection.close()  # sulgeb database ühenduse

    def get_user_input(self, userinput):
        if userinput:
            user_char = userinput[:1]  # only first letter
            if user_char.lower() in self.new_word.lower():
                self.change_user_input(user_char)  # Found letter
            else:  # tähte ei leitud
                self.counter += 1
                self.all_user_chars.append(user_char.upper())

    def change_user_input(self, user_char):
        # Replace all _ with found letter
        concurrent_word = self.chars_to_list(self.new_word)
        x = 0
        for c in concurrent_word:
            if user_char.lower() == c.lower():
                self.user_word[x] = user_char.upper()
            x += 1

    @staticmethod
    def chars_to_list(string):
        # string to list: test > ['T', 'e, 's', 't']
        chars = []
        chars[:0] = string
        return chars

    def get_all_user_chars(self):
        return ', '.join(self.all_user_chars)
