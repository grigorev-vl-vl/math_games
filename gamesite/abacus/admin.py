from django.contrib import admin

from .models import Problem, Answer, Contest

admin.site.register(Problem)
admin.site.register(Contest)
admin.site.register(Answer)
