# Generated by Django 3.2 on 2023-12-20 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20231220_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning',
            name='date_clean',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
