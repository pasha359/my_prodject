from django.forms import ModelForm
from .models import Note


class AddPostNote(ModelForm):
    class Meta:
        model = Note
        fields = ['title','animal_category', 'info', 'place_of_find', 'img']