from django.urls import path
from . import views

app_name = 'achievements'

urlpatterns = [
    path("progress/", views.progress, name="progress"),
]