import kivy
from kivy.app import App
from kivy.uix.label import Label
import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


class MyApp(App):
    def build(self):
        return Label(text='Hello world')


MyApp().run()
