# Generated by Django 4.2.5 on 2023-11-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]