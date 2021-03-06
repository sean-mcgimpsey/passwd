# Generated by Django 3.1 on 2020-08-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200804_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='secret',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('expiry', models.DateField(auto_now=True)),
                ('expired', models.BooleanField(default=False)),
                ('uuid', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Sssecret',
        ),
    ]
