from django.shortcuts import render
import requests
import json


# Create your views here.
def index(request):
      city = request.GET.get(city)
      icon_url = 'https://openweathermap.org/img/wn/10d@2x.png'
      if city: 
            weather_data = get_weather(city)
            if weather_data is not None: 
                  weather = weather_data['weather'][0]['description']
                  temperature = weather_data['main']['temp']
                  city = weather_data['name']
                  country = weather_data['sys']['country']
                  icon = weather_data['weather'][0]['icon']
                  weather_description = weather_data['weather'][0]['description']
                  pressure = weather_data['main']['pressure']
                  humidity = weather_data['main']['humidity']
                  wind_speed = weather_data['wind']['speed']
            else: 
                  return render(request, 'weather/index.html')
            return render(request, 'weather/index.html', {
                  'icon_url': icon_url,
                  'city': city, 
                  'country': country,
                  'weather': weather,
                  'temperature': temperature,
                  'weather_description': weather_description,
                  'pressure': pressure,
                  'humidity': humidity,
                  'wind_speed': wind_speed
            })

      return render(request, 'weather/index.html')

def get_weather(city):
      url = "https://api.openweathermap.org/data/2.5/weather"
      api_key = "f93d8d73d5e8f6363de83ddc183c8346"
      parameters = {
            'q': city,
            'appid': api_key,
            'units': 'metric'
      }
      response = requests.get(url, params=parameters)
      if response.status_code == 200:
            return response.json()
      else: 
            return None
      