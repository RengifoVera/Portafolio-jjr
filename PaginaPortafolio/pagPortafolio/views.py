from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):

    if request.method=="POST":
        name=request.POST["Asunto"]
        mensaje=request.POST["name"] + " " + request.POST["email"] + " " +request.POST["tel"]+ " " + request.POST["mensaje"]
        email_from=settings.EMAIL_HOST_USER
        receptor= ["rengifovera162@gmail.com"]
        send_mail(name,mensaje,email_from,receptor)

    return render(request,"pagPortafolio/home.html")


