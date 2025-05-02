from rest_framework import serializers

from announcement.models import Item


class SubItemSeriaizer(serializers.Serializer):
    sub_category = serializers.CharField()



class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ("id", "description", "price", "article", "count")