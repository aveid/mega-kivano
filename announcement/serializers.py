from rest_framework import serializers


class SubItemSeriaizer(serializers.Serializer):
    sub_category = serializers.CharField()