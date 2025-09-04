from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class JsonErrorMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if settings.DEBUG:  
            if response.status_code == 404:
                return JsonResponse({"error": "Endpoint not found"}, status=404)
            if response.status_code == 500:
                return JsonResponse({"error": "Internal server error"}, status=500)
        return response
