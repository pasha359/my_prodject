from animals.models import Announcement, Comment
from animals.serializers import *
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from animals.permissions import IsOwner
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class AnnouncementViewSet(viewsets.ModelViewSet):
    serializer_class = AnnouncementSerialaizer
    queryset = Announcement.objects.all()
    # permission_classes = (IsOwner,)

    def get_serializer_class(self):
        if self.action == "create":
            return AnnouncementCreateSerialaizer
        return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return_serializer = self.serializer_class(instance)
        headers = self.get_success_headers(return_serializer.data)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
#       pip install drf-writable-nested

class AnnouncementDetailView(generics.UpdateAPIView):
    serializer_class = AnnouncementSerialaizer
    queryset = Announcement.objects.all()
    permission_classes = (IsOwner,) #дает разрешение на редактирование в api только тому пользователю, который и создавал запись







