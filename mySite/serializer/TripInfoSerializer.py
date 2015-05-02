
from mySite.models import TripInfo

__author__ = 'wenjuntan'
from rest_framework import serializers
class TripInfoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    country = serializers.CharField(max_length= 200, default='China')
    province = serializers.CharField(max_length= 200)
    city = serializers.CharField(max_length=200)
    comments = serializers.CharField(allow_blank=True)

    def create(self, validated_data):
        return TripInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.country = validated_data.get('country', instance.country)
        instance.province = validated_data.get('province', instance.province)
        instance.city = validated_data.get('city', instance.city)
        instance.comments = validated_data.get('comments', instance.comments)
        instance.save()
        return instance
