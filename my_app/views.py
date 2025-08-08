from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Task
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        duration = request.POST['duration']
        status = request.POST['status']

        user = Task.objects.create(name = name,duration = duration,status = status)
        user.save()
        return redirect('display')
    else:    
        return render(request,'index.html')



def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username):
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email):
                messages.info(request,'Email alredy taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username = username,
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    password = password1
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')

    else:
        return render(request,'register.html')
    




def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    




def display(request):
    stu = Task.objects.all()
    return render(request,'display.html',{'items':stu})


def delt(request,pk):
    items = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        items.delete()
        return redirect('display')
    

def edit(request,pk):
    task =  get_object_or_404(Task, pk = pk)
    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.duration = request.POST.get('duration')
        task.status = request.POST.get('status')
        task.save()
        return redirect('display')
    else:
        return render(request,'edit.html',{'task': task})


