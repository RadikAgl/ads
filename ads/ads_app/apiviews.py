"""Вьюшки для апи"""

from rest_framework import viewsets

from ads_app.models import Ad
from ads_app.serializers import AdSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
