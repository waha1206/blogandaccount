# Generated by Django 3.0.5 on 2020-06-07 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='imamge',
            new_name='image',
        ),
    ]
