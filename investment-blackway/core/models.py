from django.db import models
from django.utils import timezone


class Tax(models.Model):
    state = models.CharField(max_length=40, verbose_name='Страна эмитента')
    tax_rate = models.IntegerField(verbose_name='Налоговая ставка')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.state