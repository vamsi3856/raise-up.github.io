from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def sexualviolence(request):
    return render(request,"sexualviolence.html")

def domesticViolence(request):
    return render(request,"domesticViolence.html")

def genderdisc(request):
    return render(request,"genderdisc.html")

def childmarriage(request):
    return render(request,"childmarriage.html")

def womentrafficking(request):
    return render(request,"womentrafficking.html")

def cybercrime(request):
    return render(request,"cybercrime.html")

def getHelp(request):
    return render(request,"getHelp.html")