# Generated by Django 4.1.5 on 2023-03-27 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_creditscheme_totalhours_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditscheme',
            name='branch',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creditscheme',
            name='sem',
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
