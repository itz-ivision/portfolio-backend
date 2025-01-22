from django.db import connection
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthCheckAPIView(APIView):
    """
        View to check the overall health of the API.
    """

    def get(self, request, *args, **kwargs):
        health_status = {
            'Database': self.check_database(),
            'Cache': self.check_cache(),
            'Status': 'OK'
        }

        if any(value == 'FAIL' for value in health_status.values()):
            health_status['Status'] = 'FAIL'
            return Response(health_status, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response(health_status, status=status.HTTP_200_OK)

    def check_database(self):

        try:
            # Check Database Connection
            connection.ensure_connection()
            return 'OK'
        except Exception:
            return 'FAIL'

    def check_cache(self):

        try:
            cache.set('health_check', 'OK', timeout=1)
            if cache.get('health_check') == 'OK':
                return 'OK'
            return 'FAIL'
        except Exception:
            return 'FAIL'