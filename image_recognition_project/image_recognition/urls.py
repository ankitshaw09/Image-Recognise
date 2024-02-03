from rest_framework.routers import DefaultRouter
from .views import RecognizedImageViewSet

router = DefaultRouter()
router.register(r'recognized-images', RecognizedImageViewSet, basename='recognized-image')
urlpatterns = router.urls
