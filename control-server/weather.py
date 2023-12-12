import datetime
import requests
import logging
import dotenv
import time
import os

dotenv.load_dotenv()

logging.basicConfig(filename='module.log', level=logging.DEBUG)


class Weather:
    def __init__(self, city):
        self.city = city
        self._key = os.environ.get('WEATHER_KEY')
        self.url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self._key}"

    def __temp_to_celcius(self, temp):
        try:
            return round(float(temp) - 273.15, 2)
        except ValueError as e:
            logging.error(f"Error <to calculate temp> {e}")
            return None

    def __unix_to_datetime(self, timestamp):
        return datetime.datetime.fromtimestamp(timestamp)

    def get_temp(self, mode):
        try:
            mode = str(mode).lower()
            response = requests.get(self.url)

            if response.status_code != 200:
                return response.status_code

            response = response.json()
            weather_all = response['weather'][0]
            temp_all = response['main']
            sys_all = response['sys']

            if mode == "morning":
                temp_max = self.__temp_to_celcius(temp_all['temp_max'])
                temp_min = self.__temp_to_celcius(temp_all['temp_min'])
                sunset = self.__unix_to_datetime(sys_all['sunset'])
                sunrise = self.__unix_to_datetime(sys_all['sunrise'])

                data = {
                    "temp_max": temp_max,
                    "temp_min": temp_min,
                    "sunset": sunset,
                    "sunrise": sunrise,
                    "date": self.__unix_to_datetime(time.time())
                }

            else:
                weather_icon_url = f"https://openweathermap.org/img/wn/{weather_all['icon']}@2x.png"
                feel_temp = self.__temp_to_celcius(temp_all['feels_like'])
                temp = self.__temp_to_celcius(temp_all['temp'])
                weather_des = weather_all['main']
                data = {
                    "temp": temp,
                    "feel_like": feel_temp,
                    "description": weather_des,
                    "icon_url": weather_icon_url,
                    "date": self.__unix_to_datetime(time.time())
                }

            return data

        except requests.RequestException as e:
            logging.error(f"Request Exception: {e}")

        except KeyError as e:
            logging.error(f"Key Error: {e}")

        return None