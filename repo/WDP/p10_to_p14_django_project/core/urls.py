from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from students.api_views import StudentViewSet

router = DefaultRouter()
router.register("students", StudentViewSet, basename="api-student")   # P14

urlpatterns = [
    path("admin/", admin.site.urls),                       # P11
    path("accounts/", include("accounts.urls")),           # P12
    path("api/", include(router.urls)),                    # P14  -> /api/students/
    path("", include("students.urls")),                    # P10, P13
]
