# Generated by Django 3.2.10 on 2022-01-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('totoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-02-10'),
            preserve_default=False,
        ),
    ]
