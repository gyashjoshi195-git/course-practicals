from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student


@login_required
def student_list(request):             # READ
    return render(request, "students/student_list.html", {"students": Student.objects.all()})


@login_required
def student_create(request):           # CREATE
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Student added.")
        return redirect("student_list")
    return render(request, "students/student_form.html", {"form": form, "title": "Add Student"})


@login_required
def student_update(request, pk):       # UPDATE
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, "Student updated.")
        return redirect("student_list")
    return render(request, "students/student_form.html", {"form": form, "title": "Edit Student"})


@login_required
def student_delete(request, pk):       # DELETE
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.warning(request, "Student deleted.")
        return redirect("student_list")
    return render(request, "students/student_confirm_delete.html", {"student": student})
