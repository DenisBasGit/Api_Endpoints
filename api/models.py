from django.db import models
from sqlalchemy.orm import relationship


class Direction(models.Model):
    name = models.CharField(max_length=128)
    slag = models.CharField(max_length=128)
    number_sort = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name}'

    def natural_key(self):
        return self.name



    class Meta:
        verbose_name = 'Напрямок'
        verbose_name_plural = 'Напрямки'

    def save(self, *args, **kwargs):
        super(Direction, self).save(*args, **kwargs)


class Doctor(models.Model):
    name = models.CharField(max_length=128)
    slag = models.CharField(max_length=128)
    directions = models.ManyToManyField(Direction)
    description = models.CharField(max_length=128)
    date = models.DateField()
    years_of_experience = models.IntegerField(default=0)
    number_sort = models.IntegerField(default=1)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Лікара'
        verbose_name_plural = 'Лікарі'

    def save(self, *args, **kwargs):
        super(Doctor, self).save(*args, **kwargs)
