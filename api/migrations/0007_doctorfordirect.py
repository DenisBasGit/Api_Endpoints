# Generated by Django 4.0.5 on 2022-06-25 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_directionforchoose'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorForDirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slag', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('experience', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('number_sort', models.IntegerField(default=1)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.direction')),
            ],
        ),
    ]
