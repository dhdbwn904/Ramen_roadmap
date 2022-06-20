from cgitb import html
from http.client import ImproperConnectionState
import imp
from turtle import color
from django.shortcuts import render
import folium
from numpy import angle, size
from home.models import Restaurent
from django.forms.models import model_to_dict
from folium.features import CustomIcon



# Create your views here.
def home(request):
    map = folium.Map(location=[37.5562364, 126.9292978], zoom_start=20, width='100%', height='100%', min_zoom=10,)

    html = """
    
    """

    res_list = Restaurent.objects.all()
    for res in res_list:
        folium.Marker(
            location = [res.lat, res.lng],
            tooltip=res.name,
            icon=folium.Icon(
                color="red",
                icon_color='white',
                icon='bookmark',
            ),
            popup=html
        ).add_to(map)

    maps = map._repr_html_()

    return render(request, 'home.html', {'map' : maps})
