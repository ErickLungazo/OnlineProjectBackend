from rest_framework import serializers
from .models import Media


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'file', 'uploaded_at', 'url', 'file_type', 'file_size', 'original_filename']
        read_only_fields = ['uploaded_at', 'url', 'file_type', 'file_size', 'original_filename']

    def validate_file(self, value):
        if value.size > 5 * 1024 * 1024:  # 5 MB
            raise serializers.ValidationError("File size must be under 5 MB.")
        return value
