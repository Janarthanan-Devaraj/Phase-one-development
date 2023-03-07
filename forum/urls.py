from django.urls import path

from . import views

app_name = 'forum'

urlpatterns = [
    path('threads/', views.thread_list, name="thread_list"),
    path('thread/<str:pk>/', views.thread, name="thread"),
    path('create-thread/', views.createThread, name="create-thread"),
]
