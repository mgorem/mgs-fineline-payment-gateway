from django.shortcuts import render
from django.http import HttpResponse


def getAccessToken(request):
    return HttpResponse("Hello, mgs fineline customer")