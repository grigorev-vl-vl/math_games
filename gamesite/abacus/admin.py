from django.contrib import admin

from .models import Problem, Contest, ProblemInclusion


class ProblemInclusionInline(admin.TabularInline):
    model = ProblemInclusion
    extra = 2


class ProblemAdmin(admin.ModelAdmin):
    inlines = (ProblemInclusionInline, )


class ContestAdmin(admin.ModelAdmin):
    inlines = (ProblemInclusionInline, )


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Contest, ContestAdmin)
