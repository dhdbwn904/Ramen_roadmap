# Generated by Django 4.0.5 on 2022-06-20 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_restaurent_lat_restaurent_lng'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurent',
            name='img',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='restaurent',
            name='review',
            field=models.CharField(default='', max_length=300),
        ),
    ]
