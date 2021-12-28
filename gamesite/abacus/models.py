from django.db import models


class Problem(models.Model):
    problem_text = models.TextField()
    pub_date = models.DateTimeField('date_published')
    answer = models.FloatField()

    def check_answer(self, your_answer):
        """Returns True if the answer is correct"""
        return your_answer == self.answer

    def __str__(self):
        return self.problem_text


class Contest(models.Model):
    problem = models.ManyToManyField(Problem, through='ProblemInclusion')
    headline = models.CharField(max_length=200)

    def __str__(self):
        return self.headline


class ProblemInclusion(models.Model):
    """There are scores and theme of each problem in a given contest"""
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    theme = models.CharField(max_length=200)



