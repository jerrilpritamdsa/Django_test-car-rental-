# Generated by Django 4.1.5 on 2023-01-12 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renter',
            name='email',
            field=models.EmailField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='renter',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
