from django.db import models


class Student(models.Model):          # P10: Django model
    COURSES = [("CSE", "Computer Engg"), ("IT", "Information Tech"), ("ME", "Mechanical")]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=10, choices=COURSES, default="CSE")
    marks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.course})"
