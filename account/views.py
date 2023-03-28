from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from django.urls import reverse
from .models import *

def loginl(request):
    if request.method == "POST":
        request.session['count'] = 0
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home/")
        else:
            messages.error(request, "Incorrect username or password.")
            if request.session['count']==0:
                return redirect('/')

            
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect("/login")

def creditScheme(request):
    if request.method == 'POST':
        courseCode = request.POST.get('courseCode')
        courseName = request.POST.get('courseName')
        teachingSchemeTH = request.POST.get('teachingSchemeth')
        teachingSchemeP = request.POST.get('teachingSchemep')
        teachingSchemeTUT = request.POST.get('teachingSchemetut')
        TotalHours = int(request.POST.get('teachingSchemeth')) + int(request.POST.get('teachingSchemep')) + int(request.POST.get('teachingSchemetut'))
        creditAssignedTH = request.POST.get('creditAssignedth')
        creditAssignedP = request.POST.get('creditAssignedp')
        creditAssignedTUT = request.POST.get('creditAssignedtut')
        totalCredits = int(request.POST.get('creditAssignedth')) + int(request.POST.get('creditAssignedp')) + int(request.POST.get('creditAssignedtut'))
        courseCategories = request.POST.get('courseCategories')
        branch=request.GET.get('branch', None)
        sem=request.GET.get('sem', None)
        programme=request.GET.get('programme', None)
        contact_data = CreditScheme(courseCode=courseCode, courseName=courseName, teachingSchemeTH=teachingSchemeTH,teachingSchemeP=teachingSchemeP,teachingSchemeTUT=teachingSchemeTUT, TotalHours=TotalHours, creditAssignedTH=creditAssignedTH,creditAssignedP=creditAssignedP,creditAssignedTUT=creditAssignedTUT, totalCredits=totalCredits, courseCategories=courseCategories,branch=branch, sem=sem,programme=programme)
        contact_data.save()
        request.session['branch']=request.GET.get('branch', None)
        request.session['sem']=request.GET.get('sem', None)
        request.session['programme']=request.GET.get('programme', None)
    # data = CreditScheme.objects.all()
    data = CreditScheme.objects.filter(branch= request.GET.get('branch'), programme= request.GET.get('programme'), sem= request.GET.get('sem')).values()
    totalteachingSchemeTH=sum(data.values_list('teachingSchemeTH', flat=True))
    totalteachingSchemeP=sum(data.values_list('teachingSchemeP', flat=True))
    totalteachingSchemeTUT=sum(data.values_list('teachingSchemeTUT', flat=True))
    totalTotalHours=sum(data.values_list('TotalHours', flat=True))
    totalcreditAssignedTH=sum(data.values_list('creditAssignedTH', flat=True))
    totalcreditAssignedP=sum(data.values_list('creditAssignedP', flat=True))
    totalcreditAssignedTUT=sum(data.values_list('creditAssignedTUT', flat=True))
    totaltotalCredits=sum(data.values_list('totalCredits', flat=True))
    
    # totalteachingSchemeTH=CreditScheme.objects.aggregate(Sum('teachingSchemeTH'))
    student = {'val':"Credit",'data':data, 'totalteachingSchemeTH':totalteachingSchemeTH, 'totalteachingSchemeP':totalteachingSchemeP,'totalteachingSchemeTUT':totalteachingSchemeTUT,'totalTotalHours':totalTotalHours, 'totalcreditAssignedTH':totalcreditAssignedTH,'totalcreditAssignedP':totalcreditAssignedP,'totalcreditAssignedTUT':totalcreditAssignedTUT, 'totalcreditAssignedTUT':totalcreditAssignedTUT,'totaltotalCredits':totaltotalCredits}
    return render(request,"creditScheme.html",student)

def examinationScheme(request):
    branch=request.session['branch']
    sem=request.session['sem']
    programme=request.session['programme']
    student={'branch':branch,'sem':sem, 'programme':programme,'val':"Examination"}
    return render(request, 'examinationScheme.html',student)


