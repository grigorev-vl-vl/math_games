from django.urls import path

from . import views

urlpatterns = [
    # ex: /abacus/
    path('', views.index, name='index'),
    # ex: /abacus/6
    # path('')
    # TODO path to game
]
