from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RecognizedImageViewSet, FeedbackView

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'recognized-images', RecognizedImageViewSet, basename='recognized-image')

# Define the urlpatterns
urlpatterns = router.urls + [
    path('feedback/', FeedbackView.as_view(), name='feedback'),  # Add the FeedbackView as a separate endpoint
]
