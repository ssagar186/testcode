import requests
import json

class Golf_check:
    def __init__(self):
        self.temperature_fahrenheit = None
        self.temperature_kelvin = None
        self.get_temp()
    def get_temp(self):
        http_request = requests.post('https://api.openweathermap.org/data/2.5/forecast?id=4180439&appid=7e8bc371335cb8fe11adbc293f3f480c')
        weather_data = http_request.text
        weather_data = json.loads(weather_data)
        print(weather_data)
        temperature_kelvin = weather_data['list'][0]['main']['temp']
        sky_description = weather_data['list'][0]['weather'][0]['main']
        sky_description = sky_description
        temperature_fahrenheit = int((temperature_kelvin-273.15)*9/5+32)
        self.temperature_fahrenheit = temperature_fahrenheit
        self.temperature_kelvin = temperature_kelvin
        if temperature_fahrenheit in range(40,85):
            if sky_description == "Clear":
                print(f"It is a good day to go golfing. The temperature outside is {temperature_fahrenheit}F and conditions are {sky_description}")
            if not sky_description == "Clear":
                print(f"It is not a good day to go golfing. It is {temperature_fahrenheit}F but conditions are {sky_description}")
        if not temperature_fahrenheit in range(40,85):
            print(f"It is not a good day to go golfing. The temperature outside is {temperature_fahrenheit}F")

def main():
    golfcheck = Golf_check()
if __name__ == '__main__':
    main()