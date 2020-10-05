class openweathermap:
    def __init__(self, lat, lon,appid, exclude = [], units = "standard"):
        """
        A class for the OpenWeatherMap website

        Parameters
        ----------
        :param lat: str
            Latitude for the location
        :param lon: str
            Longitude for the location
        :param appid: str
            ID for the app
        :param exclude: list of str
            The information you want to exclude. Includes 'current, minutely, hourly
            daily, alerts'
        :param units: str
            String for the type of units. Includes standard, metric and imperial.
        """
        self.data ={}
        self.data["lat"] = lat
        self.data["lon"] = lon
        self.data["appid"] = appid
        self.data["exclude"] = exclude
        self.data["units"] = units
        self.base = "https://api.openweathermap.org/data/2.5/onecall?"
    
    def make_url(self):
        """
        Makes a URL using the variables and appends them to the website

        :return: Website url
        """
        keys = self.data.keys()
        iterator = self.base
        for i, key in enumerate(keys):
            itm = self.data[key]
            if not i==0 and itm !=[]:
                iterator += "&"
            if isinstance(itm, str):
                iterator += key + "=" + itm
            else:
                for iy, temp in enumerate(itm):
                    if not iy==0:
                        iterator += "&"
                    iterator += key + "=" + temp
        return iterator