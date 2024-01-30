# Generated by Django 4.2.5 on 2023-11-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=255)),
                ('priority', models.CharField(choices=[('high', 'high'), ('medium', 'medium'), ('low', 'low')], max_length=100)),
            ],
        ),
    ]
