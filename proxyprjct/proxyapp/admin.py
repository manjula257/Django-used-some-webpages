from django.contrib import admin
from .models import Student,StudentProxy

class AdminStudent(admin.ModelAdmin):
    list_display=['name','location','marks']

class AdminStudentProxy(admin.ModelAdmin):
    list_display=['name','location','marks']

admin.site.register(Student,AdminStudent)
admin.site.register(StudentProxy,AdminStudentProxy)


