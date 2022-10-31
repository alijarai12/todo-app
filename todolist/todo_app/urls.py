from django.urls import path
from .import views
urlpatterns = [
    #path('', views.index, name='index'),

    path('', views.first, name='first'),
    path('registerfirst/', views.registerfirst, name='registerfirst'),


    #path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    #path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('addlist/', views.addlist, name='addlist'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),


    path('home/', views.home, name='home'),
    #path('show/<int:id>/', views.show, name='show'),

]