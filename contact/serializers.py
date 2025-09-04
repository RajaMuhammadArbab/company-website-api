from rest_framework import serializers
from .models import ContactSubmission

class ContactSubmissionSerializer(serializers.ModelSerializer):
    
    message = serializers.CharField(min_length=10)
    
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']