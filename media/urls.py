from django.urls import path
from .views import MediaListCreateAPIView,MediaDetailUpdateDeleteAPIView

urlpatterns = [
    path('', MediaListCreateAPIView.as_view(), name='media-list'),
    path('<int:pk>/', MediaDetailUpdateDeleteAPIView.as_view(), name='media-detail'),

]
