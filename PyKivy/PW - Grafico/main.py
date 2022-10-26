from Termo_Utils.Termo import Termo
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Manager(ScreenManager):
    pass


class DBConf(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Main(App):
    def build(self):
        return Manager()


if __name__ == "__main__":
    Main().run()
