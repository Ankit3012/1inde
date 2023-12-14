from django.db import models
from datetime import date
# shri nagar,  firozabad, gautam buddha, Nazi, delhi
class GhadiManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-date')

class Ghadi(models.Model):
    sn = models.CharField(default='Wait', max_length=255)
    fb = models.CharField(default='Wait', max_length=255)
    gb = models.CharField(default='Wait', max_length=255)
    nazi = models.CharField(default='Wait', max_length=255)
    dl = models.CharField(default='Wait', max_length=255)
    date = models.DateField(default=date.today)

    objects = GhadiManager()

    def __str__(self):
        return f'{self.sn} | {self.fb} | {self.gb} | {self.nazi} | {self.dl} | {self.date}'
