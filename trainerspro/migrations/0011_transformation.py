# Generated by Django 3.2 on 2021-08-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerspro', '0010_auto_20210821_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('before', models.ImageField(upload_to='')),
                ('after', models.ImageField(upload_to='')),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
