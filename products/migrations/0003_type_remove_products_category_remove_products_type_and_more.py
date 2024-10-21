# Generated by Django 5.1 on 2024-10-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_location_remove_products_location_products_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.RemoveField(
            model_name='products',
            name='type',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_category', to='products.category'),
        ),
        migrations.AddField(
            model_name='products',
            name='type',
            field=models.ManyToManyField(blank=True, null=True, related_name='product_type', to='products.type'),
        ),
    ]
