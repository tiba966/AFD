# Generated by Django 4.0.4 on 2023-06-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapage', '0005_alter_mediadetail_media_desc2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediadetail',
            name='media_desc1',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]
