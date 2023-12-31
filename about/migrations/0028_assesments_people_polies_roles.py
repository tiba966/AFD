# Generated by Django 4.0.4 on 2023-07-29 14:30

import about.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0027_whereweworkbackground'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assesments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner_assesments', models.FileField(upload_to='background/about/', validators=[about.validators.validate_image_extension])),
                ('text_assesments', models.TextField(blank=True, default='', max_length=1000)),
                ('text_assesments_ar', models.TextField(blank=True, default='', max_length=1000)),
                ('text_assesments_dr', models.TextField(blank=True, default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner_people', models.FileField(upload_to='background/about/', validators=[about.validators.validate_image_extension])),
                ('text_people', models.TextField(blank=True, default='', max_length=1000)),
                ('text_people_ar', models.TextField(blank=True, default='', max_length=1000)),
                ('text_people_dr', models.TextField(blank=True, default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Polies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner_polies', models.FileField(upload_to='background/about/', validators=[about.validators.validate_image_extension])),
                ('text_polies', models.TextField(blank=True, default='', max_length=1000)),
                ('text_polies_ar', models.TextField(blank=True, default='', max_length=1000)),
                ('text_polies_dr', models.TextField(blank=True, default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner_roles', models.FileField(upload_to='background/about/', validators=[about.validators.validate_image_extension])),
                ('text_roles', models.TextField(blank=True, default='', max_length=1000)),
                ('text_roles_ar', models.TextField(blank=True, default='', max_length=1000)),
                ('text_roles_dr', models.TextField(blank=True, default='', max_length=1000)),
            ],
        ),
    ]
