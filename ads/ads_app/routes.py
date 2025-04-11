from rest_framework import routers

from ads_app.apiviews import AdViewSet

router = routers.DefaultRouter()
router.register('ads', AdViewSet, basename='ad')