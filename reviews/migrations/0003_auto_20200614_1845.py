# Generated by Django 3.0.5 on 2020-06-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_mymovie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymovie',
            name='movieId',
            field=models.IntegerField(),
        ),
    ]
