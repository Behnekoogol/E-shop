# Generated by Django 4.2.6 on 2023-12-07 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='gender',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
    ]
