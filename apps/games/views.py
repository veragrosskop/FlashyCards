from django.shortcuts import render
from django.http import HttpResponse

# Views
def study(request):
    return render(request, 'games/base.html')

def quiz(request):
    return render(request, 'games/base.html')
