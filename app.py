from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.codeinput import CodeInput
 
from kivy.config import Config
Config.set('graphics', 'resizable', '0'); # запрет на ресайз окна
Config.set('graphics', 'width', '640'); # высота окна
Config.set('graphics', 'height', '480'); # ширина окна

class MainApp(App):
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})
 
        # return label
        return Button(
            text="Кнопка", 
            font_size=14,
            on_press=self.btn_press,
            background_color=[1, 0, 0, 1], # красная кнопка
            background_normal=''
        )
    
    def btn_press(self, instance):
        print("Кнопка нажата")
        instance.text = "Нажато"
 
if __name__ == '__main__':
    app = MainApp()
    app.run()