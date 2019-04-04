from django.contrib import admin

from MCpolls.models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
