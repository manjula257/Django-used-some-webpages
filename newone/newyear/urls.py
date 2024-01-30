from django.urls import path
from . import views
urlpatterns=[
    # path("<str:name>",views.greet,name="greet"),
    path('newyear/<int:year>/', views.newyear_view, name='newyear'),
]