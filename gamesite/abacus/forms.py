from django import forms
from .models import Problem


class AbacusAnswer(forms.Form):
    answer_form = forms.CharField(label=' ', max_length=50)


