# Generated by Django 4.1.4 on 2022-12-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usertable'),
    ]

    operations = [
        migrations.CreateModel(
            name='kseb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumerno', models.IntegerField(default=0, unique=True)),
                ('solarcapacity', models.IntegerField(default=0)),
            ],
        ),
    ]
