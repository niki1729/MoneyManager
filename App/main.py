"""
MoneyManager App

"""


import os
import sys
from pathlib import Path

from kivy.lang import Builder

from kivymd.app import MDApp


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
#: import AddingTransactionScreen libs.baseclass.addingtransactionscreen.AddingTransactionScreen

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
        super().__init__(**kwargs)
        self.title = "MoneyManager"
        self.icon = f"{os.environ['APP_ROOT']}/assets/images/MMApp.png"

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.theme_style = "Dark"

        return Builder.load_string(KV)


MoneyManager().run()
