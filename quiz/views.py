from django.shortcuts import render

def start(request):
	return render(request, "start.html")

def quize(request, quiz_number):
	return render(request, "quize.html")

def questions(request, quiz_number, question_number):
	return render(request, "questions.html")

def results(request, quiz_number):
	return render(request, "results.html")
