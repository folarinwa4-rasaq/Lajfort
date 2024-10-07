from django.shortcuts import render,redirect
from .models import About,Gallerie,Message,VicePrincipal,Principal,Founder,HeadTeacher
from django.http  import HttpResponse

# Create your views here.

def home(request):
    about = About.objects.all()
    gallery = Gallerie.objects.all().order_by('-id')[:6]
    principal = Principal.objects.all()
    vicePrincipal = VicePrincipal.objects.all()
    founder = Founder.objects.all()
    headTeacher = HeadTeacher.objects.all()
    return render(request,'home.html',{'about':about,'gallery':gallery,'principal':principal,'vicePrincipal':vicePrincipal,'founder':founder,'headTeacher':headTeacher})

def about(request):
    about = About.objects.all()
    return render(request, 'about.html',{'about':about})

def gallery(request):
    gallery = Gallerie.objects.all()
    return render(request, 'gallery.html',{'gallery':gallery})

def contact(request):
    return render(request, 'contact.html')

def message(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        content = Message(name=name, email=email, message=message)
        content.save()
    return render(request, 'contact.html')