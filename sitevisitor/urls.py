from django.urls import path
from .views import home,register_user,user_login, user_home

app_name = 'sitevisitor'
urlpatterns=[
    path('',home, name= 'home'),
    path('sign_up/', register_user, name = 'sign_up'),
    path('sign_in/',user_login, name='sign_in'),
    path('user_home/',user_home, name='user_home'),



]