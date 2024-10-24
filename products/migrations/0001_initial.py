# Generated by Django 5.1 on 2024-10-18 14:10

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('Hot', 'Hot'), ('New', 'New'), ('Offer', 'Offer')], max_length=20)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('discount_price', models.IntegerField(blank=True, null=True)),
                ('sold', models.IntegerField(blank=True, default=0, null=True)),
                ('available', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, choices=[('Uttara', 'UTTARA'), ('Mirpur', 'MIRPUR'), ('Dhanmondi', 'DHANMONDI')], max_length=20)),
                ('delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='products.category')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='product_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
