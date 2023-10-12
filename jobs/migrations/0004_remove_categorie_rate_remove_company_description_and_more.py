# Generated by Django 4.2.6 on 2023-10-12 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='company',
            name='description',
        ),
        migrations.RemoveField(
            model_name='job',
            name='salary',
        ),
        migrations.AddField(
            model_name='categorie',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='count'),
        ),
        migrations.AddField(
            model_name='company',
            name='company_description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Company_description'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Job_description'),
        ),
        migrations.AddField(
            model_name='job',
            name='rounding_salary',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Rounding_salary'),
        ),
        migrations.AlterField(
            model_name='company',
            name='salary',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Salary'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_jop', to='jobs.company', verbose_name='Company'),
        ),
    ]
