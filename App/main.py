"""
MoneyManager App

"""

import os
import sys
from pathlib import Path

from kivy.lang import Builder
from kivymd.app import MDApp

from backend.main_backend import MainBackend

from backend.categories_control import CategoriesControl, Category
from backend.accounts_control import AccountsControl, Account
from backend.transaction_list_control import TransactionListControl

# TODO: Why is there a error: when the three lines are imported
#  File "D:\Users\Nikita\Documents\MoneyManager\App\backend\categories_control.py", line 26, in __init__
#      list_cat = open("usr_data/list_categories.txt", "a")
#  FileNotFoundError: [Errno 2] No such file or directory: 'usr_data/list_categories.txt'


# Window.size=(600, 700)


if getattr(sys, "frozen", False):  # bundle mode with PyInstaller
    os.environ["APP_ROOT"] = sys._MEIPASS
else:
    os.environ["APP_ROOT"] = str(Path(__file__).parent)

KV_DIR = f"{os.environ['APP_ROOT']}/libs/kv/"

for kv_file in os.listdir(KV_DIR):
    with open(os.path.join(KV_DIR, kv_file), encoding="utf-8") as kv:
        Builder.load_string(kv.read())

KV = """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import RegisterScreen libs.baseclass.register_screen.RegisterScreen
#:import RootScreen libs.baseclass.root_screen.RootScreen
#:import AddingTransactionScreen libs.baseclass.addingtransactionscreen.AddingTransactionScreen

ScreenManager:
    transition: FadeTransition()

    RegisterScreen:
        name: "mmapp register screen"

    RootScreen:
        name: "mmapp root screen"
    
    AddingTransactionScreen:
        name: "mmapp transaction screen"

"""


class MoneyManager(MDApp):
    def __init__(self, **kwargs):
        self.m_back = MainBackend(TransactionListControl(), CategoriesControl(), AccountsControl())
        super().__init__(**kwargs)
        self.title = "MoneyManager"
        self.icon = f"{os.environ['APP_ROOT']}/assets/images/MMApp.png"

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"

        return Builder.load_string(KV)

    def save_transaction(self, amount, date, time_trans, name, category, account):
        self.m_back.save_transaction(amount, date, time_trans, name, category, account)



MoneyManager().run()

# TODO: on_enter: if not len(rv.data): root.function here you can have on enter function in the .kv file
"""spacing: "10dp"
padding: "20dp"""

"""Must be one of: ['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 
'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']
"""
