from django.urls import path

from . import views

urlpatterns = [
    # ex: /abacus/
    path('', views.index, name='index'),
    # ex: /abacus/6
    # path('')
    # TODO path to game
    # ex: /problems/
    path('problems/', views.problems_list, name='problems_list'),
    # ex: /problems/5
    path('problems/<int:problem_id>/', views.problem_details, name='problem'),
]
