from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HomeContentView.as_view(), name='home-content'),
    path('about/', views.AboutContentView.as_view(), name='about-content'),
    path('services/', views.ServiceListView.as_view(), name='services-list'),
    
]