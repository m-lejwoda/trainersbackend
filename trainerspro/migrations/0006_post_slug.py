# Generated by Django 3.2 on 2021-07-24 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerspro', '0005_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
