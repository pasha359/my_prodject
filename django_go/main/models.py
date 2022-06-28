from django.db import models
from django.utils import timezone
from users.models import CustomUser
from django.contrib.auth import login, logout

sex_choices = (
    ('MEN', 'men'),
    ('WOMEN', 'women')
)

boolean_choices = (
    ('NO', 'no'),
    ('YES', 'yes')
)

class Person(models.Model):
    person_name = models.CharField(max_length=50, verbose_name='person_name')
    age = models.IntegerField(verbose_name='age')
    sex = models.CharField(max_length=10, choices=sex_choices, verbose_name='sex')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Passport(models.Model):
    number = models.CharField(max_length=50, verbose_name='номер документа')
    person_id = models.OneToOneField(Person, on_delete=models.CASCADE, verbose_name='Клиент')

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'

class Propertys(models.Model):
    property_name = models.CharField(max_length=50, verbose_name='property_name')
    image = models.ImageField(upload_to='images/%y/$m//$d/', blank=True)
    fine_is_paid = models.CharField(max_length=10, choices=boolean_choices)
    taken_by_owner = models.CharField(max_length=10, choices=boolean_choices)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Имущество'
        verbose_name_plural = 'Имущества'


class Notes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    property = models.ForeignKey('Propertys', on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    contact = models.EmailField(blank=True, null=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-date']