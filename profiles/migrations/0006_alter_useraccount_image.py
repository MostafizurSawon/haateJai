# Generated by Django 5.1 on 2024-10-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.URLField(blank=True, default='https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100183.jpg', null=True),
        ),
    ]
