from django.shortcuts import render

# Create your views here.



def home(request):
    return render(request,'home.html')


def product_list(request):
    return render(request,'product-list.html')

def product_detail(request,pk):
    return render(request,'product-detail.html')