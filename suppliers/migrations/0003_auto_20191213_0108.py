# Generated by Django 3.0 on 2019-12-13 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0002_auto_20191213_0052'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fornecedor',
            new_name='Suppliers',
        ),
    ]