from django.contrib import admin

from .models import Student,Employee,Customer

class AdminStudent(admin.ModelAdmin):
    list_display=['name','location','marks','institute']

class AdminEmployee(admin.ModelAdmin):
    list_display=['name','location','salary','company']

class AdminCustomer(admin.ModelAdmin):
    list_display=['name','location','sales','product']

admin.site.register(Student,AdminStudent)
admin.site.register(Employee,AdminEmployee)
admin.site.register(Customer,AdminCustomer)

