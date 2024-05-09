from rest_framework import serializers
from .models import *

class PopulationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryPopulation
        fields = ['age_group', 'female_population', 'male_population']