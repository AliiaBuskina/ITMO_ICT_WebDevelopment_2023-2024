# Generated by Django 3.2 on 2023-12-08 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('passport_number', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('from_location', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('1', '1 bed'), ('2', '2 beds'), ('3', '3 beds')], max_length=1)),
                ('floor', models.IntegerField()),
                ('price', models.IntegerField()),
                ('cleaners', models.ManyToManyField(through='hotel.Cleaning', to='hotel.Staff')),
            ],
        ),
        migrations.AddField(
            model_name='cleaning',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleaning', to='hotel.room'),
        ),
        migrations.AddField(
            model_name='cleaning',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleaning', to='hotel.staff'),
        ),
        migrations.CreateModel(
            name='Checkin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('check_in_date', models.DateField(auto_now_add=True)),
                ('check_out_date', models.DateField(auto_now_add=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.room')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.staff')),
            ],
        ),
    ]
