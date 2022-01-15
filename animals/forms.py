from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils import timezone

selections = (
    ('CAT','cat'),
    ('DOG','dog'),
    ('BIRD','bird'),
    ('OTHER','other')
)

class AnnouncementForm(forms.Form):

    clases = forms.CharField(max_length=10,
                widget=forms.Select(choices=selections))
    breed = forms.CharField(max_length=20)
    animal_name = forms.CharField(max_length=20)
    animal_details = forms.CharField(max_length=200)
    img = forms.ImageField(required=False)
    city = forms.CharField(max_length=20)
    region = forms.CharField(max_length=20)
    district = forms.CharField(max_length=20)
    data = forms.DateField(initial=timezone.now)
    mail_contacts = forms.EmailField(help_text='A valid email address, please.')
    phone_contacts = forms.IntegerField()
    # user = forms.CharField(max_length=20)

    # def is_valid(self):
    #     super(AnnouncementForm, self).is_valid()

    def save(self):

        new_clases = AnimalType.objects.create(
            clases=self.cleaned_data['clases'])
        new_breed = Breed.objects.create(
            name=self.cleaned_data['breed'],
            animal_type=new_clases)
        new_animal = Animal.objects.create(
            animal_name=self.cleaned_data['animal_name'],
            animal_details=self.cleaned_data['animal_details'],
            img=self.cleaned_data['img'],
            breed=new_breed,
            )
        new_location = Location.objects.create(
            city=self.cleaned_data['city'],
            region=self.cleaned_data['region'],
            district=self.cleaned_data['district']
        )
        new_announcement = Announcement.objects.create(
            data=self.cleaned_data['data'],
            mail_contacts=self.cleaned_data['mail_contacts'],
            phone_contacts=self.cleaned_data['phone_contacts'],
            location=new_location,
            animal=new_animal,
            # user=self.cleaned_data['NoteUser']
        )

        all = new_clases, new_breed, new_animal,new_location, new_announcement
        return all


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)


#___________user forms_______________________

class NoteUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = NoteUser
        fields = ('username', 'email')

class NoteUserChangeForm(UserChangeForm):

    class Meta:
        model = NoteUser
        fields = ('username', 'email')