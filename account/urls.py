from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.loginl),
    path('home/', views.home),
    path('login/', views.loginl, name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('login/home/', views.home, name='login-home'),
    path('login/home/creditScheme/', views.creditScheme, name='creditScheme')
]
