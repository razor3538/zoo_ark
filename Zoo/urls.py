from .  views import *
from django.urls import path


app_name = "product"

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('detail/', DetailView.as_view()),
    path('product/<int:pk>', ProductView.as_view())
]