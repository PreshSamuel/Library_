from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
class Homepage(View):

    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)

class Signup(View):

    template_name = "signup.html"

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
       
        if password != confirm_password:
            return redirect('lib_app:signup')
        else:
            request.session['username'] = username
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            return redirect('lib_app:home')
        
class Login(View):

    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        user =authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "logged in")
            return redirect('lib_app:home')
        else:
            return redirect('lib_app:home')