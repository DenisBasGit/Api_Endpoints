# Generated by Django 4.0.5 on 2022-06-25 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.direction'),
        ),
    ]
