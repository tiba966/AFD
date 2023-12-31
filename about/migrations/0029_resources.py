# Generated by Django 4.0.4 on 2023-07-29 15:53

import about.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0028_assesments_people_polies_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner_resourc', models.FileField(upload_to='background/about/', validators=[about.validators.validate_image_extension])),
                ('text_resourc', models.TextField(blank=True, default='', max_length=1000)),
                ('text_resourc_ar', models.TextField(blank=True, default='', max_length=1000)),
                ('text_resourc_dr', models.TextField(blank=True, default='', max_length=1000)),
            ],
        ),
    ]
