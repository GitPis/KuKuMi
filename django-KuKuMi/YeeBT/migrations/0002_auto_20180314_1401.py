# Generated by Django 2.0.2 on 2018-03-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YeeBT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='mac',
            field=models.CharField(max_length=17, unique=True),
        ),
    ]