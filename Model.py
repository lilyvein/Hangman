import glob


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
