from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone

User = get_user_model()

class Note (models.Model):
    category = (
        ('CAT', 'cat'),
        ('DOG', 'dog'),
        ('BIRD', 'bird'),
        ('AMPHIBIAN', 'amphibian'),
        ('OTHER', 'other'),
    )
    user = models.ForeignKey('auth.User', verbose_name='name of author', on_delete=models.CASCADE)
    animal_category = models.CharField('animal category', choices=category, max_length=50)
    title = models.CharField('title', max_length=50)
    place_of_find = models.CharField ('place of find',max_length=50)
    img = models.ImageField(upload_to='images',null=True, blank=True)
    info = models.TextField('Info of note', max_length=1000)
    data = models.DateTimeField('date of publication', default=timezone.now())

    def __str__(self):
        return f'заметка {self.id} => статья {self.title}'

    def get_absolut_way(self):
        return reverse ('post', kwargs={'post_id':self.pk}) #метод формирует маршрут post/id статьях на главной странице 'подробнее'

class Comments(models.Model):
    author = models.CharField('author', max_length=50)
    text = models.CharField('info of comment', max_length=200)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='coments')

    def __str__(self):
        return f'комментатор {self.author} к статье {self.note}'