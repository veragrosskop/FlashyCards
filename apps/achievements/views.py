from django.shortcuts import render
from django.http import HttpResponse

# Views
def progress(request):
    return render(request, 'achievements/base.html')

