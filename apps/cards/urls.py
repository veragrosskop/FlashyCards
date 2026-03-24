from django.urls import path
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.shortcuts import render
# #from django.views.generic import TemplateView
from . import views

app_name = 'cards'

urlpatterns = [
    path("decks/", views.decks, name="decks"),
]