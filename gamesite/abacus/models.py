from django.db import models
from django.db.models import FloatField


class Problem(models.Model):
    problem_text = models.TextField()
    pub_date = models.DateTimeField('date_published')
    answer = models.FloatField()

    def __str__(self):
        return self.problem_text


class Contest(models.Model):
    problem = models.ManyToManyField(Problem, through='ProblemInclusion')
    headline = models.CharField(max_length=200)

    def __str__(self):
        return self.headline


class ProblemInclusion(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    theme = models.CharField(max_length=200)

