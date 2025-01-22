from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAdminUser


class AdminAwareRouter(DefaultRouter):
    def register(self, prefix, viewset, basename=None):
        if IsAdminUser in viewset.permission_classes:
            prefix = f'admin/{prefix}'
        super().register(prefix, viewset, basename)
