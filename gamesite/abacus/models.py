from django.db import models

class Problem(models.Model):
    problem_text = models.TextField()
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return self.problem_text


class Answer(models.Model):
    question = models.ForeignKey(Problem, on_delete=models.CASCADE)
    answer_number = models.FloatField(default=0)
    def __str__(self):
        return self.answer_number