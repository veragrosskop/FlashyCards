from django.shortcuts import render
from django.http import HttpResponse

# Views
def decks(request):
    return render(request, 'cards/decks.html')
