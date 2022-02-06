


from sre_parse import REPEAT_CHARS
from turtle import onkey, onkeypress
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import CoreLabel
from weather import *
import sys
import random

class playerGame(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.on_key_closed, self)
        self.keyboard.bind(on_key_up=self.on_key_up)

        with self.canvas:
            self.player = Rectangle(pos=(500, 250), size=(100, 100))
            self.sign = Rectangle(pos = (300,300), size = (50,50))
    
    def collide(player, sign):
        r1x = player[0][0]
        r1y = player[0][1]
        r2x = sign[0][0]
        r2y = sign[0][1]
        r1w = player[1][0]
        r1h = player[1][1]
        r2w = sign[1][0]
        r2h = sign[1][1]

        if (r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y):
            return True
        else:
            return False

    def on_key_closed(self):
        self.keyboard.unbind(on_key_up=self.on_key_up)
        self.keyboard = None
    
    def on_key_up(self, keyboard, keycode):
        key = keycode[-1]
        xpos = self.player.pos[0]
        ypos = self.player.pos[1]
        
        if key == "w" or key == "up":
            ypos += 100
        elif key == "a" or key == "left":
            xpos -= 100
        elif key == "s" or key == "down":
            ypos -= 100
        elif key == "d" or key == "right":
            xpos += 100
        elif key == "z":
            sys.exit()
        else:
            print("Please use WASD or Arrow Keys")
    
        self.player.pos = (xpos,ypos)
        if playerGame.collide((self.player.pos, self.player.size), (self.sign.pos, self.sign.size)):
            print("Ow I stubbed my toe")


class playerApp(App):
    def build(self):
        return playerGame()


if __name__ == "__main__":
    # z_code = int(input())
    # print(check_conditions(z_code))
    playerApp().run()
