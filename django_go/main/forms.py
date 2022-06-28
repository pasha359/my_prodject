from django import forms
from .models import *
from django.utils import timezone


sex_choices = (
    ('MEN', 'men'),
    ('WOMEN', 'women')
)

class NotesForm(forms.Form):
    person_name = forms.CharField(max_length=150, label='ФИО')
    age = forms.IntegerField(label='Полных лет')
    sex = forms.ChoiceField(choices=sex_choices, label='Пол')
    number = forms.CharField(max_length=150, label='Номер документа')
    image = forms.ImageField(label='Фото имущества', required=False)
    property_name = forms.CharField(max_length=150,label='Описание имущества')
    fine_is_paid = forms.ChoiceField(choices=boolean_choices, label='Штраф оплачен')
    taken_by_owner = forms.ChoiceField(choices=boolean_choices, label='Авто забарно владельцем')
    contact = forms.EmailField(label='email для оповещения')
    date = forms.DateTimeField(initial=timezone.now, label='Дата')


    def save(self):
        new_person = Person.objects.create(
            person_name=self.cleaned_data['person_name'],
            age = self.cleaned_data['age'],
            sex = self.cleaned_data['sex'])

        new_passport = Passport.objects.create(
            number=self.cleaned_data['number'],
            person_id = new_person)

        new_propertys = Propertys.objects.create(
            property_name = self.cleaned_data['property_name'],
            image = self.cleaned_data['image'],
            fine_is_paid = self.cleaned_data['fine_is_paid'],
            taken_by_owner = self.cleaned_data['taken_by_owner'],
            person_id = new_person)

        new_notes = Notes.objects.create(
            date=self.cleaned_data['date'],
            contact=self.cleaned_data['contact'],
            # user = self.cleaned_data['CustomUser'],
            property = new_propertys)


        all = new_person, new_passport, new_propertys, new_notes

        return all
