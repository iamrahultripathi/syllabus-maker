from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET

def loginl(request):
    if request.method == "POST":
        request.session['count'] = 0
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='HOD').exists():
                return redirect("home/")
            elif user.groups.filter(name='Teachers').exists():
                return redirect("teacher", username=username)
            

        else:
            messages.error(request, "Incorrect username or password.")
            if request.session['count']==0:
                return redirect('/')

    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='/')
def teacher(request, username):
    data = Assignfaculty.objects.filter(faculty1=username) | Assignfaculty.objects.filter(faculty2=username) | Assignfaculty.objects.filter(faculty3=username).values()
    
    context={'data':data,
             }
    
    return render(request, 'teacher.html', context)

    




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
        

    data = CreditScheme.objects.filter(branch=request.GET.get('branch'), programme=request.GET.get('programme'), sem=request.GET.get('sem')).values()
    totalteachingSchemeTH=sum(data.values_list('teachingSchemeTH', flat=True))
    totalteachingSchemeP=sum(data.values_list('teachingSchemeP', flat=True))
    totalteachingSchemeTUT=sum(data.values_list('teachingSchemeTUT', flat=True))
    totalTotalHours=sum(data.values_list('TotalHours', flat=True))
    totalcreditAssignedTH=sum(data.values_list('creditAssignedTH', flat=True))
    totalcreditAssignedP=sum(data.values_list('creditAssignedP', flat=True))
    totalcreditAssignedTUT=sum(data.values_list('creditAssignedTUT', flat=True))
    totaltotalCredits=sum(data.values_list('totalCredits', flat=True))
    
    # totalteachingSchemeTH=CreditScheme.objects.aggregate(Sum('teachingSchemeTH'))
    student = {'val':"Credit",'myvalue':1, 'data':data, 'totalteachingSchemeTH':totalteachingSchemeTH, 'totalteachingSchemeP':totalteachingSchemeP,'totalteachingSchemeTUT':totalteachingSchemeTUT,'totalTotalHours':totalTotalHours, 'totalcreditAssignedTH':totalcreditAssignedTH,'totalcreditAssignedP':totalcreditAssignedP,'totalcreditAssignedTUT':totalcreditAssignedTUT, 'totalcreditAssignedTUT':totalcreditAssignedTUT,'totaltotalCredits':totaltotalCredits}
    return render(request,"creditScheme.html",student)

def examinationScheme(request):
    branch=request.session['branch']
    sem=request.session['sem']
    programme=request.session['programme']
    
    
    if request.method == 'POST':
        courseCodeEx=request.POST.get('courseCodeEx')
        courseNameEx=request.POST.get('courseNameEx')
        courseCategoriesEx=request.POST.get('courseCategoriesEx')
        caISE = request.POST.get('caISE')
        caIA = request.POST.get('caIA')
        caTotal = int(request.POST.get('caISE')) + int(request.POST.get('caIA'))
        ese = request.POST.get('ese')
        tw = request.POST.get('tw')
        oral = request.POST.get('oral')
        oralAndPrac = request.POST.get('oralAndPrac')
        caLabTut=request.POST.get('caLabTut')
        totalEx = int(request.POST.get('caISE')) + int(request.POST.get('caIA')) +int(request.POST.get('caLabTut')) + int(request.POST.get('ese')) + int(request.POST.get('tw')) + int(request.POST.get('oral')) + int(request.POST.get('oralAndPrac'))
        contact_data = ExamSchm(courseCodeEx=courseCodeEx,courseNameEx=courseNameEx,courseCategoriesEx=courseCategoriesEx,caLabTut=caLabTut, caISE=caISE,caIA=caIA,caTotal=caTotal, ese=ese, tw=tw,oral=oral,oralAndPrac=oralAndPrac, totalEx=totalEx,branch=branch, sem=sem,programme=programme)
        contact_data.save()
    data = ExamSchm.objects.filter(branch=branch, programme=programme, sem=sem).values()
    data1 = CreditScheme.objects.filter(branch=branch, programme=programme, sem=sem).values('courseCode', 'courseName','courseCategories')
    data2 = ExamSchm.objects.filter(branch=branch, programme=programme, sem=sem).values('courseCodeEx', 'courseNameEx')
    totalISE=sum(data.values_list('caISE', flat=True))
    totalIA=sum(data.values_list('caIA', flat=True))
    totalcaTotal=sum(data.values_list('caTotal', flat=True))
    totalese=sum(data.values_list('ese', flat=True))
    totaltw=sum(data.values_list('tw', flat=True))
    totaloral=sum(data.values_list('oral', flat=True))
    totaloralAndPrac=sum(data.values_list('oralAndPrac', flat=True))
    totalcaLabTut=sum(data.values_list('caLabTut', flat=True))
    totalAll=sum(data.values_list('totalEx', flat=True))
    # for filter_dict in data1:
    #     data2 = data2.exclude(**filter_dict)
    # query_set = list(data2.values())
    # print(query_set)
    result = []
    for d1 in data1:
        match = False
        for d2 in data2:
            if d1['courseCode'] == d2['courseCodeEx'] and d1['courseName'] == d2['courseNameEx']:
               match = True
               break
        if not match:
            result.append(d1)
    
    student={'result':result,'data':data,'myvalue':2,'totalISE':totalISE,'totalcaLabTut':totalcaLabTut, 'totalIA':totalIA,'totalcaTotal':totalcaTotal,'totalese':totalese,'totaltw':totaltw, 'totaloral':totaloral, 'totaloralAndPrac':totaloralAndPrac,'totalAll':totalAll,
             'branch':branch,'sem':sem, 'programme':programme,
             'val':"Examination"}
    return render(request, 'examinationScheme.html',student)


def facultyAssign(request):
    branch=request.session['branch']
    sem=request.session['sem']
    programme=request.session['programme']
    if request.method == 'POST':
        courseCodeEx=request.POST.get('courseCodeEx')
        courseNameEx=request.POST.get('courseNameEx')
        faculty1 = request.POST.get('faculty1')
        faculty2 = request.POST.get('faculty2')
        faculty3 = request.POST.get('faculty3')
        reviewer = request.POST.get('reviewer')
        contact_data =  Assignfaculty( courseCodeEx=courseCodeEx, courseNameEx=courseNameEx,faculty1=faculty1,faculty2=faculty2,faculty3=faculty3,reviewer=reviewer,branch=branch, sem=sem,programme=programme)
        contact_data.save()
    data1 = CreditScheme.objects.filter(branch=branch, programme=programme, sem=sem).values('courseCode', 'courseName')
    data = Assignfaculty.objects.filter(branch=branch, programme=programme, sem=sem).values()
    result = []
    for d1 in data1:
        result.append(d1)
    student={'data':data,
             'branch':branch,'sem':sem, 'programme':programme,
             'val':"Assign", 'result':result}
    return render(request, 'assignfaculty.html',student)
def courseDetail(request, username, course_code, course_name):
    course_code=course_code
    course_name=course_name
    data = CreditScheme.objects.filter(courseCode=course_code, courseName=course_name).values()
    data1= ExamSchm.objects.filter(courseCodeEx=course_code, courseNameEx=course_name).values()
    sumData={
        'data':data,
        'data1':data1
    }
    
    print('data:', data)
    print('data1:', data1)

    return render(request, 'courseDetail.html',sumData)

@csrf_exempt
def savestudentCredit(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    student=CreditScheme.objects.get(id=id)
    if type=="courseCode":
       student.courseCode=value

    if type == "courseName":
        student.courseName = value

    if type == "teachingSchemeTH":
        student.teachingSchemeTH = value

    if type == "teachingSchemeP":
        student.teachingSchemeP = value

    if type == "teachingSchemeTUT":
        student.teachingSchemeTUT = value

    if type == "creditAssignedTH":
        student.creditAssignedTH = value

    if type == "creditAssignedP":
        student.creditAssignedP = value

    if type == "creditAssignedTUT":
        student.creditAssignedTUT = value

    if type == "courseCategories":
        student.courseCategories = value
    student.TotalHours = int(student.teachingSchemeTH) + int(student.teachingSchemeP) + int(student.teachingSchemeTUT)
    student.totalCredits = int(student.creditAssignedTH) + int(student.creditAssignedP) + int(student.creditAssignedTUT)
    
    
    student.save()
    return JsonResponse({"success":"Updated"})

@csrf_exempt
def savestudentExamination(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    student=ExamSchm.objects.get(id=id)
    if type=="courseCodeEx":
       student.courseCodeEx=value

    if type == "courseNameEx":
        student.courseNameEx = value

    if type == "caISE":
        student.caISE = value

    if type == "caIA":
        student.caIA = value

    if type == "ese":
        student.ese = value

    if type == "tw":
        student.tw = value

    if type == "oral":
        student.oral = value

    if type == "oralAndPrac":
        student.oralAndPrac = value

    if type == "caLabTut":
        student.caLabTut = value

    if type == "courseCategoriesEx":
        student.courseCategoriesEx = value
    student.caTotal = int(student.caISE) + int(student.caIA)
    student.totalEx = int(student.caISE) + int(student.caIA) + int(student.ese) + int(student.tw) + int(student.oral) + int(student.oralAndPrac) + int(student.caLabTut)
    
    
    student.save()
    return JsonResponse({"success":"Updated"})


@csrf_exempt

def delete_row(request):
    print("hello")
    if request.method == 'GET':
        id = request.GET.get('id')
        CreditScheme.objects.filter(id=id).delete()
        return HttpResponse('Row deleted successfully.')
    
@require_GET
def get_course_name(request):
    course_code = request.GET.get('courseCode')
    course = get_object_or_404(CreditScheme, courseCode=course_code)
    data = {'courseName': course.courseName}
    print(data)
    return JsonResponse(data)