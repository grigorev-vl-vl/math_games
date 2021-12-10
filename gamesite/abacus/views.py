from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Problem, Contest, Answer


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

def context_problems(request, contest_id):
    template = loader.get_template('abacus/contest_screen.html')
    contest = get_object_or_404(Contest, pk=contest_id)
    contest_problems_list = contest.problem.all
    context = {
        'contest_problems_list': contest_problems_list,
    }
    return HttpResponse(template.render(context, request))
