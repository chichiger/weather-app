from tkinter import *
import requests
import json
from PIL import ImageTk, Image
from datetime import datetime
 
#Initialize Window
 
root =Tk()
root.geometry("400x400")
root.resizable(0,0) #to make the window size fixed
root.configure(background='lemon chiffon')
root.title("Chichiger's Weather App🌤")


#adding an option to show weather emoji based on weather_id
THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)

 
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
def weather_dislay_icon(weather_id):
    """
    Args:
        weather_id (int): Weather condition code from the OpenWeather API

    Returns:
        Contains a weather symbol
    """
    if weather_id in THUNDERSTORM:
        display_params = ("💥")
    elif weather_id in DRIZZLE:
        display_params = ("💧")
    elif weather_id in RAIN:
        display_params = ("💦")
    elif weather_id in SNOW:
        display_params = ("⛄️")
    elif weather_id in ATMOSPHERE:
        display_params = ("🌀")
    elif weather_id in CLEAR:
        display_params = ("🔆")
    elif weather_id in CLOUDY:
        display_params = ("💨")
    else:
        display_params = ("🌈")
    return display_params
 
city_value = StringVar()
 
def showWeather():
    api_key = "21c30eeb5c96ef4679ad7476fe545a8a"
 
    # Get city name from user from the input field (later in the code)
    city_name=city_value.get()
 
    # API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    # Get the response from fetched url
    response = requests.get(weather_url)
 
    # changing response from json to python readable 
    weather_info = response.json()
 
 
    tfield.delete("1.0", "end") #this line makes sure the output is updated when there is new city
 
 
    if weather_info['cod'] == 200:
        kelvin = 273
 
        temp = int(weather_info['main']['temp'] - kelvin) #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        weather_id = weather_info["weather"][0]["id"]
        weather_symbol = weather_dislay_icon(weather_id)
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
         
        weather = f"\nWeather of: {city_name}\nWeather Id: {weather_symbol}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
    tfield.insert(INSERT, weather)   #to insert or send value in our Text Field to display output
 
 
 
#myImage = ImageTk.PhotoImage(Image.open('latest.png'))
city_head= Label(root, text = 'Search by City or Zip Code🔎', font = ('Comic Sans MS bold', 12), bg='lemon chiffon').pack(pady=10) #to generate label heading

#myImage = myImage.resize(100,100)
#myImage.show()
inp_city = Entry(root, textvariable = city_value,  width = 24, bg='lavender',font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Look Up Weather", font=('Comic Sans MS bold', 10),  activebackground='green', fg='blue', padx=5, pady=5 ).pack(pady= 20)
 
#to show output
 
weather_now = Label(root, text = "The Weather is:", font = ('Comic Sans MS bold', 12), bg='lemon chiffon').pack(pady=10)
 
tfield = Text(root, width=46, height=10, bg='pale turquoise')
tfield.pack()
 
root.mainloop()