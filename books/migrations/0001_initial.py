# Generated by Django 3.1.5 on 2021-02-14 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('author', models.CharField(max_length=256)),
                ('genre', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('my_review', models.TextField()),
                ('release_year', models.PositiveIntegerField(default=0)),
                ('length', models.PositiveIntegerField()),
                ('photo', models.ImageField(upload_to='static/images')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1028)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='books.bookmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='books.bookmodel')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]