from kivymd.uix.screen import MDScreen


class RegisterScreen(MDScreen):
    def control_password(self):
        print(self.ids.register_username.text, self.ids.register_password.text)
        if self.ids.register_username.text == "" and self.ids.register_password.text == "":
            self.goto_register_screen()

    def goto_register_screen(self):
        self.parent.current = "mmapp root screen"
