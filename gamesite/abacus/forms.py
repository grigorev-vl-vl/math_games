from django import forms
from .models import Problem


class AnswerForm(forms.Form):
    your_answer = forms.FloatField(label='Your answer')
    gmeow = forms.CharField(label='Your answer')


