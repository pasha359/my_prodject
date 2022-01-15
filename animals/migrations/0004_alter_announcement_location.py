# Generated by Django 3.2.9 on 2021-12-23 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_alter_announcement_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='announcements', to='animals.location', verbose_name='find place'),
        ),
    ]
