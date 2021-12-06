from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the abacus index.")

def students_screen(request):
    return HttpResponse("Hello, there. You're looking at the student's screen")
