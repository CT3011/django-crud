# Generated by Django 4.1.1 on 2022-09-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_task_options_remove_task_published_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subcategory',
            field=models.CharField(choices=[('spacific', 'spacific'), ('all', 'all'), ('dep', 'dep')], default='all', max_length=10),
        ),
    ]