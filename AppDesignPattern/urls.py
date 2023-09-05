from django.urls import path
from AppDesignPattern.views import index

app_name = 'AppPatterns'

urlpatterns = [
    path('', index, name='index'),
]
