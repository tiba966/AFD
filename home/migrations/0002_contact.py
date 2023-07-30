# Generated by Django 4.0.4 on 2023-06-18 21:40

from django.db import migrations, models
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_bg_image', models.FileField(blank=True, upload_to='background/index/', validators=[home.validators.validate_image_extension])),
            ],
        ),
    ]