from django.shortcuts import render, get_object_or_404
from .models import Question


def question_list(request):
   questions = Question.objects.all()
   return render(request, 'ankieta/question_list.html', {'questions': questions})

def question_detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'ankieta/question_detail.html', {'question': question})
