# Generated by Django 4.1.5 on 2023-03-27 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_creditscheme_branch_creditscheme_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditscheme',
            name='sem',
            field=models.CharField(max_length=255),
        ),
    ]
