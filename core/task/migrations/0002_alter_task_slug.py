# Generated by Django 4.1.1 on 2022-09-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(max_length=150, unique_for_date='published'),
        ),
    ]
