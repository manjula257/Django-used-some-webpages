# Generated by Django 4.2.5 on 2023-11-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedata',
            name='Image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='imagedata',
            name='Imgname',
            field=models.CharField(max_length=255),
        ),
    ]