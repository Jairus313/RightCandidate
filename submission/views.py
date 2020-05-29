from django.shortcuts import render, redirect
from django.http import HttpResponse
from application.models import Candidate

# Create your views here.

def submit(request):
    candidates = Candidate.objects.all() 
    context = {"candidates":candidates}
    skills = ["python","django"]

    return render(request,"submission.html",{"candidates":candidates})