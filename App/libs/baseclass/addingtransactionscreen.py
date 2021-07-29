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

        self.ids.date_of_transaction_inp.text = str(time.strftime("%d.%m.%y"))
        self.ids.time_of_transaction_inp.text = str(time.strftime("%H:%M:%S"))

        self.ids.every_month_payment_date_text_field.text = str(time.strftime("%d.%m.%y"))

    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1

    def save_transaction(self):
        #
        # ! !need to create control of the input here. Not only date and time but other things too and do it better!
        #
        if self.ids.checkbox_every_month.state == "normal":
            print(
                "saved" + self.ids.date_of_transaction_inp.text + "    " + self.ids.time_of_transaction_inp.text)
            Snackbar(
                text="Saved, transaction date: " + self.ids.date_of_transaction_inp.text +
                     " transaction time: " + self.ids.time_of_transaction_inp.text).open()

        else:
            print(
                "saved" + self.ids.date_of_transaction_inp.text + "    " + self.ids.time_of_transaction_inp.text)
            Snackbar(
                text="Saved, MONTHLY ON THE " + self.ids.every_month_payment_date_text_field.text
                     + ", transaction date: " + self.ids.date_of_transaction_inp.text +
                     " transaction time: " + self.ids.time_of_transaction_inp.text).open()
        self.parent.current = "mmapp root screen"

    def abort_transaction(self):
        print("ecs")
        self.parent.current = "mmapp root screen"

    def every_month_payment(self, checkbox, value):
        if checkbox.state == "down":
            print("HI")
            self.ids.every_month_payment_date_text_field.disabled = False

        if checkbox.state == "normal":
            self.ids.every_month_payment_date_text_field.disabled = True


"""
self.ids.date_and_time.text = str(time.strftime("%d.%m.%y") + "   " + time.strftime("%H:%M:%S"))
                Label:
                    id: date_and_time
                    text:""
                    font_size: 30"""
