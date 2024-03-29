# Generated by Django 3.1.5 on 2021-01-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=264, unique=True)),
                ('last_name', models.CharField(max_length=264, unique=True)),
                ('user_email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
