from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    # return HttpResponse("Base page")
    return render(request, "home/index.html", context={'name': 'Home', \
                                                       'image': 'time-bunny.jpg', \
                                                        'alt_desc': 'time bunny meme'})

def tasks(request):
    task_chart = []
    # task_chart = [
    #     {'task_name': 'Exercise', 'task_description': '5 sets of sit-ups\n5sets of pull-ups', 'task_time': '8AM', 'task_status': 'Done'},
    #     {'task_name': 'Breakfast', 'task_description': 'Have ample food for a good morning', 'task_time': '8:30AM', 'task_status': 'Not-Done'},
    #     {'task_name': 'Read books', 'task_description': 'Read 10 pages of any book', 'task_time': '9AM', 'task_status': 'Done'},
    #     {'task_name': 'Online meeting', 'task_description': 'Progress report on project', 'task_time': '10AM', 'task_status': 'Done'},
    # ]

    queryset = taskLists.objects.all()
    lenq = len(queryset)

    for i in range(lenq):
        task_chart.append({'task_name': queryset[i].task_name, \
                        'task_description': queryset[i].task_description, \
                            'task_time': queryset[i].task_time, \
                                'task_status': queryset[i].task_status})

    if request.method=="POST":
        data = request.POST
        task_name=data.get('task_name')
        task_description=data.get('task_description')
        task_time=data.get('task_time')
        task_status=data.get('task_status')
        print(task_name, task_description, task_time, task_status)

        taskLists.objects.create(
            task_name=task_name,
            task_description=task_description,
            task_time=task_time,
            task_status=task_status,
        )

        # queryset = taskLists.objects.all()
        task_chart.append({'task_name': task_name, \
                        'task_description': task_description, \
                            'task_time': task_time, \
                                'task_status': task_status})
    
    return render(request, 'home/tasks.html', context={'name': 'Tasks', 'task_chart': task_chart})