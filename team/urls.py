from django.urls import path
from . import views

urlpatterns = [
    path('team/', views.TeamMemberListView.as_view(), name='team-list'),
    path('team/add/', views.TeamMemberCreateView.as_view(), name='team-add'),
]