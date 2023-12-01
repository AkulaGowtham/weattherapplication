import requests
import numpy as np
import joblib
from sklearn.externals import joblib
from tkinter import *

class WeatherForecastInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("Weather Forecast Interface")

        # Create a label for the city name
        self.city_label = Label(self.root, text="Enter city name:")
        self.city_label.grid(row=0, column=0)

        # Create an entry field for the city name
        self.city_entry = Entry(self.root)
        self.city_entry.grid(row=0, column=1)

        # Create a button to get the weather forecast
        self.get_forecast_button = Button(self.root, text="Get Forecast", command=self.get_forecast)
        self.get_forecast_button.grid(row=0, column=2)

        # Create a label to display the weather forecast
        self.forecast_label = Label(self.root, text="")
        self.forecast_label.grid(row=1, column=0, columnspan=3)

        # Load the machine learning model
        self.model = joblib.load('weather_forecast_model.pkl')

    def get_forecast(self):
        # Get the city name from the entry field
        city = self.city_entry.get()

        # Get the weather data for the city
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=20a06e018f556e93503d6cd2112bc128').json()

        # Preprocess the weather data
        temperature = weather_data['main']['temp'] - 273.15
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        # Make a prediction for the weather forecast
        prediction = self.model.predict(np.array([[temperature, humidity, wind_speed]]))

        # Display the weather forecast
        self.forecast_label.config(text=f"The weather forecast for {city} is {prediction[0][0]:.2f} degrees Celsius.")

if __name__ == '__main__':
    # Create an instance of the WeatherForecastInterface class
    interface = WeatherForecastInterface()

    # Call the get_forecast() method on the instance
    interface.get_forecast()

    # Start the mainloop()
    interface.root.mainloop()