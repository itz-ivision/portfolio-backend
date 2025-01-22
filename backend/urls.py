from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="ThirdEyeVision",
        default_version="v1",
        description="API documentation for ThirdEyeVision for internal use only.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="thirdeyevision.ai.contact@gmail.com"),
        license=openapi.License(name='BSD License')
    ),
    public=False,
    permission_classes=[permissions.AllowAny,]
)


urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path("api/admin/", admin.site.urls),
    path("api/", include('api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc')
]
