from rest_framework import serializers
from shipparams.models import Ship_params

class Shipserializer(serializers.ModelSerializer):

    class Meta:
        model = Ship_params
        fields = '__all__'
