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
            return JsonResponse(f"CREATED A NEW TASK SUCESSFULLY {serializer.data}",status=201,safe=False)
        return JsonResponse("FAILED TO CREAET A NEW TASK",status=400,safe=False)
    
    else:
        return JsonResponse("REQUEST NOT ALLOWED",status=400,safe=False)