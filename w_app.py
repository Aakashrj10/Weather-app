""" A simple weather app with features:
    1. Get current for any city
    2. Shows temperatures, feels-like, humidity, description
    3.Handles error (e.g.,city not found)
"""
import request

API_KEY = "9495fb69e0593f4fd5a48164bab78240"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" # for degree celsius

    }


    response = request.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        

        print(f"\n Weather in {city.title()}:")
        print(f" Description: {weather}")
        print(f" Temperature: {temp}°C")
        print(f" Feels like: {feels}°C")
        print(f" Humidity: {humidity}%\n")

    else:
        print("\n City not found or API error")

def main():
    print("=== Weather App ===")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        get_weather(city)


if __name__ == "__main__":
    main()

