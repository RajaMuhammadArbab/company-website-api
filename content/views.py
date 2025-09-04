from rest_framework import generics
from .models import HomeContent, AboutContent, Service
from .serializers import HomeContentSerializer, AboutContentSerializer, ServiceSerializer
from django.http import JsonResponse

class HomeContentView(generics.RetrieveAPIView):
    serializer_class = HomeContentSerializer
    
    def get_object(self):
        # Get the first HomeContent object or create a default one
        obj, created = HomeContent.objects.get_or_create(
            id=1,
            defaults={
                'title': 'Welcome to Our Company',
                'description': 'This is a default homepage description.',
                'hero_title': 'Innovative Solutions',
                'hero_subtitle': 'We provide the best services for your business'
            }
        )
        return obj

class AboutContentView(generics.RetrieveAPIView):
    serializer_class = AboutContentSerializer
    
    def get_object(self):
        # Get the first AboutContent object or create a default one
        obj, created = AboutContent.objects.get_or_create(
            id=1,
            defaults={
                'title': 'About Our Company',
                'description': 'This is a default about page description.',
                'mission': 'Our mission is to provide excellent services.',
                'vision': 'Our vision is to be the industry leader.'
            }
        )
        return obj

class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    

   
    