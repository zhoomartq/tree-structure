from django.db import models
from django.utils import timezone



class Worker(models.Model):
    fullname = models.CharField(max_length=255, verbose_name='ФИО')
    position = models.CharField(max_length=155, verbose_name='Должность')
    start_date = models.DateField(default=timezone.now, verbose_name='Дата создания')
    salary = models.CharField(max_length=20, verbose_name='Зарплата')
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, blank=True, related_name='childrens', verbose_name='Начальник')


    class Meta:
        verbose_name = 'Сотрудник'

    def __str__(self):
        return self.fullname
