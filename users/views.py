from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')  
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password_confirm = request.POST.get("password_confirm")

        if password_confirm != password:
            context = {'error': 'Паролі не співпадають!'}
            return render(request, 'users/register.html', context)
        
        if CustomUser.objects.filter(email=email).exists():
            context = {'error': 'Користувач з таким email вже існує!'}
            return render(request, 'users/register.html', context)

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            context = {'error': 'Користувач з таким номером телефону вже існує!'}
            return render(request, 'users/register.html', context)
        
        user = CustomUser.objects.create_user(
            username=email, 
            email=email, 
            phone_number=phone_number,  
            first_name=first_name, 
            last_name=last_name, 
            password=password
        )
        
        login(request, user)  
        return redirect('main_page')
    
    return render(request, 'users/register.html')

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user) 
            return redirect("main_page")
        else:   
            context = {"error": "Неправильний логін або пароль"}
            return render(request, "users/login.html", context)

    return render(request, "users/login.html")

def user_logout(request):
    logout(request)  
    return redirect("main_page")

def user_detail(request, user_id):
    if request.user.is_authenticated:
        user_detail = get_object_or_404(CustomUser, id=user_id)
        context = {'user_detail': user_detail}
        return render(request, "users/user_detail.html", context)
    else:
        return redirect("login")
