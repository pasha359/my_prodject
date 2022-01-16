from animals.models import Note, Comments
from animals.serializers import NoteDetailSerializer,CommentsDetailSerializer, NoteLitSerializer, CommentsListSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from animals.permissions import IsOwner

class NoteCreate(generics.CreateAPIView):
    serializer_class = NoteDetailSerializer

class CommentsCreate(generics.CreateAPIView):
    serializer_class = CommentsDetailSerializer

class ListCommentsView(generics.ListAPIView):
    serializer_class = CommentsListSerializer
    queryset = Comments.objects.all()

class ListNoteView(generics.ListAPIView):
    serializer_class = NoteLitSerializer
    queryset = Note.objects.all()


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteDetailSerializer
    queryset = Note.objects.all()
    permission_classes = (IsOwner,) #дает разрешение на редактирование в api только тому пользователю, который и создавал запись