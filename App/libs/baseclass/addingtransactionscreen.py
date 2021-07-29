import time
from random import randint

from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from datetime import date


class AddingTransactionScreen(MDScreen):
    def on_enter(self, *args):
        self.display_date_time()

    def display_date_time(self):
        # self.ids.date_and_time.text=str(date.today())
        self.ids.date_and_time.text = str(time.strftime("%d.%m.%y") + "   " + time.strftime("%H:%M:%S"))

    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1

    def save_transaction(self):
        print("saved")
        Snackbar(text="Saved").open()
        self.parent.current = "mmapp root screen"

    def abort_transaction(self):
        print("ecs")
        self.parent.current = "mmapp root screen"
