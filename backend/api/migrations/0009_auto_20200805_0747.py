# Generated by Django 3.1 on 2020-08-05 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200805_0723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='expiry',
        ),
        migrations.AddField(
            model_name='secret',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
