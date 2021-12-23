from django.urls import path
from . import views

app_name = 'back'
urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.Login,name='login'),
    path('logout',views.Logout,name='logot'),
    path('stu/stuinfo',views.StuInfo,name='stuinfo'),
    path('stu/xuanke',views.qianxuesen_Getxuanke,name='xuanke'),
    path('stu/pingjiao',views.Pingjiao,name='pingjiao'),
    path('resetpwd',views.resetPw,name='resetpwd'),
    path('tea/list',views.list,name='list'),
    path('tea/details',views.details,name='details'),
    path('tea/charts', views.Charts, name='charts'),
]