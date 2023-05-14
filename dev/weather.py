import requests

city = "Houston"
api_key = input("Please supply API Key > ")

base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
response = requests.get(complete_url)

print (complete_url)

if response.status_code == 200:
    data = response.json()
    main = data["main"]
    weather_data = data["weather"][0]
    temperature = main["temp"]
    humidity = main["humidity"]
    pressure = main["pressure"]
    weather_description = weather_data["description"]