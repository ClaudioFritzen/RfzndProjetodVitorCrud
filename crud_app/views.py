from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import CustomUser


def menu(request):
    return render(request, "menu.html")


def register_user(request):
    return render(request, "register_user.html")


def check_user(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, "check_user.html", context)


def update_user(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }
    return render(request, "update_user.html", context)

def specific_user(request,id):
    user = CustomUser.objects.get(id=id)
    return render(request, "specific_user.html", {'users':user})
    pessoa = Pessoa.objects.get(id=id)
    return render(request, "update.html", {'pessoa': pessoa})


def delete_user(request):
    return render(request, template_name="delete_user.html")



    


def save(request):
    first_name = request.POST.get("First Name")
    last_name = request.POST.get("Last Name")
    cpf = request.POST.get("CPF")
    age = request.POST.get("Age")
    email = request.POST.get("Email")
    CustomUser.objects.create(f_name=first_name, l_name=last_name, cpf=cpf, age=age, email=email)
    users = CustomUser.objects.all()
    context = {
        "users": users
    }
    return render(request, "save.html", context=context)
