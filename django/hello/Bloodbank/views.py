from tkinter import Variable
from django.shortcuts import render,HttpResponse
from datetime import datetime
from Bloodbank.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        "variable1":"This is jimil",
        "variable2":"This is pranav"
    }
    return render(request,"index.html",context)
    #return HttpResponse("This is Bloodbank")
def about(request):
    return render(request,"about.html")
def services(request):
    return render(request,"services.html") 
def contact_view(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact1=contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
        contact1.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,"contact.html")     