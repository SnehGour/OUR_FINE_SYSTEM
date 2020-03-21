# Generated by Django 3.0.3 on 2020-03-21 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FineSystemapp', '0010_auto_20200321_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply_Fine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fine_Amount', models.IntegerField()),
                ('Date', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='rules',
            name='Fine_amount',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Fine_apply',
        ),
        migrations.AddField(
            model_name='apply_fine',
            name='Rule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FineSystemapp.RULEs'),
        ),
        migrations.AddField(
            model_name='apply_fine',
            name='Username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FineSystemapp.login'),
        ),
    ]
