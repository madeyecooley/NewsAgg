from django.http import HttpResponse
from django.shortcuts import render
from .gather_db import get_data

def index(request):
#    return HttpResponse("<h1>This is the articles app homepage</h1>")
    data = get_data()
    return render(request, 'index.html', { 'dictionary' : data })


