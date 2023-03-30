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
        request.session['courseCodeEx']=courseCode
        request.session['courseNameEx']=courseName
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
    courseCode = request.session['courseCodeEx']
    courseName = request.session['courseNameEx']
    if request.method == 'POST':
        caISE = request.POST.get('caISE')
        caIA = request.POST.get('caIA')
        caTotal = int(request.POST.get('caISE')) + int(request.POST.get('caIA'))
        ese = request.POST.get('ese')
        tw = request.POST.get('tw')
        oral = request.POST.get('oral')
        oralAndPrac = request.POST.get('oralAndPrac')
        totalEx = int(request.POST.get('caISE')) + int(request.POST.get('caIA')) + int(request.POST.get('ese')) + int(request.POST.get('tw')) + int(request.POST.get('oral')) + int(request.POST.get('oralAndPrac'))
        contact_data = ExamSchm(courseCodeEx=courseCode, courseNameEx=courseName, caISE=caISE,caIA=caIA,caTotal=caTotal, ese=ese, tw=tw,oral=oral,oralAndPrac=oralAndPrac, totalEx=totalEx,branch=branch, sem=sem,programme=programme)
        contact_data.save()
    data = ExamSchm.objects.filter(branch=branch, programme=programme, sem=sem).values()
    totalISE=sum(data.values_list('caISE', flat=True))
    totalIA=sum(data.values_list('caIA', flat=True))
    totalcaTotal=sum(data.values_list('caTotal', flat=True))
    totalese=sum(data.values_list('ese', flat=True))
    totaltw=sum(data.values_list('tw', flat=True))
    totaloral=sum(data.values_list('oral', flat=True))
    totaloralAndPrac=sum(data.values_list('oralAndPrac', flat=True))
    totalAll=sum(data.values_list('totalEx', flat=True))
        
    student={'data':data,'totalISE':totalISE,'totalIA':totalIA,'totalcaTotal':totalcaTotal,'totalese':totalese,'totaltw':totaltw, 'totaloral':totaloral, 'totaloralAndPrac':totaloralAndPrac,'totalAll':totalAll,
             'branch':branch,'sem':sem, 'programme':programme,
             'val':"Examination",'courseCode':courseCode,'courseName':courseName}
    return render(request, 'examinationScheme.html',student)


