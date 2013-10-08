from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html');