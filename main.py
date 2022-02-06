
import json
from startscreen import MainApp
from weather import check_conditions

# MainApp().run()

with open('zipcode.json', 'r') as openfile:
    json_zip = json.load(openfile)

zipcode = json_zip["zipcode"]
print("hello" )

temperature = check_conditions(int(zipcode))[0]
print(temperature)