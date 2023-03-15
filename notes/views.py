from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import FileResponse
from django.db.models import Count
from django.db.models import Q
from django.urls import reverse
from user.models import AcademicsInfo
from .models import Notes, Department, Semester
from .forms import NotesForm


def index(request):
    departments = Department.objects.all()
    data = {}
    for department in departments:
        semesters = Semester.objects.filter(
            notes__department=department
        ).distinct()
        data[department] = {}
        for semester in semesters:
            notes = Notes.objects.filter(
                Q(semester=semester) & Q(department=department)
            ).order_by("-created")
            data[department][semester] = notes
    context = {"data": data}
    return render(request,'notes/notes_list.html', context)

def notes_by_semester(request, department_id, semester_id):
    notes = Notes.objects.filter(
        Q(semester_id=semester_id) & Q(department_id=department_id)
    ).order_by("-created")
    department = Department.objects.get(pk=department_id)
    semester = Semester.objects.get(pk=semester_id)
    context = {
        "notes": notes,
        "department": department,
        "semester": semester,
    }
    return render(request, "notes/notes_by_semester.html", context)

def createNotes(request):
    form = NotesForm()
    semesters = Semester.objects.all()
    if request.method == "POST":
        form = NotesForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            academics = AcademicsInfo.objects.get(user=request.user)
            department_short_name = academics.department
            department_full_name = dict(AcademicsInfo.DEPARTMENT_CHOICES).get(department_short_name)
            department, _ = Department.objects.get_or_create(name = department_full_name)
            
            semester_name = request.POST.get('semester_num')
            semester, created = Semester.objects.get_or_create(name=semester_name)

            Notes.objects.create(
                author=request.user,
                department=department, # extract the first object from the tuple
                semester=semester,
                subject=request.POST.get('subject'),
                unit=request.POST.get('unit'),
                pdf=request.FILES.get('pdf'),
                created=request.POST.get('created'),
            )
            return redirect('notes:index')
        else:
            for field, errors in form.errors.items():
                print(f"{field}: {', '.join(errors)}")

    context = {'form': form, 'semesters' : semesters}
    return render(request, 'notes/notes_form.html', context)

def download_pdf(request, pdf_id):
    note = get_object_or_404(Notes, id=pdf_id)
    response = FileResponse(note.pdf)
    return response