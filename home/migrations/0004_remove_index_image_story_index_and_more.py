# Generated by Django 4.0.4 on 2023-06-19 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_slider_slide_dsc_index_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='image_story_index',
        ),
        migrations.RemoveField(
            model_name='index',
            name='text_story_index',
        ),
        migrations.RemoveField(
            model_name='index',
            name='text_story_index_ar',
        ),
        migrations.RemoveField(
            model_name='index',
            name='whatDoDetail_text',
        ),
        migrations.RemoveField(
            model_name='index',
            name='whatDoDetail_text_ar',
        ),
    ]
