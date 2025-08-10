from django.db import models
class SchoolSetting(models.Model):
    school_name = models.CharField(max_length=255, default='Placeholder School')
    currency = models.CharField(max_length=10, default='KES')
    terms_per_year = models.IntegerField(default=3)

class Student(models.Model):
    adm_no = models.CharField(max_length=50, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50, blank=True)

class Teacher(models.Model):
    staff_no = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=255)
