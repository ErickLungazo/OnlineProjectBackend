from django.db import models
from courses.models import Course  # Assuming the course model is in the same app
from accounts.models import CustomUser

class Unit(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="units")
    lecturer = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='lecturer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
