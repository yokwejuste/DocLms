from django.shortcuts import render
from .pyrebase_settings import *
from django.shortcuts import render

from .pyrebase_settings import *


def index(request):
    # accessing our firebase data and storing it in a variable
    name = database.child('Data').child('Name').get().val()
    stack = database.child('Data').child('Stack').get().val()
    framework = database.child('Data').child('Framework').get().val()

    context = {
        'name': name,
        'stack': stack,
        'framework': framework
    }
    return render(request, 'index.html', context)
