from django.shortcuts import render
import json # request openweathermap return result in json format
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city= request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=5864b80a2d4f7a934f6ad737ce3239ac').read()
        json_data = json.loads(res)
        temp1=float(json_data['main']['temp'])
        temp=temp1-273.15
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(temp)+'C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})
    