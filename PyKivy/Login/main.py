from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from __getUser import confere_senha

Window.size = (500, 500)


class Manager(ScreenManager):
    pass


class LoginScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def confere_usuario(self):
        usuario = self.ids.username.text
        passwd = self.ids.passwd.text
        confere = confere_senha(usuario, passwd)

        if confere is True:
            self.ids.username.text = ""

        self.ids.login_log.text = str(confere) if confere is not True else ""
        self.ids.passwd.text = ""


class Main(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    Main().run()
