from django.urls import path

from . import views

app_name = 'feeds'

urlpatterns = [
    path('', views.feed_list, name="index"),
]
