# Generated by Django 4.2.2 on 2023-06-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0007_careerdetail_career_desc_careerdetail_career_desc_ar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerdetail',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]