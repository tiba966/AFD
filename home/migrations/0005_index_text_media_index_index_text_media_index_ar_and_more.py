# Generated by Django 4.0.4 on 2023-06-28 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_index_image_story_index_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='text_media_index',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='index',
            name='text_media_index_ar',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='index',
            name='text_themes_index',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='index',
            name='text_themes_index_ar',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
    ]