# Generated by Django 4.0.4 on 2023-07-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_index_text_media_index_index_text_media_index_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='text_about_index_dr',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='index',
            name='text_media_index_dr',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='index',
            name='text_themes_index_dr',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='slider',
            name='slide_subtitle_index_dr',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='slider',
            name='slide_title_index_dr',
            field=models.CharField(blank=True, default='', max_length=300),
        ),
    ]
