from http.client import ImproperConnectionState
from django.shortcuts import render
import folium
from numpy import size

# Create your views here.
def home(request):
    map = folium.Map(location=[37.5562364, 126.9292978], zoom_start=20, width='100%', height='100%', min_zoom=10,)
    maps = map._repr_html_()

    return render(request, 'home.html', {'map' : maps})