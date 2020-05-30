from django.shortcuts import render, redirect
from django.http import HttpResponse
from application.models import Candidate


skilled = ["python","javascript","html","css","nodejs"]
skill = []

# Create your views here.
def index(request):
    skilled = ["python","javascript","html","css","nodejs"]
    skill = []
    
    if request.method == "POST":
        fname = request.POST["fname"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        skills = request.POST["skills"]

        totalSkills = skills.split(",")

        for i in range(len(totalSkills)):
            if totalSkills[i] in skilled:
                if totalSkills[i] in skill:
                    continue
                else:
                    skill.append(skills[i])

        percent = (len(skill)/len(skilled)) * 100            

        candidate = Candidate.objects.create(fname=fname, phone=phone, email=email, skills=skills, compactibility=percent)
        candidate.save()
        print("done")
        return redirect("/")

    else:    
        return render(request,'index.html')