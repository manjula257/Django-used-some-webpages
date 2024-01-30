from django.contrib import admin
from .models import Student,Employee,Customer

class AdminStudent(admin.ModelAdmin):
    list_display=['name','location']

class AdminEmployee(admin.ModelAdmin):
    list_display=['name','location','salary','department']

class AdminCustomer(admin.ModelAdmin):
    list_display=['name','location','salary','department','product','payment']

admin.site.register(Student,AdminStudent)
admin.site.register(Employee,AdminEmployee)
admin.site.register(Customer,AdminCustomer)


