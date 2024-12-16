import requests
import os
from dotenv import load_dotenv
import json


class Weather:
    def __init__(self):
        # Loading .env file
        load_dotenv()
        self.API_KEY=os.getenv('API_KEY')
        self.url=f'https://api.openweathermap.org/data/2.5/weather?lat={40.4548}&lon={-73.3124}&appid={self.API_KEY}'

    # Method to fetch and save weather details in a file.
    def fetch_weather_details(self):
        self.content=requests.get(self.url)
        self.content=self.content.text
        with open("./artifacts/weather.json", "w") as json_file:
            json.dump(self.content, json_file, indent=4)  # Pretty-print JSON with an indent

        return None

    # Method to get data from saved file.
    def get_weather_data(self):
        self.weather_data=json.load(open('./artifacts/weather.json'))
        self.weather_data=eval(self.weather_data)
        self.weather=self.weather_data['weather'][0]['main']
        self.temperature=round(((self.weather_data['main']['temp']-273.2)*1.8)+32, 1)
        return self.weather, self.temperature
