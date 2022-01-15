# Generated by Django 3.2.9 on 2021-12-23 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_alter_announcement_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.location', verbose_name='find place'),
        ),
    ]
