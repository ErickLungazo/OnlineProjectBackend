from django.db import models

from schools.models import School  # Assuming School is in the schools app
from units.models import Unit


class Assessment(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="assessments")

    def __str__(self):
        return self.name


class Paper(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="papers")
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="papers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Paper for {self.assessment.name} - {self.unit.name}"
