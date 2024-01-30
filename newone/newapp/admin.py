from django.contrib import admin
from .models import Students,Courses

class AdminStudents(admin.ModelAdmin):
    list_display=['sname','loc','marks']

class AdminCourses(admin.ModelAdmin):
    list_display=['cname','iname','fee']

admin.site.register(Students,AdminStudents)
admin.site.register(Courses,AdminCourses)
