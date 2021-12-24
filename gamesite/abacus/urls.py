from django.urls import path

from . import views

urlpatterns = [
    # ex: /abacus/
    path('', views.index, name='index'),
    # ex: /abacus/6
    # path('')
    # TODO path to game
    # ex: abacus/problems/
    path('problems/', views.problems_list, name='problems_list'),
    # ex: abacus/problems/5
    path('problems/<int:problem_id>/', views.problem_details, name='problem'),
    # ex: abacust/contest/5
    path('contest/<int:contest_id>/', views.context_problems, name='contest'),
    # ex: abacus/login
    path('login/', views.login_view, name='login'),
    # ex: abacus/form
    path('form', views.simple_form, name='simple_form')
]
