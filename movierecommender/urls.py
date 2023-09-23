from django.urls import path
from . import views


urlpatterns = [
    # route is a string contains a URL pattern
    path('', views.movie_recommendation_view, name='recommendations'),
]
