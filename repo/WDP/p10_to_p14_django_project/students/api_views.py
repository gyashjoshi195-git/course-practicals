from rest_framework import viewsets, permissions
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):    # P14: full CRUD API
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]  # use IsAuthenticated in production
