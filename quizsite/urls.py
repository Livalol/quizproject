from django.urls import path
from quiz import views

urlpatterns = [
	path("", views.start),
	path("quiz/<int:quiz_number>/", views.quiz),
	path("quiz/<int:quiz_number>/questions/<int:question_number>/", views.questions),
	path("quiz/<int:quiz_number>/results/", views.results),
]