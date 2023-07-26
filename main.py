import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.unix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class GrridLayout:
    pass


def widget(param):
    pass


class Label_:
    pass


class childApp(GrridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        self.cols = 5
        self.add-widget(Label(text = 'Student Name'))
        self.s-name = TextInput()
        self.add-widget(self.s-name)

        self.add_widget_(Label_(text='Student Marks'))
        self.s_marks = TextInput(_)
        self.add_widget_(self.s_marks)

        self.add_widget_(Label_(text='Student Gender'))
        self.s_gender = TextInput(_)
        self.add_widget_(self.s_gender)

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()
