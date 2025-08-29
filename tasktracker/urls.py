from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "accounts/", include("django.contrib.auth.urls")
    ),  # Login, logout, password reset
    path("", include("tasks.urls")),  # Your app
    path("api/", include("tasks.api_urls")),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api/dashboard/", DashboardAPIView.as_view(), name="dashboard-api"),
]
