# Generated by Django 4.0.4 on 2023-06-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0006_careerdetail_careerlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='careerdetail',
            name='career_desc',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='career_desc_ar',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]