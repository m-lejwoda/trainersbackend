# Generated by Django 3.2 on 2021-07-17 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerspro', '0003_auto_20210716_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='stripe_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]
