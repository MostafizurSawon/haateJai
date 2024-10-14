# Generated by Django 5.1 on 2024-10-11 13:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('Super', 'Super'), ('Regular', 'Regular'), ('Below Average', 'Below Average')], default='Regular', max_length=20)),
                ('verify', models.BooleanField(default=False)),
                ('created_on', models.DateField(auto_now_add=True, null=True)),
                ('image', models.URLField(blank=True, default='https://img.freepik.com/premium-photo/poster-anime-character-with-fiery-background_943629-32000.jpg', null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('mobile', models.CharField(blank=True, max_length=14)),
                ('points', models.IntegerField(blank=True, default=0, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('hometown', models.CharField(max_length=20)),
                ('address', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('x', models.URLField(blank=True, null=True)),
                ('portfolio', models.URLField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
