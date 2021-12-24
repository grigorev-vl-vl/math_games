from django import forms


class AnswerForm(forms.Form):
    your_answer = forms.FloatField(label='Your answer')
