from quiz.models import Quiz
from django.shortcuts import render


# quizzes = [
# 	{
# 		"quiz_number": 1,
# 		"name": "Know your History",
# 		"description": "Hur bra kan du dina klassiker?",
# 		"gif": "https://media.giphy.com/media/oSYflamt3IEjm/giphy.gif",
# 	},
# 	{
# 		"quiz_number": 2,
# 		"name": "Unless you know the code, it has no meaning",
# 		"description": "Kan du dina lag?",
# 		"gif": "https://media.giphy.com/media/gU25raLP4pUu4/giphy.gif",
# 	},
# 	{
# 		"quiz_number": 3,
# 		"name": "What about AI?",
# 		"description": "Kan du din hackerhistoria?",
# 		"gif": "https://media.giphy.com/media/BdrSy2gqURFEk/giphy.gif",
# 	},
# ]
def startpage(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quize.html", context)

def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = quiz.questions.all()
	question = questions[question_number - 1]
	context = {
		"question_number": question_number,
    	"question": question.question,
	    "answer1": question.answer1,
    	"answer2": question.answer2,
	    "answer3": question.answer3,
	    "gif": question.gif,
	    "quiz": quiz,
		"quiz_number": quiz_number,

	}
	return render(request, "questions.html", context)

def completed(request, quiz_number):
	context = {
	    	"correct": 12,
	    	"total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "results.html", context)