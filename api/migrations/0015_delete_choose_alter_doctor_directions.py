# Generated by Django 4.0.5 on 2022-06-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_alter_choose_options_remove_doctor_direction'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choose',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='directions',
            field=models.ManyToManyField(max_length=128, to='api.direction'),
        ),
    ]