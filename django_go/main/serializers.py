from rest_framework import serializers
from main.models import *
from django.utils import timezone

sex_choices = (
    ('MEN', 'men'),
    ('WOMEN', 'women')
)

boolean_choices = (
    ('NO', 'no'),
    ('YES', 'yes')
)

class NoteCreateSerialaizer(serializers.Serializer):

    person_name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    sex = serializers.ChoiceField(choices=sex_choices)
    number = serializers.CharField(max_length=50)
    image = serializers.ImageField(required=False)
    property_name = serializers.CharField(max_length=30)
    fine_is_paid = serializers.ChoiceField(choices=boolean_choices)
    taken_by_owner = serializers.ChoiceField(choices=boolean_choices)
    date = serializers.DateField(initial=timezone.now)
    contact = serializers.EmailField(help_text='A valid email address, please.')

    def create(self, validated_data):

        new_person = Person.objects.create(
            person_name=validated_data.get('person_name'),
            age=validated_data.get('age'),
            sex=validated_data.get('sex'))
        new_passport = Passport.objects.create(
            number=validated_data.get('number'),
            person_id=new_person)
        new_propertys = Propertys.objects.create(
            property_name=validated_data.get('property_name'),
            image=validated_data.get('image'),
            fine_is_paid=validated_data.get('fine_is_paid'),
            taken_by_owner=validated_data.get('taken_by_owner'),
            person_id=new_person,
            )
        new_notes = Notes.objects.create(
            contact=validated_data.get('contact'),
            property=new_propertys
        )
        return new_notes

    def update(self, instance, validated_data):
        instance.person_name = validated_data.get('person_name', instance.person_name)
        instance.age = validated_data.get('age', instance.age)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.number = validated_data.get('number', instance.number)
        instance.property_name = validated_data.get('property_name', instance.property_name)
        instance.fine_is_paid = validated_data.get('fine_is_paid', instance.fine_is_paid)
        instance.taken_by_owner = validated_data.get('taken_by_owner', instance.taken_by_owner)
        instance.contact = validated_data.get('contact', instance.contact)
        instance.image = validated_data.get('image', instance.image)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.save()
        return instance










class PassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passport
        fields = ['number', ]

class PersonSerializer(serializers.ModelSerializer):
    passport = PassportSerializer()

    class Meta:
        model = Person
        fields = ['person_name', 'age', 'sex', 'passport']

class PropertySerializer(serializers.ModelSerializer):
    person_id = PersonSerializer()
    class Meta:
        model = Propertys
        fields = ['person_id','property_name', 'image', 'fine_is_paid','taken_by_owner']

class NotesSerializer(serializers.ModelSerializer):
    property = PropertySerializer()
    class Meta:
        model = Notes
        fields = ['id','property', 'contact', 'date']

class NotesDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #user определяется автоматически в create
    class Meta:
        model = Notes
        fields = '__all__'






