# Generated by Django 4.1.4 on 2022-12-11 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_kseb'),
    ]

    operations = [
        migrations.CreateModel(
            name='transactionlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.IntegerField(default=0)),
                ('receiver', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]
