from django.db import models
from schools.models import School  # Assuming schools is the app managing School

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="courses")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
