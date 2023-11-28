from django.db import models
from datetime import date

class GhadiManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-date')

class Ghadi(models.Model):
    sg = models.CharField(default='Not declared', max_length=255)
    fb = models.CharField(default='Not declared', max_length=255)
    gb = models.CharField(default='Not declared', max_length=255)
    gali = models.CharField(default='Not declared', max_length=255)
    ds = models.CharField(default='Not declared', max_length=255)
    date = models.DateField(default=date.today)

    objects = GhadiManager()

    def __str__(self):
        return f'{self.sg} | {self.fb} | {self.gb} | {self.gali} | {self.ds} | {self.date}'
