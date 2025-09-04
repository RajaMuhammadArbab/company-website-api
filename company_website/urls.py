from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),

   
    path('api/', include('content.urls')),
    path('api/', include('contact.urls')),
    path('api/', include('team.urls')),

   
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


def custom_page_not_found_view(request, exception):
    return JsonResponse({"error": "Endpoint not found"}, status=404)

def custom_error_view(request):
    return JsonResponse({"error": "Internal server error"}, status=500)


handler404 = custom_page_not_found_view
handler500 = custom_error_view
