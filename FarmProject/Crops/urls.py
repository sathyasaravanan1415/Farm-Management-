from rest_framework.routers import DefaultRouter
from .views import cropviewset

router=DefaultRouter()
router.register(f'crop',cropviewset)
urlpatterns=router.urls