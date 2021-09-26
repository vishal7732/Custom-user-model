from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        birthday = request.POST['birthday']
        phone = request.POST['phone']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if len(password1) < 6 or len(password1) > 10:
                messages.info(request, 'Pls use min 6 max 10 alphanumeric in Password')
                return redirect('/register')    
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('/register')
            else:
                user= User.objects.create_user(name=name, birthday=birthday, email=email, mobile=phone, password=password1)
                user.save();
                messages.info(request, 'Registration Successful')
                auth.login(request, user)
                return redirect('/chat')
        else:
            messages.info(request, 'Passeword not matching')
            return redirect('/register')
        
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/register')

        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def chat(request):
        return render(request, 'chat.html')