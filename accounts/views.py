from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from UserProfile.models import Profile_User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']        
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return redirect('signup')
            else: 
                user = User.objects.create_user(username = username, password = password)
                user.save()
                user_model = User.objects.get(username = username)
                new_Profile = Profile_User.objects.create(user = user_model,id_user = user.id)
                new_Profile.save()
                messages.info(request,'your account are created')
        else:
            messages.info(request,'your password is not the same')

    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']        
        password = request.POST['password']

        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, 'you are conected')
        
            return  redirect('index')
        
        else:
            messages.info(request,'you are not connected')

    return render (request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signin')