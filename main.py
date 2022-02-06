


from kivy.app import App
from kivy.uix.widget import Widget
from weather import *



class snake_game(Widget):
    pass

class snake_app(App):
    def build(self):
        return snake_game()


if __name__ == "__main__":
    z_code = int(input())
    print(check_conditions(z_code))
    # snake_app().run()
