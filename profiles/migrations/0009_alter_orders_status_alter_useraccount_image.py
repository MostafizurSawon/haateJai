# Generated by Django 5.1 on 2024-10-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_useraccount_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='image',
            field=models.URLField(blank=True, default='https://img.freepik.com/free-photo/androgynous-avatar-non-binary-queer-person_23-2151100183.jpg', null=True),
        ),
    ]