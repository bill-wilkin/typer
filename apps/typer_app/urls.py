from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('race-page', views.race_page),  # Renders race.html
    path('finish', views.finish),  # post request after typing ends
    path('results-page', views.results_page),  # renders results page
]
