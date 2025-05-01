from random import randint

from rest_framework import generics, status
from rest_framework.response import Response

from announcement.models import Item
from announcement.serializers import SubItemSeriaizer
from category.models import SubCategory
from .utils import result_parse


class CreateItemAPIView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = SubItemSeriaizer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            category = serializer.validated_data.get("sub_category")
            for item in result_parse(category):
                sub_obj, _ = SubCategory.objects.get_or_create(title=category)
                count = randint(1, 50)
                self.get_queryset().get_or_create(sub_category=sub_obj, **item, count=count)
        return Response({"result": "success"}, status=status.HTTP_201_CREATED)