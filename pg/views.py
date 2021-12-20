from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):

    time = request.headers.get('time', 'default')

    nums = ['one', 'two', 'three', 'four', 'five', time]

    data = {"names" : nums}

    return HttpResponse(json.dumps(data), content_type='application/json')