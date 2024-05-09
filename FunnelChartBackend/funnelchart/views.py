from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import PopulationSerializer

# Create your views here.

class ReactView(APIView):
    serializer_class = PopulationSerializer
    def get(self, request):
        records = [{"age_group": record.age_group, 
                   }
                  for record in CountryPopulation.objects.all()]
        return Response(records)

    def post(self, request):
        serializer = PopulationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            print('Data has not been serialized properly..')

def funnelChartView(request):
    records, data = CountryPopulation.objects.all(), {}
    data['age_group'] = [record.age_group for record in records]
    data['female_population'] = [record.female_population for record in records]
    data['male_population'] = [record.male_population for record in records]
    
    return render(request, 'funnel-chart.html', {'data':data}) 