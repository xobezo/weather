import requests
import numpy as np
import datetime as dt
import json
import os
from openweathermap import *

if __name__ == "__main__":
    ## Uses personal data to get website url
    with open('account.json') as json_file:
        data = json.load(json_file)
        account = json.loads(data)
    weather = openweathermap(lat = account['lat'], lon = account['lon'],appid = account['appid'])


    # Gets the data from the internet and converrts it to JSON
    r = requests.get(weather.make_url())
    data = r.json()

    # Pull time out of the data.
    timestamp = data['current']["dt"]
    current_time = dt.datetime.fromtimestamp(timestamp)

    # Names the folders I will use to store the data. I want it to be easily accessible later
    folders = ["data", current_time.year, current_time.strftime("%B"), current_time.day]

    # Creates the folders if they do not exist
    for itm in folders:
        itm = str(itm)
        if not os.path.exists(itm):
            os.mkdir(itm)
        os.chdir(itm)

    # Creates the data file for this time
    filename = str(current_time.hour) + ".JSON"
    with open(filename, "w") as write_file:
        json.dump(data, write_file)