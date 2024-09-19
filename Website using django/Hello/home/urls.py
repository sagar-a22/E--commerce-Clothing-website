from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("product_list", views.product_list, name='product'),
    path("contact", views.contact, name='contact'),
    path('login', views.loginuser,name='login'),
    path('logout', views.logoutuser,name='logout'),
    path('signin', views.signinuser,name='signin'),
    path('product/<int:product_id>/', views.detail, name='product_detail'),
    path('buynow', views.buy,name='buy'),
     
    
]