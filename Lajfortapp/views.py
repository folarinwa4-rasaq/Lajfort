from django.shortcuts import render,redirect
from .models import About,Gallerie,Message,VicePrincipal,Principal,Founder,HeadTeacher,Career,Student,Result,Overall_score
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

def career(request):
    career = Career.objects.all()
    return render(request, 'career.html', {'career':career})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        clas = request.POST['class']
        password2 = request.POST['password2']

        if password == password2:
            if Student.objects.filter(name=username).exists():
                user = User.objects.create_user(username=username, password=password)
                #user.save();
                return redirect('result')
            else:
                messages.warning(request, 'User does not exist')
                return redirect('signup')
        else:
            messages.info(request, 'password not the same')
            return redirect('signup')
    else:
        return render(request, 'signup.html')
    
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
    
        user = auth.authenticate(username=name, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('result')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
@login_required(login_url='login')
def result(request):
    user = request.user
    student = Student.objects.get(name=user.username)
    result = Result.objects.filter(student=student)
    total = Overall_score.objects.filter(student=student)
    return render(request, 'result.html',{'result':result,'student':student,'total':total})

def admin(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username):
                messages.warning(request, 'Admin Already Exist')
                return redirect('admin')
            else:
                user = User.objects.create_superuser(username=username, password=password)
                return redirect('admin:login')
        else:
            messages.info(request, 'password not the same')
            return redirect('admin')
    else:
        return render(request, 'adminsignup.html')