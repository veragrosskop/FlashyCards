from django.shortcuts import render
from django.http import HttpResponse

# Views
def account(request):
    return render(request, 'users/account.html')