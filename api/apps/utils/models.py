"""
Предоставляет готовые интерефейсы для разных типов моделей.

"""
import logging

from django.db import models

logger = logging.getLogger(__name__)


class DateAutoModelMixin(models.Model):
    """
    Предоставляет интерфейс для работы с
    date_create и date_update Date.

    """
    date_create = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    date_update = models.DateField(verbose_name='Дата последнего изменения', auto_now=True)

    class Meta:
        abstract = True


class DateTimeAutoModelMixin(models.Model):
    """
    Предоставляет интерфейс для работы с
    date_create и date_update типа DateTime.

    """
    date_create = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    date_update = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now=True)

    class Meta:
        abstract = True


class DateModelMixin(DateAutoModelMixin):
    """
    Предоставляет интерфейс для работы с
    date_create и date_update Date без авто заполнения.

    """
    date_create = models.DateField(verbose_name='Дата создания')
    date_update = models.DateField(verbose_name='Дата последнего изменения')

    class Meta:
        abstract = True


class DateTimeModelMixin(DateTimeAutoModelMixin):
    """
    Предоставляет интерфейс для работы с
    date_create и date_update DateTime без авто заполнения.

    """
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_update = models.DateTimeField(verbose_name='Дата последнего изменения')

    class Meta:
        abstract = True
