from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Media
from .serializers import MediaSerializer


# Create your views here.
class MediaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticated]


class MediaDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticated]
