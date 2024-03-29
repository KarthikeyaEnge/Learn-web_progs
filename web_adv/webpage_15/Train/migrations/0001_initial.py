# Generated by Django 4.1 on 2022-08-23 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='Train.station')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='Train.station')),
            ],
        ),
    ]
