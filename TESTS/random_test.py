"""from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
FloatLayout:
    MDCheckbox:
        on_active: app.on_checkbox_active(*args)

        size_hint: None, None
        size: "48dp", "48dp"
        pos_hint: {'center_x': .5, 'center_y': .5}

'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_checkbox_active(self, checkbox, value):
        if value:
            print('The checkbox', checkbox, 'is active', 'and', checkbox.state, 'state')
        else:
            print('The checkbox', checkbox, 'is inactive', 'and', checkbox.state, 'state')



Test().run()
"""
"""from datetime import datetime, date

print(date.today())"""

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.picker import MDTimePicker

"""KV =""" '''
FloatLayout:
    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
'''
"""
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

KV = """
"""MDScreen:

    MDFlatButton:
        text: 'Open Dialog'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_alert_dialog()"""
"""


class Example(MDApp):
    dialog = None

    def build(self):
        return Builder.load_string(KV)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="DISCARD", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()


Example().run()
"""

"""from kivymd.app import MDApp
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.theming import ThemeManager
Builder.load_string("""
""" 
#:import toast kivymd.toast.toast
<MyRoot@BoxLayout>
    orientation: 'vertical'
    MDToolbar:
        title: "Test MDDropDownItem"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10
        left_action_items: [['menu', lambda x: x]]
    FloatLayout:

        MDDropDownItem:
            id: dropdown_item
            pos_hint: {'center_x': 0.5, 'center_y': 0.6}
            items: app.items
            dropdown_bg: [1, 1, 1, 1]
        MDRaisedButton:
            pos_hint: {'center_x': 0.5, 'center_y': 0.3}
            text: 'Chek Item'
            on_release: toast(dropdown_item.current_item)"""
""")
class Test(MDApp):
    def build(self):
        self.items = [f"Item {i}" for i in range(50)]
        return Factory.MyRoot()

Test().run()
"""


