# Generated by Django 4.0.4 on 2023-07-09 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0007_careerdetail_career_desc_careerdetail_career_desc_ar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careerdetail',
            old_name='duties_4',
            new_name='career_duties_text_dr',
        ),
        migrations.RenameField(
            model_name='careerdetail',
            old_name='duties_4_ar',
            new_name='career_summary_text_dr',
        ),
        migrations.RenameField(
            model_name='careerdetail',
            old_name='duties_5',
            new_name='duties_1_dr',
        ),
        migrations.RenameField(
            model_name='careerdetail',
            old_name='duties_5_ar',
            new_name='duties_2_dr',
        ),
        migrations.RenameField(
            model_name='careerdetail',
            old_name='skill_4',
            new_name='duties_3_dr',
        ),
        migrations.RenameField(
            model_name='careerdetail',
            old_name='skill_4_ar',
            new_name='skill_1_dr',
        ),
        migrations.RenameField(
            model_name='careerdetail',
            old_name='skill_5',
            new_name='skill_2_dr',
        ),
        migrations.RenameField(
            model_name='careerdetail',
            old_name='skill_5_ar',
            new_name='skill_3_dr',
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='career_desc_dr',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='career_employee_type_dr',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='career_name_dr',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='job_type_dr',
            field=models.CharField(blank=True, choices=[('1', 'دوام كامل'), ('2', 'دوام جزئي'), ('3', 'تدريب')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='careerdetail',
            name='location_dr',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='donate',
            name='donate_benefi_1_dr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donate',
            name='donate_benefi_2_dr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donate',
            name='donate_benefi_3_dr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donate',
            name='donate_benefi_4_dr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='donate',
            name='donate_text_support_dr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='getinvolved',
            name='Donate_text_dr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='getinvolved',
            name='Volunteers_text_dr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='getinvolved',
            name='career_text_dr',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='volunteer_text_dr',
            field=models.TextField(blank=True, null=True),
        ),
    ]
