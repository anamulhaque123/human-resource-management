# Generated by Django 2.2.13 on 2023-02-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0002_auto_20230207_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp530', max_length=70),
        ),
    ]
