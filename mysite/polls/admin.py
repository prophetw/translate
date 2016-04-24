from django.contrib import admin

from .models import Question
# Register your models here.

# 自定义 admin 的 form
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question)