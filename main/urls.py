from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reservation/', views.reservation, name='reservation'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('adminPage/', views.adminPage, name='admin-page'),
    path('updateStatus/<str:id>/', views.updateStatus, name='update-status'),
    path('deleteEvent/<str:id>', views.deleteEvent, name='delete-event')
]
