# Generated by Django 3.2 on 2021-07-31 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainerspro', '0009_auto_20210731_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trainerspro.package'),
        ),
    ]
