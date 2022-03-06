from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import AbacusAnswer
from django.urls import reverse
from django.views.decorators.csrf import ensure_csrf_cookie

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

def team_screen(request, contest_id, team_id):
    """ (request, contest_id) -> nice page of abaka"""
    template = loader.get_template(f'abacus/team-{team_id}.html')
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

@ensure_csrf_cookie
def get_answer(request, contest_id, team_id):
    """ (request, contest_id) -> nice page of abaka"""
    template = loader.get_template(f'abacus/team-{team_id}-forms.html')
    contest = get_object_or_404(Contest, pk=contest_id)

    if request.method == 'POST':
        print('meow')
        print(request)
        print(request.POST)
        return HttpResponseRedirect(reverse('results_screen', args=(contest_id,)))
    elif request.method == 'GET':
        context = {

        }
        return HttpResponse(template.render(context, request))
