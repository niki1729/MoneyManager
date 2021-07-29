from kivymd.uix.screen import MDScreen


class RootScreen(MDScreen):

    def adding_transaction_screen(self):
        self.parent.current = "mmapp transaction screen"

# icon: "cog"