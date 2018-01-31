#views.py

import os
from django.http import HttpResponse
from django.shortcuts import render
from .gather_db import get_data
#from /spiders/spiders/spiders import db_data.txt

def index(request):
#    return HttpResponse("<h1>This is the articles app homepage</h1>")
    #os.system("> ./spiders/spiders/spiders/db_data.txt")
    data = get_data()
    return render(request, 'index.html', { 'dictionary' : data })


