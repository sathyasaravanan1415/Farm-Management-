from rest_framework.routers import DefaultRouter
from .views import FarmerProfileViewSet, RegisterViewSet

router = DefaultRouter()

router.register(r'profiles', FarmerProfileViewSet)
router.register(r'register', RegisterViewSet, basename='register')

urlpatterns = router.urls

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = router.urls + [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]