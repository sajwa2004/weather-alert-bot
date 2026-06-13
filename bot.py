import requests
import os

API_KEY = os.environ["8f3da119559b7bc9fb4594bf89c1e2a7"]
CITY = "Kasaragod"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={8f3da119559b7bc9fb4594bf89c1e2a7}&units=metric"

response = requests.get(URL)
data = response.json()

temp = data["main"]["temp"]
weather = data["weather"][0]["main"]

if temp > 35 or weather.lower() == "rain":
    print(f"Alert! Weather in {CITY}: {temp}°C, {weather}")
else:
    print(f"Weather is fine in {CITY}: {temp}°C, {weather}")
