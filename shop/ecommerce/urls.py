
from django.urls import path
from . import views

app_name='ecommerce'

urlpatterns = [
    path('',views.home,name='home'),
    path('product-list/',views.product_list,name='product-list'),
    path('product-detail/<int:pk>/',views.product_detail,name='product-detail'),

]
