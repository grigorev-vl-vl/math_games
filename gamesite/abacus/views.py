from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm

from .models import Problem, Contest, ProblemInclusion


def index(request):
    return HttpResponse("Hello, world. You're at the abacus index.")


def students_screen(request):
    return HttpResponse("Hello, there. You're looking at the student's screen")


def problems_list(request):
    return HttpResponse("Hello! You're looking at the list of problems")


def problem_details(request, problem_id):
    template = loader.get_template('abacus/problem_details.html')
    problem = get_object_or_404(Problem, pk=problem_id)
    context = {
        'problem': problem,
    }
    return HttpResponse(template.render(context, request))


def context_problems(request, contest_id):
    template = loader.get_template('abacus/contest_screen.html')
    contest = get_object_or_404(Contest, pk=contest_id)
    contest_problems_list = contest.problem.all

    context = {
        'contest_problems_list': contest_problems_list,
    }
    return HttpResponse(template.render(context, request))


# TODO what's problem_id? Is it absolute id? Or the problem gets it's own id in contest
def answering_problem(request, contest_id, problem_id):
    template = loader.get_template('abacus/answering_problem.html')
    contest = get_object_or_404(Contest, pk=contest_id)
    problem = contest.problem.get(id=problem_id)
    if request.method == 'POST':
        # Create a filled form:
        answer_form = AnswerForm(request.POST)
        # check whether it's valid:
        if answer_form.is_valid():
            # check whether the answer is correct:
            # TODO But here we just create 'form' for that problem_id, this is not it's number in contest
            # TODO yet we don't know which problem is in question
            if answer_form.cleaned_data['your_answer'] == problem.answer:
                print(answer_form.cleaned_data['your_answer'])
                return HttpResponse("Solved!")
    # If we see GET, then we show a blank form:
    else:
        answer_form = AnswerForm()

    context = {
        'answer_form': answer_form,
        'problem': problem,
    }
    return HttpResponse(template.render(context, request))


def simple_form(request):
    template = loader.get_template('abacus/simple_form.html')
    if request.method == 'POST':
        # Create a filled form:
        form = AnswerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponse("The form is valid!")

    # If we see GET, then we show a blank form:
    else:
        form = AnswerForm()

    return render(request, 'abacus/simple_form.html', {'form': form})


def nice_cat(request):
    template = loader.get_template('abacus/not_found_page.html')
    context = {}
    return HttpResponse(template.render(context, request))

def example_template(request):
    template = loader.get_template('abacus/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

