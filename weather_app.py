import tkinter as tk
from tkinter import font
import requests

root = tk.Tk()

HEIGHT = 500
WIDTH = 600


def format_response(weather):
    try:
        name =(weather['name'])
        desc = (weather[0]['description'])
        temp = (weather['main']['temp'])

        final_str = " city: %s \nCondition: %S \nTemperate(F): %s" % (name, desc,temp)
    except:
        final_str = 'There was a Problem Finding that city' 
        return final_str

def get_weather(city):
    weather_key = 'a809ed50df638e21c97d4ba5af7e917'
    url = 'https://api.openweathermap.org/data/2.5/'
    params = {'APPID': weather_key, 'q':city, 'units':'imperial'}
    response = requests.get(url, params = params)
    weather = response.json()

    label['text'] = format_response(weather)
   
canvas = tk.Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

background = tk.PhotoImage(file = 'landscape.png')
background_image = tk.Label(root, image = background)
background_image.place(relwidth = 1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd = 5)
frame.place(relx = 0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor = 'n')

entry = tk.Entry(frame, bg='white', font=('courier', 18) )
entry.place(relwidth = 0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", command= lambda: get_weather(entry.get()), font=('courier', 12))
button.place(relx = 0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#80c1ff", bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight=0.6, anchor = 'n')

label = tk.Label(lower_frame, anchor = 'nw', justify ='left', font=('courier', 18) ) 
label.place( relwidth=1, relheight=1)
























root.mainloop()






#After this program create a GUI guessing app