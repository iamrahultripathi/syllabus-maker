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
    path('login/teacher/<str:username>/', views.teacher, name='teacher'),
    path('login/<str:username>/<str:course_code>/<str:course_name>/courseDetail', views.courseDetail, name='courseDetail'),
    
    path('login/home/creditScheme/', views.creditScheme, name='creditScheme'),
    path('savestudentCredit', views.savestudentCredit, name='savestudentCredit'),
    path('savestudentExamination', views.savestudentExamination, name='savestudentExamination'),
    path('login/home/creditScheme/examinationScheme/', views.examinationScheme, name='examinationScheme'),
    path('login/home/creditScheme/examinationScheme/facultyAssign',views.facultyAssign,name='facultyAssign')
]
