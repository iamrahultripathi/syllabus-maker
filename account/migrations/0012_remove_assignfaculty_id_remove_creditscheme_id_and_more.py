# Generated by Django 4.1.5 on 2023-03-31 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_assignfaculty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignfaculty',
            name='id',
        ),
        migrations.RemoveField(
            model_name='creditscheme',
            name='id',
        ),
        migrations.RemoveField(
            model_name='examschm',
            name='id',
        ),
        migrations.AlterField(
            model_name='assignfaculty',
            name='courseCodeEx',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='creditscheme',
            name='courseCode',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='examschm',
            name='courseCodeEx',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]