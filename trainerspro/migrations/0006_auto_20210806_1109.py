# Generated by Django 3.2 on 2021-08-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerspro', '0005_auto_20210805_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='package_num',
        ),
        migrations.AddField(
            model_name='package',
            name='package_num',
            field=models.IntegerField(default=1),
        ),
    ]
