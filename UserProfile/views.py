from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile_User


# Create your views here.
@login_required(login_url= 'signin')
def index(request):
    return render(request, 'index.html')

# Votre fonction de vue
@login_required(login_url='signin')
def settings(request):
    if request.method == 'POST':
        try:
            # Récupérez le Profile_User associé à l'utilisateur actuellement connecté
            user_connect = Profile_User.objects.get(user = request.user)
            print(user_connect)
        except Profile_User.DoesNotExist:
            # Gérez le cas où le Profile_User n'existe pas
            print("Le Profile_User n'existe pas pour cet utilisateur.")
        location = request.POST['location']
        about = request.POST['about']
        if location == '':
            messages.info(request, 'vous avez laisser le champ de location vide ! ')
        if about == '':
            messages.info(request, 'vous avez laisser votre bio vide ! ')
        else:
            user_connect.location = location
            user_connect.about = about
            user_connect.save()
            messages.success(request,'vos informations ont bienété sauvegarder')


        print(location, about)

    return render(request, 'setting.html')

