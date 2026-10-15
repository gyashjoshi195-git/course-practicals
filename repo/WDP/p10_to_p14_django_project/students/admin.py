from django.contrib import admin
from .models import Student


@admin.register(Student)             # P11: Django admin customisation
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "course", "marks", "created_at")
    list_filter = ("course",)
    search_fields = ("name", "email")
    ordering = ("-created_at",)
    list_per_page = 10
