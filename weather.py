import requests

city = "Houston"
api_key = "30d44e8b1ea3fd1ee4e9c72584a31116"

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