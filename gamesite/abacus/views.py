from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Problem


def index(request):
    return HttpResponse("Hello, world. You're at the abacus index.")

def students_screen(request):
    return HttpResponse("Hello, there. You're looking at the student's screen")

def problems_list(request):
    return HttpResponse("Hello! You're looking at the list of problems")

def problem_details(request, problem_id):
    template = loader.get_template('abacus/problem_text.html')
    context = {}
    return HttpResponse(template.render(context, request))
