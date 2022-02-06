
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.window import Window

Window.size = (900, 620)



class MainApp(App):
    def build(self):
        Window.clearcolor = (37/255, 151/255, 217/255, 0.8)
        backgroundimg = Image(source="background.jpg")
        layout = GridLayout(rows =2, row_force_default = True, row_default_height = 40, spacing=10,padding=40, top = -150, right = 420)
        self.value = TextInput(text='Enter Zipcode here ', size_hint_x = None, width = 200)
        enter = Button(text = 'Enter Zipcode', on_press = self.submit, size_hint_x = None, width = 200)
        layout.add_widget(self.value)
        layout.add_widget(enter)
        # return  backgroundimg
        return layout
    
    def submit(self,obj):
        print("zipcode: " + self.value.text)

MainApp().run()

