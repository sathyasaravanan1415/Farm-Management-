from rest_framework.routers import DefaultRouter
from .views import FarmerProfileViewSet, RegisterViewSet

router = DefaultRouter()

router.register(r'profiles', FarmerProfileViewSet)
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = router.urls