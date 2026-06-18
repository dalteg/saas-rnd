from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.
def login_view(requests):
    if  requests.method == "POST":
        username = requests.POST.get("username") or None
        password = requests.POST.get("password") or None
        if all([username, password]):
            user = authenticate(requests, username=username, password=password)
            if user is not None:
                login(requests, user)
                print("Login here!")
                return redirect("/")
    return render(requests, "auth/login.html", {})


def register_view(request):
    if  request.method == "POST":
        print(request.POST)
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None
        #In future  I will  handle this section using  forms 
        #user_exists = User.objects.filter(username__iexact=username).exists
        #email_exists = User.objects.filter(email__iexact=username).exists
        try:
            User.objects.create_user(username, email=email, password=password)
        except:
            pass
    return render(request, "auth/register.html", {})