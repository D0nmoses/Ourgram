from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):

    current_user = request.user


    title = 'Home'

    return render('all-posts/home.html',{"title": title,"user": current_user})