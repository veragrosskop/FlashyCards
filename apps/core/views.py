from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return render(request, 'core/home.html')

def index(request):
    return HttpResponse("Hello, world. You're at the core index.")
# Create your views here.
