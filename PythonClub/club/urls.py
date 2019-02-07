from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('resources/', views.resources, name='resources'),
    path('meetings/', views.meetings, name='meetings'),
    path('agenda_detail/<int:id>', views.agenda_detail, name='agenda_detail'),
]