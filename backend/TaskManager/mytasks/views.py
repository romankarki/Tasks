from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@csrf_exempt
def task_list(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer =TaskSerializer(tasks,many=True) 
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method =='POST':
        data = JSONParser().parse(request)
        serializer= TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)
    else:
        return JsonResponse("REQUEST NOT ALLOWED",status=400,safe=False)