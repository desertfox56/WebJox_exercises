from .views import RegistrUserView, ClientViewSet, ManagerViewSet,CustomTokenObtainPairView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'managers', ManagerViewSet)

urlpatterns = [
    path('register/', RegistrUserView.as_view(), name='register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
