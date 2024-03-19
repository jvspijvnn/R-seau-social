from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile_User,POST,Comment,Liked
from django.contrib.auth.models import User
from .forms import CommentForm


# Create your views here.
@login_required(login_url= 'signin')
def index(request):
    post = POST.objects.all()
    comment = Comment.objects.all()
    form = CommentForm()
    profiles = Profile_User.objects.all()
    return render(request, 'index.html',{'new_post':post, 'comments':comment,'form':form, 'profiles':profiles})
 
#uploading post
@login_required(login_url= 'signin')
def upload(request):
    if request.method == "POST":
        user = request.user.username
        image = request.FILES["img"]
        if image != "":
            new_post = POST.objects.create(user = user, image = image)
            new_post.save()
            return redirect('/')

        else: 
            return redirect('/')
    
    return HttpResponse('bienas noches')


# Votre fonction de vue
@login_required(login_url='signin')
def settings(request):
    
    customer = Profile_User.objects.get(user = request.user)
    print(customer)


    return render(request, 'setting.html')

def like(request,post_id):
    post = POST.objects.get(id = post_id)
    username = request.user.username
    like_filter = Liked.objects.filter(post_id = post_id, username = username).first()
    if like_filter == None:
        new_like = Liked.objects.create(post_id = post_id, username = username)
        new_like.save()
        post.number_of_like = post.number_of_like+1
        post.save()
        return redirect('/')
        
    else:
        like_filter.delete()
        post.number_of_like = post.number_of_like-1
        post.save()
        return redirect('/')

    return HttpResponse("ça a marché")
    

       
def profile(request):
    return render(request,'profile.html')




