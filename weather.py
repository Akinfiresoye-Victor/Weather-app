from tkinter import *
import requests


api_key='0bf4360d86a22e077adad658bfa02e37'



root=Tk()

root.title('Api')

#creating a function to get the weather of a city
def get_city():
    try:
        city=my_city.get()
        api_call=f'http://api.openweathermap.org/data/2.5/weather?q={city},uk&APPID={api_key}'
        weather_data= requests.get(api_call).json()['main']
        my_weather='Temp is'+ ' ' +str(weather_data['temp'])+' humidity is'+ ' '+str(weather_data['humidity'])+' pressure is' + ' '+ str(weather_data['pressure'])
        display.delete('1.0', END)
        display.insert('1.0', my_weather)
    except KeyError:
        message='Please enter a valid city name'
        display.delete('1.0', END)
        display.insert('1.0', message)    
    
    
city_lbl=Label(root, text='City Name')
city_lbl.grid(row=0, column=0)

my_city=StringVar()
city_entry=Entry(root, textvariable=my_city)
city_entry.grid(row=0, column=1)

my_button= Button(root, text='submit', command=get_city)
my_button.grid(row=0, column=2)

#text is used for making larger text boxes
display=Text(root, height=4, width=45)
display.grid(row=1, column=0, columnspan=3)



mainloop()