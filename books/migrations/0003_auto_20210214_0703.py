# Generated by Django 3.1.5 on 2021-02-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210214_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.CharField(default=None, max_length=256),
        ),
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.TextField(),
        ),
    ]
