from datetime import datetime, date
import time

import labels

print("Good luck")
from random import randint

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.tab import MDTabsBase
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label

from labels import *

labels.DATE = time.strftime("%d.%m.%y")
labels.TIME = time.strftime("%H:%M:%S")


# For PopupWindow, probably wil be used several times
class P(FloatLayout):
    pass


class Tab(FloatLayout, MDTabsBase):
    pass


class AddingTransactionScreen(Screen):
    pass


class OverviewScreen(Screen):
    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1


class HomeScreen(Screen):
    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print(tab_text)
        if tab_text == "Overview":
            print(instance_tab)
        if tab_text == "Total":
            pass

    def total_list_categories(self):
        print("YES")


class TotalScreen(Screen):
    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1

    def we_call(self):
        self.add_categories_widgets()

    def add_categories_widgets(self):
        print("HI")
        for i in range(20):
            self.ids.boxlayout_totalscreen.add_widget(Label(text="HI" + str(i)))

    def callback(self):
        print("nein")


class CategoriesSettingsScreen(Screen):
    def change_color(self):
        self.ids.welcome_label.color = randint(0, 100) / 100, randint(0, 100) / 100, randint(0, 100) / 100, 1


class CurrentMonthScreen(Screen):
    pass


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

    # https://kivymd.readthedocs.io/en/latest/components/navigation-drawer/

    def actual_date(self):
        self.ids.contentnavigationdrawer_mdlabel.text = date.today()
        print("yes")


class MainApp(MDApp):
    def on_start(self):
        pass

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        # self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        GUI = Builder.load_file("main.kv")
        return GUI

    def switch_theme_style(self):
        self.theme_cls.theme_style = (
            "Light" if self.theme_cls.theme_style == "Dark" else "Dark"
        )
        # self.root.ids.backdrop.ids._front_layer.md_bg_color = [0, 0, 0, 0]

    data = {
        'language-python': 'Python',
        'language-php': 'PHP',
        'language-cpp': 'C++',
    }


MainApp().run()
