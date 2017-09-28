from quiz.models import Quiz
from django.shortcuts import render
from django.shortcuts import redirect

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
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	questions = list(quiz.questions.all())
	saved_answers = request.session.get(str(quiz_number), {})
	num_correct_answers = 0
	for question_number, answer in saved_answers.items():
		correct_answer = questions[int(question_number) - 1].correct
		if correct_answer == answer:
			num_correct_answers = num_correct_answers + 1
	num_questions = quiz.questions.count()
	context = {
		"correct": num_correct_answers,
		"total": num_questions,
	}
	return render(request, "results.html", context)

# Förklaring till hur denna fungerar:
# Med request.POST["answer"] hämtar vi ut det val som användaren valde för denna fråga.
# Vi hämtar ut en dictionary med alla svar användaren har gjort hittills och sparar den i saved_answers
# Vi lägger till användarens svar i saved_answers, kopplar till den fråga som användaren är just nu, question_number
# Och sen sparar vi hela listan med frågor som användaren har svarat på igen.
# Slutligen så skickar vi användaren vidare till nästa fråga, genoma att ta den fråga vi är på, question_page, och plussa på 1.

def answer(request, quiz_number, question_number):
	answer = request.POST["answer"]
	saved_answers = request.session.get(str(quiz_number), {})
	saved_answers[question_number] = int(answer)
	request.session[quiz_number] = saved_answers
	quiz = Quiz.objects.get(quiz_number=quiz_number)
	num_questions = quiz.questions.count()
	if num_questions <= question_number:
		return redirect("completed_page", quiz_number)
	else:
		return redirect("question_page", quiz_number, question_number + 1)



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