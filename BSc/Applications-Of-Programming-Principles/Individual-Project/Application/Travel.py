import requests
import urllib
import pprint
from flask import Flask, render_template, request, g

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The code that allows the user to search for something in London.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@app.route('/placecheck')
def placecheck():
    g.result = request.args.get('query')
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query={}+in+London&key=AIzaSyAX3GilMeopBVzXRnkhIkxiQo4i7OtBUoM'.format(g.result)
    r = requests.get(url).json()

    location1 = {
        'name': r['results'][0]['name'],
        'formatted_address': r['results'][0]['formatted_address'],
        'rating': r['results'][0]['rating'],
        }

    location2 = {
        'name': r['results'][1]['name'],
        'formatted_address': r['results'][1]['formatted_address'],
        'rating': r['results'][1]['rating'],
        }

    location3 = {
        'name': r['results'][2]['name'],
        'formatted_address': r['results'][2]['formatted_address'],
        'rating': r['results'][2]['rating'],
        }

    location4 = {
        'name': r['results'][3]['name'],
        'formatted_address': r['results'][3]['formatted_address'],
        'rating': r['results'][3]['rating'],
        }

    location5 = {
        'name': r['results'][4]['name'],
        'formatted_address': r['results'][4]['formatted_address'],
        'rating': r['results'][4]['rating'],
        }

    location6 = {
        'name': r['results'][5]['name'],
        'formatted_address': r['results'][5]['formatted_address'],
        'rating': r['results'][5]['rating'],
        }

    location7 = {
        'name': r['results'][6]['name'],
        'formatted_address': r['results'][6]['formatted_address'],
        'rating': r['results'][6]['rating'],
        }

    location8 = {
        'name': r['results'][7]['name'],
        'formatted_address': r['results'][7]['formatted_address'],
        'rating': r['results'][7]['rating'],
        }

    location9 = {
        'name': r['results'][8]['name'],
        'formatted_address': r['results'][8]['formatted_address'],
        'rating': r['results'][8]['rating'],
        }

    location10 = {
        'name': r['results'][9]['name'],
        'formatted_address': r['results'][9]['formatted_address'],
        'rating': r['results'][9]['rating'],
        }

    return render_template('places.html',
                           location1=location1,
                           location2=location2,
                           location3=location3,
                           location4=location4,
                           location5=location5,
                           location6=location6,
                           location7=location7,
                           location8=location8,
                           location9=location9,
                           location10=location10)

@app.route('/places')
def places():
    g.result = ''
    return render_template('places.html')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Code for journeys
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@app.route('/check')
def check():
    APP_KEY = 'b0ff1186e7e90369d423c1be16b1ae88'

    g.start = request.args.get('Start')
    g.end = request.args.get('End')
    g.date = request.args.get('Date')

    from_ = g.start
    to = g.end
    journey_path_format = 'api.tfl.gov.uk/Journey/JourneyResults/{}/to/{}'
    url_path = urllib.parse.quote(journey_path_format.format(from_, to))

    params = {'nationalSearch': 'true', 'date': g.date}

    r = requests.get('https://' + url_path, params=params)

    all_info = r.json()

    if r.status_code == 400:
        print("Bad Request - 400")
    elif r.status_code == 300:
        print("Multiple Choice")
    else:
        print("")
        
        journeys = all_info["journeys"]
        for journey_idx, journey in enumerate(journeys):
            legs = journey['legs']
            print('{}: Legs = {}'.format(journey_idx, len(legs)))
            legs_list = []
            for leg_idx, leg in enumerate(legs):
                arrival = leg['arrivalPoint']
                departure = leg['departurePoint']
                legs_list.append(' {}: {} {} to {} {} '.format(
                    leg_idx,
                    departure['commonName'], leg['departureTime'],
                    arrival['commonName'], leg['arrivalTime']))

        #print(legs_list) #Code to check the journeys
        
        return render_template('journey.html',
                               msg_start=request.args.get('Start'),
                               msg_end=request.args.get('End'),
                               msg_date=request.args.get('Date'),
                               msg_journey=legs_list
                               )

@app.route("/journey")
def journey():
    g.start = ''
    g.end = ''
    g.date = ''
    return render_template('journey.html')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The code for the weather
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@app.route("/weather", methods=['GET', 'POST'])
def weather():
    #Used OpenWeatherMap and Pretty Printed's video to help create this. https://www.youtube.com/watch?v=lWA0GgUN8kg

    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?id=2643743&cnt=7&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    r = requests.get(url).json()

    weather1 = {
        'temperature_day' : r['list'][0]['temp']['day'],
        'temperature_night' : r['list'][0]['temp']['night'],
        'temperature_min' : r['list'][0]['temp']['min'],
        'temperature_max' : r['list'][0]['temp']['max'],
        'description' : r['list'][0]['weather'][0]['description'],
        'icon' : r['list'][0]['weather'][0]['icon'],  
    }

    weather2 = {
        'temperature_day' : r['list'][1]['temp']['day'],
        'temperature_night' : r['list'][1]['temp']['night'],
        'temperature_min' : r['list'][1]['temp']['min'],
        'temperature_max' : r['list'][1]['temp']['max'],
        'description' : r['list'][1]['weather'][0]['description'],
        'icon' : r['list'][1]['weather'][0]['icon'],  
    }

    weather3 = {
        'temperature_day' : r['list'][2]['temp']['day'],
        'temperature_night' : r['list'][2]['temp']['night'],
        'temperature_min' : r['list'][2]['temp']['min'],
        'temperature_max' : r['list'][2]['temp']['max'],
        'description' : r['list'][2]['weather'][0]['description'],
        'icon' : r['list'][2]['weather'][0]['icon'],  
    }

    weather4 = {
        'temperature_day' : r['list'][3]['temp']['day'],
        'temperature_night' : r['list'][3]['temp']['night'],
        'temperature_min' : r['list'][3]['temp']['min'],
        'temperature_max' : r['list'][3]['temp']['max'],
        'description' : r['list'][3]['weather'][0]['description'],
        'icon' : r['list'][3]['weather'][0]['icon'],  
    }

    weather5 = {
        'temperature_day' : r['list'][4]['temp']['day'],
        'temperature_night' : r['list'][4]['temp']['night'],
        'temperature_min' : r['list'][4]['temp']['min'],
        'temperature_max' : r['list'][4]['temp']['max'],
        'description' : r['list'][4]['weather'][0]['description'],
        'icon' : r['list'][4]['weather'][0]['icon'],  
    }

    weather6 = {
        'temperature_day' : r['list'][5]['temp']['day'],
        'temperature_night' : r['list'][5]['temp']['night'],
        'temperature_min' : r['list'][5]['temp']['min'],
        'temperature_max' : r['list'][5]['temp']['max'],
        'description' : r['list'][5]['weather'][0]['description'],
        'icon' : r['list'][5]['weather'][0]['icon'],  
    }

    weather7 = {
        'temperature_day' : r['list'][6]['temp']['day'],
        'temperature_night' : r['list'][6]['temp']['night'],
        'temperature_min' : r['list'][6]['temp']['min'],
        'temperature_max' : r['list'][6]['temp']['max'],
        'description' : r['list'][6]['weather'][0]['description'],
        'icon' : r['list'][6]['weather'][0]['icon'],  
    }

    return render_template('weather.html',
                       weather1=weather1,
                       weather2=weather2,
                       weather3=weather3,
                       weather4=weather4,
                       weather5=weather5,
                       weather6=weather6,
                       weather7=weather7,
                       )

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The code for the map
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#The map code is stored in the HTML file and is loaded when the template is rendered.
@app.route("/map")
def map():
    return render_template('map.html')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The code for the news
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

@app.route("/news")
def news():
    url = 'https://newsapi.org/v2/top-headlines?country=gb&apiKey=d9f4be1771d240aba26a2f75632705b1'
   
    r = requests.get(url).json()

    news = {
        'source' : r['articles'][0]['source']['name'],
        'author' : r['articles'][0]['author'],
        'title' : r['articles'][0]['title'],
        'description' : r['articles'][0]['description'],
        'url' : r['articles'][0]['url'],
        'published' : r['articles'][0]['publishedAt'],
        }

    news2 = {
        'source' : r['articles'][1]['source']['name'],
        'author' : r['articles'][1]['author'],
        'title' : r['articles'][1]['title'],
        'description' : r['articles'][1]['description'],
        'url' : r['articles'][1]['url'],
        'published' : r['articles'][1]['publishedAt'],
        }

    news3 = {
        'source' : r['articles'][2]['source']['name'],
        'author' : r['articles'][2]['author'],
        'title' : r['articles'][2]['title'],
        'description' : r['articles'][2]['description'],
        'url' : r['articles'][2]['url'],
        'published' : r['articles'][2]['publishedAt'],
        }

    news4 = {
        'source' : r['articles'][3]['source']['name'],
        'author' : r['articles'][3]['author'],
        'title' : r['articles'][3]['title'],
        'description' : r['articles'][3]['description'],
        'url' : r['articles'][3]['url'],
        'published' : r['articles'][3]['publishedAt'],
        }

    news5 = {
        'source' : r['articles'][4]['source']['name'],
        'author' : r['articles'][4]['author'],
        'title' : r['articles'][4]['title'],
        'description' : r['articles'][4]['description'],
        'url' : r['articles'][4]['url'],
        'published' : r['articles'][4]['publishedAt'],
        }

    news6 = {
        'source' : r['articles'][5]['source']['name'],
        'author' : r['articles'][5]['author'],
        'title' : r['articles'][5]['title'],
        'description' : r['articles'][5]['description'],
        'url' : r['articles'][5]['url'],
        'published' : r['articles'][5]['publishedAt'],
        }

    news7 = {
        'source' : r['articles'][6]['source']['name'],
        'author' : r['articles'][6]['author'],
        'title' : r['articles'][6]['title'],
        'description' : r['articles'][6]['description'],
        'url' : r['articles'][6]['url'],
        'published' : r['articles'][6]['publishedAt'],
        }

    news8 = {
        'source' : r['articles'][7]['source']['name'],
        'author' : r['articles'][7]['author'],
        'title' : r['articles'][7]['title'],
        'description' : r['articles'][7]['description'],
        'url' : r['articles'][7]['url'],
        'published' : r['articles'][7]['publishedAt'],
        }

    news9 = {
        'source' : r['articles'][8]['source']['name'],
        'author' : r['articles'][8]['author'],
        'title' : r['articles'][8]['title'],
        'description' : r['articles'][8]['description'],
        'url' : r['articles'][8]['url'],
        'published' : r['articles'][8]['publishedAt'],
        }

    news10 = {
        'source' : r['articles'][9]['source']['name'],
        'author' : r['articles'][9]['author'],
        'title' : r['articles'][9]['title'],
        'description' : r['articles'][9]['description'],
        'url' : r['articles'][9]['url'],
        'published' : r['articles'][9]['publishedAt'],
        }

    return render_template('news.html',
                           news=news,
                           news2=news2,
                           news3=news3,
                           news4=news4,
                           news5=news5,
                           news6=news6,
                           news7=news7,
                           news8=news8,
                           news9=news9,
                           news10=news10,)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The code for the directions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
@app.route('/checkdirections')
def checkdirections():
    APP_KEY = 'AIzaSyDaJkjgxSYnTMJp9fcZkWhxxA3-hf9buTs'

    g.origin = request.args.get('origin')
    g.destination = request.args.get('destination')
    g.mode = request.args.get('mode')

    directions = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin="+g.origin+"&destination="+g.destination+"&mode="+g.mode+"&region=uk&key=AIzaSyDaJkjgxSYnTMJp9fcZkWhxxA3-hf9buTs")
    r = directions.json()
    # for stage in r['routes'][0]['legs'][0]['steps']:
        #route.append(stage['html_instructions'])
        #formatting = ""
        #for instruction in route:
            #resutlts_formatted = formatting + "<br>" + instruction
    return render_template('directions.html')

@app.route("/directions")
def directions():
    g.origin = ''
    g.destination = ''
    g.mode = ''
    return render_template('directions.html')

if __name__ == '__main__':
    app.run(debug=True)
