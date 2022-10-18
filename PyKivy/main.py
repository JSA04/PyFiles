from turtle import width
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', "width", 50)
Config.set('graphics', "height", 50)

class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.size = (4, 4)
        self.rows = 2

        self.SecondGrid = GridLayout()
        self.SecondGrid.cols = 2

        self.SecondGrid.add_widget(Label(text='Password:'))

        self.password = TextInput(multiline=False)
        self.SecondGrid.add_widget(self.password)

        self.add_widget(self.SecondGrid)

        self.submit = Button(text="Submit Password", font_size=20)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
    
    def pressed(self, instance):
        print(self.password.text)
        self.password.text = ""


class Main(App):
    def build(self):
        return MainGrid()


if __name__ == "__main__":
    try:
        Main().run()
    except KeyboardInterrupt:
        print("App encerrado")
