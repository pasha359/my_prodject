from rest_framework import serializers
from animals.models import Note, Comments

class NoteDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #user определяется автоматически в create
    class Meta:
        model = Note
        fields = '__all__'

class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'


class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['author','text']

class NoteLitSerializer(serializers.ModelSerializer):

    coments = CommentsListSerializer(read_only=True, many=True)
    class Meta:
        model = Note
        fields = '__all__'





