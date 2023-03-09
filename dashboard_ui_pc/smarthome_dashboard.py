import kivy

kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image



Window.clearcolor = (1, 1, 1, 1)  # установка белого фона


class Kitchen(BoxLayout):
    def __init__(self, **kwargs):
        super(Kitchen, self).__init__(**kwargs)

        # добавление изображения чайника
        image = Image(source="kettle.png", size_hint=(0.5, 0.5), pos_hint = {'x': 0.1, 'y': 0.5})
        self.add_widget(image)

        # добавление надписи "Чайник"
        label = Label(text="Чайник", font_size='20sp', bold=True, color=(0, 0, 0, 100),size_hint=(0.3, 0.1),pos_hint = {'x': 0.1, 'y': 0.9})
        self.add_widget(label)

        # добавление кнопки "Включить"
        on_button = Button(text="Включить", font_size='14sp', size_hint=(0.3, 0.1), color=(1, 1, 1, 100),
                           background_color=(0, 1, 0, 1),pos_hint = {'x': 0.5, 'y': 0.9})
        on_button.bind(on_press=self.turn_on_kettle)
        self.add_widget(on_button)

        # добавление кнопки "Выключить"
        off_button = Button(text="Выключить", font_size='14sp', size_hint=(0.3, 0.1), color=(1, 1, 1, 100),
                            background_color=(1, 0, 0, 1),pos_hint = {'x': 0.5, 'y': 0.9})
        off_button.bind(on_press=self.turn_off_kettle)
        self.add_widget(off_button)

        # добавление кнопки "Главное меню"
        main_menu_button = Button(text="Главное меню", font_size='14sp', size_hint=(0.3, 0.1), color=(1, 1, 1, 100),
                                  background_color=(0, 0, 0, 100),pos_hint = {'x': 0.5, 'y': 0.9})
        main_menu_button.bind(on_press=self.go_to_main_menu)
        self.add_widget(main_menu_button)

    def turn_on_kettle(self, *args):
        # код для включения чайника
        print("Чайник включен")

    def turn_off_kettle(self, *args):
        # код для выключения чайника
        print("Чайник выключен")

    def go_to_main_menu(self, *args):
        # создание экземпляра класса MainMenu и отображение его на экране
        main_menu = MainMenu()
        self.clear_widgets()
        self.add_widget(main_menu)


class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

        # создание и добавление надписи "Умный дом" в левый верхний угол
        label = Label(text="Умный дом", font_size='20sp', bold=True, color=(0, 0, 0, 100),size_hint=(0.1, 0.1),pos_hint = {'x': 0, 'y': 0.9})
        self.add_widget(label)

        # создание и добавление кнопки "Кухня" в левый верхний угол
        kitchen_button = Button(text="Кухня", font_size='14sp', size_hint=(0.2, 0.1), color=(1, 1, 1, 100),
                                background_color=(0, 0, 1, 1))
        kitchen_button.bind(on_press=self.go_to_kitchen)
        self.add_widget(kitchen_button)

        # создание и добавление кнопки выхода в правый верхний угол
        exit_button = Button(text="Выход", font_size='14sp', size_hint=(0.1, 0.1), color=(1, 1, 1, 100),
                             background_color=(0, 0, 0, 100),pos_hint = {'x': 0, 'y': 0.9})
        exit_button.bind(on_press=self.exit_app)
        self.add_widget(exit_button)

    def go_to_kitchen(self, *args):
        # создание экземпляра класса Kitchen и отображение его на экране
        kitchen = Kitchen()
        self.clear_widgets()
        self.add_widget(kitchen)

    def exit_app(self, *args):
        App.get_running_app().stop()  # остановка приложения

class MyApp(App):
    def build(self):
        return MainMenu()

if __name__ == '__main__':
    MyApp().run()