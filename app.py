from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
# from kivy.uix.codeinput import CodeInput
 
from kivy.config import Config
Config.set('graphics', 'resizable', '1'); # запрет на ресайз окна
Config.set('graphics', 'width', '55'); # высота окна
Config.set('graphics', 'height', '55'); # ширина окна

from kivy.uix.floatlayout import FloatLayout

class MainApp(App):
    def build(self):
        self.icon = 'source/favicon.png'
        self.title = 'WbW'
        fl = FloatLayout(size=(10, 50))

        fl.add_widget(Button(
            text="Кнопка", 
            font_size=14,
            on_press=self.btn_press,
            background_color=[1, 0, 0, 1], # красный цвет кнопки
            background_normal='',
            size_hint=(.15, .15),
            pos_hint={'center_x': .5, 'center_y': .1}
        ))

        fl.add_widget(Label(text='▼',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .45}
        ))

        fl.add_widget(Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5}
        ))

        fl.add_widget(Label(text='▲',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .55}
        ))

        fl.add_widget(TextInput(
            text='Hello world',
            size_hint=(.15, .05),
            pos_hint={'center_x': .15, 'center_y': .05}
        ))

        fl.add_widget(TextInput(
            text='Hello world',
            size_hint=(.15, .05),
            pos_hint={'center_x': .15, 'center_y': .20}
        ))
        return fl
        # return label

    
    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text = "Нажато"
 
if __name__ == '__main__':
    app = MainApp()
    app.run()
