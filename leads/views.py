from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import LeadCreateSerializer
from .models import Lead


class LeadCreateAPIView(generics.CreateAPIView):
    """Создание лида (обратная связь/заявка)"""
    queryset = Lead.objects.all()
    serializer_class = LeadCreateSerializer
    permission_classes = [AllowAny]

