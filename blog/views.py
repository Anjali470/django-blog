from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.object.create_user(username=username, password=password, email=email)
        user.save()
    return render(request, 'blog/signup.html')

def login(request):
    

    return render(request, 'blog/login.html')