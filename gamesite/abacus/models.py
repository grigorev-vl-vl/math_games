from django.db import models
from django.db.models import FloatField


class Problem(models.Model):
    problem_text = models.TextField()
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.problem_text


class Answer(models.Model):
    question = models.ForeignKey(Problem, on_delete=models.CASCADE)
    answer_value: FloatField = models.FloatField(default=0)

    def __str__(self):
        return self.answer_value


class Contest(models.Model):
    problem = models.ManyToManyField(Problem, through='ProblemInclusion')
    headline = models.CharField(max_length=200)

    def __str__(self):
        return self.headline

    def check_answer(self, answer):
        # TODO bound here answer instead of score. It's not score here. It's just an exercise in 'through' model
        right_answer = ProblemInclusion.objects.get(contest=self, problem=self.problem)
        if answer == right_answer.score:
            return True
        else:
            return False

class ProblemInclusion(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    theme = models.CharField(max_length=200)

