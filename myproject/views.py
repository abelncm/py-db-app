from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    context = {}
    # return HttpResponse('<h1>Procceed to URL: /admin or /onlinecourse</h1>')
    return render(request, 'home.html', context)

