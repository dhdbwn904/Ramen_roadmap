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
    map = folium.Map(location=[37.549250, 126.920575], zoom_start=15, width='100%', height='100%', min_zoom=10,)
    
    res_list = Restaurent.objects.all()
    for res in res_list:
        folium.Marker(
            location = [res.lat, res.lng],
            tooltip=res.name,
            popup="""
            <div style="width: 250px; height: auto; font-family: aggro; font-size: 25px; overflow:auto; text-align: center;">
        <img src="{0}" style="width: 100%; height: auto">
        <div style="font-size : 35px; font-weight: bold;">{1}</div>
        <div style="font-size: 20px; padding-bottom: 5px; color: #f31f1f">★{2}</div>
        <div style="font-size: 15px; font-weight: lighter;">{3}</div> 
        </div>
            """.format(res.img, res.name, res.point, res.address),
            icon=folium.Icon(
                color="red",
                icon_color='white',
                icon='bookmark'
            )
        ).add_to(map)

    maps = map._repr_html_()
    return render(request, 'home.html', {'map' : maps})
