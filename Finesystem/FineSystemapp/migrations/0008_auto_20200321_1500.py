# Generated by Django 3.0.3 on 2020-03-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FineSystemapp', '0007_auto_20200321_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='login',
            name='Username',
            field=models.CharField(max_length=100),
        ),
    ]
