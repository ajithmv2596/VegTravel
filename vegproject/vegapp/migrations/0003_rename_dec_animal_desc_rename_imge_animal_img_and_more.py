# Generated by Django 4.1.4 on 2022-12-13 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vegapp', '0002_animal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='dec',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='imge',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='nam',
            new_name='name',
        ),
    ]