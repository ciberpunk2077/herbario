from django.urls import path

from .campo import *

app_name = 'catalogo-api'

urlpatterns = [
    path('api/campos/<int:pk>/remove/', PlantaDeleteApiView.as_view(), name="api-planta-remove"),

]
