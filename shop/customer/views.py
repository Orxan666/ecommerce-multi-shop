from django.shortcuts import render

# Create your views here.


def contact(request):
    return render(request, "contact.html")


def wishlist(request):
    return render(request, "wishlist.html")


def bascet(request):
    return render(request, "bascet.html")


def checkout(request):
    return render(request, "checkout.html")


def login_view(request):
    return render(request, "login.html")


def logout_view(request):
    pass


def register(request):
    return render(request, "register.html")
