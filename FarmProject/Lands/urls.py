from rest_framework.routers import DefaultRouter
from .views import landViewSet

router = DefaultRouter()
router.register(r'lands',landViewSet)
urlpatterns=router.urls