from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/',views.logoutvie,name='logout'),
    path('register/',views.register,name='register'),
    path('delete-task/<str:name>/',views.delete,name='delete'),
    path('update/<str:name>/',views.update,name='update')

]