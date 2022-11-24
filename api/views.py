from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def api_home(request, *args, **kwags):
    return JsonResponse({"message:Hi there this is an API"},safe=False)