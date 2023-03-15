from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name="index"),
    path('create-notes/', views.createNotes, name = "create-notes"),
    path('<int:department_id>/<int:semester_id>/', views.notes_by_semester, name="notes_by_semester"),
    path('<int:pdf_id>/download/', views.download_pdf, name='download_pdf'),
]
