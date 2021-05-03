# weather-webapp
This is small weather web application made with `Flask` and `Bootstrap 5`, it relies on [OpenWeatherMap API](https://openweathermap.org/api). At that moment I don't host it, \
but I'm planning to do it.

## How it looks like
![index](https://drive.google.com/uc?export=view&id=1BlZ7U29IBkxonQmBVxqdQ3bUy754FmkT)
![forecast](https://drive.google.com/uc?export=view&id=1Qd9oYbMQHyja3BdnpN5cMhhMPcYmP42m)

## What does it have
1. Sessions. If you have searched for certain city, this app will remember it. If you want to get \
a new location, press "new location" button.
2. Depending on OpenWeatherMap response, \
   it will place certain [images](/static/weather-images) to match weather type (Rain, Snow, etc)

## To run it locally
1. Get OpenWeatherMap API key from [official site](https://openweathermap.org/api).
2. `(venv)$ pip install -r requirements.txt`
3. `(venv)$ touch config.py`
```python
# config.py

WEATHER_TOKEN = 'token_from_open_weather_map'
SESSION_SECRET = 'flask_session_secret_key'
```
4. `(venv)$ python app.py`

## Plans
1. Location suggestion while typing
2. Flask Session -> DB
3. Flask -> Django
4. Set video as background