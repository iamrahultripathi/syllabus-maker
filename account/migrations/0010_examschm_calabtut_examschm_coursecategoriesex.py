# Generated by Django 4.1.5 on 2023-03-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_rename_branch_examschm_branch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examschm',
            name='caLabTut',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examschm',
            name='courseCategoriesEx',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
    ]
