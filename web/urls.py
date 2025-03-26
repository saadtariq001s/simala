from django.urls import path
from .views import index  # Import the view

urlpatterns = [
    path('', index, name='index'),  # This maps the home ('/') route to index view
]
