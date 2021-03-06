# Generated by Django 3.0.2 on 2020-03-19 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='counter',
            fields=[
                ('counterid', models.AutoField(primary_key=True, serialize=False)),
                ('Total_cases', models.CharField(default='Unavailable', max_length=100)),
                ('Deaths', models.CharField(default='Unavailable', max_length=100)),
                ('Recovered', models.CharField(default='Unavailable', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='manunews',
            fields=[
                ('newsid', models.AutoField(primary_key=True, serialize=False)),
                ('headline', models.CharField(default='', max_length=1000)),
                ('content', models.CharField(default='', max_length=2000)),
                ('image', models.TextField(default='', max_length=10000)),
                ('link', models.CharField(default='', max_length=500)),
                ('channel', models.CharField(default='', max_length=15)),
                ('time', models.CharField(default='', max_length=10)),
                ('type', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
