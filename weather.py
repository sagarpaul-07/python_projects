import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=3280446ce5b1d90fb5bcc1afa36b3b94")
            
            self.response_json = response.json()
            self.temp = self.response_json["main"]["temp"]
            self.temp_min = self.response_json["main"]["temp_min"]
            self.temp_max = self.response_json["main"]["temp_max"]
        except:
            print(f"Failed to fetch weather data for {self.name}.")
    def temp_print(self):
            units_symbol = "°F" if self.units == "imperial" else "°C"
            print(f"In {self.name}, the current temperature is: {self.temp} {units_symbol}")
            print(f"The minimum temperature today will be: {self.temp_min} {units_symbol}")
            print(f"The maximum temperature today will be: {self.temp_max} {units_symbol}")
my_city = City("Tokyo", 35.6895, 139.6917)
my_city.temp_print()

vacation_city = City("Los Angeles", 34.0522, -118.2437)
vacation_city.temp_print()