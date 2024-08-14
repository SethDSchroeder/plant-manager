from django.urls import path
from .views import PlantView

urlpatterns = [
    path('home', PlantView.as_view())
]
