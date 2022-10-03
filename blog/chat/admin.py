from django.contrib import admin

from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']



    def get_question(self, obj):
        return obj.question.question_text


class AnswerAdmin(admin.ModelAdmin):
    fields = ['answer_text', 'question']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

