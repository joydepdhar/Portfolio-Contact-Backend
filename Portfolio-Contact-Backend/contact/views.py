from rest_framework import generics
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from django.core.mail import send_mail
from django.conf import settings

class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    def perform_create(self, serializer):
            instance = serializer.save()
            send_mail(
                subject=f"New Contact: {instance.subject}",
                message=f"From: {instance.name} <{instance.email}>\n\n{instance.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )