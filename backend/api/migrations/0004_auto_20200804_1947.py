# Generated by Django 3.1 on 2020-08-04 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200804_1905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='expired',
        ),
        migrations.RemoveField(
            model_name='secret',
            name='expiry',
        ),
        migrations.RemoveField(
            model_name='secret',
            name='uuid',
        ),
    ]
