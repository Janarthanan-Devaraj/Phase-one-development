from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('signup/step0/', views.signupStepZero, name="signup-step0"),
    path('signup/BackTostep0/', views.goBackStepZero, name="go-back-step-zero"),
    path('signup/step1/', views.signupStepOne, name="signup-step1"),
    path('signup/BackTostep1/', views.goBackStepOne, name="go-back-step-one"),
    path('signup/step2/', views.signupStepTwo, name="signup-step2"),
    path('signup/BackTostep2/', views.goBackStepTwo, name="go-back-step-two"),
    path('signup/step3/', views.signupStepThree, name="signup-step3"),
    path('profile/<str:pk>/',views.profileView, name="profile"),
    path('edit-profile/',views.editProfile, name="edit-profile"),
]
