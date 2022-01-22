from django.urls import path


from . import views

app_name = 'abacus'
urlpatterns = [
    path('contest/<int:contest_id>/', views.contest_screen, name='contest_screen'),
    path('contest/<int:contest_id>/problem/<int:problem_id>', views.answer_form, name='answer_form'),
    path('contest/<int:contest_id>/team1', views.team_screen, name='team_screen'),
    path('contest/<int:contest_id>/results', views.results_screen, name='results_screen'),
    ]




