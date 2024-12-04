from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
from new.models import Question, JobSeeker, Application

def save_question(request):
    if request.method == "POST":       
        app_id = request.POST.get('app_id') 
        try:
            application = Application.objects.get(app_id=app_id)
        except Application.DoesNotExist:
            raise Http404("Application not found")
        
        # Retrieve questions from the POST request
        question1 = request.POST.get('question1', '')
        question2 = request.POST.get('question2', '')
        question3 = request.POST.get('question3', '')
        question4 = request.POST.get('question4', '')
        question5 = request.POST.get('question5', '')
        question6 = request.POST.get('question6', '')
        question7 = request.POST.get('question7', '')
        question8 = request.POST.get('question8', '')
        question9 = request.POST.get('question9', '')
        question10 = request.POST.get('question10', '')

        # Save all questions as a single database entry
        Question.objects.create(
            application=application,
            question1=question1,
            question2=question2,
            question3=question3,
            question4=question4,
            question5=question5,
            question6=question6,
            question7=question7,
            question8=question8,
            question9=question9,
            question10=question10
        )
        return redirect('Dashboard') 

    return render(request, 'Set_assessment.html') 

