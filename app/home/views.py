from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse("Base page")
    return render(request, "home/index.html", context={'name': 'Home', \
                                                       'image': 'time-bunny.jpg', \
                                                        'alt_desc': 'time bunny meme'})

def tasks(request):
    task_chart = [
        {'task_name': 'Exercise', 'task_description': '5 sets of sit-ups\n5sets of pull-ups', 'task_time': '8AM', 'task_status': 'Done'},
        {'task_name': 'Breakfast', 'task_description': 'Have ample food for a good morning', 'task_time': '8:30AM', 'task_status': 'Not-Done'},
        {'task_name': 'Read books', 'task_description': 'Read 10 pages of any book', 'task_time': '9AM', 'task_status': 'Done'},
        {'task_name': 'Online meeting', 'task_description': 'Progress report on project', 'task_time': '10AM', 'task_status': 'Done'},
    ]
    return render(request, 'home/tasks.html', context={'name': 'Tasks', 'task_chart': task_chart})