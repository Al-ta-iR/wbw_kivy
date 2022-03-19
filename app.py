from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# from kivy.uix.codeinput import CodeInput
 
# from kivy.config import Config
# Config.set('graphics', 'resizable', '0'); # запрет на ресайз окна
# Config.set('graphics', 'width', '640'); # высота окна
# Config.set('graphics', 'height', '480'); # ширина окна

from kivy.uix.floatlayout import FloatLayout

class MainApp(App):
    def build(self):
        self.title = 'WbW'
        fl = FloatLayout(size = (50, 50))

        fl.add_widget(Button(
            text="Кнопка", 
            font_size=14,
            on_press=self.btn_press,
            background_color=[1, 0, 0, 1], # красная кнопка
            background_normal='',
            size_hint=(.15, .15),
            pos_hint={'center_x': .5, 'center_y': .1}
        ))

        fl.add_widget(Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5}
        ))

        fl.add_widget(TextInput(
            text='Hello world',
            size_hint=(.15, .05),
            pos_hint={'center_x': .15, 'center_y': .05}
        ))
        return fl
        # return label

    
    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text = "Нажато"
 
if __name__ == '__main__':
    app = MainApp()
    app.run()
