from django.shortcuts import render, redirect
from django.http import HttpResponse
from application.models import Candidate

# Create your views here.
def index(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        skills = request.POST["skills"]

        candidate = Candidate.objects.create(fname=fname, phone=phone, email=email, skills=skills)
        candidate.save()
        print("done")
        return redirect("/")

    else:    
        return render(request,'index.html')