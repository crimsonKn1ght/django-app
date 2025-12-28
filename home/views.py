from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    people = [
        {'name': 'Ricky', 'age': 20},
        {'name': 'Sharma', 'age': 16},
        {'name': 'Mastor', 'age': 23},
        {'name': 'Halluwalia', 'age': 29},
    ]

    hometowns = [
        'Manali', 'Darjeeling', 'ChinaTown', 'Delhi'
    ]

    return render(request, "home/index.html", context={'name': 'Django in \'25', 'peoples': people, 'hometown': hometowns})
    # return HttpResponse("This is a Django server setup.")

def contact(request):
    page = 'contact'
    return render(request, "home/contact.html", context={'name': page})

def about(request):
    page = 'about'
    return render(request, "home/about.html", context={'name': page})