# Generated by Django 3.0.8 on 2020-08-02 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='instructor_id',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='students',
            name='student_id',
            field=models.CharField(max_length=30),
        ),
    ]
