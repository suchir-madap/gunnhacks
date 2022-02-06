


from kivy.app import App
from kivy.uix.widget import Widget


class snake_game(Widget):
    pass


class snake_app(App):
    def build(self):
        return snake_game()


if __name__ == "__main__":
    snake_app().run()
