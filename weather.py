import requests
from dotenv import load_dotenv
from pprint import pprint
import os

load_dotenv()

def get_current_weather(city="Kyiv"):
    
    request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric"

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n*** Get current weather Conditions ***\n")
    city = input("\nPlease enter a city name:\n")
    weather_data = get_current_weather(city)

    # pprint(weather_data)
    print(f'Current weather for {weather_data["name"]}')
    print(f'\nThe temperature is {weather_data["main"]["temp"]}')
    print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')

