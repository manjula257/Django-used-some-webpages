# Generated by Django 4.2.5 on 2023-10-16 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('commondata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='absapp.commondata')),
                ('sales', models.IntegerField()),
                ('products', models.IntegerField()),
            ],
            bases=('absapp.commondata',),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('commondata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='absapp.commondata')),
                ('salary', models.IntegerField()),
                ('company', models.CharField(max_length=50)),
            ],
            bases=('absapp.commondata',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('commondata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='absapp.commondata')),
                ('marks', models.IntegerField()),
                ('institute', models.CharField(max_length=50)),
            ],
            bases=('absapp.commondata',),
        ),
    ]
