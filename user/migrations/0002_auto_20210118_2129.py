# Generated by Django 2.2.15 on 2021-01-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
