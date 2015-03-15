from django.shortcuts import render_to_response
from django.template import RequestContext
from rest_framework import viewsets
import requests
import json

from weatherapp.models import *
from weatherapp.serializers import *


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


def home(request):
    r = requests.get('http://127.0.0.1:8000/station/',
            auth=('username', 'password'))
    result = r.text
    output = json.loads(result)
    count = int(output['count']) - 1
    name = output['results'][count]['name']
    temperature = output['results'][count]['temperature']
    lat = output['results'][count]['lat']
    lon = output['results'][count]['lon']

    data = {
            'name': name,
            'temperature': temperature,
            'lat': lat,
            'lon': lon,
            }

    return render_to_response('index.html', data,
            context_instance = RequestContext(request))
