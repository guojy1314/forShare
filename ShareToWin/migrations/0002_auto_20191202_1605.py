# Generated by Django 2.2.7 on 2019-12-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShareToWin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
