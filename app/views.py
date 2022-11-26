from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def loveu(request):
    return HttpResponse('<marquee> vinay </marquee>')