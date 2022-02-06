
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.label import Label 
import json
Window.size = (900, 620)



class MainApp(App):
    def build(self):
        Window.clearcolor = (37/255, 151/255, 217/255, 0.8)
        backgroundimg = Image(source="background.jpg", size_hint_x = None, width = 200, size_hint_y = None, height = 200)
        layout = GridLayout(rows =4, row_force_default = True, row_default_height = 40, spacing=10,padding=40, top = -100, right = 420)
        label = Label(text='Type Zipcode Below', size_hint_x = None, width = 200, font_size='20sp')
        self.value = TextInput(text='', size_hint_x = None, width = 200)
        enter = Button(text = 'Enter Zipcode', on_press = self.submit, size_hint_x = None, width = 200)
        layout.add_widget(backgroundimg)
        layout.add_widget(label)
        layout.add_widget(self.value)
        layout.add_widget(enter)
        # return  backgroundimg
        return layout
    
    def submit(self,obj):
        print(self.value.text)
        zipcode = self.value.text
        Window.close()
        zip_dict = {'zipcode': str(zipcode)}
        json_dumping = json.dumps(zip_dict)
        with open("zipcode.json", "w") as outfile:
            outfile.write(json_dumping)
        return zipcode

MainApp().run()

