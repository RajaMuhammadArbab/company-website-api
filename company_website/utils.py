from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        return response

    
    return Response(
        {"error": "Resource not found or invalid request."},
        status=status.HTTP_404_NOT_FOUND
    )
