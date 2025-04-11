from rest_framework import serializers

from ads_app.models import Ad


class AdSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.CharField(source='user.id', read_only=True)
    class Meta:
        model = Ad
        fields = ['title', 'description', 'user_id', 'category', 'condition', 'image', 'created_at']
