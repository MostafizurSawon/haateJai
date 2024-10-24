# Generated by Django 5.1 on 2024-10-21 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='location',
        ),
        migrations.AddField(
            model_name='products',
            name='location',
            field=models.ManyToManyField(blank=True, related_name='product_location', to='products.location'),
        ),
    ]
