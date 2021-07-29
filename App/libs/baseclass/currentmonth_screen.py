from kivymd.uix.screen import MDScreen


from random import randint

class CurrentMonthScreen(MDScreen):
    """
    Here I will display Bills what needs to be paid and Budget left for the current Month
    """
    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1