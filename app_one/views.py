from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja
from django.contrib import messages


def home_page(request):
    context = {
        "Dojos": Dojo.objects.all()  
    }
    return render(request,"index.html",context)

def create_dojo(request):
    
    if request.method =="POST":
        errors = Dojo.objects.basic_validator(request.POST)
        if (len(errors)>0):
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
        else:
            new_dojo = Dojo.objects.create(
                name = request.POST["name"],
                city = request.POST["city"],
                state = request.POST["state"]

            )
            print(new_dojo)   
    return redirect('/')

def create_ninja(request):
    if request.method =="POST":
        dojo_id = int(request.POST["dojo"])
        dojo_get = Dojo.objects.get(id = dojo_id) 
    
        Ninja.objects.create(
            first_name = request.POST["first_name"],
            last_name = request.POST['last_name'],
            dojo_id = dojo_get
        )
    return redirect('/')