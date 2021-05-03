from flask import Flask, render_template, request, redirect, url_for, session
import requests

import config


app = Flask(__name__)
app.secret_key = config.SESSION_SECRET

WEATHER_URL = "https://community-open-weather-map.p.rapidapi.com/weather"
HEADERS = {
    'x-rapidapi-key': config.WEATHER_TOKEN,
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
}
QUERY = {
    "q": "moscow",
    "units": "metric"
}


@app.route('/', methods=["POST", "GET"])
def input_city():
    print(f"{request.cookies['csrftoken'] = }")
    print(f"{session = }")
    if request.method == "POST":
        location_name = request.form["location-name"]
        session[request.cookies['csrftoken']] = location_name
        return redirect(url_for("get_weather"))
        # return redirect(url_for("get_weather"))
    else:
        if session.get(request.cookies['csrftoken'], None) is not None:
            return redirect(url_for("get_weather"))
        return render_template('index.html')


@app.route('/weather')
def get_weather():
    print(f"{request.cookies['csrftoken'] = }")
    print(f"{session = }")

    if request_text := session.get(request.cookies['csrftoken'], None):
        QUERY['q'] = request_text
        print(QUERY)
    else:
        return render_template('weather.html', context={'code': 406})

    resp = requests.get(WEATHER_URL, headers=HEADERS, params=QUERY)

    # 404 or something - instant render
    if not resp.ok:
        context = {
            'code': 400,
            'query': request_text,
        }
        print(context)
        return render_template('weather.html', context=context)

    resp = resp.json()

    context = {
        'code': 200,
        'city': {
            'name': resp['name'],
            'country': resp['sys']['country'],
            'id': resp['sys']['id']
        },
        'weather': {
            'temp': round(resp['main']['temp']),
            'temp_feels_like': round(resp['main']['feels_like']),
            'description': resp['weather'][0]['description'],
            'category': resp['weather'][0]['main'],
            'icon': resp['weather'][0]['icon']
        }
    }
    print(context)
    return render_template('weather.html', context=context)


@app.route('/drop')
def drop_previous_location():
    session.pop(request.cookies['csrftoken'])
    return redirect(url_for('input_city'))


if __name__ == '__main__':
    app.run(debug=True)
