# Generated by Django 4.0.4 on 2023-06-17 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0002_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='volunteer_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='volunteer_text_ar',
            field=models.TextField(blank=True, null=True),
        ),
    ]
