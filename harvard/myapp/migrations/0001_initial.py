# Generated by Django 4.2.5 on 2023-11-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imgname', models.CharField(max_length=50)),
                ('Image', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
