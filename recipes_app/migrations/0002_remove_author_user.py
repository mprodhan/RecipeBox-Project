# Generated by Django 3.1 on 2020-08-20 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='User',
        ),
    ]
