


from turtle import onkey, onkeypress
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from weather import *



class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.on_key_closed, self)
        self.keyboard.bind(on_key_up=self.on_key_up)

        with self.canvas:
            self.player = Rectangle(pos=(500, 500), size=(100, 100))
    
    def on_key_closed(self):
        self.keyboard.unbind(on_key_up=self.on_key_up)
        self.keyboard = None
    
    def on_key_up(self, keyboard, keycode):
        k_pressed = keycode[-1]
        xpos = self.player.pos[0]
        ypos = self.player.pos[1]
        print(keycode[-1])

        if k_pressed == "w":
            ypos += 50
        elif k_pressed == "a":
            xpos -= 50
        elif k_pressed == "s":
            ypos -= 50
        elif k_pressed == "d":
            xpos += 50
        
        self.player.pos = (xpos,ypos)

class SnakeApp(App):
    def build(self):
        return SnakeGame()


if __name__ == "__main__":
    # z_code = int(input())
    # print(check_conditions(z_code))
    SnakeApp().run()
