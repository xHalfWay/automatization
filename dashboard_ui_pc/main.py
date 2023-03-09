from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from paho.mqtt.client import Client

# Определение функции обработчика сообщений
def on_message(client, userdata, message):
    print(message.topic, message.payload.decode())

# Определение класса для главного экрана
class MainScreen(BoxLayout):
    topic = StringProperty('')
    message = StringProperty('')

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Создание MQTT клиента
        self.client = Client()
        self.client.connect('broker.hivemq.com', 1883)

        # Подписка на топик
        self.client.subscribe('test/topic')
        self.client.on_message = on_message
        self.client.loop_start()

    def publish_message(self):
        # Отправка сообщения
        self.client.publish(self.topic, self.message)

class MQTTApp(App):
    def build(self):
        # Загрузка экрана из kv-файла
        Builder.load_file('main.kv')
        return MainScreen()

if __name__ == '__main__':
    MQTTApp().run()