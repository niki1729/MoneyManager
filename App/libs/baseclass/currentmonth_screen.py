from kivymd.uix.screen import MDScreen


from random import randint

class CurrentMonthScreen(MDScreen):
    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1