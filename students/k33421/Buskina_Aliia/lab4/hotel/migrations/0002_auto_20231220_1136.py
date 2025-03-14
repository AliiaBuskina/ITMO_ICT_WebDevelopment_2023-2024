# Generated by Django 3.2 on 2023-12-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
