from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):   # P14
    class Meta:
        model = Student
        fields = ["id", "name", "email", "course", "marks", "created_at"]
        read_only_fields = ["id", "created_at"]

    def validate_marks(self, value):
        if value > 100:
            raise serializers.ValidationError("Marks cannot exceed 100.")
        return value
