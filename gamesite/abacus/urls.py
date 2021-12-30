from django.urls import path


from . import views

app_name = 'abacus'
urlpatterns = [
    path('contest/<int:contest_id>/', views.contest_screen, name='contest_screen'),
    path('contest/<int:contest_id>/problem/<int:problem_id>', views.answer_form, name='answer_form')
    ]




