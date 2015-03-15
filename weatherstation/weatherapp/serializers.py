from weatherapp.models import Station
from rest_framework import serializers

class StationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Station
        fields = ('url', 'name', 'timestamp', 'temperature', 'lat', 'lon')
