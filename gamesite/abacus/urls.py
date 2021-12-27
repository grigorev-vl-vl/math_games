from django.urls import path


from . import views

urlpatterns = [
    # ex: /abacus/
    path('', views.index, name='index'),
    # ex: abacus/problems/
    path('problems/', views.problems_list, name='problems_list'),
    # ex: abacus/problems/5
    path('problems/<int:problem_id>/', views.problem_details, name='problem_details'),
    # ex: abacus/contest/5
    path('contest/<int:contest_id>/', views.context_problems, name='contest'),
    # ex: abacus/form
    path('form', views.simple_form, name='simple_form'),
    # ex: abacus/contest/5/problem/6
    path('contest/<int:contest_id>/problem/<int:problem_id>', views.answering_problem, name='answering_problem'),
    # ex: abacus/nicecat
    path('nicecat/', views.nice_cat, name='nice_cat'),
    # ex: abacus/example_test
    path('example_test', views.students_screen, name='example_test'),
    # f
    path('starter_template', views.example_template, name='starter_template'),
    # f
    path('abacus_main_page/contest/<int:contest_id>', views.abacus_main_page, name='abacus_main_page'),
]
