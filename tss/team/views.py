from django.shortcuts import render
from .models import *
# Create your views here.

# Team view start
def team(request):

    employees = employee_profile.objects.all(),

    if employees:
        context = {
        'employees' : employees,
        'title': 'Our Team'
        }
    else:
        context = {
        'title': 'Our Team'
        }

    return render(request, 'team/team.html', context)
# Team view end