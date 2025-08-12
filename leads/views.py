from rest_framework import generics
from .serializers import LeadCreateSerializer
from .models import Lead


class LeadCreateAPIView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadCreateSerializer
