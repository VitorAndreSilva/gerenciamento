from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    # API
    path('api/<str:version>/', include('loja.urls')),
    # Autenticação
    path('api/<str:version>/auth/login/', TokenObtainPairView.as_view()),
    path('api/<str:version>/auth/refresh/', TokenRefreshView.as_view())
]
