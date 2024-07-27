# Generated by Django 5.0.7 on 2024-07-27 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CamDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('camdb_id', models.CharField(max_length=100, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('views', models.PositiveIntegerField()),
                ('position', models.PositiveIntegerField()),
            ],
        ),
    ]
