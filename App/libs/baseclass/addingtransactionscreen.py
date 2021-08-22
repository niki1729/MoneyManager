import time
from random import randint

from kivymd.uix.screen import MDScreen
from kivymd.uix.snackbar import Snackbar
from datetime import date


class AddingTransactionScreen(MDScreen):
    def on_enter(self, *args):
        self.display_date_time()

    def display_date_time(self):
        self.ids.date_of_transaction_inp.text = str(time.strftime("%d.%m.%y"))
        self.ids.time_of_transaction_inp.text = str(time.strftime("%H:%M:%S"))

        self.ids.every_month_payment_date_text_field.text = str(time.strftime("%d.%m.%y"))

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

            # root.save_transaction()

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

    def control_data(self):
        """
        Controlls all the different inputs, i.e. date, time, amount, name and date for monthly payments
        :return: True if all correct,
        """
        # TODO create this function
        result = True
        try:
            d = date(self.ids.date_of_transaction_inp.text)
        except:
            result = "Date"


        return result

    def every_month_payment(self, checkbox, value):
        if checkbox.state == "down":
            print("HI")
            self.ids.every_month_payment_date_text_field.disabled = False

        if checkbox.state == "normal":
            self.ids.every_month_payment_date_text_field.disabled = True

    def print_add_transaction(self):
        print("root.print_add_transaction")


"""
self.ids.date_and_time.text = str(time.strftime("%d.%m.%y") + "   " + time.strftime("%H:%M:%S"))
                Label:
                    id: date_and_time
                    text:""
                    font_size: 30"""

"""
Label:
                        size_hint_y: 2
                        id: welcome_label
                        text: "Welcome to Transaction!"
                        font_size: 40
                        color: 1,0,1,1
                    Button:
                        size_hint_y: 2
                        text: "Press me for fun"
                        color: 1, 1, 0, 1
                        color_before: 1,0,0,1
                        background_down: "grey_color.png"
                        on_release: root.change_color()
                        """
