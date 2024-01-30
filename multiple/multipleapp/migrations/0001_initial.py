# Generated by Django 4.2.5 on 2023-10-16 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee1',
            fields=[
                ('Employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('salary', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('employee1_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='multipleapp.employee1')),
                ('student_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='multipleapp.student')),
                ('Customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=50)),
                ('payment', models.IntegerField()),
            ],
            bases=('multipleapp.student', 'multipleapp.employee1'),
        ),
    ]