# Generated by Django 4.1.7 on 2023-04-13 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_examschm_credit_scheme_alter_examschm_coursecodeex_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examschm',
            name='credit_scheme',
        ),
        migrations.AlterField(
            model_name='examschm',
            name='courseCodeEx',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='examschm',
            name='courseNameEx',
            field=models.CharField(max_length=255),
        ),
    ]
