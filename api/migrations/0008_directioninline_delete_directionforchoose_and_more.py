# Generated by Django 4.0.5 on 2022-06-25 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_doctorfordirect'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectionInLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slag', models.CharField(max_length=128)),
                ('number_sort', models.IntegerField(default=1)),
            ],
        ),
        migrations.DeleteModel(
            name='DirectionForChoose',
        ),
        migrations.DeleteModel(
            name='DoctorForDirect',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.directioninline'),
        ),
    ]
