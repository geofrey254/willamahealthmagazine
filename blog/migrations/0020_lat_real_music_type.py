# Generated by Django 3.2 on 2021-05-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210516_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='lat_real',
            name='music_type',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Trending')], default=0),
        ),
    ]
