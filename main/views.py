from users.models import Profile
from datetime import date, datetime

from django.shortcuts import render
import requests

from main.models import News
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    today = date.today()
    latest_news = News.objects.all().order_by('-date')[:10]
    birthdays = Profile.objects.filter(
        birth_date__month=today.month, 
        birth_date__day=today.day
    )
    weather_data = get_weather_forecast()
    context = {
        'news': latest_news,
        'birthdays': birthdays,
        'weather': weather_data
    }
    return render(request,'main.html',context)

def get_weather_forecast():
    url='http://api.openweathermap.org/data/2.5//forecast?appid=9e0ac0e40a74eb2f4b1d8d04e9d3cdc2&q=Lviv&units=metric'
    try:
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            data = response.json()
            current = data['list'][0]
            forecast = []
            for item in data['list'][1:5]:
                dt_object = datetime.fromtimestamp(item['dt'])
                forecast.append({
                    'time': dt_object.strftime('%H:%M'),
                    'temp': round(item['main']['temp']),
                    'desc': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon'], # Код іконки (напр. 01d)
                })
            return {
                'city': data['city']['name'],
                'current_temp': round(current['main']['temp']),
                'current_desc': current['weather'][0]['description'],
                'current_icon': current['weather'][0]['icon'],
                'hourly': forecast
            }
    except Exception as e:
        print(f"Weather error: {e}")
        return None
