from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def index(request):

    nums = ['one', 'two', 'three', 'four', 'five']

    data = {"names" : nums}

    return HttpResponse(json.dumps(data), content_type='application/json')