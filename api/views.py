import os
import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from rest_framework.throttling import UserRateThrottle
from .throttling import MinuteRateThrottle
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# Create your views here.

api_key=os.environ.get("weather_api_key")


# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/[location]/[date1]/[date2]?key=YOUR_API_KEY 
class LocationWeatherApiView(APIView):
    throttle_classes = [UserRateThrottle,MinuteRateThrottle]

    @swagger_auto_schema(manual_parameters = [openapi.Parameter('city', openapi.IN_QUERY, description="city parameter", type=openapi.TYPE_STRING)])
    
    def get(self,request):
        city=request.query_params.get('city')
        if city == None:
            return Response({'error':'city can not be None!'})
        
        cache_key = f"Weather_data_{city}"
        cache_data = cache.get(cache_key)

        if cache_data:
            return Response(cache_data)
        
        weather_url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/?key={api_key}'

        try:
            response = requests.get(weather_url)

            if response.status_code == 200:
                response_data = response.json()
                cache.set(cache_key , response_data, timeout=60*60)
                return Response(response_data)
            else:
                return Response({'error':'Unable to fetch data'},status=response.status_code)       
        except requests.exceptions.RequestException as e:
            return Response({'error':'an error occurred'},status=500)
              


# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/38.9697,-77.385?key=YOUR_API_KEY 
class LatLonWeatherApiView(APIView):
    @swagger_auto_schema(manual_parameters = [openapi.Parameter('latitude', openapi.IN_QUERY, description="latitude parameter", type=openapi.TYPE_STRING),
                                              openapi.Parameter('longitude', openapi.IN_QUERY, description="longitude parameter", type=openapi.TYPE_STRING)])

    def get(self,request):
        lat=request.query_params.get('latitude')
        lon=request.query_params.get('longitude')
        if lat==None or lon==None:
            return Response({'error':'latitude and longitude can not be None'})
        weather_url=f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}?key={api_key}'
        try:
            response=requests.get(weather_url)
            response_data=response.json()

            if response.status_code == 200:
                return Response(response_data)
            return Response({'error':'Unable to get fetch data'})
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


