# Generated by Django 3.1.3 on 2020-12-01 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_auto_20201127_1014'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bedrooms',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]