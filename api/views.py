from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET'])
def api_home(request):
    data = ['/advocate', 'advocate:username']
    return Response(data)

@api_view(['GET'])
def advocate_list(request):
    data = ['Dzodi', 'louis','mac']
    return Response(data)

@api_view(['GET'])   
def advocate_detail(request,username):
    data = username
    return Response(data)