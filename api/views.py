from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def api_home(request):
    data = ['/advocate', 'advocate:username']
    return Response(data)

@api_view(['GET','POST'])
def advocate_list(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query is None:
            query = ''
        
        advocates = Advocate.objects.filter(username__icontains=query)
        #data = ['Dzodi', 'louis','mac']
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        username = request.data['username']
        bio = request.data['bio']
        advocate = Advocate.objects.create(username=username,bio=bio)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])   
def advocate_detail(request,username):
    if request.method == 'GET':
        advocate = Advocate.objects.get(username=username)
        serializer = AdvocateSerializer(advocate, many=False)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        advocate = Advocate.objects.get(username=username)
        username = request.data['username']
        bio = request.data['bio']
        advocate.username = username
        advocate.bio = bio
        advocate.save()
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)

    if request.method == 'DELETE':
        advocate = Advocate.objects.get(username=username)
        advocate.delete()
        return Response('user deleted')

@api_view(['GET','POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)