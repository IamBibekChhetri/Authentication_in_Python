from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('profile/',views.profile,name="profile"),
    path('changePassword/',views.changePassword,name="changePassword"),
    path('emailVerification/',views.emailVerification,name="emailVerification"),
    path('otpVerification',views.otpVerification,name="otpVerification"),
    # path('resetPassword/',views.resetPassword,name="resetPassword"),
]
