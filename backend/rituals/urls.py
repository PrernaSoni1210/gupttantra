from django.urls import path
from . import views


urlpatterns = [
    path('', views.rituals_list, name='rituals'),
]