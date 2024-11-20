import os
import uuid
from django.db import models
from django.core.exceptions import ValidationError


def upload_to_unique(instance, filename):
    # Generate a unique identifier
    unique_id = uuid.uuid4().hex
    # Get the file extension (e.g., '.png')
    ext = filename.split('.')[-1]
    # Build the unique filename with the UUID and original extension
    unique_filename = f"{unique_id}.{ext}"
    # Specify the upload path
    return os.path.join('uploads', unique_filename)


class Media(models.Model):
    file = models.FileField(upload_to=upload_to_unique)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # New attributes
    file_type = models.CharField(max_length=50, blank=True, null=True)  # e.g., 'image/png'
    file_size = models.PositiveIntegerField(blank=True, null=True)  # Size in bytes
    original_filename = models.CharField(max_length=255, blank=True, null=True)  # Original file name

    def __str__(self):
        return self.file.name

    @property
    def url(self):
        if self.file:
            return self.file.url
        return None

    def clean(self):
        super().clean()
        # Check file size
        if self.file.size > 5 * 1024 * 1024:  # 5 MB
            raise ValidationError("File size must be under 5 MB.")

    def save(self, *args, **kwargs):
        # Get the file type and size when the file is saved
        if self.file:
            self.file_type = self.file.file.content_type  # e.g., 'image/png'
            self.file_size = self.file.size  # Size in bytes
            self.original_filename = os.path.basename(self.file.name)  # Extract original file name

        super().save(*args, **kwargs)
