# Generated by Django 5.1 on 2024-10-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_alter_orders_status_alter_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.URLField(blank=True, default='https://img.freepik.com/free-photo/cartoon-character-with-handbag-sunglasses_71767-99.jpg', null=True),
        ),
    ]