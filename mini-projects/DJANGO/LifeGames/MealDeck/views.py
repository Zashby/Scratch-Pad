from django.shortcuts import render, redirect

from django.http import HttpResponse, JsonResponse

import json

from django.urls import reverse

from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return HttpResponse('Hello World')