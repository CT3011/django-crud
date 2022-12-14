# Generated by Django 4.1.1 on 2022-09-18 04:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('-published',)},
        ),
        migrations.AddField(
            model_name='task',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
