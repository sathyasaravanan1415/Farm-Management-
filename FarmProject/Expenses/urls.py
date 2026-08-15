from rest_framework.routers import DefaultRouter
from .views import ExpensesViewSet

router = DefaultRouter()
router.register(r'expenses',ExpensesViewSet)
urlpatterns=router.urls