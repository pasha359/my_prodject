from rest_framework import serializers
from animals.models import *
from django.utils import timezone

selections = (
    ('CAT'),
    ('DOG'),
    ('BIRD'),
    ('OTHER'))

class AnnouncementCreateSerialaizer(serializers.Serializer):

    clases = serializers.ChoiceField(choices=selections)
    breed = serializers.CharField(max_length=20)
    animal_name = serializers.CharField(max_length=20)
    animal_details = serializers.CharField(max_length=200)
    img = serializers.ImageField(required=False)
    city = serializers.CharField(max_length=20)
    region = serializers.CharField(max_length=20)
    district = serializers.CharField(max_length=20)
    data = serializers.DateField(initial=timezone.now)
    mail_contacts = serializers.EmailField(help_text='A valid email address, please.')
    phone_contacts = serializers.IntegerField()

    def create(self, validated_data):

        new_clases = AnimalType.objects.create(
            clases=validated_data.get('clases'))
        new_breed = Breed.objects.create(
            name=validated_data.get('breed'),
            animal_type=new_clases)
        new_animal = Animal.objects.create(
            animal_name=validated_data.get('animal_name'),
            animal_details=validated_data.get('animal_details'),
            img=validated_data.get('img'),
            breed=new_breed,
            )
        new_location = Location.objects.create(
            city=validated_data.get('city'),
            region=validated_data.get('region'),
            district=validated_data.get('district')
        )
        new_announcement = Announcement.objects.create(
            data=validated_data.get('data'),
            mail_contacts=validated_data.get('mail_contacts'),
            phone_contacts=validated_data.get('phone_contacts'),
            location=new_location,
            animal=new_animal
        )
        return new_announcement


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = ["clases",]

class BreedSerializer(serializers.ModelSerializer):
    animal_type = AnimalTypeSerializer()
    class Meta:
        model = Breed
        fields = [
            "name",
            "animal_type"
        ]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "city",
            "region",
            "district"
        ]

class AnimalSerializer(serializers.ModelSerializer):
    breed = BreedSerializer()
    class Meta:
        model = Animal
        fields = [
            "animal_name",
            "animal_details",
            "img",
            "breed"
        ]

class AnnouncementSerialaizer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    location = LocationSerializer()

    class Meta:
        model = Announcement
        fields = [
            "id",
            "user",
            "animal",
            "location",
            "mail_contacts",
            "phone_contacts",
        ]


class AnnouncementDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault()) #user определяется автоматически в create
    class Meta:
        model = Announcement
        fields = '__all__'









