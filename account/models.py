from django.db import models

# Create your models here.

class Teacher(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class CreditScheme(models.Model):
  courseCode = models.CharField(max_length=255)
  courseName = models.CharField(max_length=255)
  teachingSchemeTH = models.IntegerField()
  teachingSchemeP = models.IntegerField()
  teachingSchemeTUT = models.IntegerField()
  TotalHours = models.IntegerField()
  creditAssignedTH = models.IntegerField()
  creditAssignedP = models.IntegerField()
  creditAssignedTUT = models.IntegerField()
  totalCredits = models.IntegerField()
  courseCategories = models.CharField(max_length=255)
  branch=models.CharField(max_length=255)
  sem=models.CharField(max_length=255)
  programme=models.CharField(max_length=255)

  def __str__(self):
     return self.branch+'_'+self.programme+'_'+self.sem+'_'+self.courseName
  
class ExamSchm(models.Model):
  courseCodeEx = models.CharField(max_length=255)
  courseNameEx = models.CharField(max_length=255)
  caISE = models.IntegerField()
  caIA = models.IntegerField()
  caTotal = models.IntegerField()
  ese = models.IntegerField()
  tw = models.IntegerField()
  oral = models.IntegerField()
  oralAndPrac = models.IntegerField()
  totalEx = models.IntegerField()
  branch=models.CharField(max_length=255)
  sem=models.CharField(max_length=255)
  programme=models.CharField(max_length=255)
  courseCategoriesEx = models.CharField(max_length=255)
  caLabTut=models.IntegerField()


  def __str__(self):
         return self.branch+'_'+self.programme+'_'+self.sem+'_'+self.courseNameEx
  
class Assignfaculty(models.Model):
       courseCodeEx = models.CharField(max_length=255)
       courseNameEx = models.CharField(max_length=255)
       faculty1=models.CharField(max_length=255)
       faculty2=models.CharField(max_length=255)
       faculty3=models.CharField(max_length=255)
       reviewer=models.CharField(max_length=255)
       branch=models.CharField(max_length=255)
       sem=models.CharField(max_length=255)
       programme=models.CharField(max_length=255)
       
      
 