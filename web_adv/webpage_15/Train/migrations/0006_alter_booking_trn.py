# Generated by Django 4.1 on 2022-08-27 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Train', '0005_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='trn',
            field=models.CharField(max_length=64),
        ),
    ]