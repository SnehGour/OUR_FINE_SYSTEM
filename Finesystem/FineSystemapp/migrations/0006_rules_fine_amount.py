# Generated by Django 3.0.3 on 2020-03-21 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FineSystemapp', '0005_auto_20200321_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='rules',
            name='Fine_amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
