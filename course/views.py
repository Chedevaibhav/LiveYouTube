from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(r):
    return HttpResponse("<h1> Hii Welcome To Our first session</h1>")