# Generated by Django 3.0.3 on 2020-03-21 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FineSystemapp', '0003_auto_20200316_0210'),
    ]

    operations = [
        migrations.CreateModel(
            name='RULEs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FineSystemapp.Fine_apply')),
            ],
        ),
    ]