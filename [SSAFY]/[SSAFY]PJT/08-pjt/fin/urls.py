from django.urls import path
from .import views

urlpatterns = [
    path('invert/', views.invert),
    path('preprocess/', views.preprocess),
    path('age/', views.age),
]
