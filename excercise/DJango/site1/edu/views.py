from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)
from datetime import datetime

# Create your views here.
def index(request):
    context = {
        'title': 'Login',
        'name' : 'Kenny',
        'date' : datetime.now()
    }
    
    return render(request, 'edu/index.html', context)