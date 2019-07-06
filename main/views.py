from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("<i><strong>Hello World</strong></i> WAHSDKLFJ;A")