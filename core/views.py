from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
def home(request):
    return HttpResponse('<h2>School SMS - Demo</h2><p><a href="/students/">Students</a> | <a href="/admin/">Admin</a></p>')
def student_list(request):
    students = Student.objects.all()
    out = '<h2>Students (demo)</h2><ul>'
    for s in students:
        out += f'<li>{s.adm_no} - {s.firstname} {s.lastname} ({s.student_class})</li>'
    out += '</ul>'
    return HttpResponse(out)
