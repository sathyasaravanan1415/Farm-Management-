from rest_framework.routers import DefaultRouter
from .views import FarmerViewSet

router = DefaultRouter()
router.register(r'farmers',FarmerViewSet)
urlpatterns=router.urls