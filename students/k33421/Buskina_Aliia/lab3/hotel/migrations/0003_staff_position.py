# Generated by Django 3.2 on 2023-12-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_auto_20231220_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('hostess', 'Hostess'), ('cleaner', 'Cleaner')], default='cleaner', max_length=10),
        ),
    ]
