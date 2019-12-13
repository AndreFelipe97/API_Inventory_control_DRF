# Generated by Django 3.0 on 2019-12-13 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('suppliers', '0003_auto_20191213_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('suppliers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='suppliers.Suppliers')),
            ],
        ),
    ]