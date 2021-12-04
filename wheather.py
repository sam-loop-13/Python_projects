
from pyowm import OWM
from pyowm.utils.config import get_default_config

owm = OWM('e09d51832ca7556db72a96c2fc5f7f29')  # You MUST provide a valid API key

config_dict = get_default_config()
config_dict['language'] = 'ua' 

place = input("В якому місті цікавить погода? -> ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]
#vl = w.humidity
print("В місті " + place + " зазаз " + w.detailed_status)
print("Температура " + str(temp))
print("Вологість "+ str(w.humidity))





"""import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = pyowm.OWM('e09d51832ca7556db72a96c2fc5f7f29')

#place = input("погода в городе: ")

observation = owm.weather_at_place('London,GB')

w = observation.get_weather() 
print(w)


#from pyowm.owm import OWM
#owm = OWM('your-free-api-key')
"""
""" 
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('your free OWM API key')
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather 

# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place('London,GB')
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds    


"""