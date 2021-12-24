from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import AnswerForm

from .models import Problem, Contest, Answer, ProblemInclusion


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


    if request.method == 'POST':
        # Create a filled form:
        form = AnswerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # check whether the answer is correct:
            # TODO it's an exercise in 'through' something
            # TODO dunno what to do with 'problem'. In the template we iterate through problems in contest_problems_list.
            # TODO But here we just create 'form' for that problem, yet we don't know which problem is in question
            right_answer = ProblemInclusion.objects.get(contest=contest, problem=Problem.objects.get(id=1)).score
            if form.cleaned_data['your_answer'] == right_answer:
                solved = True
                print(form.cleaned_data['your_answer'])
                #return HttpResponse("Solved!")
    # If we see GET, then we show a blank form:
    else:
        form = AnswerForm()

    context = {
        'contest_problems_list': contest_problems_list,
        'form': form,
    }
    return HttpResponse(template.render(context, request))


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Hello {}!".format(username))
    else:
        return HttpResponse("Hello, anonymous")





def simple_form(request):
    template = loader.get_template('abacus/simple_form.html')
    if request.method == 'POST':
        # Create a filled form:
        form = AnswerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return HttpResponse("The form is valid!")

    # If we see GET, then we show a blanck form:
    else:
        form = AnswerForm()

    return render(request, 'abacus/simple_form.html', {'form': form})
