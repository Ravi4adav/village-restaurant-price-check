import requests
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import pytz
import re


load_dotenv()
GMAP_KEY=os.getenv("GMAP_KEY")
place_id='ChIJPYSDLXWBwokRHLcHIl02Kh8'

class Timings:
    def __init__(self):
        self.url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=opening_hours&key={GMAP_KEY}"

    def fetch_timings_data(self):
        self.content=requests.get(self.url)
        self.content=self.content.json()
        with open('./artifacts/timings.json', 'w') as json_file:
            json.dump(self.content, json_file, indent=4)
        return None

    def weekday_timings(self):
        self.content=json.load(open('./artifacts/timings.json'))
        self.open_status=self.content['result']['opening_hours']['open_now']
        self.timings=[]
        for results in self.content['result']['opening_hours']['weekday_text']:
            self.content=re.sub(r'\s'," ",results)
            self.timings.append(self.content)
        return self.open_status, self.timings


    def busy_timings(self):
         # Get current time in "America/New_York"
        timezone_ny = pytz.timezone('America/New_York')
        datetime_ny = datetime.now(timezone_ny)
        print(datetime_ny.hour)
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekdays=weekdays[datetime_ny.weekday()]
        if weekdays=="Monday" and (datetime_ny.hour>=18 and date_ny.hour<=21):
            return "Busy"
        elif weekdays=="Wednesday" and (datetime_ny.hour>=18 and date_ny.hour<=21):
            return "Busy"
        elif weekdays=="Friday" and (datetime_ny.hour>=19 and date_ny.hour<=22):
            return "Busy"
        elif weekdays=="Saturday" and (datetime_ny.hour>=19 and date_ny.hour<=21):
            return "Busy"
        elif weekdays=="Sunday" and ((datetime_ny.hour>=13 and date_ny.hour<=15) or (datetime_ny.hour>=18 and date_ny.hour<=22)):
            return "Busy"
        else:
            return "Regular"
