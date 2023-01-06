from tkinter import simpledialog

from GameTime import GameTime
from Model import Model
from View import View


class Controller:

    def __init__(self):
        self.model = Model()
        self.view = View(self, self.model)
        self.gametime = GameTime(self.view.lbl_time)  # loob objekti et saame mängu aega kogu aeg kasutada

    def main(self):
        self.view.main()

    def click_btn_new(self):
        self.view.btn_new['state'] = 'disabled'
        self.view.btn_cancel['state'] = 'normal'
        self.view.btn_send['state'] = 'normal'
        self.view.char_input['state'] = 'normal'
        self.view.change_image(0)  # image change with index
        self.model.start_new_game()  # alustab uut mängu
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text='Wrong 0 letter(s)', fg='black')
        self.view.char_input.focus()  # active input filesd
        self.gametime.reset()
        self.gametime.start()

    def click_btn_cancel(self):
        self.gametime.stop()
        self.view.btn_new['state'] = 'normal'
        self.view.btn_cancel['state'] = 'disabled'
        self.view.btn_send['state'] = 'disabled'
        self.view.char_input['state'] = 'disabled'
        self.view.char_input.delete(0, 'end')
        self.view.change_image(len(self.model.image_files) - 1)

    def click_btn_send(self):
        self.model.get_user_input(self.view.userinput.get().strip())
        self.view.lbl_result.configure(text=self.model.user_word)
        self.view.lbl_error.configure(text=f'Wrong{self.model.counter} letters(s). {self.model.get_all_user_chars()} ')   # see näitab vigaseid tähti
        self.view.char_input.delete(0, 'end')
        if self.model.counter > 0:
            self.view.lbl_error.configure(fg='red')  # font color
            self.view.change_image(self.model.counter)  # error image change
        self.is_game_over()

    def is_game_over(self):
        if self.model.counter >= 11 or '_' not in self.model.user_word \
                or self.model.counter >= (len(self.model.image_files) - 1):

            self.gametime.stop()
            self.view.btn_new['state'] = 'normal'
            self.view.btn_cancel['state'] = 'disabled'
            self.view.btn_send['state'] = 'disabled'
            self.view.char_input['state'] = 'disabled'
            player_name = simpledialog.askstring('Game over', 'What is the player\'s name', parent=self.view)  # kolm argumenti, tiitel ribal olev tekst ,2. tekst  3 kuhu peale panna, põhi mängu peale pannakse see aken
            self.model.set_player_name(player_name, self.gametime.counter)
            self.view.change_image(len(self.model.image_files) - 1)

    def click_btn_leaderboard(self):
        popup_window = self.view.create_popup_window()
        data = self.model.read_leaderboard_file_contents()
        self.view.generate_leaderboard(popup_window, data)
