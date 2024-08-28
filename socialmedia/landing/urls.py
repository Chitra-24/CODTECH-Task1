from django.urls import path,include
from landing.views import *
from landing import views

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('login/',views.login_page,name='login'),
    path('register/',views.reg_page,name='register'),
    path('logout/',views.log_out_page,name='logout'),
]