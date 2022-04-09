from django.shortcuts import render
from django.http import HttpResponse


def login_me(request):
    return render(request, 'login.html', {'name': 'Userrito'})
