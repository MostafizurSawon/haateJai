# Generated by Django 5.1 on 2024-10-11 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.URLField(blank=True, default='https://img.freepik.com/free-photo/anime-style-character-space_23-2151134190.jpg', null=True),
        ),
    ]
