from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm


from .models import Problem, Contest, ProblemInclusion


def contest_screen(request, contest_id):
    """(request, contest_id) -> list of all problem_text in contest """
    template = loader.get_template('abacus/contest_screen.html')
    contest = get_object_or_404(Contest, pk=contest_id)
    themes = ProblemInclusion.objects.filter(contest=contest).values_list('theme', flat=True).distinct()
    scores = ProblemInclusion.objects.filter(contest=contest).values_list('score', flat=True).distinct()

    context = {
        'contest_id': contest_id,
        'contest': contest,
        'themes': themes,
        'scores': scores,
    }
    return HttpResponse(template.render(context, request))

def team_screen(request, contest_id):
    """ (request, contest_id) -> nice page of abaka"""
    template = loader.get_template('abacus/team-1.html')
    contest = get_object_or_404(Contest, pk=contest_id)

    context = {

    }
    return HttpResponse(template.render(context, request))

def results_screen(request, contest_id):
    """ (request, contest_id) -> nice page of abaka"""
    template = loader.get_template('abacus/results.html')
    contest = get_object_or_404(Contest, pk=contest_id)

    context = {

    }
    return HttpResponse(template.render(context, request))

def answer_form(request, contest_id, problem_id):
    template = loader.get_template('abacus/answer_form.html')
    problem = get_object_or_404(Problem, pk=problem_id)
    contest = get_object_or_404(Contest, pk=contest_id)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            # TODO send the answer to backend? Where do I check it?
            if problem.check_answer(answer_form.cleaned_data['your_answer']):
                return HttpResponse("Solved!")
        # TODO what if form isn't valid
    else:
        answer_form = AnswerForm()

    context = {
        'problem': problem,
        'answer_form': answer_form,
    }
    return HttpResponse(template.render(context, request))

"""
def answer_problem_form(request, contest_id, theme, score):
    template = loader.get_template('abacus/answer_form.html')
    contest = get_object_or_404(Contest, pk=contest_id)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            # TODO send the answer to backend? Where do I check it?
            if problem.check_answer(answer_form.cleaned_data['your_answer']):
                return HttpResponse("Solved!")
        # TODO what if form isn't valid
    else:
        answer_form = AnswerForm()

    context = {
        'problem': problem,
        'answer_form': answer_form,
    }
    return HttpResponse(template.render(context, request))

"""
"""
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


def abacus_main_page(request, contest_id):
    template = loader.get_template('abacus/abacus_main_page.html')
    contest = get_object_or_404(Contest, pk=contest_id)
    contest_problems_list = contest.problem.all
    problem = Problem.objects.get(id=1)
    print(problem.answer)
    if request.method == 'POST':
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            print(problem.answer)
            if answer_form.cleaned_data['your_answer'] == problem.answer:
                return HttpResponse('meow')
    else:
        answer_form = AnswerForm()

    context = {
        'contest': contest,
        'contest_problems_list': contest_problems_list,
        'answer_form': answer_form,
    }
    return HttpResponse(template.render(context, request))

def meow(request):
    template = loader.get_template('abacus/base.html')
    context = {}
    return HttpResponse(template.render(context, request))
"""
