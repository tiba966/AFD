# Generated by Django 4.0.4 on 2023-07-29 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0023_methodologylist_remove_methodology_methodology_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wherewework',
            name='image_banner_where_we_work',
        ),
        migrations.AddField(
            model_name='wherewework',
            name='address',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='wherewework',
            name='address_ar',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='wherewework',
            name='address_dr',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
        migrations.AddField(
            model_name='wherewework',
            name='address_num',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]
