from django.shortcuts import render

quizzes = [
	{
		"quiz_number": 1,
		"name": "Know your History",
		"description": "Hur bra kan du dina klassiker?"
	},
	{
		"quiz_number": 2,
		"name": "Unless you know the code, it has no meaning",
		"description": "Kan du dina lag?"
	},
	{
		"quiz_number": 3,
		"name": "What about AI?",
		"description": "Kan du din hackerhistoria?"
	},
]


def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[quiz_number - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quize.html", context)


def question(request, quiz_number, question_number):
	return render(request, "questions.html")

def completed(request, quiz_number):
	return render(request, "results.html")